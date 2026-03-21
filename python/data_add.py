import argparse
from gcc_postgres import task as t
from gcc_postgres import pcn
#y = [['q']['a']['a'],['q']['a']['a']['a']]
#dir = ['a'],['b'],['c'],['d']

# DB
# |
# |papasitos
# |_ planned_stages
#   |_ q_a

def connection():
    cn = pcn.d_cn(__file__)
    return cn


def quiz_input(table_name,value_dict,caller_file=__file__,schema_name='papasitos'):
    t.di_table(table_name,value_dict,caller_file,schema_name)




def add_info(q,a):
    ...
    # Use a breakpoint in the code line below to debug your script.
    #if quality_control(q,a) == False:
    #    print('Fail')
    #    quit(0)
        #quit

def main(q,a):
    add_info(q,a)


# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
