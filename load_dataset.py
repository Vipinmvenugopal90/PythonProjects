#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Loading data to a dictionary for easy fetching
def transdata_load():
    transaction_dataset = {}    
    try:
        #Opening the file
        filename='Transaction.txt'
        with open(filename,'r+') as f:
            lines = f.readlines()            
            #Spliting each lines
            for line in lines:
                (userId, transaction_id, trans_desc, trans_amount,trans_xccord,trans_yccord,trans_label) = line.split(':')
                transaction_dataset.setdefault(userId, {}) 
                #Assigning each columns to dict
                listtrans = {'trans_desc' : trans_desc,'trans_amount': float(trans_amount),'trans_label':trans_label.replace("\n",""),'xaxis': float(trans_xccord),'yaxis' : float(trans_yccord)}                
                transaction_dataset[userId][transaction_id] = listtrans
                #Closing the file            
            f.close()
            return transaction_dataset
                                
    except IOError:
        print("File not exist or check the file name")

        
    
    


    

