#1fel.
vezeteknev = input("Vezetéknév:")
keresztnev = input("Keresztnév:")
nev1 = vezeteknev+keresztnev
nev2 = keresztnev+vezeteknev
print(nev1)
print(nev2)

#2fel.
szam = int(input("Kérek egy számot:"))
szam0 = szam-1
szam1 = szam+1
print(szam0)
print(szam1)

#3.fel
szam1 = int(input("Kérek egy számot:"))
szam2 = int(input("Kérek egy másik számot:"))
print (szam1+szam2)
print (szam1-szam2)
print (szam1*szam2)
print (szam1/szam2)

#8.fel
import random
szam1 = int(input("Add meg az első számot"))
stam2 = int(input("Add meg a masodik számot"))
for i in range(10):
  print(random.uniform(szam1, szam2), end = "\t")