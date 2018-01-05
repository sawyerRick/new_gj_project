# 同步数据库
import pymongo
import time

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
test_lib = new_ganjiLib['test_lib']

all_links_ = [i['url'] for i in links_lib.find()]
all_links = set([i['url'] for i in links_lib.find()])  # 总数据量
links = set([i['url'] for i in links_lib.find()])  # 干净的数据量
rest_of_links = all_links - links  # 需要增加的数据量

print(len(all_links_))
print(len(all_links))
print(len(links))
print(len(rest_of_links))
