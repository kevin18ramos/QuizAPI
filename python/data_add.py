import argparse
from gcc_postgres import task as t
from gcc_postgres import cn as c
#y = [['q']['a']['a'],['q']['a']['a']['a']]
#dir = ['a'],['b'],['c'],['d']

# DB
# |
# |papasitos
# |_ planned_stages
#   |_ q_a

def connection():
    cn = c.d_cn(__file__)
    return cn


def quiz_input(question_pre_add):
    t.di_table(caller_file=__file__,schema_name='papasitos',table_name='default_quiz',value_dict=question_pre_add)




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
