#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Function to calculate the minimum and maximum transaction amount of a particular user
#User inputs the user_id and the function returns the minimum and maximum transaction amount
def minmax(uid,transaction_dataset):
    amount=[]
    uid=verify_user_id(uid,transaction_dataset)
    if (uid == False):
        print("This user_id not exist")
    else:        
        #For loop for fetching the trasaction amount from dataset
        for i in transaction_dataset[uid]:
            amount.append(transaction_dataset[uid][i]["trans_amount"])
        Output = sorted(amount, key = float)
        print("\nThe minimum transaction amount is",min(amount),"The maximum transaction amount is",max(amount))
         
    
        

#Function to calculate the location centroid of all trasactions of a particular user
#User inputs the user_id and the function returns the average of xaxis and yaxis (centroid) of transaction
def location_centroid(uid,transaction_dataset):
    uid=verify_user_id(uid,transaction_dataset)
    if (uid == False):
        print("This user_id not exist")
    else:        
        x_axis=[]
        y_axis=[]
        centroid=[]
        #Loop to fetch the x axis and y axis of all transactions of a user
        for i in transaction_dataset[uid]:
            x_axis.append(transaction_dataset[uid][i]["xaxis"])
            y_axis.append(transaction_dataset[uid][i]["yaxis"])
        print("The centroid is",(round(sum(x_axis)/len(x_axis),2)),(round(sum(y_axis)/len(y_axis),2)))
        return (round(sum(x_axis)/len(x_axis),2)),(round(sum(y_axis)/len(y_axis),2))
        

#Function to calculate the distance between a particular transaction and centroid of that particular user
#User inputs the user_id,transaction id and the function returns the distance from the centroid       
def distance(uid,desc,transaction_dataset):
    uid=verify_user_id(uid,transaction_dataset)
    desc=verify_transaction_id(uid,desc,transaction_dataset)
    if (uid == False or desc == False):
        print("This user_id not exist")
    else:        
        t1=split_desc(desc,transaction_dataset)
        #Calling the centroid of the given user
        cen=location_centroid(uid,transaction_dataset)
        #Finding the difference of xaxis of a given trasaction and xaxis of centroid
        if (transaction_dataset[uid][t1]["xaxis"] > cen[0]):
            x_diff=transaction_dataset[uid][t1]["xaxis"]-cen[0]
        else:
            x_diff=cen[0]-transaction_dataset[uid][t1]["xaxis"] 
        #Finding the difference of yaxis of a given trasaction and yaxis of centroid  
        if (transaction_dataset[uid][t1]["yaxis"] > cen[1]):
            y_diff=transaction_dataset[uid][t1]["yaxis"]-cen[1]
        else:
            y_diff=cen[1]-transaction_dataset[uid][t1]["yaxis"] 
        print('\033[1m'+"The difference is"+'\033[0m',round(x_diff,2) ,round(y_diff,2))
        

#Displays all the transactions under given user
def find_transaction_desc(uid,transaction_dataset):
    desc=[]
    uid=verify_user_id(uid,transaction_dataset)
    if (uid == False):
        print("This user_id is not exist")
    else: 
        #Fetching the transaction details and appending to a list (desc)
        for i in transaction_dataset[uid]:
            desc.append(i+" "+transaction_dataset[uid][i]["trans_desc"])
        print("Please find the transaction under user : "  ,uid )
        #Printing the list with all transaction list
        flag=input("Do you want print all transaction or top 10 yes/no : ")        
        if (flag =='yes'):
            for x in range(len(desc)):
                print(desc[x])
        elif (flag =='no'):
            data=desc[0:10]            
            for x in range(len(data)):
                print(data[x])
        else:
            print("Please give yes or no...Printing the top 10 trasactions")
            data=desc[0:10]            
            for x in range(len(data)):
                print(data[x])
        
        return True

        
#Calculating the standard deviation and variance within one function.
#Standard Deviation is the square root of Variance
def standard_deviation_and_variance(uid,transaction_dataset):
    uid=verify_user_id(uid,transaction_dataset)
    if (uid == False):
        print("This user_id not exist")
    else: 
        amount=[]
        #Fetching all trasaction under given user
        for i in transaction_dataset[uid]:
            amount.append(transaction_dataset[uid][i]["trans_amount"])
        sum=0
        #Identifying the mean
        for i in range(len(amount)):
            sum+=amount[i]
        mean= sum/len(amount)
        sum_squared_deviation = 0
        #Finding the difference of each transaction from mean and finding the sum of difference
        for i in range(len(amount)):
            sum_squared_deviation+=(amount[i]- mean)**2        
        Variance = ((sum_squared_deviation)/len(amount))
        Standard_Deviation = Variance ** 0.5
        return round(Standard_Deviation,2),round(Variance,2)

#Identifying whether the given user is fraud or not usning the trans label
def fradualent(uid,desc,transaction_dataset):
    uid=verify_user_id(uid,transaction_dataset)
    desc=verify_transaction_id(uid,desc,transaction_dataset)
    if (uid == False or desc == False):
        print("This user_id/transaction id not exist")
    else: 
        t1=split_desc(desc,transaction_dataset)
        trans_label=transaction_dataset[uid][t1]["trans_label"]        
        if(trans_label =='false'):            
            print('\033[32m'+'\033[1m'+ "This transaction is not fraud" +'\033[0m')
        elif trans_label == 'true':
            print('\033[31m'+'\033[1m'+ "This transaction is fraud" +'\033[0m')
            #Displaying all the details if the given transaction is fraud
            print("The details are",transaction_dataset[uid][t1]["trans_desc"],"Amount",transaction_dataset[uid][t1]["trans_amount"],"Xaxis",transaction_dataset[uid][t1]["xaxis"],"Yaxis",transaction_dataset[uid][t1]["yaxis"])
        else:
            print("This user_id/transaction id is not exist")

#Calculating the distance between the two different transaction  of the same user
def distance_trans_userid(uid,desc1,desc2,transaction_dataset): 
    uid=verify_user_id(uid,transaction_dataset)
    desc1=verify_transaction_id(uid,desc1,transaction_dataset)
    desc2=verify_transaction_id(uid,desc2,transaction_dataset)
    if (uid == False or desc1 == False or desc2 == False):
        print("This user_id/transaction id not exist")
    else: 
        print("Distance between any two transaction of a user ")
        #Spliting the transaction id from the given input
        t1=split_desc(desc1,transaction_dataset)
        t2=split_desc(desc2,transaction_dataset)
        #Calculating the difference of xaxis from two different transactions of the given user
        if (transaction_dataset[uid][t1]["xaxis"] > transaction_dataset[uid][t2]["xaxis"]):
            x_diff=transaction_dataset[uid][t1]["xaxis"]-transaction_dataset[uid][t2]["xaxis"]
        else:
            x_diff=transaction_dataset[uid][t2]["xaxis"]-transaction_dataset[uid][t1]["xaxis"] 
        #Calculating the difference of yaxis from two different transactions of the given user
        if (transaction_dataset[uid][t1]["yaxis"] > transaction_dataset[uid][t2]["yaxis"]):
            y_diff=transaction_dataset[uid][t1]["yaxis"]-transaction_dataset[uid][t2]["xaxis"]
        else:
            y_diff=transaction_dataset[uid][t2]["yaxis"]-transaction_dataset[uid][t1]["yaxis"] 
        print("The difference is",round(x_diff,2) ,round(y_diff,2))


#Calculates the distance between two transaction of two different user        
def distance_userid(uid,uid2,desc1,desc2,transaction_dataset):
    uid=verify_user_id(uid,transaction_dataset)
    uid2=verify_user_id(uid2,transaction_dataset)
    if (uid ==uid2):
        print("Give different user id")
        
    else:
        desc1=verify_transaction_id(uid,desc1,transaction_dataset)
        desc2=verify_transaction_id(uid2,desc2,transaction_dataset)
        if (uid == False or desc1 == False or uid2 == False or desc2 == False):
            print("This user_id/transaction id not exist")
        else: 
            print("Distance between any two transaction of a different users ")
            #Spliting the transaction id from the given input
            t1=split_desc(desc1,transaction_dataset)
            t2=split_desc(desc2,transaction_dataset)
            #Calculating the difference of xaxis from two different transactions of the given users
            if (transaction_dataset[uid][t1]["xaxis"] > transaction_dataset[uid2][t2]["xaxis"]):
                x_diff=transaction_dataset[uid][t1]["xaxis"]-transaction_dataset[uid2][t2]["xaxis"]
            else:
                x_diff=transaction_dataset[uid2][t2]["xaxis"]-transaction_dataset[uid][t1]["xaxis"] 
            #Calculating the difference of yaxis from two different transactions of the given users   
            if (transaction_dataset[uid][t1]["yaxis"] > transaction_dataset[uid2][t2]["yaxis"]):
                y_diff=transaction_dataset[uid][t1]["yaxis"]-transaction_dataset[uid2][t2]["yaxis"]
            else:
                y_diff=transaction_dataset[uid2][t2]["yaxis"]-transaction_dataset[uid][t1]["yaxis"] 
            print("The difference is",round(x_diff,2) ,round(y_diff,2))
        

#Function to verify the transaction  
def verify_transaction_id(uid,desc,transaction_dataset):
    try:
        
        splitted1=desc.split(" ", 1)
        t1=str(splitted1[0])
        #Verifying that the given transaction is exist for the given user
        if(t1 in transaction_dataset[uid]):
            return t1
        else:
            print("Invalid transaction id")
            return False 
    except KeyError:
        print("Invalid transaction id")
        return False 
    
#Function to verify the user      
def verify_user_id(uid,transaction_dataset):  
    #Verifying that the given transaction is exist for the given user
    if uid in transaction_dataset:
         return uid
    else:
        return False
    
#Function to get transaction id from user input    
def split_desc(desc,transaction_dataset):   
    splitted1=desc.split(" ", 1)
    t1=str(splitted1[0])
    return t1

       
         
