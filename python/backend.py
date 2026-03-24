from gcc_postgres import task as t
from gcc_postgres import pcn

def quality_control(q,a):
    if " __ " in q or "____" in q or " _ " in q or " ___ " not in q:
        return False

def add_info(q,a):
    # Use a breakpoint in the code line below to debug your script.
    x = quality_control(q,a)

def user_creds():
    conn, cursor = pcn.d_cn(caller_file=__file__)
    sql = "select user_id,role from user_accounts "
    cursor.execute(sql)

def validating_user(columns):

    output = t.find_user(columns)
    if output['confirmation']:
        user_id,role = user_creds()
        return output['confirmation'],user_id,role
    else:
        return False