#packages
import os
import time
import json

#displays value to the corresponding key
def read(key):
    isExist=os.path.exists("datastore.json")  
    if isExist!=True: 
        f=open('datastore.json','x')
        print("file is empty")
    else:
        with open('datastore.json','r') as openfile: 
            json_object = json.load(openfile) 
            if key in json_object:
                print(json_object[key]) 
            else:
                print("please enter valid key")
#creates a new key value pair
def create(key,value):
   
    with open('datastore.json','r') as openfile: 
        json_object = json.load(openfile) 
        json_object[key]=value
            
    with open("datastore.json", 'w') as file:
        json.dump(json_object,file)
    print("created successfully")
    
#delete key-value from data store
def delete(key):
    isExist=os.path.exists("datastore.json")  
    if isExist!=True: 
        f=open('datastore.json','x')
        print("file is empty")
    else:
        with open('datastore.json','r') as openfile: 
            json_object = json.load(openfile) 
        if key in json_object:
            del json_object[key]
            with open("datastore.json", 'w') as file:
                json.dump(json_object,file)
                print("deleted successfully")
        else:
            print("please enter valid key")
            #displays data store
def display():  
    isExist=os.path.exists("datastore.json")  
    if isExist!=True: 
        f=open('datastore.json','x')
        print("file is empty")
    else:
        with open('datastore.json','r') as openfile: 
            json_object = json.load(openfile) 
            print(json_object)
            #to check the time to live property
def check_time_to_live_property():
    for i in range(len(l)):
        if l[i][1]!=0 and l[i][1]<time.time():
            delete(l[i][0])
            print("because of time to live property")
            l=[]
while True:
    print("enter 1:create 2.read 3.delete 4.display 5.exit:")
    option=input()
    check_time_to_live_property()
    if option=="1":
        isExist=os.path.exists("datastore.json")  
        if isExist!=True:
            json_object=json.loads("{}")
            with open("datastore.json", 'w') as file:
                json.dump(json_object,file)
        file_size=os.path.getsize('datastore.json') 
        if file_size>(1024*1024*1024):
            print("file size is exceeded the limit of 1GB")
        else:
            key=input("enter key:")
            value=input("enter value(json):")
            timeout=input("enter time to live property value(optional).provide 0 if doesnot want to set property")
            value=json.loads(value)
            if len(key)<=32 and len(value)<(16*1024*1024):
                key='"{}"'.format(key)
                key=json.loads(key)
                create(key,value)
                if timeout=="0":
                    temp=[key,0]
                else:
                    temp=[key,time.time()+float(timeout)]
                l.append(temp)
            else:
                print("please enter key of size less than or equal to 32 char and json value size less than or equal to 16kb")
    elif option=="2":
        read(input("enter key:"))
    elif option=="3":
        delete(input("enter key to delete:"))
    elif option=="4":
        display()
    else:
        break
        
    
    
 
                
