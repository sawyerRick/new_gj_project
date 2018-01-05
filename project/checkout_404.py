from bs4 import BeautifulSoup
import requests

def check_404(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    error = soup.find("p","error-tips1")
    if error:
        return 1
    else:
        return 0
    
    
#print(check_404('http://cq.ganji.com/rirongbaihuo/'))