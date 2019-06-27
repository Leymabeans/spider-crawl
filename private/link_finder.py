#Imports and Prerequisites
from html.parser import HTMLParser
from urllib import parse


#Takes in HTML code and looks for links (a tags)
class LinkFinder(HTMLParser):
    #Initializing the class and variables
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()


    #Looks for links (a tags)
    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)


    #Returns the full URL links
    def page_links(self):
        return self.links

    #Returns any errors in the HTML Parser
    def error(self, message):
        pass

