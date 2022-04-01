import pickle 

secretFile = open("secreatFile.txt" ,"rb")
location = pickle.load(secretFile)
print(location['Phillipa'])
secretFile.close()