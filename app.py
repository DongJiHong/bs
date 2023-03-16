import datetime
from collections import Counter

from flask import render_template, request, flash, redirect, session, url_for
from flask_bootstrap import Bootstrap4
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

from CF_ITEM_PYTHON import InformationItemRecommend, BookItemRecommend
from conf import *

bootstrap = Bootstrap4(app)
# 字符串随便起
app.secret_key = "username"

# session 过期时间 10分钟
app.permanent_session_lifetime = datetime.timedelta(seconds=10 * 60)


# 注册
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        label = request.form.getlist('label')
        if not all([username, password, password2]):
            flash('参数不完整')
        elif len(username) < 4:
            flash('用户名太短')
        elif password != password2:
            flash('两次密码不一致,请重新输入')
        elif len(password) < 6:
            flash('密码长度太短,请重新输入')
        else:
            user = Users.query.filter(Users.username == username).first()
            if user:
                flash('用户名已存在,请重新输入')
            else:
                labels = ",".join(label)
                password_hash = generate_password_hash(password)
                new_user = Users(username=username, password=password_hash, id=None, label=labels)
                # 添加提交
                db.session.add(new_user)
                db.session.commit()
            return redirect("/login/")
    return render_template('register.html')


# 登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            flash('参数不完整')
        user = Users.query.filter(Users.username == username).first()
        if user:
            token = check_password_hash(user.password, password)
            if token:
                session.permanent = True
                session['username'] = username
                return redirect("/")
            else:
                flash("密码错误")
        else:
            flash("用户名错误")
    return render_template('login.html')


# 退出登录
@app.route('/quit/')
def quit():
    session.pop("username", None)
    return redirect('/')


# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    limit = 8
    page = request.args.get('page', 1, type=int)
    data_csdn = Csdn.query.order_by(Csdn.browse.desc()).paginate(page, per_page=limit)
    data = aside()
    return render_template("index.html", csdn=data_csdn.items, douban=data[0],
                           saying=data[1], pagination=data_csdn)


# 资讯
@app.route('/information/')
def information():
    limit = 8
    page = request.args.get('page', 1, type=int)
    data_csdn = Csdn.query.order_by(Csdn.browse.desc()).paginate(page, per_page=limit)
    data = aside()
    return render_template("information.html", csdn=data_csdn.items, douban=data[0],
                           saying=data[1], pagination=data_csdn)


# 图书
@app.route('/book/')
def book():
    data = aside()
    page = request.args.get('page', 1, type=int)
    limit = 10
    book = Douban.query.paginate(page, per_page=limit)
    return render_template("category.html", book=book.items, douban=data[0],
                           saying=data[1], pagination=book)


# 查找图书，并分页显示
@app.route("/find_book/")
def find_book(limit=12):
    keyword = request.args.get('search')
    if keyword == "":
        return redirect(url_for("book"))
    else:
        page = request.args.get('page', 1, type=int)
        # 按条件查询数据并分页显示
        pagination = Douban.query.filter(or_(
            Douban.author.contains(keyword), Douban.book_name.contains(keyword), Douban.content.contains(keyword)
        )).paginate(page, per_page=limit)
        data = aside()
        return render_template("category.html", book=pagination.items, douban=data[0],
                               saying=data[1], pagination=pagination)


# 查找资讯，并分页显示
@app.route("/find_csdn/")
def find_csdn(limit=12):
    keyword = request.args.get('search')
    if keyword == "":
        return redirect(url_for("information"))
    else:
        page = request.args.get('page', 1, type=int)
        # 按条件查询数据并分页显示
        pagination = Csdn.query.filter(or_(
            Csdn.title.contains(keyword), Csdn.name.contains(keyword), Csdn.content.contains(keyword)
        )).paginate(page, per_page=limit)
        data = aside()
        return render_template("information.html", csdn=pagination.items, douban=data[0],
                               saying=data[1], pagination=pagination)


# 跳转资讯详情页，并存入用户访问记录
@app.route('/information_detail/<int:id>')
def information_detail(id):
    try:
        data = Csdn.query.filter(Csdn.id == id).first()
        Csdn.query.filter_by(id=id).update({"browse": data.browse + 1})
        user = session.get('username')
        if user:
            users = Users.query.filter(Users.username == user).first()
            label = str(users.label).lower() + "," + str(data.label).lower()
            label = ",".join(list(set(label.split(","))))
            Users.query.filter_by(id=users.id).update({Users.label: label}, synchronize_session=False)
            db.session.commit()
            time = datetime.date.today()
            new_record = RecordInformation(user_id=users.id, information_id=id, time=time)
            db.session.add(new_record)
        db.session.commit()
    except Exception as e:
        print("未登录用户")
        print(e)
    finally:
        return render_template("csdn_detail.html", data=data)


# 跳转图书详情页，并存入用户访问记录
@app.route('/book_detail/<int:id>')
def book_detail(id):
    data = Douban.query.filter(Douban.id == id).first()
    try:
        user = session.get('username')
        if user:
            users = Users.query.filter(Users.username == user).first()
            label = str(users.label).lower() + "," + str(data.label).lower()
            label = ",".join(list(set(label.split(","))))
            Users.query.filter_by(id=users.id).update({Users.label: label}, synchronize_session=False)
            time = datetime.date.today()
            new_record = RecordBook(user_id=users.id, book_id=id, time=time)
            db.session.add(new_record)
            db.session.commit()
    except Exception as e:
        print(e)
    finally:
        return render_template("book_detail.html", data=data)


# 个性化推荐
@app.route("/recommend_information/")
def recommend_information():
    user = session.get('username')
    if user:
        num = 50
        page = request.args.get('page', 1, type=int)
        limit = 10
        pagination = int(num / limit)  # 总页数
        user = Users.query.filter(Users.username == user).first()
        user_id = user.id
        information_recommend = InformationItemRecommend(user_id).recommend(num)
        start = (page - 1) * limit
        finish = page * limit
        information_data = information_recommend[start:finish]
        return render_template("recommend_information.html", information=information_data, pagination=pagination)
    return redirect("/")


@app.route("/recommend_book/")
def recommend_book():
    user = session.get('username')
    if user:
        num = 50
        page = request.args.get('page', 1, type=int)
        limit = 10
        pagination = int(num / limit)  # 总页数
        user = Users.query.filter(Users.username == user).first()
        user_id = user.id
        book_recommend = BookItemRecommend(user_id).recommend(num)
        start = (page - 1) * limit
        finish = page * limit
        book_data = book_recommend[start:finish]
        return render_template("recommend_book.html", book=book_data, pagination=pagination)
    return redirect("/")


# 最近浏览记录 图表
@app.route("/recording_information/")
def recording_information():
    try:
        page = request.args.get('page', 1, type=int)
        limit = 8
        user = session.get("username")
        users = Users.query.filter(Users.username == user).first()
        recording_csdn = RecordInformation.query.filter(RecordInformation.user_id == users.id).order_by(
            RecordInformation.id.desc()).paginate(page, per_page=limit)
        data_csdn = recording_csdn.items
        page_view = []
        data_csdns = []
        for i in data_csdn:
            page_view.append(Counter({
                i.time.strftime("%Y/%m/%d"): 1
            }))
            data_csdns.append(Csdn.query.filter(Csdn.id == i.information_id).first())
        data = Counter(dict())
        for item in page_view:
            data = Counter(dict(data + item))
        date = [item for item in dict(data).keys()]
        data = [item for item in dict(data).values()]
        return render_template("recording_information.html", data_csdn=data_csdns, csdn=recording_csdn, date=date,
                               data=data)
    except Exception as e:
        print(e)
        return redirect("/")


# 查找资讯浏览记录
@app.route("/recordingInformation/")
def recordingInformation(limit=8):
    keyword = request.args.get('search')
    if keyword == "":
        return redirect(url_for("recording_information"))
    else:
        page = request.args.get('page', 1, type=int)
        # 按条件查询数据并分页显示
        user = session.get("username")
        users = Users.query.filter(Users.username == user).first()
        recording_csdn = RecordInformation.query.filter(RecordInformation.user_id == users.id).all()
        information_id = []
        page_view = []
        for i in recording_csdn:
            information_id.append(i.information_id)
            page_view.append(Counter({
                i.time.strftime("%Y/%m/%d"): 1
            }))
        data = Counter(dict())
        for item in page_view:
            data = Counter(dict(data + item))
        date = [item for item in dict(data).keys()]
        data = [item for item in dict(data).values()]
        pagination = Csdn.query.filter(or_(
            Csdn.title.contains(keyword), Csdn.name.contains(keyword), Csdn.content.contains(keyword)),
            Csdn.id.in_(information_id)).paginate(page, per_page=limit)
        return render_template("recording_information.html", data_csdn=pagination.items, csdn=pagination, date=date,
                               data=data)


# 图书浏览记录
@app.route("/recording_book/")
def recording_book():
    try:
        page = request.args.get('page', 1, type=int)
        limit = 8
        user = session.get("username")
        print(user)
        users = Users.query.filter(Users.username == user).first()
        recording_book = RecordBook.query.filter(RecordBook.user_id == users.id).order_by(
            RecordBook.id.desc()).paginate(page, per_page=limit)
        data_book = recording_book.items
        page_view = []
        data_books = []
        for i in data_book:
            page_view.append(Counter({
                i.time.strftime("%Y/%m/%d"): 1
            }))
            data_books.append(Douban.query.filter(Douban.id == i.book_id).first())
        data = Counter(dict())
        for item in page_view:
            data = Counter(dict(data + item))
        date = [item for item in dict(data).keys()]
        data = [item for item in dict(data).values()]
        return render_template("recording_book.html", data_book=data_books, book=recording_book, date=date, data=data)
    except Exception as e:
        print(e)
        return redirect("/")


# 查找图书浏览记录
@app.route("/recordingBook/")
def recordingBook(limit=8):
    keyword = request.args.get('search')
    if keyword == "":
        return redirect(url_for("recording_book"))
    else:
        page = request.args.get('page', 1, type=int)
        # 按条件查询数据并分页显示
        user = session.get("username")
        users = Users.query.filter(Users.username == user).first()
        recording_book = RecordBook.query.filter(RecordBook.user_id == users.id).all()
        book_id = []
        page_view = []
        for i in recording_book:
            book_id.append(i.book_id)
            page_view.append(Counter({
                i.time.strftime("%Y/%m/%d"): 1
            }))
        data = Counter(dict())
        for item in page_view:
            data = Counter(dict(data + item))
        date = [item for item in dict(data).keys()]
        data = [item for item in dict(data).values()]
        pagination = Douban.query.filter(or_(
            Douban.author.contains(keyword), Douban.book_name.contains(keyword), Douban.content.contains(keyword)
        ), Douban.id.in_(book_id)).paginate(page, per_page=limit)
        return render_template("recording_book.html", data_book=pagination.items, book=pagination, date=date, data=data)


# 点赞
@app.route("/like/<int:id>")
def like(id):
    try:
        user = session.get('username')
        if user:
            users = Users.query.filter(Users.username == user).first()
            # 查询点赞记录判断是否已经点赞
            behavior = Behavior.query.filter(Behavior.user_id == users.id, Behavior.information_id == id).first()
            data = Csdn.query.filter(Csdn.id == id).first()
            if behavior:
                # 已经踩 取消踩 变为点赞
                if behavior.behavior == 0:
                    Behavior.query.filter_by(id=behavior.id).update({Behavior.behavior: 1}, synchronize_session=False)
                    # 踩 -1
                    difference = data.difference - 1
                    likes = data.likes + 1
                    Csdn.query.filter_by(id=id).update({Csdn.difference: difference}, {Csdn.likes: likes},
                                                       synchronize_session=False)
                    db.session.commit()
            else:
                # 没有记录添加记录
                new_record = Behavior(user_id=users.id, information_id=id, behavior=1)
                db.session.add(new_record)
                # 资讯点赞数+1
                likes = data.likes + 1
                Csdn.query.filter_by(id=id).update({Csdn.likes: likes}, synchronize_session=False)
                db.session.commit()
    except Exception as e:
        print(e)
    return redirect(request.host_url)


# 踩
@app.route("/difference/<int:id>")
def difference(id):
    try:
        user = session.get('username')
        if user:
            users = Users.query.filter(Users.username == user).first()
            data = Csdn.query.filter(Csdn.id == id).first()
            # 查询点赞记录判断是否已经踩
            behavior = Behavior.query.filter(Behavior.user_id == users.id, Behavior.information_id == id).first()
            if behavior:
                # 已经点赞 取消点赞 变为踩
                if behavior.behavior == 1:
                    Behavior.query.filter_by(id=behavior.id).update({Behavior.behavior: 0}, synchronize_session=False)
                    # 点赞 -1
                    likes = data.likes - 1
                    difference = data.difference + 1
                    Csdn.query.filter_by(id=id).update({Csdn.likes: likes}, {Csdn.difference: difference},
                                                       synchronize_session=False)
                    db.session.commit()
            else:
                # 没有记录添加记录
                new_record = Behavior(user_id=users.id, information_id=id, behavior=0)
                db.session.add(new_record)
                # 资讯踩数+1
                difference = data.difference + 1
                Csdn.query.filter_by(id=id).update({Csdn.difference: difference}, synchronize_session=False)
                db.session.commit()
    except Exception as e:
        print(e)
    return redirect(request.host_url)


if __name__ == '__main__':
    app.run(debug=True)
