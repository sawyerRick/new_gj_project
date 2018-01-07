import requests

url = 'http://bj.ganji.com/'
wb_data = requests.get(url)
if wb_data.status_code == 404:
    print('404page')