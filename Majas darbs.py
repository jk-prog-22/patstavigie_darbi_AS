product1 = "Banani"
price1 = 1
total1 = 200

product2 = "Melones"
price2 = 3
total2 = 40

print("Kopejais bananu skaits", total1)

sold1 = int(input("Pardotie banani"))
balance1 = total1 - sold1
income1 = sold1 * price1

print("Atlikusais bananu skaits", balance1)

noapalots1 = round(income1,)

print("Pelna1", noapalots1)
print()
print()

print("Kopejais melonu skaits",total2)
sold2 = int(input("Pardotas melones"))
balance2 = total2 - sold2
income2 = price2 * sold2

print("Atlikusas melones noliktava", balance2)
noapalots2 = round(income2,)

print("Pelna2", noapalots2)
print()

total = income1 + income2
print("Kopejie ienakumi", total)

