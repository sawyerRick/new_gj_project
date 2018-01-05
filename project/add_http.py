import pymongo

client = pymongo.MongoClient()
ganjiLib = client['ganjiLib']
sheet_1 = ganjiLib['sheet_1']

def add_http(link):
    if 'http' in link:
        print('goodlink')
        return link
    else:
        print("badlink")
        print(link)
        link = 'http:' + link
        return link
