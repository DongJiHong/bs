import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/bs"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class ImageUrl:
    def __init__(self):
        pass

    @staticmethod
    def random_num():
        num = random.randint(4, 8)
        nums = "blog" + str(num)
        return nums


app.add_template_global(ImageUrl.random_num, "buildImageUrl")


# 定义一个用户及密码的数据库
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    label = db.Column(db.Text)  # 资讯标签


# csdn 资讯
class Csdn(db.Model):
    __tablename__ = "csdn"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(255))  # 链接
    title = db.Column(db.String(1000))  # 标题
    name = db.Column(db.String(50))  # 名字
    content = db.Column(db.Text)  # 简介
    label = db.Column(db.String(255))  # 标签
    browse = db.Column(db.Integer)  # 浏览量
    likes = db.Column(db.Integer)  # 喜欢
    difference = db.Column(db.Integer)  # 踩
    popular = db.Column(db.Integer)  # 流行度


# 资讯点赞踩记录
class Behavior(db.Model):
    __tablename__ = "behavior_information"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)  # 用户ID
    information_id = db.Column(db.Integer)  # 资讯id
    behavior = db.Column(db.Integer)  # 0 踩 1 赞


# 豆瓣图书
class Douban(db.Model):
    __tablename__ = "douban"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    author = db.Column(db.String(255))  # 作者
    book_name = db.Column(db.String(500))  # 书名
    content = db.Column(db.Text)  # 简介
    img_url = db.Column(db.String(255))  # 图片url
    label = db.Column(db.String(255))  # 标签
    price = db.Column(db.String(255))  # 价格
    publication = db.Column(db.String(500))  # 出版社
    score = db.Column(db.Integer)  # 评分
    time = db.Column(db.String(50))  # 发布时间
    url = db.Column(db.String(255))  # url
    popular = db.Column(db.Integer)  # 流行度


# 资讯用户访问记录
class RecordInformation(db.Model):
    __tablename__ = "record_information"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    information_id = db.Column(db.Integer)
    time = db.Column(db.Date)


# 图书用户访问记录
class RecordBook(db.Model):
    __tablename__ = "record_book"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    time = db.Column(db.Date)


# 名人名言
class Saying(db.Model):
    __tablename__ = "saying"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    author = db.Column(db.String(100))  # 作者
    content = db.Column(db.Text)  # 内容


# 校园动态
class Trends(db.Model):
    __tablename__ = "trends"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(1000))  # 标题
    pub_time = db.Column(db.String(50))  # 发布时间
    url = db.Column(db.String(100))  # 详情页url


# 校园风光
class Scene(db.Model):
    __tablename__ = "scene"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(1000))  # title
    img_url = db.Column(db.String(100))  # 图片url
    time = db.Column(db.String(50))


# 推荐评分表篇
class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)
    feedback = db.Column(db.String(1000))


# 推荐表
class Recommend(db.Model):
    __tablename__ = "recommend"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    genre = db.Column(db.Integer)  # 0-book 1-information


# 推荐结果表
class RecommendItem(db.Model):
    __tablename__ = "recommend_item"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recommend_id = db.Column(db.Integer)
    info_id = db.Column(db.Integer)


# 定义一个用户及密码的数据库
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    grade = db.Column(db.Boolean)


# 旁白推荐和名言
def aside():
    data_douban = Douban.query.filter().order_by(func.rand()).limit(9)
    data_saying = Saying.query.filter().order_by(func.rand()).limit(1)
    data = [data_douban, data_saying]
    return data


class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    d_1 = db.Column(db.Boolean)
    d_2 = db.Column(db.Boolean)
    d_3 = db.Column(db.Boolean)
    d_4 = db.Column(db.Boolean)
    d_5 = db.Column(db.Text)
