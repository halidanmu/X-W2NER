# -*- coding:utf-8 -*-
"""
author: Chang Liu
date: 2022year03month15day
"""

import re
import json

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

def convert(texts,tags,type):
    json_list=[]
    for num in range(len(texts)):
        sentence = texts[num]
        tag = tags[num]
        ner_list = []
        json_dict = {}
        json_dict["sentence"] = sentence
        tag = ''.join(tag)
        b_position = [m.start() for m in re.finditer('b', tag)]
        e_position = [m.start() for m in re.finditer('e', tag)]
        s_position = [[m.start()] for m in re.finditer('s', tag)]
        print(b_position)
        print(e_position)
        print(s_position)
        index_list = []
        for i in range(len(b_position)):
            index = list(range(b_position[i], e_position[i] + 1))
            index_list.append(index)
        index_list.extend(s_position)
        index_list.sort()
        for i in index_list:
            index_type = {}
            index_type["index"] = i
            index_type["type"] = 'mor'
            ner_list.append(index_type)
            json_dict["ner"] = ner_list
        json_list.append(json_dict)

    for i in json_list:
        if 'ner' not in i:
            json_list.remove(i)

    with open("/root/autodl-nas/liuchang/W2NER/data/ug_ms/{}.json".format(type),"w") as json_file:
        json.dump(json_list, json_file)
convert(train_texts,train_tags,'train')
convert(val_texts,val_tags,'dev')
convert(test_texts,test_tags,'test')