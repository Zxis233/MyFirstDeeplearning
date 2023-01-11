import datetime
import os
import re

import pandas as pd
import httpx
from jsonpath import jsonpath


def trans_time(v_str):
    # 转换GMT时间为标准格式
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
    ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time


def get_weibo_list(v_keyword, v_max_page):
    # v_keyword 搜索关键字 v_max_page 爬取前几页
    # 请求地址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
    }
    # for page in range(1, v_max_page + 1):
    for page in range(1, 2):
        print('开始爬取第{}页微博'.format(page))
        # 请求地址
        url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type=1&q=乌鲁木齐火灾&page_type=searchall'
        # 请求参数
        params = {
            "containerid": "100103type=1&q={}".format(v_keyword),
            "page_type": "searchall",
            "page": page
        }
        # 发送请求
        r = httpx.get(url, headers=headers, params=params)
        print(r.status_code)
        cards = r.json()["data"]["cards"]
        text_list = jsonpath(cards, '$..mblog.text')  # 微博内容
        dr = re.compile(r'<[^>]+', re.S)  # 正则表达式数据清洗
        text_list2 = []
        print('text_list is:')
        print(text_list)
        if not text_list:  # 如果未获取
            continue
        if type(text_list) == list and len(text_list) > 0:
            for text in text_list:
                text2 = dr.sub('', text)  # 正则表达式提取微博内容
                print(text2)
                text_list2.append(text2)
        # 微博创建时间
        time_list = jsonpath(cards, '$..mblog.created_at')
        # time_list = [trans_time(v_str=i) for i in text_list]
        # 用户信息
        id_list = jsonpath(cards, '$..mblog.id')
        screen_name_list = jsonpath(cards, '$..mblog.user.screen_name')
        follow_count_list = jsonpath(cards, '$..mblog.user.follow_count')
        followers_count_list = jsonpath(cards, '$..mblog.user.followers_count')
        verified_list = jsonpath(cards, '$..mblog.user.verified')
        description_list = jsonpath(cards, '$..mblog.user.description')

        # df = pd.DataFrame(
        #     {
        #         'id': id_list,
        #         'screen_name': screen_name_list,
        #         'followers_count': followers_count_list,
        #         'follow_count': follow_count_list,
        #         'verified': verified_list,
        #         'description': description_list,
        #         'text': text_list2,
        #         'time': time_list,
        #     }
        # )

        print(len(id_list))
        print(len(screen_name_list))
        print(len(follow_count_list))
        print(len(followers_count_list))
        print(len(verified_list))
        print(len(description_list))

        if os.path.exists(weibo_file):
            header = None
        else:
            header = ['id', 'screen_name', 'followers_count', 'follow_count', 'verified', 'description', 'text', 'time']
        # df.to_csv(weibo_file, mode='a+', index=False, header=header, encoding='utf_8_sig')


if __name__ == '__main__':
    max_search_page = 10
    search_keyword = '乌鲁木齐火灾'
    weibo_file = '微博清单_{}_前{}页.csv'.format(search_keyword, max_search_page)
    if os.path.exists(weibo_file):
        os.remove(weibo_file)
        print('微博清单存在，已删除:{}'.format(weibo_file))
    get_weibo_list(v_keyword=search_keyword, v_max_page=max_search_page)
    # 清洗重复数据
    # df = pd.read_csv(weibo_file)
    # df.drop_duplicates(subset=[''], inplace=True, keep='first')
    # df.to_csv(weibo_file, index=False, encoding='utf_8_sig')


    # path = Service('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
    # driver = webdriver.Chrome(service=path)

    # driver.get('https://www.bilibili.com')
    # time.sleep(3)
    # print(driver.title)
    # driver = webdriver.Chrome()
    # 上面是配置好环境变量的写法，也可用绝对路径
