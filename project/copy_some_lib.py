#备份数据库
import pymongo

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
real_links = new_ganjiLib['real_links']
detail = new_ganjiLib['detail']
copy_version = new_ganjiLib['copy_version']

for i in detail.find():
    copy_version.insert_one(i['massages'])

for i in copy_version.find():
    print(i)
