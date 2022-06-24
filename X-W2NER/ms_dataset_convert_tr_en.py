# -*- coding:utf-8 -*-
"""
author: Chang Liu
date: 2022year05month11day
"""

import json
import numpy as np
import random
from sklearn.model_selection import train_test_split

def read_ugms(file_name):
    file1=open(r'/root/autodl-nas/liuchang/baseline/THUUMS/data/{}'.format(file_name),'r',encoding='utf-8')
    file_lines=file1.readlines()
    file1.close()
    list1=[]
    for i in file_lines:
        data=i.split()
        list1.append(data)
    return list1
train_texts=read_ugms('train.src')
train_tags=read_ugms('train.trg')
val_texts=read_ugms('dev.src')
val_tags=read_ugms('dev.trg')
test_texts=read_ugms('test.src')
test_tags=read_ugms('test.trg')
print(test_texts[0])
print(test_tags[0])

eng_dic = {}
tur_dic = {}
morpheme_list = []
label_list = []

input_files = ['/root/autodl-nas/liuchang/morphological_segmentation/goldstd_combined.segmentation.eng',
               '/root/autodl-nas/liuchang/morphological_segmentation/goldstd_combined.segmentation.tur' ]
dictionaries = (eng_dic, tur_dic)

for filename in input_files:
    with open(filename) as inputfile:
        for line in inputfile:
            actual_line = line.split('\t')
            result = []
            actual_morph = ''
            flag = 0
            for c in actual_line[1]:
                if c == ':' and flag == 0:
                    result.append(actual_morph)
                    actual_morph = ''
                    flag = 1
                if flag == 0:
                    actual_morph += c
                if c == ',':
                    break
                if flag == 1 and c == ' ':
                    flag = 0

            label = []
            for morph in result:
                if len(morph) == 1:
                    label.append('s')
                else:
                    label.append('b')
                    for i in range(len(morph)-2):
                        label.append('m')
                    label.append('e')
            morpheme = list(actual_line[0])
            morpheme_list.append(morpheme)
            label_list.append(label)
train_texts_con = train_texts + morpheme_list
train_tags_con = train_tags + label_list
#texts_tags = zip(train_texts_con,train_tags_con)
#texts_tags_shuffle = random.shuffle(texts_tags)

# 利用随机数种子
np.random.seed(12)
np.random.shuffle(train_texts_con)
np.random.seed(12)
np.random.shuffle(train_tags_con)


def convert(texts,tags,type):
    json_list=[]
    for num in range(len(texts)):
        sentence = texts[num]
        tag = tags[num]
        ner_list = []
        json_dict = {}
        json_dict["sentence"] = sentence
        for i in range(len(sentence)):
            index_type = {}
            index_type["index"] = []
            index_type["index"].append(i)
            index_type["type"] = tag[i]
            ner_list.append(index_type)
            json_dict["ner"] = ner_list
        json_list.append(json_dict)

    for i in json_list:
        if 'ner' not in i:
            json_list.remove(i)

    with open("/root/autodl-nas/liuchang/W2NER/data/ug_tr_en_ms/{}.json".format(type),"w") as json_file:
        json.dump(json_list, json_file)
convert(train_texts_con,train_tags_con,'train')
convert(val_texts,val_tags,'dev')
convert(test_texts,test_tags,'test')