def topic(x):
    if x == "option1":
        a = open("intel/Math.txt", "r")
    elif x == "option2":
        a = open("intel/Phy.txt", "r")
    elif x == "option3":
        a = open("intel/Chem.txt", "r")
    elif x == "option4":
        a = open("intel/Bio.txt", "r")
    b = a.read()
    b = b.split("\n")
    return b


def combine(cha, rep):

    if rep == "option1":
        rep = "Questions with answers"
    elif rep == "option2":
        rep = "MCQ"
    elif rep == "option3":
        rep = "Points"
    elif rep == "option4":
        rep = "All"

    vfr = str("Genterate " + rep + " of " + cha)
    print(vfr)
    return vfr


def save(a, filename, rep):
    if rep == "option1":
        de = "Qna/"
    elif rep == "option2":
        de = "MCQ/"
    elif rep == "option3":
        de = "Points/"
    filenam = ""
    for i in filename:
        if i != " ":
            filenam += i
    print(filenam)
    y = filenam + ".txt"
    x = "templates/Output/" + de + filenam + ".txt"
    z = open(x, "w")
    z.write(a)
    z.close()
    return x, y
