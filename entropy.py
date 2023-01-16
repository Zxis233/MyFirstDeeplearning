import math


def calEntropy(string: str) -> float:
    h = 0.0
    sumt = 0
    letter = [0] * 26
    string = string.lower()
    for i in range(len(string)):
        if string[i].isalpha():
            letter[ord(string[i]) - ord('a')] += 1
            sumt += 1

    # print('\n', letter)
    for i in range(26):
        if sumt != 0:
            p = 1.0 * letter[i] / sumt
            if p > 0:
                h += -(p * math.log(p, 2))
        else:
            h = 0

    return h


if __name__ == '__main__':
    test = input("输入一个英文句子：")
    print('\n熵为：', calEntropy(test))
