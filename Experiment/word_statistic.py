import jieba
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib
from hanziconv import HanziConv
import codecs
from collections import Counter


def get_counts(txt, word_list):
    # get a Text file and Chinese word list
    seg_list = jieba.cut(txt)
    # stopwords = [line.strip() for line in open("CS.txt", encoding="utf-8").readlines()]
    counts = Counter()
    for word in seg_list:
        if word in word_list:
            counts[word] += 1
    return counts


def get_words(path):
    words = []
    with codecs.open(path, 'r', 'utf8') as f:
        line = f.readline()
        while line:
            word = line.strip().replace('\n', '')
            word = HanziConv.toTraditional(word)
            words += word
            line = f.readline()
        return words


def get_range(num, operation):
    # operation为1则向上取，为0位向下取数
    length = len(str(num))
    div = (10 ** length) // 10
    if operation == 1:
        return num // div * div + div
    else:
        return num // div * div - div


def show_statistic(count_result, title):
    label_list = list(dict(count_result.most_common(20)).keys())
    num_list = list(dict(count_result.most_common(20)).values())
    x = np.array(label_list)
    y = np.array(num_list)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    plt.title(title + "词频统计")
    plt.xlabel(title)
    plt.ylabel("出现次数")
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    # 获取文言虚实词列表
    classical_words = get_words('Classical_words.txt')
    sustain_words = get_words('Sustain_words.txt')
    # 设置结巴文言分词的字典
    jieba.set_dictionary('dict.txt.big')
    # 文言虚实词计数
    with codecs.open('dreamofredmaison.txt', 'r', 'utf8') as f:
        txt = f.read()
    classical_count = get_counts(txt, classical_words)
    print(classical_count)
    with codecs.open('dreamofredmaison.txt', 'r', 'utf8') as f:
        txt = f.read()
    sustain_count = get_counts(txt, sustain_words)
    print(sustain_count)
    show_statistic(classical_count, '文言虚词')
    show_statistic(sustain_count, '文言实词')
