import requests, pprint, string, sqlite3
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_all_links():
    all_bg_sites = 'http://register.start.bg/'
    bg_sites = requests.get(all_bg_sites)
    sites = []

    soup = BeautifulSoup(bg_sites.content, 'html.parser')
    
    for link in soup.find_all('a'):
        if str(link.get('href')).startswith('link.php?'):
            sites.append(all_bg_sites + link.get('href'))

    return sites

def get_all_domain_servers():

    for site in get_all_links():
        try:
            s = requests.get(site)
            sp = urlparse(s.url)
            sr = sp.scheme + "://" + sp.netloc
            if sr[-3:] == ".bg":
                r = requests.get(sr)
                yield r.headers["Server"]
            else:
                pass

        except Exception:
            pass

def create_table():
    connection = sqlite3.connect('CrawlBG.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CrawlBG
            (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, url TEXT, server_name TEXT, server_count INTEGER);
        """
    )

    connection.commit()
    connection.close()