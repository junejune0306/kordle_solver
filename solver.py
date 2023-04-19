from pprint import pprint

fixed = []
notfixed = []
gcnt = {}
ycnt = {}

def add_green(letter, idx):
    if [letter, idx] not in fixed:
        fixed.append([letter, idx])
        if letter in gcnt:
            gcnt[letter] += 1
        else:
            gcnt[letter] = 1
        pprint(fixed)
        pprint(gcnt)

def add_yellow(letter, idx):
    if [letter, idx] not in notfixed:
        notfixed.append([letter, idx])
        ycnt[letter] = 1
        pprint(notfixed)
        pprint(ycnt)

def add_gray(letter, idx):
    if [letter, idx] not in notfixed:
        notfixed.append([letter, idx])
        pprint(notfixed)

def search():
    global words
    print("searching in", len(words), "words...")
    for fix, idx in fixed:
        tmplist = []
        for w in words:
            if w[idx] == fix:
                tmplist.append(w)
        words = tmplist[:]
    for fix, idx in notfixed:
        tmplist = []
        for w in words:
            if w[idx] != fix:
                tmplist.append(w)
        words = tmplist[:]
    for i in gcnt.keys():
        tmplist = []
        for w in words:
            if w.count(i) >= gcnt[i]:
                tmplist.append(w)
        words = tmplist[:]
    for i in ycnt.keys():
        tmplist = []
        for w in words:
            if w.count(i) >= ycnt[i]:
                tmplist.append(w)
        words = tmplist[:]
    print(len(words), "words remain")
    if len(words) > 10:
        pprint(words[:10])
    else:
        pprint(words)

def reset():
    global words, fixed, notfixed, gcnt, ycnt
    words = open("modified.txt", "r").read().split()
    fixed = []
    notfixed = []
    gcnt = {}
    ycnt = {}

def autoinput():
    #s = open("input.txt", "rb").read().decode("utf-8").split("</div>")[:-2]
    s = input().split("</div>")[:-2]
    for i in range(12):
        if "green" in s[i]:
            add_green(s[i][-1], i)
        elif "yellow" in s[i]:
            add_yellow(s[i][-1], i)
        else:
            add_gray(s[i][-1], i)

words = open("modified.txt", "r").read().split()

menu = """
1: add green
2: add yellow
3: add gray
4: search
5: print all
6: autoinput
7: reset
> """
while 1:
    try:
        select = input(menu)
        #add green
        if select == "1":
            letter, idx = input("letter, index: ").split()
            idx = int(idx) - 1
            add_green(letter, idx)
        #add yellow
        elif select == "2":
            letter, idx = input("letter, index: ").split()
            idx = int(idx) - 1
            add_yellow(letter, idx)
        #add gray
        elif select == "3":
            letter, idx = input("letter, index: ").split()
            idx = int(idx) - 1
            add_gray(letter, idx)
        #search
        elif select == "4":
            search()
        #print all
        elif select == "5":
            pprint(words)
        #autoread
        elif select == "6":
            autoinput()
        #reset
        elif select == "7":
            reset()
    except:
        print("error")
        pass
