# -*- coding: utf-8 -*-
# @Time : 2019/11/25 上午10:44
# @Author : guofei
# @File : test001.py
# @Projcet :
# @Software: PyCharm


from sklearn.model_selection import validation_curve
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor, BaggingClassifier, BaggingRegressor, GradientBoostingClassifier,GradientBoostingRegressor
from sklearn.ensemble import IsolationForest, VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine

class Dog(object):
    def __init__(self, face="lily", voice="load",action ='sprawn'):
        self.face = face
        self.voice = voice
        self.action = action


class Cat(Dog):
    def __init__(self, voice='low', action='kick'):
        super(Cat, self).__init__( voice=voice, action=action)

if __name__ == '__main__':
    wine = load_wine()
    X = wine.data
    y = wine.target

    clf = RandomForestClassifier(n_estimators=20, random_state=43)
    clf.fit(X, y)
    for i in range(20):
        print(clf.estimators_[i].random_state)
