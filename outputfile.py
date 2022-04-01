from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

todofile = open("TODOLIST.txt" ,"r")

toDoList = todofile.read()

for line in toDoList:
    mc.postToChat(line)
    time.sleep(3)
    
todofile.close()