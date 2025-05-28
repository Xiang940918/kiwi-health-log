import os

os.makedirs("UserInformation", exist_ok=True)

def add_bugs(qua):
    bug_qua="UserInformation/bug_qua.txt"

    try:
        with open(bug_qua, "r", encoding="utf-8") as f:
            bugs_total = int(f.read())
    except FileNotFoundError:
        bugs_total = 0

    bugs_total+=qua

    with open(bug_qua,"w",encoding="utf-8") as f:
        f.write(f"{bugs_total}") 

    return bugs_total