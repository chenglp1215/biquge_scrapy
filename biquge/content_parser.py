# coding=utf-8
import copy

from bs4 import BeautifulSoup


class ModifyContent(object):

    def __init__(self, content):
        self.soup = BeautifulSoup(content)
        self.page_content = self.soup.find(id="content")
        self.page_title = self.soup.find(class_="bookname")

    @staticmethod
    def clear_attr(content, tag_name, attrs):
        for each in content(tag_name):
            for each_attr in attrs:
                del (each[each_attr])

    def del_tag(self, tag_name):
        for each in self.page_content(tag_name):
            each.extract()

    def get_content(self):
        content = u""
        for each in self.page_content.children:
            if unicode(each).strip() == u"<br/>":
                continue
            else:
                content += u"%s\n" % unicode(each)
        return content

    def get_title(self):
        return self.page_title.h1.text