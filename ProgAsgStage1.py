plst=[["PELLETS",22.75,100],["MASH",20.50,90],["ENHANCED FOOD",25.50,125.50]]
qlst=[["PELLETS      ",0,0],["MASH         ",0,0],["ENHANCED FOOD",0,0]]



#function for printing menu 
def print_menu():
        print("*"*70,"\n","*"*70)
        
        print("   Chook Food"," "*6,"Price(10kg)"," "*6,"Price(50kg)\n")

        print("1.) Pellets"," "*10,"$22.75"," "*10,"$100")
        print("2.) Mash"," "*13,"$20.50"," "*10,"$90")
        print("3.) Enhanced Food"," "*4,"$25.50"," "*10,"$125.50")

        print("-"*70)
        print("::Enter 4 for quit::\n")
             

# function for price calculation
def cal_fun(op):
    index= op-1
    food_lst = qlst[index]
   
    print("\n\t\t>>>",food_lst[0],"<<<")
    print("SELECT THE WEIGHT OF FOOD :")
    print("1. 10 kg\n2. 50 kg\n3.Customize Weight\n::Enter Q for QUIT")
    wt= input("Enter : ")
    if wt is "1":
        wt10(index)
        
    elif wt is "2":
        wt50(index)
        
    elif wt is "3":
        cstmwt(index)
    elif wt is "q":
        return
    else:
        print("\t*INVALID ENTERY")

    

#function for 10kg weight
def wt10(fd_index):
     food_lst = qlst[fd_index]
     price_lst= plst[fd_index]
    
     print("** Food Packing 10kg **\n")
     qt= int(input("Enter the Number of Bags : "))
     
     food_lst[1]=qt
     

# function for 50kg weight
def wt50(fd_index):
     food_lst = qlst[fd_index]
     price_lst= plst[fd_index]
    
     print("** Food Packing 50kg **\n")
     qt= int(input("Enter the Number of Bags : "))
     
     food_lst[2]=qt
     
 
#function for customize weight
def cstmwt(fd_index):
    food_lst = qlst[fd_index]
    price_lst= plst[fd_index]
    print("\n\t\t\t>>>BEST BUY BEST VALUE<<<")
    cw=int(input("\nEnter Weight of Chook Food (multiple of 10): "))
    if cw%10 is 0 and cw>=50: 
        while cw >= 50:
            food_lst[2] = food_lst[2]+1
            cw = cw-50         
            food_lst[1]= int(cw/10)
            break
    elif cw%10 is 0 and cw<50:
         food_lst[1]= int(cw/10)
    else:
        print("*INVALID ENTERY(Please check the weight and enter again)")
        cstmwt(fd_index)        
    
# function for printing bill    
def print_bill():
    print("="*70,"\n\t\tBILL:\n")
    print("Chook Food"," "*12,"Quantity(10kg)"," "*6,"Quantity(50kg)"," "*8,"Amount\n")
    i=0 
    bill=0

    for q in qlst:
        
        p=plst[i]
        
        if q[1] or q[2] is not 0:
             tot =q[1]*p[1]+q[2]*p[2]
             print(q[0]," "*14,q[1]," "*19,q[2]," "*16,"$",tot)
             bill= bill+tot
        i=i+1
    print("\n\n\t\t::TOTAL AMOUNT = $",bill)    
    print("\n\n\t\t>>>THANK YOU<<<")
    
#main function
def main():
    print_menu()
    op =int(input("SELECT : "))
    
    if op is 4:
        return ">>>THANK YOU<<<"
    elif op is 1 or op is 2 or op is 3:    
        cal_fun(op)
        check= input("\n::Enter P for Bill-Pay or Press ENTER key for CONTINUE SHOPPING::")
        if check is "p":
            print_bill()

        else:
            main()
    
    else: 
        print("*INVALID ENTERY")
        main()
   #print("Net bill : ",netbill)
    #print(qlst)
main()