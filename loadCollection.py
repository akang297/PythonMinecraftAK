from mcpi.minecraft import Minecraft
import pickle
mc = Minecraft.create()
def buildStructure(x,y,z,structure):
    startingX = x
    startingY = y

    for depth in structure:
        for height in reversed(depth):
            for block in height:
                mc.setBlock(x,y,z,block)
                y+= 1
            x+=1
            y=startingY
            
        z+=1
        x=startingX
        
pos = mc.player.getTilePos()
structureName= input("Enter the structure's name")
with open("COPYSTRUCTURE.txt","rb") as s:
    structure2 = pickle.load(s)

input("Move to the position you want to create the structure and press Enter in this window")
x,y,z= pos.x,pos.y,pos.z

buildStructure(x,y,z,structure2)

      