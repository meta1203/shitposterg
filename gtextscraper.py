import sys
from lxml import html
import requests

def parseHtml(tree):
    posts = tree.xpath('//blockquote[@class="postMessage"]/text()')
    with open("g.txt", "a", encoding="utf-16") as myfile:
        for x in posts:
            myfile.write(x + "\n")

def downloadPage(urlLoc):
    page = requests.get(urlLoc)
    return html.fromstring(page.content)

if len(sys.argv) < 2:
    print("Not enough arguments!")
    exit(1)

urlLoc = sys.argv[1]

parseHtml(downloadPage(urlLoc))
