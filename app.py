import datetime
from collections import Counter

from flask import render_template, request, flash, redirect, session, url_for
from flask_bootstrap import Bootstrap4
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

from CF_ITEM_PYTHON import BookItemRecommends, InformationItemRecommends
from conf import *

bootstrap = Bootstrap4(app)
# 字符串随便起
app.secret_key = "username"

# session 过期时间 30分钟
app.permanent_session_lifetime = datetime.timedelta(seconds=30 * 60)


# 管理员登录
@app.route("/admin/", methods=['GET', 'POST'])
def admin_login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            flash('参数不完整')
        admin = Admin.query.filter(Admin.username == username).first()
        if admin:
            token = check_password_hash(admin.password, password)
            if token:
                session.permanent = True
                session['grade'] = admin.grade
                session['admin'] = username
                return redirect("/Index")
            else:
                flash("密码错误")
        else:
            flash("用户名错误")
    return render_template("admin_login.html")


# 管理员主界面
@app.route('/Index/', methods=['GET', 'POST'])
def admin_index():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        limit = 10
        page = request.args.get('page', 1, type=int)
        admin_list = Admin.query.paginate(page, per_page=limit)
        return render_template("admin_index.html", admin=admin_list.items, pagination=admin_list)
    else:
        return redirect("/admin")


# 新建管理员
@app.route('/add/', methods=['GET', 'POST'])
def admin_add():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        if request.method == "POST":
            username = request.form.get('username')
            password = request.form.get('password')
            password2 = request.form.get('password2')
            if not all([username, password, password2]):
                flash('参数不完整')
            elif len(username) < 4:
                flash('用户名太短')
            elif password != password2:
                flash('两次密码不一致,请重新输入')
            elif len(password) < 6:
                flash('密码长度太短,请重新输入')
            else:
                user = Admin.query.filter(Admin.username == username).first()
                if user:
                    flash('用户名已存在,请重新输入')
                else:
                    password_hash = generate_password_hash(password)
                    new_admin = Admin(username=username, password=password_hash, id=None, grade=False)
                    # 添加提交
                    db.session.add(new_admin)
                    db.session.commit()
                return redirect("/Index/")
        return render_template("admin_add.html")
    else:
        return redirect("/admin")


# 管理员修改
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def admin_update(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        admin = Admin.query.filter(Admin.id == id).first()
        if request.method == "POST":
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            if len(username) < 4:
                flash('用户名太短')
            elif len(password) < 6:
                flash('密码长度太短,请重新输入')
            elif username == "" and password == "":
                flash("请输入修改信息")
            else:
                password_hash = generate_password_hash(password)
                admin.password = password_hash
                admin.username = username
                db.session.commit()
                return redirect("/Index")
        return render_template("admin_update.html", admin=admin)
    else:
        return redirect("/admin")


# 管理员删除
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def admin_delete(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        Admin.query.filter(Admin.id == id).delete()
        db.session.commit()
        return redirect("/Index")
    else:
        return redirect("/admin")


# 用户管理
@app.route('/user/', methods=['GET', 'POST'])
def admin_user():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        limit = 10
        page = request.args.get('page', 1, type=int)
        user = Users.query.paginate(page, per_page=limit)
        return render_template("user.html", user=user.items, pagination=user)
    else:
        return redirect("/admin")


# 修改用户
@app.route('/user_update/<int:id>', methods=['GET', 'POST'])
def user_update(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        user = Users.query.filter(Users.id == id).first()
        if request.method == "POST":
            password = request.form.get('password', '')
            if len(password) < 6:
                flash('密码长度太短,请重新输入')
            else:
                password_hash = generate_password_hash(password)
                user.password = password_hash
                db.session.commit()
                return redirect("/user")
        return render_template("user_update.html", user=user)
    else:
        return redirect("/admin")


# 用户删除
@app.route('/user_delete/<int:id>', methods=['GET', 'POST'])
def user_delete(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        Users.query.filter(Users.id == id).delete()
        db.session.commit()
        return redirect("/user")
    else:
        return redirect("/admin")


# 校园动态管理
@app.route('/trends/', methods=['GET', 'POST'])
def admin_trends():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        limit = 10
        page = request.args.get('page', 1, type=int)
        trends = Trends.query.order_by(Trends.pub_time.desc()).paginate(page, per_page=limit)
        return render_template("trends.html", trends=trends.items, pagination=trends)
    else:
        return redirect("/admin")


# 修改校园动态
@app.route('/trends_update/<int:id>', methods=['GET', 'POST'])
def trends_update(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        trends = Trends.query.filter(Trends.id == id).first()
        if request.method == "POST":
            title = request.form.get('title', '')
            if title == "":
                flash('请输入标题')
            else:
                trends.title = title
                db.session.commit()
                return redirect("/trends")
        return render_template("trends_update.html", trends=trends)
    else:
        return redirect("/admin")


# 删除校园动态
@app.route('/trends_delete/<int:id>', methods=['GET', 'POST'])
def trends_delete(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        Trends.query.filter(Trends.id == id).delete()
        db.session.commit()
        return redirect("/trends")
    else:
        return redirect("/admin")


# 添加校园动态
@app.route('/trends_add/', methods=['GET', 'POST'])
def trends_add():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        if request.method == "POST":
            title = request.form.get('title', '')
            pub_time = request.form.get('pub_time', '')
            url = request.form.get('url', '')
            if not all([title, pub_time, url]):
                flash('参数不全')
            else:
                new_trends = Trends(title=title, pub_time=pub_time, id=None, url=url)
                # 添加提交
                db.session.add(new_trends)
                db.session.commit()
                return redirect("/trends")
        return render_template("trend_add.html")
    else:
        return redirect("/admin")


# 资讯管理
@app.route('/informations/', methods=['GET', 'POST'])
def admin_informations():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        limit = 10
        page = request.args.get('page', 1, type=int)
        informations = Csdn.query.paginate(page, per_page=limit)
        return render_template("informations.html", informations=informations.items, pagination=informations)
    else:
        return redirect("/admin")


# 修改资讯
@app.route('/informations_update/<int:id>', methods=['GET', 'POST'])
def informations_update(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        informations = Csdn.query.filter(Csdn.id == id).first()
        if request.method == "POST":
            title = request.form.get('title', '')
            name = request.form.get('name', '')
            content = request.form.get('content', '')
            if title == "":
                flash('请输入标题')
            else:
                informations.title = title
                informations.name = name
                informations.content = content
                db.session.commit()
                return redirect("/informations")
        return render_template("informations_update.html", informations=informations)
    else:
        return redirect("/admin")


# 删除资讯
@app.route('/informations_delete/<int:id>', methods=['GET', 'POST'])
def informations_delete(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        Csdn.query.filter(Csdn.id == id).delete()
        db.session.commit()
        return redirect("/informations")
    else:
        return redirect("/admin")


# 添加资讯
@app.route('/informations_add/', methods=['GET', 'POST'])
def informations_add():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        if request.method == "POST":
            title = request.form.get('title', '')
            name = request.form.get('name', '')
            content = request.form.get('content', '')
            url = request.form.get('url', '')
            label = request.form.getlist('label')
            print(title, name, content, label, url)
            if not all([title, name, content, label, url]):
                flash('参数不全')
            else:
                label = ",".join(label)
                print(label)
                new_informations = Csdn(title=title, name=name, content=content, url=url, label=label, browse=0,
                                        likes=0,
                                        difference=0, popular=0, id=None)
                # 添加提交
                db.session.add(new_informations)
                db.session.commit()
                return redirect("/informations")
        return render_template("informations_add.html")
    else:
        return redirect("/admin")


# 图书管理
@app.route('/books/', methods=['GET', 'POST'])
def admin_books():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        limit = 10
        page = request.args.get('page', 1, type=int)
        books = Douban.query.paginate(page, per_page=limit)
        return render_template("books.html", books=books.items, pagination=books)
    else:
        return redirect("/admin")


# 修改图书
@app.route('/books_update/<int:id>', methods=['GET', 'POST'])
def books_update(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        books = Douban.query.filter(Douban.id == id).first()
        if request.method == "POST":
            book_name = request.form.get('book_name', '')
            author = request.form.get('author', '')
            content = request.form.get('content', '')
            publication = request.form.get('publication', '')
            if not all([book_name, author, content, publication]):
                flash('参数不完')
            else:
                book.book_name = book_name
                book.author = author
                book.content = content
                book.publication = publication
                db.session.commit()
                return redirect("/books")
        return render_template("books_update.html", books=books)
    else:
        return redirect("/admin")


# 删除图书
@app.route('/books_delete/<int:id>', methods=['GET', 'POST'])
def books_delete(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        Douban.query.filter(Douban.id == id).delete()
        db.session.commit()
        return redirect("/books")
    else:
        return redirect("/admin")


# 添加图书
@app.route('/books_add/', methods=['GET', 'POST'])
def books_add():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        if request.method == "POST":
            book_name = request.form.get('book_name', '')
            author = request.form.get('author', '')
            content = request.form.get('content', '')
            publication = request.form.get('publication', '')
            url = request.form.get('url', '')
            label = request.form.get('label', "")
            if not all([book_name, author, content, label, url, publication]):
                flash('参数不全')
            else:
                img_url = "https://img2.doubanio.com/view/subject/s/public/s4172692.jpg"
                time = str(datetime.date.today())
                new_informations = Douban(book_name=book_name, author=author, content=content, url=url, label=label,
                                          img_url=img_url, price=8, publication=publication, time=time,
                                          popular=0, id=None)
                # 添加提交
                db.session.add(new_informations)
                db.session.commit()
                return redirect("/books")
        return render_template("books_add.html")
    else:
        return redirect("/admin")


# 校园风光管理
@app.route('/scenes/', methods=['GET', 'POST'])
def admin_scenes():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        limit = 10
        page = request.args.get('page', 1, type=int)
        scenes = Scene.query.order_by(Scene.time.desc()).paginate(page, per_page=limit)
        return render_template("scenes.html", scenes=scenes.items, pagination=scenes)
    else:
        return redirect("/admin")


# 修改校园风光
@app.route('/scenes_update/<int:id>', methods=['GET', 'POST'])
def scenes_update(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        scenes = Scene.query.filter(Scene.id == id).first()
        if request.method == "POST":
            title = request.form.get('title', '')
            img_url = request.form.get('ing_url', '')
            if img_url == "":
                scenes.title = title
            elif title == "":
                scenes.img_url = img_url
            else:
                scenes.title = title
                scenes.img_url = img_url
            db.session.commit()
            return redirect("/scenes")
        return render_template("scenes_update.html", scenes=scenes)
    else:
        return redirect("/admin")


# 删除校园风光
@app.route('/scenes_delete/<int:id>', methods=['GET', 'POST'])
def scenes_delete(id):
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        Scene.query.filter(Scene.id == id).delete()
        db.session.commit()
        return redirect("/scenes")
    else:
        return redirect("/admin")


# 添加校园风光
@app.route('/scenes_add/', methods=['GET', 'POST'])
def scenes_add():
    admin_is_login = session.get("admin", "")
    if admin_is_login:
        if request.method == "POST":
            title = request.form.get('title', '')
            time = request.form.get('time', '')
            img_url = request.form.get('img_url', '')
            if not all([title, time, img_url]):
                flash('参数不全')
            else:
                new_scene = Scene(title=title, time=time, id=None, img_url=img_url)
                # 添加提交
                db.session.add(new_scene)
                db.session.commit()
                return redirect("/scenes")
        return render_template("scenes_add.html")
    else:
        return redirect("/admin")


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
    if session.get("admin", ""):
        session.pop("admin", None)
        return redirect('/admin')
    elif session.get("username", ""):
        session.pop("username", None)
        return redirect("/")
    else:
        session.pop("username", None)
        return redirect('/')


# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    limit = 10
    page = request.args.get('page', 1, type=int)
    data_trend = Trends.query.order_by(Trends.pub_time.desc()).paginate(page, per_page=limit)
    data = aside()
    return render_template("index.html", trends=data_trend.items, douban=data[0],
                           saying=data[1], pagination=data_trend)


# 查找校园热点
@app.route('/find_trends', methods=['GET', 'POST'])
def find_trends(limit=10):
    keyword = request.args.get('search')
    if keyword == "":
        return redirect(url_for("/"))
    page = request.args.get('page', 1, type=int)
    data_trend = Trends.query.filter(Trends.title.contains(keyword)).order_by(
        Trends.pub_time.desc()).paginate(page, per_page=limit)
    data = aside()
    return render_template("index.html", trends=data_trend.items, douban=data[0],
                           saying=data[1], pagination=data_trend)


# 校园风光
@app.route('/scene/')
def scene():
    limit = 9
    page = request.args.get('page', 1, type=int)
    data_scene = Scene.query.order_by(func.rand()).paginate(page, per_page=limit)
    data = aside()
    return render_template("scene.html", scene=data_scene.items, douban=data[0],
                           saying=data[1], pagination=data_scene)


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
    return render_template("book.html", book=book.items, douban=data[0],
                           saying=data[1], pagination=book)


# 查找图书，并分页显示
@app.route("/find_book/")
def find_book(limit=10):
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
        return render_template("book.html", book=pagination.items, douban=data[0],
                               saying=data[1], pagination=pagination)


# 查找资讯，并分页显示
@app.route("/find_csdn/")
def find_csdn(limit=8):
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
    data = Csdn.query.filter(Csdn.id == id).first()
    try:
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


# 个性化推荐 资讯
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
        information_recommend = InformationItemRecommends(user_id).recommend(num)
        start = (page - 1) * limit
        finish = page * limit
        information_data = information_recommend[start:finish]
        return render_template("recommend_information.html", information=information_data, pagination=pagination)
    return redirect("/")


# 个性化推荐 图书
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
        book_recommend = BookItemRecommends(user_id).recommend(num)
        start = (page - 1) * limit
        finish = page * limit
        book_data = book_recommend[start:finish]
        return render_template("recommend_book.html", book=book_data, pagination=pagination)
    return redirect("/")


# 资讯浏览记录 图表
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
        data_csdns = []
        for i in data_csdn:
            data_csdns.append(Csdn.query.filter(Csdn.id == i.information_id).first())
        page_view = []
        echarts = RecordInformation.query.filter(RecordInformation.user_id == users.id).all()
        for i in echarts:
            page_view.append(Counter({
                i.time.strftime("%Y/%m/%d"): 1
            }))
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
            Csdn.id.in_(information_id)
        ).paginate(page, per_page=limit)
        return render_template("recording_information.html", data_csdn=pagination.items, csdn=pagination, date=date,
                               data=data)


# 图书浏览记录
@app.route("/recording_book/")
def recording_book():
    try:
        page = request.args.get('page', 1, type=int)
        limit = 8
        user = session.get("username")
        users = Users.query.filter(Users.username == user).first()
        recording_book = RecordBook.query.filter(RecordBook.user_id == users.id).order_by(
            RecordBook.id.desc()).paginate(page, per_page=limit)
        data_book = recording_book.items
        data_books = []
        for i in data_book:
            data_books.append(Douban.query.filter(Douban.id == i.book_id).first())
        page_view = []
        echarts = RecordBook.query.filter(RecordBook.user_id == users.id).all()
        for i in echarts:
            page_view.append(Counter({
                i.time.strftime("%Y/%m/%d"): 1
            }))
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


@app.route("/feedback/", methods=['get', 'post'])
def feedback():
    if request.method == 'POST':
        username = session.get("username")
        if username:
            score = request.form.get("score")
            feedbacks = request.form.get("feedback")
            print(score, feedbacks)
            if score:
                score = int(score)
                if score not in range(1, 11):
                    return redirect("/feedback/")
                elif len(feedbacks) >= 100:
                    return redirect("/feedback/")
                else:
                    user = Users.query.filter(Users.username == username).first()
                    new_feedback = Feedback(user_id=user.id, score=score, feedback=feedbacks)
                    db.session.add(new_feedback)
                    db.session.commit()
                    return "提交成功"
            return redirect("/feedback/")
        return redirect("/feedback/")
    return render_template("feedback.html")


# 个性化调差问卷
@app.route('/questionnaire/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        # data = {1: True, 0: False}
        data = {"True": True, "False": False}
        d_1 = data.get(request.form.get("1"))
        d_2 = data.get(request.form.get("2"))
        d_3 = data.get(request.form.get("3"))
        d_4 = data.get(request.form.get("4"))
        # d_1 = request.form.get("2")
        # d_2 = request.form.get("3")
        # d_3 = request.form.get("4")
        # d_4 = request.form.get("5")
        d_5 = request.form.get("5")
        if all([d_1, d_2, d_3, d_4]):
            flash("参数不全")
        new_questionnaire = Questionnaire(d_1=d_1, d_2=d_2, d_3=d_3, d_4=d_4, d_5=d_5)
        db.session.add(new_questionnaire)
        db.session.commit()
        return redirect("/recommend_information")
    return render_template('questionnaire.html')


if __name__ == '__main__':
    app.run(debug=True)
