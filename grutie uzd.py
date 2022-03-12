#1.uzd
valstis = ['Latvija','Lietuva','Igaunija']
for valsts in valstis:
    print(valsts, end=" ")

print()
#2.uzd
for sk in range(50,24,-1):
    print(sk,end= " ")
print()
#3.uzd
sum = 0
for z in range(10, 29):
    if z % 3 == 0:
        sum = sum + z

print("Skaitļu summa ir", sum)
#4.uzd
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("BumRum,", end=" ")
    elif i % 3 == 0:
        print("Bum,", end=" ")
    elif i % 5 == 0:
        print("Rum,", end=" ")        
    else:
        print(i, ",", sep="", end=" ")

