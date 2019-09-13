#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#类名通常是大写字母开头，紧接着（object）表示该类是从哪个类继承下来的
class Student(object):
    #self指向创建的实例本身 第一个实例参数永远是self，并且调用时，不用传该参数
    def __init__(self, name, score):
        self._name = name
        self._score = score
    def print_score(self):
        print('%s: %s' % (self._name, self._score))
    def get_grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

class Animal(object):
    def run(self):
        print('animal is running ......')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
