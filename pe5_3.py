lijst = []
infile = open("kaartnummers.txt", "r")
regel = len(infile.readlines())

infile.seek(0)
for x in range(0, regel):
    r = infile.readline()
    lijst.append(r[0:6])

infile.close()

mx = max(lijst)
mx_regel = lijst.index(mx) + 1
print("Deze file telt", regel, "regels")
print("Het grootste kaartnummer is:", mx, "en dat staat op regel", mx_regel)
