#多进程爬取
from multiprocessing import Pool
from get_page_links import get_links_from
from spider1_get_urls import urls

def get_all_links_from(channel):
    for i in range(1, 101):
        get_links_from(channel, i)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from, urls.split())
