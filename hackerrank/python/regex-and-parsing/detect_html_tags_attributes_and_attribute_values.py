from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("-> {} > {}".format(name, value))
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("-> {} > {}".format(name, value))


parser = MyHTMLParser()

n = int(input())
html = ""

for _ in range(n):
    html += input()

parser.feed(html)