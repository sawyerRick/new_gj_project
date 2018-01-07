#备份数据库
import pymongo
import json

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
real_links = new_ganjiLib['real_links']
detail = new_ganjiLib['detail']
copy_version = new_ganjiLib['copy_version']
good_details = new_ganjiLib['good_details']

# for i in detail.find():
#     copy_version.insert_one(i['massages'])
#
# for i in copy_version.find():
#     print(i)
#
with open('/Users\sawyer\Desktop/sample.json', 'r', encoding='utf-8') as file:
    all = file.readlines()
    json = json.load(all)
    for i in json:
        print(i['cates'])
    file.close()
