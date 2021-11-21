import requests
from bs4 import BeautifulSoup
from proxy_info import login, password

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

proxies = {
    # 'https': 'http://proxy_ip:proxy_port'
    'https': f'http://{login}:{password}@proxy_ip:proxy_port'
}


def get_location(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')
    
    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()
    
    print(f'IP: {ip}\nLocation: {location}')


def main():
    get_location(url='https://2ip.ru')
    
    
if __name__ == '__main__':
    main()
