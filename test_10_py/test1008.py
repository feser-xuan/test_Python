# -*- coding:utf-8 -*-
# author: Weixuan.Ding
# time  : 2018/10/8

# 二分查找
# def bi_search(lst , x):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#          mid = (low + high) / 2
#          if lst[mid] == x:
#              return mid
#          elif lst[mid] > x:
#              high = mid - 1
#          else:
#              low = mid + 1
#     return -1
# lst = [1, 3, 5, 10 ,13]
#
# print bi_search(lst,3)

# #排序
#
# def selection_sort_v1(lst):
#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i+1,len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#         lst.insert(i,lst.pop(min_index))
#
# def swap(list,i,j):
#     tmp = lst[i]
#     lst[i] = lst[j]
#     lst[j] = tmp
#
# def selection_sort_v2(lst):
#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i+1,len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#         swap(lst,i,min_index)
#
# def bubble_sort(lst):
#     top  = len(lst) - 1
#     is_exchanged = True
#     while is_exchanged:
#         is_exchanged = False
#         for i in range(top):
#             if lst[i] > lst[i + 1]:
#                 is_exchanged = True
#                 swap(lst,i,i+1)
#         top -= 1
#
# lst = [1, 3, 5, 10 ,13,2]
# bubble_sort(lst)
# print lst

# 列表

students = [['zhang',84],['wang',98],['li',76]]

# s = 0
# for student in students:
#     s += student[1]
#
# print float(s) / len(students)
#
# print float(sum([x[1] for x in students])) / len(students)
#
# lst = [x**2 for x in range(1,10)]
# print lst
#
# print [i for i in range(1,7)if 6 % i ==0]
# def f(a):
#     return a[1]

# students.sort(key= lambda x : x[1],reverse=True)
# #students.sort(key=f ,reverse=True)
# print students

words = ['abc','defgh','df','lsefgd']

# lst = []
# for word in words:
#     lst.append((len(word),word))
#
# lst.sort(reverse=True)
#
# res = []
#
# for length, word in  lst:
#     res.append(word)
#
# print res

# words.sort(key=lambda x: len(x),reverse = False)
# print words

#字典
# my_dict = {'John':96511234,'Bob':43543543,'Mike':324324324}
#
# print my_dict['Bob']
# print my_dict

# s = 'sagrrerrhtgfdag'
# d = {}
#
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#
# print d
# lst = [0] * 26
#
# for i in s:
#     lst[ord(i) - 97] += 1
#
# print lst

###############################

# f = open('emma.txt')
#
# word_freq = {}
#
# for line in f:
#     words = line.strip().split()
#     for word in words:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1
#
# freq_word = []
# for word,freq in word_freq.items():
#     freq_word.append((freq,word))
#
# freq_word.sort(reverse=True)
#
# for freq,word in freq_word[:20]:
#     print word
#
# f.close()

# d1 = {'Zhang':123,'Wang':456,'Li':123,'Zhao':456}
# d2 = {}
#
# for name, room in d1.items():
#     if room in d2:
#         d2[room].append(name)
#     else:
#         d2[room] = [name]
# print d2

#分词

def load_dict (filename):
    word_dict = set()
    max_len = 1
    f = open(filename)
    for line in f:
        word = unicode(line.strip(), 'utf-8')
        word_dict.add(word)
        if len(word) > max_len:
            max_len = len(word)
    return  max_len, word_dict

def fmm_word_seg(sent, max_len ,word_dict):
    begin = 0
    words = []
    sent = unicode(sent, 'utf-8')

    while begin < len(sent):
        for end in range(begin + max_len,begin ,-1):
            if sent[begin:end] in word_dict:
                words.append(sent[begin:end])
                break
        begin = end
    return words

max_len, word_dict=load_dict('lexicon.dic')
sent = raw_input('Input a sententce:')
words = fmm_word_seg(sent,max_len,word_dict)
for word in words:
    print word