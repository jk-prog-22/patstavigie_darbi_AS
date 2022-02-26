vecums = int(input("Cik tev gadu?"))

if vecums >= 18:
    print("Apsveicu, tu esi pilgadīgs!")
else:
    print("Tev vēl japaaugas!")
if vecums > 65:
    print("Tev laiks doties pensijā!")

if vecums < 10: 
    print("Pirmā dekāde")
elif vecums < 20:
    print("Otrā dekāde")
elif vecums < 30:
    print("Trešā dekāde")
elif vecums < 40:
    print("Ceturtā dekāde")
elif vecums < 50:
    print("Piektā dekāde")
elif vecums < 60:
    print("Sestā dekāde")
else:
    print("Kāda vairs starpība....")



