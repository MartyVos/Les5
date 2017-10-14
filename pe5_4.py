import datetime

c = 1
infile = open("hardlopers.txt", "a")
print("Typ je naam. Type STOP om te stoppen:")

while c == 1:
    naam = input()
    if naam == "STOP":
        c = 0
    else:
        vandaag = datetime.datetime.today()
        s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
        loper = s + naam + "\n"
        infile.write(loper)
infile.close()
