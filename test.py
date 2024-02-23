import json
import random
import re

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

def verify_brackets(cad: str, l_brack:str = "(", r_brack:str = ")") -> bool:
    resp = False
    simb = []
    l_cont = 0
    r_cont = 0

    for i in cad:
        if i == l_brack:
            l_cont += 1
            simb.append(i)
        elif i == r_brack:
            r_cont += 1
            simb.append(i)

    ini = 0
    if l_cont == r_cont and simb[ini] == l_brack:
        i = 1
        while len(simb) > 0:
            if simb[ini] == simb[i]:
                ini = i
                i += 1
            else:
                simb.pop(i)
                simb.pop(ini)
            if i == len(simb):
                ini = 0
                i = ini +1

    if len(simb) == 0:
        resp = True

    return resp

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
    reg_filler = "[A-Z 0-9/]*"
    total = 0
    s_tot = 0
    pass_score = 7

    with open ('info.json') as file:
        info = json.load(file)

    message = "> If you insert a command, type the action between <>\n> Example: COMMAND <action>"
    print(message)

    test_solu = info['CANDE']["commands"]["show directories"]
    test_user = input("> Ingrese un comando: ")

    resp = verify_brackets(test_user, "<", ">")

    while not resp:
        print("\n> Not valid input. Verify the brackets.")
        print("> Your response was:", test_user)
        test_user = input("\n> Ingrese un comando: ")
        resp = verify_brackets(test_user, "<", ">")


    print(resp)



    '''
    generated = []
    for _ in range(test_size):
        rn1, rn2, seq = generate_seq()
        while seq in generated:
            rn1, rn2, seq = generate_seq()
        generated.append(seq)
        if rn1 == 0:
            message = f"> What is the shortcut to {c_shortcuts[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_shortcuts[rn2]]
            print(message)
        elif rn1 == 1:
            message = f"> What is the command to {c_commands[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_commands[rn2]]
            print(message)
        else:
            message = f"> What is the command to {c_workfile[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_workfile[rn2]]
            print(message)
    

    test_user = input("> Ingrese un comando: ")
    test_solu = info['CANDE']["commands"]["show directories"]

    end = len(test_solu)
    if "<" in test_solu:
        lim = test_solu.index("<") - 1
        print(f"|{test_solu[:lim]},{test_user[:lim]}|")
        if test_solu[:lim] == test_user[:lim]:
            sub_tot = pass_score

        reg_verifier = test_solu[:lim] + reg_filler
        


    

    print(f"Tu respuesta: {test_user}\nLa solucion: {test_solu}")
    if test_user == test_solu:
        print(True)
    else:
        print(False)

    '''