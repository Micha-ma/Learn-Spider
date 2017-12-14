#URL管理器主要就是管理待抓取和已抓取的两个集合，不需要做太多修改就可以运用于其他爬虫。
class URLManager(object):
    def __init__(self):
        self.new_urls = set()  #未爬取的URL集合
        self.old_urls = set()  #已爬取的URL集合

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return: 
        '''
        return self.new_url_size()!=0

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return: 
        '''
        new_url = self.new_urls.pop() #从未爬取的URL集合中取出一个
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        将新的URL添加到未爬取的URL集合中
        :param url: 新的单个URL
        :return: 
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        将新的URL添加到未爬取的URL集合中
        :param urls: 新的URL集合
        :return: 
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)

    def new_url_size(self):
        '''
        获取未爬取URL集合的大小
        :return: 
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已爬取URL集合的大小
        :return: 
        '''
        return len(self.old_urls)