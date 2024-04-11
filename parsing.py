import requests
import bs4 
from config import logger

class Parser(object):
    def __init__(self, url, filter, headers=None, package_size=None):
        self.url = url
        self.filter = filter
        self.headers = headers
        self.package_size = package_size


    def parse_project_list(self):
        requests.put(f'{self.url}/projects/filter/', self.filter, headers=self.headers)
        response = requests.get(f'{self.url}/projects/', headers=self.headers)
        filter_res = requests.get(f'{self.url}/projects/filter/', headers=self.headers)
        logger.debug(filter_res.text)
        if not filter_res.ok:
            raise Exception('Filter not applied')
        projects_html = bs4.SoupStrainer('div', class_='b-post__grid')
        soup = bs4.BeautifulSoup(response.text, 'lxml', parse_only=projects_html)
        projects = soup.find_all('a')
        projects_urls = [f'{self.url}{project.attrs['href']}' for project in projects]
        projects_titles = [project.text for project in projects]
        data = [(projects_titles[i], projects_urls[i]) for i in range(len(projects))][:self.package_size]
        return data
