# This is a sample Python script.
import argparse
import Postgres as pg

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#y = [['q']['a']['a'],['q']['a']['a']['a']]
#dir = ['a'],['b'],['c'],['d']

# DB
# |
# |papasitos
# |_ planned_stages
#   |_ q_a

def connection(file_path):
    cn = pg.connection(file_path)
    return cn


def create_quiz(pt, category, q_style, a_am,q_am,qp,a1,a2,a3,a4):
    questions
    answer = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(pt, category, q_style, a_am,q_am,qp,a1,a2,a3,a4)




def add_info(q,a):
    # Use a breakpoint in the code line below to debug your script.
    if quality_control(q,a) == False:
        print('Fail')
        quit(0)
        #quit

def main(q,a):
    add_info(q,a)


# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
