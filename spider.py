#Imports and Prerequisites
from urllib.request import urlopen
from link_finder import LinkFinder
from crawler import *


class Spider:

    #Global variables that each spider can use
    directory = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()


    def __init__(self, directory, base_url, domain_name):
        Spider.directory = directory
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.directory + '/queue.txt'
        Spider.crawled_file = Spider.directory + '/crawled.txt'
        self.boot()
        self.crawl_page('Spider 1', Spider.base_url)


