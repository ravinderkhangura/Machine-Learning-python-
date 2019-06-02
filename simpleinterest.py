print("\tSIMPLE INTEREST \n\n\n")
p = int(input("ENTER PRINCIPAL : "))
r = int(input("\nENTER THE RATE (%) : "))
t = int(input("\nENTER THE TIME PERIOD (years) : "))
si= p*r*t/100
t = si+p
print("\nSIMPLE INTEREST : ",si)
print("\nTOTAL AMOUNT : ",t)
print("\n\n\n")