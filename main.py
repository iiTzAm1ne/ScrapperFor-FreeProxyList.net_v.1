import requests
from bs4 import BeautifulSoup
import threading
from tkinter import messagebox, filedialog
import os

proxies = []
good_proxies = []

def scrapProxies(textBox):
    global proxies
    proxy_link = 'https://free-proxy-list.net/'
    source = requests.get(url=proxy_link).content
    html = BeautifulSoup(source, 'html.parser')
    tbody = html.find('tbody')

    for row in tbody.find_all('tr'):
        ip = row.contents[0].text
        port = row.contents[1].text
        textBox.insert('1.0', f"{ip}:{port}\n")
        proxies.append(f"{ip}:{port}")


def checkerHandler(textBox):
    for _ in proxies:
        t = threading.Thread(target=proxyChecker, args=(_, textBox,))
        t.start()

# noinspection PyBroadException
def proxyChecker(proxy, textBox):
    global good_proxies
    try:
        r = requests.get(url='http://httpbin.org/ip', proxies={'http': f'http://{proxy}'}, timeout=1)
        if r.status_code == 200:
            print(f"Good Proxy: {proxy}")
            textBox.insert('1.0', f"{proxy}\n")
            #good_proxies.append(proxy)
        else:
            print(f"Bad Proxy: {proxy}")
    except Exception as e:
        pass

def proxySave():

    if len(proxies) == 0:
        messagebox.showerror('Error', 'save function has been stopped cause by error!!')
    else:

        if os.path.exists('http.txt'):
            os.remove('http.txt')

        with open('http.txt', 'a+') as f:
            [f.write(f"{line}\n") for line in proxies]
        f.close()

        messagebox.showinfo('Proxy Save', 'your proxies has been saved successfully!!')

def openFile(textBox):
    global proxies

    file = filedialog.askopenfile('r', filetypes=[('Text', '*.txt')])
    proxies = [proxy.removesuffix('\n') for proxy in file.readlines()]
    [textBox.insert('1.0', f"{proxy}\n") for proxy in proxies]
