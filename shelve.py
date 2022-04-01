import shelve
with shelve.open("locationsFile.db") as db:
    db['beatrice'] = 'Submarine'
#shelveFile['Beatrice'] = 'Submarine'
#shelveFile.close()