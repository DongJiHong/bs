# coding:utf-8
import difflib
from conf import Csdn, Douban, Users, RecordInformation, RecordBook

"""
     # information
     初始化获得传入的用户id，根据用户id查询用户的label
     根据label筛选出有相同字段的数据
     再根据label组成的列表计算数据的相似度，
     针对相识度进行排序，去除用户已经浏览的，取最高的 {{ ## }} 条数据，返回推荐数据
     
     # book
     初始化获得传入的用户id，根据用户id查询用户的label
     根据label筛选出有相同字段的数据
     再根据label组成的列表计算数据的相似度，
     针对相识度和评分进行排序，去除用户已经浏览的，取最高的 {{ ## }} 条数据，返回推荐数据
"""


class InformationItemRecommend:
    def __init__(self, user_id):
        self.user_id = user_id

    # 获取label
    def _labels(self):
        user_id = self.user_id
        user = Users.query.filter(Users.id == user_id).first()
        label = set()
        label.update(user.label.split(','))
        # behaviors = Behavior.query.filter(Behavior.user_id == user_id)
        # records = RecordInformation.query.filter(Behavior.user_id == user_id)
        # print(behaviors, records)
        # information_id = set()
        # for behavior in behaviors:
        #     information_id.add(behavior.information_id)
        # for record in records:
        #     information_id.add(record.information_id)
        # information_label = set()
        # for i in information_id:
        #     information = Csdn.query.filter(Csdn.id == i).first()
        #     print(information.label)
        #     # information_label.update(information.label.split(','))
        # print(information_label)
        return label

    # 根据label筛选数据
    def _filter(self):
        labels = self._labels()
        datas = set()
        for label in labels:
            information = Csdn.query.filter(Csdn.label.contains(label))
            for infor in information:
                datas.add(infor)
        return datas, labels

    # 比较数据相似性
    def _similarity(self):
        data_label = self._filter()
        datas = data_label[0]
        label = list(data_label[1])
        score = dict()
        for data in datas:
            info_label = list(data.label.split(','))
            sm = difflib.SequenceMatcher(None, label, info_label)
            score[data.id] = sm.ratio()
        return score

    # 对相似性结果排序,并删除用户已经浏览过的
    def _score(self):
        score = self._similarity()
        read_history = RecordInformation.query.filter(RecordInformation.user_id == self.user_id)
        for i in read_history:
            if i.information_id in score.keys():
                score.pop(i.information_id)
        data = sorted(score.items(), key=lambda kv: (kv[1], kv[0]))
        return data

    # 返回推荐结果,默认相似度最高的20条
    def recommend(self, num=20):
        datas = self._score()[-num:]
        info_data = []
        for info_id in datas:
            info_data.append(Csdn.query.filter(Csdn.id == info_id[0]).first())
        return info_data


class BookItemRecommend:
    def __init__(self, user_id):
        self.user_id = user_id

    # 获取label
    def _labels(self):
        user_id = self.user_id
        user = Users.query.filter(Users.id == user_id).first()
        label = set()
        label.update(user.label.split(','))
        return label

    # 根据label筛选数据
    def _filter(self):
        labels = self._labels()
        datas = set()
        for label in labels:
            information = Douban.query.filter(Douban.label.contains(label))
            for infor in information:
                datas.add(infor)
        return datas, labels

    # 比较数据相似性
    def _similarity(self):
        data_label = self._filter()
        datas = data_label[0]
        label = list(data_label[1])
        score = dict()
        for data in datas:
            info_label = list(data.label.split(','))
            sm = difflib.SequenceMatcher(None, label, info_label)
            score[data.id] = [sm.ratio(), data.score]
        return score

    # 对相似性结果排序,并删除用户已经浏览过的
    def _score(self):
        score = self._similarity()
        read_history = RecordBook.query.filter(RecordBook.user_id == self.user_id)
        for i in read_history:
            if i.book_id in score.keys():
                score.pop(i.book_id)
        data = sorted(score.items(), key=lambda kv: (kv[1][0], kv[1][1], kv[0]))
        return data

    # 返回推荐结果,默认相似度最高的20条
    def recommend(self, num=20):
        datas = self._score()[-num:]
        info_data = []
        for info_id in datas:
            info_data.append(Douban.query.filter(Douban.id == info_id[0]).first())
        return info_data
