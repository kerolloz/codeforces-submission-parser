#!/usr/bin/python3
import urllib.request
import os
from bs4 import BeautifulSoup
import re

problem_link = input("Enter Submission Link: ")

my_request = urllib.request.urlopen(problem_link)
my_html = my_request.read()

numbers_in_link = re.findall("([0-9]+)", problem_link) # submission number

contest_number = numbers_in_link[0]
submission_number = numbers_in_link[1]

dir_name = str(contest_number) + '_' + str(submission_number)

os.system("mkdir " + dir_name) # create a directory named after the submission number
os.chdir("./" + str(dir_name))

soup = BeautifulSoup(my_html, "html.parser")


def parse_it(div_class, file_name):
    os.system("mkdir " + file_name)
    os.chdir("./"  + file_name)
    test_number = 1
    for div in soup.find_all("div", div_class):
        with open(file_name + str(test_number) + ".txt", 'w') as out_file:
            out_file.writelines(div.contents[len(div.contents) - 2].pre.contents)
            test_number += 1

    os.chdir("..")


parse_it("file input-view", "in")
parse_it("file answer-view", "out")
