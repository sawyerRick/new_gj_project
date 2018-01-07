# 同步数据库
import pymongo
import time

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
real_links = new_ganjiLib['real_links']
detail = new_ganjiLib['detail']
real_detail = new_ganjiLib['reail_detail']
copy_version = new_ganjiLib['copy_version']


while True:
    #链接清理
    all_links = set([i['url'] for i in links_lib.find()])  # 总数据量
    links = set([i['url'] for i in real_links.find()])  # 干净的数据量
    rest_of_links = all_links - links  # 需要增加的数据量
    # #detail数据清理
    # all_details = set([i['title'] for i in copy_version.find()])
    # details = set([i['title'] for i in real_detail.find()])
    # rest_of_details = all_details - details
    # #load urls
    # for i in rest_of_links:
    #     real_links.insert_one({'url': i})
    # #load details
    # for i in rest_of_details:
    #     real_detail.insert_one(i)
    print("secceed load")
    time.sleep(10)