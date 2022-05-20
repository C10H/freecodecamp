import re
def arithmatic_arranger(lis:list,opt:bool = False):
    if len(lis)>5:
        print ("Error: Too many problems.")
        return
    for i in lis:
        if re.findall(r'[^0-9\+\-\s]', i):
            print ("Error: Operator must be '+' or '-'.")
            return
        a, sig, b = i.split(sep=' ')
        if len(a) > 4 or len(b) > 4:
            print ("Error: Numbers cannot be more than four digits.")
            return
    numlist1 = []
    siglist = []
    numlist2 = []
    numlist3 = []
    lenlist = []
    for i in lis:
        a, sig, b = i.split()
        numlist1.append(int(a))
        numlist2.append(int(b))
        siglist.append(sig)
        if sig == '+':
            numlist3.append(int(a)+int(b))
        else:
            numlist3.append(int(a)-int(b))
        lenlist.append(max(len(a), len(b)))
    if opt:
        for i in range(len(numlist1)):
            num = numlist1[i]
            print(' ' * (lenlist[i] - len(str(num)) + 2) + str(num), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
        for i in range(len(numlist2)):
            num = numlist2[i]
            print(siglist[i] + ' ' * (lenlist[i] - len(str(num)) + 1) + str(num), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
        for i in range(len(numlist2)):
            num = numlist2[i]
            print('-' * (lenlist[i] + 2), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
        for i in range(len(numlist3)):
            num = numlist3[i]
            print(' ' * (lenlist[i] - len(str(num)) + 2) + str(num), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
    if not opt:
        for i in range(len(numlist1)):
            num = numlist1[i]
            print(' ' * (lenlist[i] - len(str(num)) + 2) + str(num), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
        for i in range(len(numlist2)):
            num = numlist2[i]
            print(siglist[i] + ' ' * (lenlist[i] - len(str(num)) + 1) + str(num), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
        for i in range(len(numlist2)):
            num = numlist2[i]
            print('-' * (lenlist[i] + 2), end='')
            if i != len(numlist1) - 1:
                print(' ' * 4, end='')
                pass
            else:
                print()
                pass
    return