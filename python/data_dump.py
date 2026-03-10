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

def quality_control(ps):
    ...

def add_info(ps,q_a):
    # Use a breakpoint in the code line below to debug your script.
    quality_control(ps)


def add_info(ps,q_a):
    # Use a breakpoint in the code line below to debug your script.
    quality_control(ps, q_a)


def main(ps,q_a):
    add_info(ps,q_a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # This will ensure certain arguments exist
    parser = argparse.ArgumentParser(description="Sqoop Data from Source to S3.")
    parser.add_argument("-s","--source",help="Source Name (Google Cloud, etc.)")
    parser.add_argument("--metadb", help="Metadata database.")
    parser.add_argument("--db_to_use", help="Database to use for the processing.")
    parser.add_argument("--env",help="env to use.",default="int")
    parser.add_argument("-s3","--s3_source", help="S3 connection.", default=None)
    source = parser.parse_args().__dict__["source"]
    db_to_use = parser.parse_args().__dict__["db_to_use"]
    metadb = parser.parse_args().__dict__["metadb"]
    bucket_nm=parser.parse_args().__dict__["env"]
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
