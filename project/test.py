import time
import pymongo

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
real_links = new_ganjiLib['real_links']
detail = new_ganjiLib['detail']

reals = set([index['url'] for index in real_links.find()])
print(len(reals))