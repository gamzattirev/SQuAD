import sys
import json
from glob import glob
import os
import const

if(os.path.exists(const.OUT_TOOL_FILE)):
    os.remove(const.OUT_TOOL_FILE)

if(os.path.exists(const.OUT_GROUP_FILE)):
    os.remove(const.OUT_GROUP_FILE)


tool_dir_name = sys.argv[1]
group_dir_name = sys.argv[2]

def get_tools():
    for file in glob(tool_dir_name + '/*.json'):
        json_open = open(file, 'r')
        data = json.load(json_open)
        tool_name = data.get('objects')[0].get('name')

        with open(const.OUT_TOOL_FILE, "a", encoding='utf8') as out:
            out.write(tool_name + '\n')


def get_groups():
    for dir in glob(group_dir_name + '/G*'):
        for file in glob(dir + '/*.json'):
            json_open = open(file, 'r')
            data = json.load(json_open)
            group_name = data.get('name')

        with open(const.OUT_GROUP_FILE, "a", encoding='utf8') as out:
            group_name=group_name.split(' (')[0]
            out.write(group_name + '\n')

get_tools()
get_groups()

