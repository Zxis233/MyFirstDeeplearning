import os

if __name__ == '__main__':
    keywords = ['绿卡', '封城 静默', '不明原因 急性肝炎', 'MU5735', '医院关闭', '哈尔滨洗车摊', 
    '博士 协警', '地震前兆','投资养老', 'SPF指数']
    for keyword in keywords:
        command = 'python topic.py --topic "{}" --page 500 --sleep 1'.format(keyword)
        os.system(command)
