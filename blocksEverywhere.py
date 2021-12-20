from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random

def randomBlocklocation(blockType):
    count = 0
    while count <1000:
        x= random.randint(-127,127)
        z= random.randint(-127,127)
        y=mc.getHeight(x,z)
        mc.setBlock(x,y,z,blockType)
        count +=1
        print(count+1)
randomBlocklocation(57)