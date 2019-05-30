import tkinter
import jieba
from Experiment.word_statistic import *


root = tkinter.Tk()
root.title("文言虚实词词频统计系统")


def sustain_words_statistic():
    jieba.set_dictionary('dict.txt.big')
    with codecs.open('dreamofredmaison.txt', 'r', 'utf8') as f:
        txt = f.read()
    words = get_words('Sustain_words.txt')
    count = get_counts(txt, words)
    show_statistic(count, '文言实词')


def classical_words_statistic():
    jieba.set_dictionary('dict.txt.big')
    with codecs.open('dreamofredmaison.txt', 'r', 'utf8') as f:
        txt = f.read()
    words = get_words('Classical_words.txt')
    count = get_counts(txt, words)
    show_statistic(count, '文言虚词')


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


notice_label = tkinter.Label(root, text="请选择统计类别",
                             height=5,
                             wraplength=300, anchor='center', compound="top",
                             font="10").pack()
tkinter.Button(root, text="文言虚词统计", command=classical_words_statistic).pack()
tkinter.Button(root, text="文言实词统计", command=sustain_words_statistic).pack()
center_window(root, 300, 400)
root.resizable(0, 0)
root.mainloop()
