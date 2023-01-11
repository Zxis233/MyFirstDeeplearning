import os.path
import time
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm


file = 'cookies.json'
options = Options()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)


def add_cookies():
    cookies = json.load(open(file))
    for cookie in cookies:
        driver.add_cookie(cookie)


def get_friends(uid, pages):
    res = []
    for _ in range(pages):
        driver.get('https://weibo.com/ajax/friendships/friends?page={}&uid={}'.format(_ + 1, uid))
        driver.implicitly_wait(5)
        cnt = 0
        while True:
            if cnt == 3:
                content = {}
                break
            try:
                content = driver.find_element_by_xpath('/html/body/pre')
                content = json.loads(content.text)
                break
            except NoSuchElementException:
                driver.refresh()
                time.sleep(1)
                cnt += 1
        if 'users' in content:
            res += content['users']
        else:
            res.append(content)
    return res


def get_fans(uid, pages):
    res = []
    for _ in range(pages):
        driver.get('https://weibo.com/ajax/friendships/friends?relate=fans&page={}&uid={}&type=fans&newFollowerCount=0'
                   .format(_ + 1, uid))
        driver.implicitly_wait(5)
        cnt = 0
        while True:
            if cnt == 3:
                content = {}
                break
            try:
                content = driver.find_element_by_xpath('/html/body/pre')
                content = json.loads(content.text)
                break
            except NoSuchElementException:
                driver.refresh()
                time.sleep(1)
                cnt += 1
        if 'users' in content:
            res += content['users']
        else:
            res.append(content)
    return res


if __name__ == '__main__':
    uids = json.load(open('users_Sep.json'))
    driver.get('https://weibo.com/ajax/friendships/friends?relate=fans&page={}&uid={}&type=fans&newFollowerCount=0'
               .format(1, uids[0]))
    time.sleep(5)
    add_cookies()
    driver.refresh()
    for uid in tqdm(uids, ncols=0):
        save_path = 'neighbor/{}.json'.format(uid)
        if os.path.exists(save_path):
            continue
        data = {
            'friends': get_friends(uid, 5),
            'fans': get_fans(uid, 5)
        }
        json.dump(data, open(save_path, 'w'))
        time.sleep(3)
