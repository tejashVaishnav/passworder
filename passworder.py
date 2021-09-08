import random,array,string,pymongo,os,time,sys,datetime
import pandas as pd
from tqdm import tqdm
from time import sleep
from  pymongo import MongoClient
from termcolor import colored
def passworder():
    #Main Engine
    dt_date = datetime.datetime.now()
    curr_date=''.join(dt_date.strftime("%A, %d %b %Y"))
    print(colored("#============Enter Details:============#", "blue", "on_grey"))
    password_length = int(input("+---->Enter the length:"))
    if password_length > 14:
        print("Length must be less then 13")
        password_length = int(input("+---->Enter the length:"))
    user_mail= input("   |->Enter Email-address:")
    use_for=input("   |->For what:")
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password =[]
    for x in range(password_length):
        password.append(random.choice(password_characters))
    fp =''.join(password)

    print (colored("#============New password:============#","blue","on_grey"))
    print("||-------------------------------------||")
    print("||-------\x1b[6;30;47m",use_for,"\x1b[0m :","\x1b[6;30;42m",fp,"\033[1;35;m-----||\x1b[0m")
    print("||-------------------------------------||")
    print("#======================================#")
    print("-----|->1:Save")
    print("     |->2:Generate Again")
    print("     |->3:Goto To Home")
    generator_curr_state=int(input())
    #-----------------------------Save to DB-------------------#
    if generator_curr_state == 1:
        for i in tqdm(range(0, 100), ncols=100,
                      desc="Saving"):
            sleep(0.01)
        myclient = pymongo.MongoClient("___YOUR___CLUSTER___CONNECTION_URL_____")
        mydb = myclient["___NAME_OF_CLUSTER____"]
        mycol = mydb["__DB_NAME____"]
        mydict = {"_id":random.randint(1,100000),"name": use_for,"Email":user_mail, "password": fp}
        inserter = mycol.insert_one(mydict)
        print(colored("|--------New Password Saved---------|", "grey", "on_green"))
    #-------------------------Genrate again-----------------------#
    elif generator_curr_state == 2:
        passworder()
    #-------------------------------home page-----------------------#
    else:
        main()
def load_saves():
    #=====================Load Saves from DB=====================#
    for i in tqdm(range(0, 100), ncols=100,
                  desc="Loading"):
        sleep(0.01)
    print(colored("|--------Your Saved Passwords---------|", "blue", "on_grey"))
    myclient = pymongo.MongoClient("")
    mydb = myclient[""]
    mycol = mydb[""]
    inventory_data = [data for data in mycol.find()]
    df_inventory_data = pd.DataFrame(inventory_data)
    print (colored(df_inventory_data,"blue",attrs=['bold','underline']))
    print("+=====================================+")
    print("+--|->1:Update  Password")
    print("   |->2:Delete Password")
    print("   |->3:Exit")
    print("+=====================================+")
    load_saves_curr_state = int(input())
    #==============================update Password===========================#
    if load_saves_curr_state == 1:
        print(colored("#============Update password:============#", "blue", "on_grey"))
        update_id = int(input("Enter Password ID to Update:"))
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = []
        for x in range(12):
            password.append(random.choice(password_characters))
        fp = ''.join(password)
        print("||-------------------------------------||")
        print("||-------New passWord", "\x1b[0m :", "\x1b[6;30;42m", fp, "\033[1;35;m  -----||\x1b[0m")
        print("||-------------------------------------||")
        myclient = pymongo.MongoClient("")
        mydb = myclient[""]
        mycol = mydb[""]
        myquery = {"_id": update_id}
        newvalues = {"$set": {"password": fp}}
        mycol.update_one(myquery, newvalues)
        print(colored("|--------Password Updated ---------|", "red", "on_blue"))
    #===================================delet  Updates=================#
    elif load_saves_curr_state == 2:
        print(colored("#============Delete password:============#", "blue", "on_grey"))
        del_row = int(input("Enter the Id number of Password to Delete:"))
        myclient = pymongo.MongoClient("")
        mydb = myclient[""]
        mycol = mydb[""]
        myquery = {"_id":del_row }
        print(colored("|--------Password Deleted---------|", "grey", "on_red"))
        mycol.delete_one(myquery)
    #========================home page===================#
    else :
        main()
#=========================main driver====================#
def main():
    print("+=====================================+")
    bsk ="                                "
    print (colored("|--------------Passbook---------------|","blue","on_grey"),bsk,colored("Current User:","blue","on_grey",attrs=['bold','dark', 'underline']))
    print("+=====================================+")
    print("+--|->1:Generate New Password")
    print("   |->2:Saved Password")
    print("   |->3:Show Credits")
    print("   |->4:Exit")
    print("+=====================================+")
    user_mode=int(input())
    if  user_mode == 1:
        passworder()
    elif user_mode ==2:
        load_saves()
    elif user_mode == 3:
        sho_credits()
    else:
        exit()
while main:
    main()


