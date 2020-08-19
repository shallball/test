#coding:gbk
import time
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser


class SpiderMan(object):

    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,root_url):
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(root_url,content)
        
        for url in urls:
            content = self.downloader.download(url)
            data = self.parser.parser_release(url,content)
            self.output.output_db('Movie',data)
        self.output.close_db()

if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('https://movie.douban.com/cinema/nowplaying/xiamen/')
