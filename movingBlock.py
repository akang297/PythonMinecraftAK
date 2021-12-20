from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def calculateMove(x,y,z):
    
    currentHeight = mc.getHeight(x,z) -1
    forwardHeight = mc.getHeight(x+1,z)
    rightHeight = mc.getHeight(x+1,z)
    backwardHeight = mc.getHeight(x-1,z)
    leftHeight = mc.getHeight(x,y,z-1)
    if forwardHeight - currentHeight<3:
        return 'w'
    elif rightHeight - currentHeight < 3:
        return 'd'
    elif leftHeight - currentHeight < 3:
        return 'a'
    elif backwardHeight - currentHeight < 3:
        return 's'
    
    
    
pos = mc.player.getTilePos()
x = pos.x
z = pos.z
y = mc.getHeight(x,z)
mc.setBlock(x,y,z,103)
while True:
    if calculateMove(x,y,z) == 'w':
        print(calculateMove(x,y,z))
        x= x+1
        mc.setBlock(x,y,z,103)
        mc.setBlock(x-1,y,z,0)
    if calculateMove(x,y,z) == 'd':
        print(calculateMove(x,y,z))
        z= z+1
        mc.setBlock(x,y,z,103)
        mc.setBlock(x,y,z-1,0)
    if calculateMove(x,y,z) == 'a':
        print(calculateMove(x,y,z))
        z= z-1
        mc.setBlock(x,y,z,103)
        mc.setBlock(x,y,z+1,0)
    if calculateMove(x,y,z) == 's':
        print(calculateMove(x,y,z))
        x= x-1
        mc.setBlock(x,y,z,103)
        mc.setBlock(x+1,y,z,0)
    time.sleep(0.1)
    
