import json
import random

def generate_seq() -> list:
    rn1 = random.randint(0, len(cande_cat) - 1)
    if rn1 == 0:
        rn2 = random.randint(0, len(c_shortcuts) - 1)
    elif rn1 == 1:
        rn2 = random.randint(0, len(c_commands) - 1)
    elif rn1 == 2:
        rn2 = random.randint(0, len(c_workfile) - 1)
    else:
        raise ValueError
    seq = str(rn1) + " " + str(rn2)
    return [rn1, rn2, seq]

if __name__ == "__main__":
    cande_cat = ["short cuts", "commands", "workfile"]
    c_shortcuts = [
        "send a line", 
        "send page", 
        "clean the page", 
        "clean below", 
        "show the next page", 
        "show a previuos page", 
        "insert lines in the workfile", 
        "insert a line in the workfile"]
    c_commands = [
        "close CANDE", 
        "show directories", 
        "remove directories", 
        "create directorie:", 
        "show workfile", 
        "use file in workfile", 
        "compile", 
        "run", 
        "insert value in a running program", 
        "insert value in a WFL running program", 
        "copy files",
        "verify running programs", 
        "verify jobs", 
        "verify waitings", 
        "delete jobs", 
        "show history commands", 
        "change CANDE terminal"]
    c_workfile = [
        "create the sequence", 
        "resequence a file", 
        "consult pages", 
        "refresh page", 
        "move lines", 
        "delete lines", 
        "delete a line", 
        "show next or prevous page", 
        "find a word", 
        "save workfile"]

    test_size = 10

    with open ('info.json') as file:
        info = json.load(file)

    generated = []
    for _ in range(test_size):
        rn1, rn2, seq = generate_seq()
        while seq in generated:
            rn1, rn2, seq = generate_seq()
        generated.append(seq)
        if rn1 == 0:
            message = f"What is the shortcut to {c_shortcuts[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_shortcuts[rn2]]
            print(message)
        elif rn1 == 1:
            message = f"What is the command to {c_commands[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_commands[rn2]]
            print(message)
        else:
            message = f"What is the command to {c_workfile[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_workfile[rn2]]
            print(message)

            