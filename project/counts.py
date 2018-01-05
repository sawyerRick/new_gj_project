import time
import pymongo

client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']
real_links = new_ganjiLib['real_links']

while True:
    #print(sheet_1.find().count())
    print('real_links:', real_links.find().count())
    print('all_links:', links_lib.find().count())
    print('------------')
    time.sleep(2)

    