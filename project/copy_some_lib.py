#备份数据库
import pymongo

client = pymongo.MongoClient()
ganjiLib = client['ganjiLib']
sheet_4 = ganjiLib['sheet_4']
copy_version = ganjiLib['copy_version']

for i in sheet_4.find():
    copy_version.insert_one(i['massages'])

for i in copy_version.find():
    print(i)
