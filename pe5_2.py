infile = open("kaartnummers.txt", "r")
line = infile.readlines()

infile.seek(0)
for x in range(0, len(line)):
    s = infile.readline()
    nr = s[0:6]
    nm = s[8:].split("\n")
    print(nm[0], "heeft kaartnummer:", nr)

infile.close()
