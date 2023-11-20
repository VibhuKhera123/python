z = 0
i = 0
j = 0
c = 0
a = list("32423")
ac = ""
stk = []
act = ""
def check():
    global i, c
    global stk, ac, a
    ac = "REDUCE TO E -> "
    for z in range(len(stk)):
        if stk[z] == '4':
            print(f"{ac}4".ljust(20), end="")
            stk[z] = 'E'
            print(f"${''.join(stk)}\t{'' if j == c else a[j:]}$".ljust(20))

    new_stk = [] 

    for z in range(len(stk) - 2):
        if stk[z] == '2' and stk[z + 1] == 'E' and stk[z + 2] == '2':
            print(f"{ac}2E2".ljust(20), end="")
            stk[z:z + 3] = 'E'
            print(f"${''.join(stk)}\t{'' if j == c else a[j:]}$".ljust(20))
            i = i - 2

    new_stk = [item for item in stk if item != '']
    stk = new_stk

    for z in range(len(stk) - 2):
        if stk[z] == '3' and stk[z + 1] == 'E' and stk[z + 2] == '3':
            print(f"{ac}3E3".ljust(20), end="")
            stk[z:z + 3] = 'E'
            print(f"${''.join(stk)}\t{'' if j == c else a[j:]}$".ljust(20))
            i = i - 2
    return 
def main():
    global i, j, c
    global stk, act, a

    print("GRAMMAR is -\nE->2E2 \nE->3E3 \nE->4")
    c = len(a)
    act = "SHIFT"
    print("\nStack".ljust(20), "Input".ljust(20), "Action".ljust(20))
    print("$\t", ''.join(a), "$\t")
    for i in range(c):
        print(act.ljust(20), end='')
        stk.append(a[j])
        j += 1
        a[j - 1] = ''
        print(f"${''.join(stk)}\t{'' if j == c else a[j:]}$".ljust(20))
        check()
    check()
    if stk[0] == 'E' and len(stk) == 1:
        print("Accept")
    else:  # else reject
        print("Reject")


if __name__ == "__main__":
    main()
