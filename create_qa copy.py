import sys
import json
import os
import const
import re
import random
import string

QUESTION_TOOL='What are the tools used in the attack?'
QUESTION_GROUP='Who is the attack group?'

INPUT_FILE='input/sample_attack_report_raw.txt'
VER='v2.0'
LEN_ID=24
SENTENSE_NUM=3
MAX_LEN_PARA=1000
VUL_RATE=0.2
LABEL_TRAIN='train'
LABEL_VAL='validation'

num_train=10
dict_root={}
dict_root['version'] = VER

def get_answers():
    with open(const.OUT_TOOL_FILE, 'r') as file:
        tools=file.readlines()
        return tools

def get_group_answers():
    with open(const.OUT_GROUP_FILE, 'r') as file:
        groups=file.readlines()
        return groups


def get_id(num):
    dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(dat) for i in range(num)])

dict_root={}
dict_root['version']=VER
dict_root['data']=[]

def create_json(label,num_data):
    dict_root['data']=[]
    cnt=0

    with open(INPUT_FILE, 'r') as file:
        for row in file:
            sentenses=row.split(". ")
            paragraph = ''
            for sentense in sentenses:
                if cnt>num_data:
                    return

                paragraph = paragraph + sentense
                if len(paragraph)<MAX_LEN_PARA:
                    continue

                paragraph=paragraph.lower()
                qas = []
                dict_data={}
                dict_data['title']=paragraph.split(' ')[0]
                dict_data['paragraphs']=[]
                dict = {}
                dict_qa = {}
                dict_qa['question']=QUESTION_TOOL
                dict_qa['id'] = get_id(LEN_ID)
                dict_qa['answers'] =[]
                is_impossible='true'

                # find tools
                for tool in tools:
                    tool=tool.replace(const.NEWLINE, "")
                    tool=tool.lower()

                    pattern1 = re.compile(r'(\s+|^){0}(\s+|,|\.)' .format(tool))
                    result=pattern1.finditer(paragraph)
                    for m in result:
                        dict_answers={}
                        dict_answers['text']=tool
                        dict_answers['answer_start'] =m.start()
                        dict_qa['answers'].append(dict_answers)

                dict['qas'] = qas
                dict['qas'].append(dict_qa)

                # find groups
                dict_qa2=dict_qa.copy()

                dict_qa2['question'] = QUESTION_GROUP
                dict_qa2['id'] = get_id(LEN_ID)
                dict_qa2['answers'] = []

                for group in groups:
                    group=group.replace(const.NEWLINE, "")
                    group=group.lower()

                    pattern1 = re.compile(r'(\s+|^){0}(\s+|,|\.)' .format(group))
                    result=pattern1.finditer(paragraph)
                    for m in result:
                        dict_answers={}
                        dict_answers['text']=group
                        dict_answers['answer_start'] =m.start()
                        dict_qa2['answers'].append(dict_answers)

                dict['qas'].append(dict_qa2)



                for qa in dict['qas']:
                    if len(qa['answers'])>0:
                        is_impossible = 'false'
                    qa['is_impossible']=is_impossible
                dict['context']=paragraph
                dict_data['paragraphs'].append(dict)


                dict_root['data'].append(dict_data)

                paragraph = ''
                cnt = cnt + 1

if len(sys.argv)>0:
    num_train  = int(sys.argv[1])

num_val=round(num_train*VUL_RATE)

# if(os.path.exists(OUT_FILE)):
#     os.remove(OUT_FILE)

tools=get_answers()
groups=get_group_answers()

create_json(LABEL_TRAIN, num_train)

OUT_FILE=LABEL_TRAIN+'.json'

with open(OUT_FILE, "w", encoding='utf8') as out:
    json.dump(dict_root,out)

create_json(LABEL_VAL, num_val)

OUT_FILE=LABEL_VAL+'.json'

with open(OUT_FILE, "w", encoding='utf8') as out:
    json.dump(dict_root,out)








