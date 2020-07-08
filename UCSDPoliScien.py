# -*- coding:utf-8 _*-
""" 
@author: Leo Yang
@license: Apache Licence 
@file: UCSDPoliScien.py 
@createtime: 2020-07-03 21:40
@contact: leoyang@ucsd.edu
@site: www.leoyang.org
"""

import requests


class UCSDPoliScien:
    def __init__(self):
        # fill in your url
        self.url = 'https://polisci.ucsd.edu/grad/current-students/index.html'

    def send_get_request(self, url):
        r = requests.get(url)
        if r.text:
            html_result = r.text
            print('get result success')
            return html_result
        else:
            print('get result fail')
            return ''

    # Put all the things together
    def run(self):
        html_result = self.send_get_request(self.url)
        # write the context into a file
        with open('ucsd_result.html', 'w') as output_f:
            output_f.write(html_result)
        print('The result is written in file ucsd_result.html')


if __name__ == '__main__':
    runner = UCSDPoliScien()
    runner.run()
