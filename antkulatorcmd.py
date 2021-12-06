import math

print ("Wersja 1.5")
print ("")
print ("Jaką operację chcesz wykonać?")
print ("+ to Dodawanie")
print ("- to Odejmowanie")
print ("* to Mnożenie")
print (": to Dzielenie")
print (". to Potęgowanie")
print ("/ to Pierwiastkowanie")
print ("")



Counter=1
while Counter!=2:
    i=float(input("Podaj liczbę pierwszą i kliknij enter aby kontynuować: "))
    a=str(input("Podaj co chcesz zrobić z liczbami: "))
    o=float(input("Podaj liczbę drugą i kliknij enter aby kontynuować: "))
    if a=="+":
        p=i+o
    if a=="-":
        p=i-o
    if a=="*":
        p=i*o
    if a==":":
        p=i/o
    if a==".":
        p=i**o
    if a=="/":
        p=math.pow(i,1/o)


    print("Wynik to ",(p))
    print("")

