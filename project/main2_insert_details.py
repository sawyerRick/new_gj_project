#多进程储存详细信息
from multiprocessing import Pool
from test_insert import insert_info
from get_page_links import sheet_2

sum = sheet_2.find().count() #爬取的链接总数

if __name__ == '__main__':
    pool = Pool()
    pool.map(insert_info, sheet_2.find().limit(sum))
    pool.close()