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
            if simb[ini] == "<":
                if simb[ini] == simb[i]:
                    ini = i
                    i += 1
                else:
                    simb.pop(i)
                    simb.pop(ini)
                if i == len(simb):
                    ini = 0
                    i = ini +1
            else:
                break

    if len(simb) == 0:
        resp = True

    return resp

def verify_resp(solu:str) -> int:
    punt = 0
    b_flag = False
    test_user = input("> Ingrese el comando: ")

    try:
        if "<" in solu or ">" in solu:
            b_flag = True
            resp = verify_brackets(test_user, "<", ">")

            while not resp:
                print("\n> Not valid input. Verify the brackets.")
                print("> Your response was:", test_user)
                test_user = input("\n> Your response: ")
                resp = verify_brackets(test_user, "<", ">")
            
            if solu[0] == '?':
                cadena = "[?]" + solu[1:]
            else:
                cadena = solu

            if "$" in cadena:
                cadena = cadena[:cadena.index("$")] + "[$]" + cadena[cadena.index("$") + 1:]

            reg_val = ""
            while "<" in cadena:
                reg_val = reg_val + f"{cadena[:cadena.index("<")]}<{reg_filler}>"
                if cadena.index(">") + 1 < len(cadena):
                    cadena = cadena[cadena.index(">") + 1:]
                else:
                    cadena = cadena[cadena.index(">"):]
        else:
            if test_user == solu:
                punt = 1
            

        if b_flag:        
            regex_comp = re.compile(reg_val)
            print(regex_comp.fullmatch(test_user))
            if regex_comp.fullmatch(test_user):
                punt = 1
        
        print(f"Your response: {test_user}\nThe solution: {solu}")
        return punt
    except Exception:
        print(">> Yor response must include: < >")
        return punt
    

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
    reg_filler = "[A-z 0-9/+-]+"
    total = 0

    with open ('info.json') as file:
        info = json.load(file)

    #resp = info['CANDE']["commands"]["change CANDE terminal"]
    #verify_resp(resp)
    #re.compile("something").match("som")
    
    message = "\n> If you insert a command, type the action between <>\n> Example: COMMAND <action>\n\n"
    print("\n", "-"*20, "INSTRUCTIONS ", "-"*20)
    print(message)
    
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
            total += verify_resp(resp)
        elif rn1 == 1:
            message = f"> What is the command to {c_commands[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_commands[rn2]]
            print(message)
            total += verify_resp(resp)
        else:
            message = f"> What is the command to {c_workfile[rn2]}?"
            resp = info['CANDE'][cande_cat[rn1]][c_workfile[rn2]]
            print(message)
            total += verify_resp(resp)
    
    print(f"> Your score: {(total/test_size)*100:.2f}")
    