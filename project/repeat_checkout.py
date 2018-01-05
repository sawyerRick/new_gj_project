import pymongo

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']


all_list = [i['url'] for i in links_lib.find()]

def repeat_checkout(link):
    if link in all_list:
        print('重复数据')
        return 1
    else:
        return 0
    
# index = repeat_checkout('http://cq.ganji.com/jiaju/32561438851256x.htm')
# print(index)
