#同步数据库
import pymongo
import time

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
real_links = new_ganjiLib['real_links']

while True:
    all_links = set([i['url'] for i in links_lib.find()])#总数据量
    links = set([i['url'] for i in real_links.find()])#干净的数据量
    rest_of_links = all_links - links #需要增加的数据量
    print(links)
    
    for i in rest_of_links:
        real_links.insert_one({'url': i})
    
    print("secceed load")
    time.sleep(10)