#爬赶集二手的所有类目链接
from bs4 import BeautifulSoup
import requests

def get_type_urls():
    url = 'http://cq.ganji.com/wu/'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    type_urls = soup.select("dl.fenlei > dt > a")
    for link in type_urls:
        url = "http://cq.ganji.com" + str(link.get('href'))
        print(url)
        
#get_type_urls()

urls = """
    http://cq.ganji.com/jiaju/
    http://cq.ganji.com/rirongbaihuo/
    http://cq.ganji.com/shouji/
    http://cq.ganji.com/bangong/
    http://cq.ganji.com/nongyongpin/
    http://cq.ganji.com/jiadian/
    http://cq.ganji.com/ershoubijibendiannao/
    http://cq.ganji.com/ruanjiantushu/
    http://cq.ganji.com/yingyouyunfu/
    http://cq.ganji.com/diannao/
    http://cq.ganji.com/xianzhilipin/
    http://cq.ganji.com/fushixiaobaxuemao/
    http://cq.ganji.com/meironghuazhuang/
    http://cq.ganji.com/shuma/
    http://cq.ganji.com/laonianyongpin/
    http://cq.ganji.com/xuniwupin/
    http://cq.ganji.com/qitawupin/
    http://cq.ganji.com/ershoufree/
    http://cq.ganji.com/wupinjiaohuan/
    """