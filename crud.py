# import json,os
# d = json.load(open('file.json','r'))

# numList =['name','salary','age']
# if not os.path.isfile('file.json'):
#     open('file.json','w')
# def maintan_data(name):                 # this is data management function
#         dataFile=open('file.json','w')
#         data2=json.dumps(d,indent=4)
#         dataFile.write(data2)
# def create(name):                   # this is create user data function 
#     d2={}
#     for ask in numList:
#             print('enter the',ask)
#             r=input('____:')
#             d2[ask]=r
#     print('\n \t successfully add your data !!\n')    
#     d[name]=d2
#     maintan_data(name)

# def update_Data(name):              # this is update user data function
#     datafile2=open('file.json','r')
#     hold2=datafile2.read()
#     d=json.loads(hold2)
#     li=[k for k in d.keys()]
#     if name in li:
#         li2=[k2 for k2 in d[name].keys()]
#         print(li2)
#         ch=input('what you want to change :')
#         if ch in li2:
#             ans=input('enter the new value :')
#             d[name][ch]=ans
#             print('\n \tsuccessfully update your data !!\n') 
#         else:
#             print('you enter something wrong')
#     maintan_data()
# def delete_Data(name):              # this is delete user data function
#     datafile2=open('file.json','r')
#     hold2=datafile2.read()
#     x=json.loads(hold2)
#     del d[name]
#     print('\n \t successfully delete your data !!\n') 
#     maintan_data()
# def read_Data(d,name): #this is read function
#     print(">>>>>>>>>>>>>>>>>>")
#     print(d[name])                       
# while True:                         #this is starting 
#     f3=open('file.json')
#     s=f3.read()
#     f3.close()
#     if len(s)>1:                    #this is loading data for the json file
#         def add():
#             f4=open('file.json')
#             h5=f4.read()
#             l=json.loads(h5)
#             f4.close()
#             d=l
#         add()
#     print('\n 1) Create_Data \n 2) UPdate_Data \n 3) Delete_Data \n 4) Read_Data \n 5) Exit \n')
#     c=input('enter :')
#     if c=='exit' or c=='5':
#         print('<<<<<<<<<<come again>>>>>>>>>>>')
#         break
#     name=input('\n enter the gmail :') 
#     name=name.lower()
#     if c=='1' :
#         n=name[-10:]
#         if name not in d:
#             if n=='@gmail.com':create(name)
#         else:print('this gmail is already avalable')
#     elif c=='2' :
#         if name in d:update_Data(name)
#         else:print('this gmail not avalable\n')
#     elif c=='3' :
#         if name in d:delete_Data(name)
#         else:print('this gmail not avalable \n')
#     elif c=='4' :
#         with open('./file.json') as fs:
#             data = json.loads(fs.read())
#         if name in data:
#             read_Data(data,name)
#         else:
#             print('this gmail not avalable\n')
#     if 'total'==name:
#         print(d)  







