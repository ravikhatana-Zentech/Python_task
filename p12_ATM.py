'''Create an ATM machine
- User should be able get money out of it
- User should be able to deposite money into it
- You must ask card number and pin before any transaction
- User can get overall information about his bank account
- There should be a limit in one time transaction and total transaction in a day (Consider day as from 
starting of script to exit)
- Limit on number of transaction
- Let user choose the bank of ATM
- Every ATM will have some initial balance
- Every user has it's own bank
- If user takes money from an ATM other than his bank take 5% cut in withdrawl amount
Nice to have features:
- Insert, update and delete users (Generate card number and PIN randomly)
- Insert, update and delete ATMs
- Insert, update and delete banks
- Insert money into ATM (No database is needed for this  it can be managed using dicts)

''''



class ATM_System:
    ad = Admin("Ravi","ravi123")
    list_of_ATM = list()
    list_of_Account = list()
    no_of_atm = 0
    no_of_account = 0
    
    def Admin_login(self,sys_username,sys_password):
        re = self.ad.login(sys_username,sys_password)
        return re

    def Delete_Account(self):
        if self.no_of_account == 0:
            print("no Account is available")
            return
        sys_Card_No = int(input("enter user's card number : "))
        for sys_ac in self.list_of_Account:
            if sys_ac.Card_No == sys_Card_No:
                self.list_of_Account.remove(sys_ac)
                self.no_of_account -= 1
                print("account deleted")
            else: 
                print("*Please enter valid Card No*")
    def Change_password(self):
        sys_Card_No = int(input("enter card number : "))
        sys_Password = int(input("enter old pin : "))
        # sys_Password =
        for sys_ac1 in self.list_of_Account:
            if sys_ac1.Card_No == sys_Card_No:
                sys_ac1.Change_password(sys_Card_No,sys_Password)
                return
        else: 
            print("*Please enter valid Card No*")

    def Show_ALL_Account_list(self):
        if self.no_of_account == 0:
            print("No Account available")
            return
        print("list of account :")
        for sys_acc in self.list_of_Account:
            print(sys_acc.Card_No)

    def Create_Account(self):
        print("enter details : ")
        sys_name = input("enter name of account holder")
        sys_card_no = int(input("enter card No :"))
        sys_pin = int(input("enter 4 digit pin :"))
        sys_Bank_name = input("enter bank name :")
        sys_ballance = float(input("enter ballance Amount:"))
        # print("----------------------------------------------")
        sys_acc1 = Account(sys_name,sys_card_no,sys_Bank_name,sys_ballance,sys_pin)
        self.list_of_Account.append(sys_acc1)
        self.no_of_account+=1
        print("*Account created succesfully*")

    def Show_account(self):
        sys_card1 = int(input("enter card No :"))
        sys_pin1 = int(input("enter pin :"))
        print("---------------------------------------------")
        # amount = float(input("enter Amount :"))
        for ac in self.list_of_Account:
            if ac.Card_No == sys_card1 and ac.Ac_Password == sys_pin1:
                ac.show_Account_info()
                break
        else: 
            print("*Please enter valid Card No or pin*")
    def Withdraw_Amount(self):
        if self.no_of_atm == 0:
            print("no atm is available")
            return
        w_bank = input("select Bank :")
        w_card = int(input("enter card No :"))
        w_pin = int(input("enter pin :"))
        w_amount = float(input("enter Amount :"))
        print("---------------------------------------------")
        
        for a in Sys1.list_of_ATM:
            if a.Bank_of_ATM == w_bank:
                w_atm = a
                break
        else:
            print("*please select valid bank for ATM*")
        if(w_atm.Ballance_of_ATM<w_amount):
            print("*insufisunt amount in ATM*")
            return
        else:            
            for ac in self.list_of_Account:
                if ac.Card_No == w_card:
                    transection = ac.Withdraw(w_card,w_pin,w_amount,w_atm.Bank_of_ATM)
                    if transection:
                        w_atm.Ballance_of_ATM-=w_amount
                        print("transection done succesfully")
                    else:
                        print("transection isn't done yet please retry")
                            
                else: 
                    print("*Please enter valid Card No*")
                    break

    def Deposite_Amount(self):
        if self.no_of_atm == 0:
            print("no atm is available")
            return
        d_bank = input("select Bank :")
        d_card = int(input("enter card No :"))
        d_pin = int(input("enter pin :"))
        d_amount = float(input("enter Amount :"))
        for a in Sys1.list_of_ATM:
            if a.Bank_of_ATM == d_bank:
                d_atm = a
                break
        else:
            print("*please select valid bank for ATM*")
        for ac in self.list_of_Account:
            if ac.Card_No == d_card:
                transection = ac.Deposite(d_card,d_pin,d_amount,d_atm.Bank_of_ATM)
                if transection:
                    d_atm.Ballance_of_ATM+=d_amount  
                    print("transection done succesfully")
                else:
                    print("transection isn't done yet please retry")
            else: 
                print("*Please enter valid Card No*")
                break
                
        

                
    def show_list_of_ATM(self):
        if self.no_of_atm == 0:
            print("*no bank atm available*")
            return
        else:
            for atm in self.list_of_ATM:
                print(atm.Bank_of_ATM)
            
    def Create_ATM(self):
        Bank_of_ATM = input("enter bank name of ATM :")
        Ballance_of_ATM = float(input("enter amount for ballance of ATM :"))
        ATM_id = input("enter atm id :")
        self.list_of_ATM.append(ATM(ATM_id,Bank_of_ATM,Ballance_of_ATM))
        self.no_of_atm+=1
        

    def Fill_ATM(self):
        if self.no_of_atm == 0:
            print("NO atm ia avaialable")
            return
            
        ATM_id = input("eneter ATM id :")
        amount = float(input("enter amount :"))
        for i in Sys1.list_of_ATM:
            if i.ATM_id == ATM_id:
                i.fill_ATM(amount)
                print("*Atm filld*")
        else:
            print("*please enter valid atm id*")

    def Cheak_ATM_Ballance(self):
        if self.no_of_atm == 0:
            print("NO atm ia avaialable")
            return
               
        ATM_id = input("enter ATM id :")
        for i in self.list_of_ATM:
            if i.ATM_id == ATM_id:
                i.Cheak_ATM_Ballance()
                
        else:
            print("*please enter valid atm id*")

    def Delete_ATM(self):
        if self.no_of_atm == 0:
            print("NO atm ia avaialable")
            return
            
        ATM_id = input("enter ATM id :")
        for i in self.list_of_ATM:
            if i.ATM_id == ATM_id:
                self.list_of_ATM.remove(i)
                self.no_of_atm-=1
                print("*ATM deleted successfully*")
                
        else:
            print("*please enter valid atm id*")

class ATM:
    
    def __init__(self,ATM_id,Bank_of_ATM,Ballance_of_ATM):
        self.Bank_of_ATM = Bank_of_ATM
        self.Ballance_of_ATM = Ballance_of_ATM
        self.ATM_id = ATM_id
    def fill_ATM(self,amount_to_fill):
        self.Ballance_of_ATM += amount_to_fill 

    def Cheak_ATM_Ballance(self):
        print(f"Amount is : {self}")



class Account:
    def __init__(self,name,Card_No,Bank_Name, Ballance, Ac_Password):
        self.name = name
        self.Card_No = Card_No
        self.Bank_Name = Bank_Name 
        self.Ballance = Ballance
        self. Ac_Password =  Ac_Password
        self.Transaction_Limit = 30000
        self.Par_day_limit = 50000
        self.No_Transaction = 10

    def show_Account_info(self):
        print(f"account holder name : {self.name} \nCard No : {self.Card_No} \nPasswor : {self.Ac_Password}\nBank Name = {self.Bank_Name} \nBallance :{self.Ballance} \n")
        
    def Deposite(self,Card_No,Ac_Password,Amount,bank_atm):
        if Card_No == self.Card_No and Ac_Password == self.Ac_Password:
            if Amount<self.Transaction_Limit:
                if Amount<self.Par_day_limit:
                    if self.No_Transaction>0:
                        if bank_atm != self.Bank_Name:
                            Amount -= (Amount*5)//100
                            print("*we will cut 5% because of transection from another Bank*")
                        self.Ballance+=Amount
                        self.No_Transaction-=1
                        self.Par_day_limit-=Amount
                        print("*Amount deposited*")
                            
                        return True
                    else:
                        print("*you reached your daily no of transaction limit*")
                else:
                    print("*you reached your daily transaction limit*")
            else:
                print("*Amount exicced transection limit*")
        else:
            print("*please enter valid card No and password*")

    def Withdraw(self,Card_No,Ac_Password,Amount,bank_atm):
        if bank_atm != self.Bank_Name:
            Amount += (Amount*5)//100
            print("*we will cut 5% because of transection from another Bank*")
            
        if Card_No == self.Card_No and Ac_Password == self.Ac_Password:
            if Amount<self.Transaction_Limit:
                if Amount<self.Par_day_limit:
                    if self.No_Transaction>0:
                        if Amount<self.Ballance:
                            self.Ballance-=Amount
                            self.No_Transaction-=1
                            self.Par_day_limit-=Amount
                            print("Amount Withdrwaed")
                            return True
                    else:
                        print("*you reached your daily no of transaction limit*")
                else:
                    print("*you reached your daily transaction limit*")
            else:
                print("*Amount exceeds transection limit*")
        else:
            print("*please enter valid card No and password*")


    def Change_password(self,Card_No,Password):
        if Card_No == self.Card_No and Password == self.Ac_Password:
            New_Password = input("Enter New Password")
            self.Ac_Password = New_Password
            print("*Password changed*")
        else:
            print("*please enter valid card No and password*")
        



class Admin:
    Admin_id = ""
    password=""
    def __init__(self,Admin_id,password):
        self.Admin_id = Admin_id
        self.password = password
        
        
    def login(self,Admin_id,password):
        if(Admin_id == self.Admin_id and password == self.password):
            return True
        else:
            print("*Please enter valid id password*")
            return False

    def Create_ATM(self,Bank_of_ATM,Ballance_of_ATM):
        Sys1.Create_ATM(Bank_of_ATM,Ballance_of_ATM)

    def Create_Account(self,Card_No,Bank_Name, Ballance, Ac_Password):
        Sys1.Create_ATM(Card_No,Bank_Name, Ballance, Ac_Password)

        

    def Fill_ATM(self,ATM_id,amount_fill):
        Sys1.Fill_ATM(ATM_id,amount_fill)
       
    def Cheak_ATM_Ballance(self,ATM_id):
        Sys1.Cheak_ATM_Ballance(ATM_id)

    def Show_All_ATM(self):
        Sys1.show_list_of_ATM()

    def Show_All_Account(self):
        Sys1.Show_ALL_Account_list()








Sys1 = ATM_System()




while True:
    print("----------------------------------------------------------------------------")
    user = input("\n1.Admin \n2.user \n3.exit \nenter number as par option ")
    if user == "1":
        username = input("enter user name :")
        password = input("enter Password :")
        # print("------------------------------------------------------------------------")
        log = Sys1.Admin_login(username,password)
        while log:
            print("--------------------------------------------------------------------")
            op1 = input(" \n1.create account \n2.Delete Account  \n3.show list of all Account \n4.create Atm   \n5.Delete ATM \n6.cheak Ballance of ATM \n7.fill ATM  \n8.show list of All ATM  \n9.exit \nenter number as par option :")
            if op1 == "1":
                print("--------------------------------------------------------------------")
                Sys1.Create_Account()

            elif op1 == "2":
                print("--------------------------------------------------------------------")
                Sys1.Delete_Account()

            elif op1 == "3":
                print("--------------------------------------------------------------------")
                Sys1.Show_ALL_Account_list()

            elif op1 == "4":
                print("--------------------------------------------------------------------")
                Sys1.Create_ATM()
                
                
            elif op1 == "5":
                print("--------------------------------------------------------------------")
                Sys1.Delete_ATM()

            elif op1 == "6":
                print("--------------------------------------------------------------------")
                Sys1.Cheak_ATM_Ballance()

            elif op1 == "7":
                print("--------------------------------------------------------------------")
                Sys1.Fill_ATM()

            elif op1 == "8":
                print("--------------------------------------------------------------------")
                Sys1.show_list_of_ATM()            
                
            elif op1 == "9":
                break
            else :
                print("--------------------------------------------------------------------")
                print("*please entr valid number*")
            
            print("--------------------------------------------------------------------")
                
        
    elif user == "2":
        while True:
            print("--------------------------------------------------------------------")
            op = input("1.Deposite Amount \n2.Withdraw Amount \n3.Account info \n4.change pin \n5.back \nenter number as par option :")
            if op == "1":
                print("-------------------------")
                print("list of available bank:")
                Sys1.show_list_of_ATM()
                print("-------------------------")
                
                Sys1.Deposite_Amount()
            elif op == "2":
                print("-------------------------")
                print("*list of available bank:*")
                Sys1.show_list_of_ATM()
                print("--------------------------")
                Sys1.Withdraw_Amount()
            elif op == "3":
                Sys1.Show_account()
            elif op == "4":
                print("--------------------------")
                Sys1.Change_password()
            elif op == "5":
                break
            else:
                print("*please enter valid number*")
            
            print("--------------------------------------------------------------------")
            

    elif user == "3":
        print("Thanks for visit.")
        break

    else:
        print("*please enter valid No. of option*")
            