def quality_control(q,a):
    if " __ " in q or "____" in q or " _ " in q or " ___ " not in q:
        return False

def add_info(q,a):
    # Use a breakpoint in the code line below to debug your script.
    x = quality_control(q,a)