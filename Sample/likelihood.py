import json
import os


def calc_username_likelihood(username, bi_gram_likelihood):
    ans = 1
    for index in range(len(username) - 1):
        bi_gram = username[index] + username[index+1]
        ans *= bi_gram_likelihood[bi_gram] ** (1.0 / (len(username) - 1))
    return ans


if __name__ == '__main__':
    likelihood = json.load(open('tmp/username/Twibot-20/bi_gram_likelihood.json'))
    print(calc_username_likelihood('bot', likelihood))