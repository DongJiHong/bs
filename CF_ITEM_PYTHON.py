# coding:utf-8
import difflib

from conf import Csdn, Douban, Users, RecordInformation, RecordBook, db, Recommend, RecommendItem

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


class InformationItemRecommends:
    def __init__(self, user_id):
        self.user_id = user_id

    # 获取用户label
    def _label_user(self):
        user_id = self.user_id
        user = Users.query.filter(Users.id == user_id).first()
        label = set()
        label.update(user.label.split(','))
        return label

    # 获取咨询label
    def _label_item(self):
        user_id = self.user_id
        recommend = Recommend.query.filter(Recommend.user_id == user_id, Recommend.genre == 1).order_by(
            Recommend.id.desc()).first()
        recommend_item = RecommendItem.query.filter(RecommendItem.recommend_id == recommend.id)
        item_id = [i.info_id for i in recommend_item]
        info = Csdn.query.filter(Csdn.id.in_(item_id))
        label = set()
        for i in info:
            label.update(i.label.split(','))
        return label

    # 筛选数据
    def _filter(self, recommend):
        if recommend == 0:
            labels = self._label_user()
        elif recommend == 1:
            labels = self._label_item()
        datas = set()
        for label in labels:
            information = Csdn.query.filter(Csdn.label.contains(label))
            for infor in information:
                datas.add(infor)
        return datas, labels

    # 计算相似度
    def _similarity(self, recommend):
        if recommend == 0:
            data_label = self._filter(recommend=0)
        elif recommend == 1:
            data_label = self._filter(recommend=1)
        datas = data_label[0]
        label = list(data_label[1])
        score = dict()
        for data in datas:
            info_label = list(data.label.split(','))
            sm = difflib.SequenceMatcher(None, label, info_label)
            score[data.id] = sm.ratio()
        return score

    # 排序，删除已推荐、已浏览
    def _score(self, recommend):
        if recommend == 0:
            score = self._similarity(recommend=0)
            read_history = RecordInformation.query.filter(RecordInformation.user_id == self.user_id)
            for i in read_history:
                if i.information_id in score.keys():
                    score.pop(i.information_id)
            data = sorted(score.items(), key=lambda kv: (kv[1], kv[0]))
            return data
        elif recommend == 1:
            score = self._similarity(recommend=1)
            read_history = RecordInformation.query.filter(RecordInformation.user_id == self.user_id)
            recommend_id = [i.id for i in Recommend.query.filter(
                Recommend.user_id == self.user_id, Recommend.genre == 1)]
            recommend_history = RecommendItem.query.filter(RecommendItem.recommend_id.in_(recommend_id))
            for i in read_history:
                if i.information_id in score.keys():
                    score.pop(i.information_id)
            for i in recommend_history:
                if i.info_id in score.keys():
                    score.pop(i.info_id)
            data = sorted(score.items(), key=lambda kv: (kv[1], kv[0]))
            return data

    # 推荐，并写入DB
    def recommend(self, num=50):
        r = Recommend.query.filter(Recommend.user_id == self.user_id, Recommend.genre == 1).order_by(Recommend.id.desc()
                                                                                                     ).first()
        # 是否推荐
        if r:
            data = self._score(recommend=1)
        else:
            data = self._score(recommend=0)
        if len(data) < num:
            datas = data
        else:
            datas = data[-num:]
        new_recommend = Recommend(user_id=self.user_id, genre=1)
        db.session.add(new_recommend)
        db.session.commit()
        new_recommend_id = Recommend.query.filter(Recommend.user_id == self.user_id, Recommend.genre == 1
                                                  ).order_by(Recommend.id.desc()).first().id
        info_data = []
        for info_id in datas:
            info_data.append(Csdn.query.filter(Csdn.id == info_id[0]).first())
            new_recommend_item = RecommendItem(recommend_id=new_recommend_id, info_id=info_id[0])
            db.session.add(new_recommend_item)
        db.session.commit()
        return info_data


class BookItemRecommends:
    def __init__(self, user_id):
        self.user_id = user_id

    # 获取用户label
    def _label_user(self):
        user_id = self.user_id
        user = Users.query.filter(Users.id == user_id).first()
        label = set()
        label.update(user.label.split(','))
        return label

    # 获取图书label
    def _label_item(self):
        user_id = self.user_id
        recommend = Recommend.query.filter(Recommend.user_id == user_id, Recommend.genre == 0).order_by(
            Recommend.id.desc()).first()
        recommend_item = RecommendItem.query.filter(RecommendItem.recommend_id == recommend.id)
        item_id = [i.info_id for i in recommend_item]
        info = Douban.query.filter(Douban.id.in_(item_id))
        label = set()
        for i in info:
            label.update(i.label.split(','))
        return label

    # 筛选数据
    def _filter(self, recommend):
        labels = None
        if recommend == 0:
            labels = self._label_user()
        elif recommend == 1:
            labels = self._label_item()
        datas = set()
        for label in labels:
            information = Douban.query.filter(Douban.label.contains(label))
            for infor in information:
                datas.add(infor)
        return datas, labels

    # 计算相似度
    def _similarity(self, recommend):
        data_label = None
        if recommend == 0:
            data_label = self._filter(recommend=0)
        elif recommend == 1:
            data_label = self._filter(recommend=1)
        datas = data_label[0]
        label = list(data_label[1])
        score = dict()
        for data in datas:
            info_label = list(data.label.split(','))
            sm = difflib.SequenceMatcher(None, label, info_label)
            score[data.id] = sm.ratio()
        return score

    # 排序，删除已推荐、已浏览
    def _score(self, recommend):
        if recommend == 0:
            score = self._similarity(recommend=0)
            read_history = RecordBook.query.filter(RecordBook.user_id == self.user_id)
            for i in read_history:
                if i.book_id in score.keys():
                    score.pop(i.book_id)
            data = sorted(score.items(), key=lambda kv: (kv[1], kv[0]))
            return data
        elif recommend == 1:
            score = self._similarity(recommend=1)
            read_history = RecordBook.query.filter(RecordBook.user_id == self.user_id)
            recommend_id = [i.id for i in
                            Recommend.query.filter(Recommend.user_id == self.user_id, Recommend.genre == 0)]
            recommend_history = RecommendItem.query.filter(RecommendItem.recommend_id.in_(recommend_id))
            for i in read_history:
                if i.book_id in score.keys():
                    score.pop(i.book_id)
            for i in recommend_history:
                if i.info_id in score.keys():
                    score.pop(i.info_id)
            data = sorted(score.items(), key=lambda kv: (kv[1], kv[0]))
            return data

    # 推荐，并写入DB
    def recommend(self, num=50):
        r = Recommend.query.filter(Recommend.user_id == self.user_id, Recommend.genre == 0).order_by(Recommend.id.desc()
                                                                                                     ).first()
        # 是否推荐
        if r:
            data = self._score(recommend=1)
        else:
            data = self._score(recommend=0)
        if len(data) < num:
            datas = data
        else:
            datas = data[-num:]
        info_data = []
        new_recommend = Recommend(user_id=self.user_id, genre=0)
        db.session.add(new_recommend)
        db.session.commit()
        new_recommend_id = Recommend.query.filter(Recommend.user_id == self.user_id, Recommend.genre == 0
                                                  ).order_by(Recommend.id.desc()).first().id
        for info_id in datas:
            info_data.append(Douban.query.filter(Douban.id == info_id[0]).first())
            new_recommend_item = RecommendItem(recommend_id=new_recommend_id, info_id=info_id[0])
            db.session.add(new_recommend_item)
        db.session.commit()
        return info_data
