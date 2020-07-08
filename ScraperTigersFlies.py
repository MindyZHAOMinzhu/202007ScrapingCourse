# -*- coding:utf-8 _*-
""" 
@author: Leo Yang
@license: Apache Licence 
@file: ScraperTigersFlies.py 
@createtime: 2020-07-04 16:07
@contact: leoyang@ucsd.edu
@site: www.leoyang.org
"""

import requests


class ScraperTigersFlies(object):
    def __init__(self):
        pass

    def function_1(self):
        result_1 = 'My '
        return result_1

    def function_2(self):
        result_2 = 'First '
        return result_2

    def function_3(self):
        result_3 = 'Scraper!'
        return result_3

    def run(self):
        print(self.function_1() + self.function_2() + self.function_3())


if __name__ == '__main__':
    runner = ScraperTigersFlies()
    runner.run()
