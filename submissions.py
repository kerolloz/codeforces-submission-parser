#!/usr/bin/python3
import urllib.request
import os
import re

try:
    from bs4 import BeautifulSoup
except Exception as e:
    print(e, "\n------------------------------------------------"
             "\nYout should have BeautifulSoup installed\n"
             "You can use the followng command to install it\n",
          "sudo apt-get install python3-bs4\n"
          "------------------------------------------------"
          )
    raise e

soup = None


def parse_it(div_class, file_name):
    global soup
    os.system("mkdir " + file_name)
    os.chdir("./" + file_name)
    test_number = 0
    for div in soup.find_all("div", div_class):
        test_number += 1
        with open(file_name + str(test_number) + ".txt", 'w') as out_file:
        	out_file.writelines(div.contents[len(div.contents) - 2].pre.contents)
           
    os.chdir("..")
    return test_number


def main():
    problem_link = input(">> Enter Submission Link: ")

    my_request = urllib.request.urlopen(problem_link)
    my_html = my_request.read()

    numbers_in_link = re.findall("([0-9]+)", problem_link)  # numbers

    contest_number = numbers_in_link[0]
    submission_number = numbers_in_link[1]

    dir_name = str(contest_number) + '_' + str(submission_number)

    # create a directory named after the submission number and contest number
    os.system("mkdir " + dir_name)
    os.chdir("./" + str(dir_name))

    global soup
    soup = BeautifulSoup(my_html, "html.parser")

    number_of_testcases = parse_it("file input-view", "in")
    if parse_it("file answer-view", "out"):
        print(">> Parsed", number_of_testcases, "test case")
        print(">> DONE!",
              "\n>> Submission has been parsed Successfully to", dir_name, "!"
              )
    else:
        print(">> Something went WRONG!")


if __name__ == '__main__':
    main()
