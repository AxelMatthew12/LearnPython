print("\t\t===========================")
print("\t\t||    MINI CALCULATOR    ||")
print("\t\t===========================")
print("\t\t||                       ||")
print("\t\t     Option ( +,-,*,/)")
print("\t\t||                       ||")
Nb1=input("\t\t|| 1nd number:")
Nb2=input("\t\t|| 2nd number:")
Input=input("\t\t|| Option:  ")


Nb1= float(Nb1)
Nb2= float(Nb2)

if Input == "+":
    result = Nb1 + Nb2
elif Input == "-":
    result = Nb1 - Nb2
elif Input == "*":
    result = Nb1 * Nb2
elif Input == "/":
    result = Nb1/Nb2

else:
    result = "Invaild Result"



print("\t\t|| Result:", result)

