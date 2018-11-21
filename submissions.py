import urllib.request
from bs4 import BeautifulSoup
import re

my_request = urllib.request.urlopen("https://codeforces.com/contest/1066/submission/44223707")
my_html = my_request.read()

soup = BeautifulSoup(my_html, "html.parser")
test_number = 1

for div in soup.find_all("div", "file input-view"):
    with open("in" + str(test_number) + ".txt", 'w') as out_file:
        out_file.writelines(div.contents[len(div.contents) - 2].pre.contents)
        test_number += 1

