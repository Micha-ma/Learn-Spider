#对于爬虫来说，由5个模块组成，但一般而言网页的下载器、解析器以及调度器是需要高度定制（尤其是后两者），而URL管理器和数据存储器一般可以复用。
import DataOutput
import HtmlDownloader
import HtmlParser
import URLManager


class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager.URLManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = DataOutput.DataOutput()

    def crawl(self, root_url):
        '''
        :param root_url: 入口URL链接
        :return: 
        '''
        #添加入口URL
        self.manager.add_new_url(root_url)
        #判断url管理器内是否有新的url，同时判断已抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                #从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                #print(new_url)
                #用HTML下载器下载网页
                html = self.downloader.download(new_url)
                #print(html)
                #用HTML解析器提取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                print(data)
                #将提取的URL添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                #用存储器存储数据
                self.output.store_data(data)
                print('已抓取%s个链接' %self.manager.old_url_size())

            except Exception:
                print('Crawl failed')
        #将数据以HTML文件存储
        self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
