from bs4 import BeautifulSoup
import requests

def get_ganji_links_from(link):
    wb_data = requests.get(link)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select("dt > a > img")
    print(links)
    
get_ganji_links_from('http://bj.ganji.com/bangong/')