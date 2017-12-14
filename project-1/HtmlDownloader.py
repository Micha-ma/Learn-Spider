#下载器的主要作用就是下载指定URL的页面内容，很简单，根据不同的网站，可能需要添加cookies等凭证
import requests
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        #将爬虫伪装成浏览器
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        headers = {'User-Agent':user_agent}
        #获取url网页的内容
        html = requests.get(url, headers=headers)
        if html.status_code == 200:  #成功爬取网页内容
            html.encoding = 'utf-8'
            return html.text
        return None
