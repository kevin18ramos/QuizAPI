import argparse
import gcc.postgres as gcp


#y = [['q']['a']['a'],['q']['a']['a']['a']]
#dir = ['a'],['b'],['c'],['d']

# DB
# |
# |papasitos
# |_ planned_stages
#   |_ q_a

def connection():
    cn = gcp.connection.connection(__file__)
    return cn


def quiz_input(question_pre_add):
    cn = connection()
    gcp.di_table(caller_file=__file__,schema_name='papasitos',table_name='default_quiz',value_dict=question_pre_add,cn=cn)




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
