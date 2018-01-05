import pymongo

client = pymongo.MongoClient() #激活客户端 本地客户端参数不需要填
ganjiLib = client['ganjiLib'] #引入数据库ganjiLib
sheet_4 = ganjiLib['sheet_4'] #引入sheet_4表格
clean_data = ganjiLib['clean_data'] #建立新的表格clean_data

# for i in sheet_4.find(): #复制数据
#     clean_data.insert_one(i['massages'])
    
for i in clean_data.find(): #输出数据
    print(i['place'])


