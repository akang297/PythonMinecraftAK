from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

def brokenBlock():
    brokenBlocks =[48,67,4,4,4,4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x,y,z = pos.x,pos.y,pos.z
height,width = 100,100
brokenWall=[[brokenBlock() for col in range(width)] for row  in range(height)]


for row in reversed(brokenWall):
    for brokenWall in row:
        mc.setBlock(x,y,z,brokenWall)
        x += 1
    y+= 1
    x=pos.x