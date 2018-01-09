# coding=utf-8
import os


class Output(object):

    path = "files"

    def __init__(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def output(self, title, content):
        with open(os.path.join(self.path, "%s.txt" % title), "w") as output_file:
            output_file.write(content)

output = Output()
