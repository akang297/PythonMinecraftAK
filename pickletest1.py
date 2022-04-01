from pickle import dump,load


location = {'John':'Forest','Phillipa':'Mountains','Pete':'City'}
secretFile = open("secreatFile.txt","wb")
dump(location ,secretFile)


print(locations['Phillipa'])
secretFile.close()