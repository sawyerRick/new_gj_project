#多进程储存详细信息
from multiprocessing import Pool
from detail_spider import insert_info
import pymongo

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
real_links = new_ganjiLib['real_links']

links = [index['url'] for index in real_links.find()]

#sum = sheet_2.find().count() #爬取的链接总数

if __name__ == '__main__':
    pool = Pool()
    pool.map(insert_info, links)
    pool.close()