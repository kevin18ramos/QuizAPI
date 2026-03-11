# This is a sample Python script.
import argparse

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#y = [['q']['a']['a'],['q']['a']['a']['a']]
#dir = ['a'],['b'],['c'],['d']

# DB
# |
# |papasitos
# |_ planned_stages
#   |_ q_a

def quality_control(q,a):
    if " __ " in q or "____" in q or " _ " in q or " ___ " not in q:
        return False
    if


def add_info(q,a):
    # Use a breakpoint in the code line below to debug your script.
    x = quality_control(q,a)


def add_info(q,a):
    # Use a breakpoint in the code line below to debug your script.
    if quality_control(q,a) == False:
        print('Fail')
        quit(0)
        #quit

def main(q,a):
    add_info(q,a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # This will ensure certain arguments exist
    parser = argparse.ArgumentParser(description="Sqoop Data from Source to S3.")
    parser.add_argument("-s","--source",help="Source Name (Google Cloud, etc.)")
    parser.add_argument("--metadb", help="Metadata database.")
    parser.add_argument("--db_to_use", help="Database to use for the processing.")
    parser.add_argument("--env",help="env to use.",default="int")
    parser.add_argument("--q","question")
    parser.add_argument("--a","answer")
    source = parser.parse_args().__dict__["source"]
    db_to_use = parser.parse_args().__dict__["db_to_use"]
    metadb = parser.parse_args().__dict__["metadb"]
    q=parser.parse_args().__dict__["q"]
    a = parser.parse_args().__dict__["a"]
    main(q,a)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
