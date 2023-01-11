import os
from selenium import webdriver
import time
import json
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
from argparse import ArgumentParser

if not os.path.exists('data'):
    os.mkdir('data')

parser = ArgumentParser()
parser.add_argument('--topic', type=str)
parser.add_argument('--visible', action='store_true')
parser.add_argument('--page', type=int, default=50)
parser.add_argument('--sleep', type=int, default=2)
args = parser.parse_args()

topic = args.topic
visible = args.visible
pages = args.page
sleep = args.sleep

cnt = 0
while True:
    if os.path.exists('data/{}_{}.json'.format(topic, cnt)):
        cnt += 1
    else:
        break
save_path = 'data/{}_{}.json'.format(topic, cnt)

assert topic is not None

file = 'cookies.json'
if not visible:
    options = Options()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
else:
    driver = webdriver.Chrome(executable_path='chromedriver.exe')


def get_cookies(test_url):
    driver.get(test_url)
    driver.maximize_window()
    input('是否已经登陆微博账号，登陆成功后，输入任意键并回车')
    time.sleep(sleep)
    cookies = driver.get_cookies()
    json.dump(cookies, open(file, 'w'))
    driver.close()


def add_cookies():
    cookies = json.load(open(file))
    for cookie in cookies:
        driver.add_cookie(cookie)


if __name__ == "__main__":
    # get_cookies('https://weibo.com/login.php')
    # exit(0)
    topic_url = 'https://s.weibo.com/weibo?q={}'.format(topic)
    driver.get(topic_url)
    time.sleep(sleep)
    add_cookies()
    driver.refresh()
    time.sleep(sleep)
    data = []
    pbar = tqdm(range(pages), ncols=0)
    pbar.set_description_str('crawling {}'.format(topic))
    for _ in pbar:
        data_url = '{}&page={}'.format(topic_url, _ + 1)
        driver.get(data_url)
        time.sleep(sleep)
        content = driver.find_elements_by_class_name('card-feed')
        for item in content:
            user = item.find_element_by_xpath('div[1]/a')
            data.append(
                {
                    'user_url': user.get_attribute('href'),
                    'text': item.find_element_by_class_name('txt').text
                }
            )
        json.dump(data, open(save_path, 'w', encoding='utf-8'))
    print(len(data))
    driver.close()


