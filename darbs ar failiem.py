# atvērt failu
with open("dati.txt", "a", encoding="utf-8") as datne:
    datne.write("test\n")
    datne.write("saule\n")
    datne.write("Mēness\n")
    datne.writelines("Artūrs")
with open("dati.txt", "r", encoding="utf-8") as datne:
    tekts = datne.read()
print(tekts)



with open("dati.txt", "r", encoding="utf-8") as datne:
    tekts1 = datne.readline()
    tekts2 = datne.readline()

print(tekts1)
print(tekts2)