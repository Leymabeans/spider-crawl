#Imports and Prerequisites
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:

    #Global variables that each spider can use
    directory = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    #Setup and initialization of the spider
    def __init__(self, directory, base_url, domain_name):
        Spider.directory = directory
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.directory + '/queue.txt'
        Spider.crawled_file = Spider.directory + '/crawled.txt'
        self.boot()
        self.crawl_page('Spider 1', Spider.base_url)

    #After boot up, perform crawling process
    def boot(self):
        create_project_dir(Spider.directory)
        create_datafiles(Spider.directory, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    #Pass in url and get all links and add to directories
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + 'crawling '+ page_url)
            print('Queue ' + str(len(Spider.queue)))
            print('Crawled ' + str(len(Spider.crawled)))
            print('\n')
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()


    #Gathers links on website and converts bytes to html format
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, Spider.page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    #Checks if links are owned by website, and if those are already in the sets
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    #Adds links from sets to files
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)