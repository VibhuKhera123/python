SUCCESS = 1
FAILED = 0
def E():
    global cursor
    print(f"{cursor:<16} E -> T E'")
    if T():
        if Edash():
            return SUCCESS
        else:
            return FAILED
    else:
        return FAILED

def Edash():
    global cursor
    if cursor and cursor[0] == '+':
        print(f"{cursor:<16} E' -> + T E'")
        cursor = cursor[1:]
        if T():
            if Edash():
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    else:
        print(f"{cursor:<16} E' -> $")
        return SUCCESS

def T():
    global cursor
    print(f"{cursor:<16} T -> F T'")
    if F():
        if Tdash():
            return SUCCESS
        else:
            return FAILED
    else:
        return FAILED

def Tdash():
    global cursor
    if cursor and cursor[0] == '*':
        print(f"{cursor:<16} T' -> * F T'")
        cursor = cursor[1:]
        if F():
            if Tdash():
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    else:
        print(f"{cursor:<16} T' -> $")
        return SUCCESS
def F():
    global cursor
    if cursor and cursor[0] == '(':
        print(f"{cursor:<16} F -> ( E )")
        cursor = cursor[1:]
        if E():
            if cursor and cursor[0] == ')':
                cursor = cursor[1:]
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    elif cursor and cursor[0] == 'i':
        print(f"{cursor:<16} F -> i")
        cursor = cursor[1:]
        return SUCCESS
    else:
        return FAILED
def main():
    global cursor
    print("Enter the string")
    string = input()
    cursor = string
    print("\nInput           Action")
    print("--------------------------------")
    if E() and not cursor:  
        print("--------------------------------")
        print("String is successfully parsed")
        return 0
    else:
        print("--------------------------------")
        print("Error in parsing String")
        return 1
if __name__ == "__main__":
    main()
