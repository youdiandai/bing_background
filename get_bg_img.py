#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2019/1/14'
"""
import requests
import datetime
import os
import bs4

URL = "http://www.bing.com"


def create_download_folder():
    base_path = os.path.join(os.getcwd(), 'download')
    if not os.path.exists(base_path):
        os.mkdir(base_path)


def save_img(img_response):
    """
    save img from response
    :param img_response: response created by requests
    :return:
    """
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    img_name = time + '.jpg'
    with open(os.path.join('download', img_name), 'wb') as f:
        f.write(img_response.content)


def get_img_url():
    r = requests.get(URL)
    bsOjb = bs4.BeautifulSoup(r.text, features="html.parser")
    url_tag = bsOjb.find('img', id='bgImg')
    img_url = URL + url_tag.attrs['src']
    return img_url


def get_bg_img():
    create_download_folder()
    img_url = get_img_url()
    r = requests.get(img_url)
    save_img(r)


if __name__ == '__main__':
    get_bg_img()
