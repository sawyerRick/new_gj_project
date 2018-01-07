#爬赶集二手的所有类目链接
from bs4 import BeautifulSoup
import requests

def get_type_urls():
    url = 'http://cq.ganji.com/wu/'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    type_urls = soup.select("dl.fenlei > dt > a")
    for link in type_urls:
        url = "http://bj.ganji.com" + str(link.get('href'))
        print(url)
        
#get_type_urls()

urls = """
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/bangong/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/ershoubijibendiannao/
    http://bj.ganji.com/ruanjiantushu/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/diannao/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/shuma/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/qitawupin/
    http://bj.ganji.com/ershoufree/
    http://bj.ganji.com/wupinjiaohuan/
    """