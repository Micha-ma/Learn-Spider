#数据存储器，提供了保存到内存和输出至HTML文件两种方式，最好是保存到数据库。
import codecs

class DataOutput(object):
    def __init__(self):
        self.datas=[]
    #存储到内存内
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    #将内存里的数据保存在html文件内
    def output_html(self):
        fout = codecs.open('baike.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %data['url'])
            fout.write("<td>%s</td>" %data['title'])
            fout.write("<td>%s</td>" %data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("<table>")
        fout.write("<body>")
        fout.write("<html>")
        fout.close()
