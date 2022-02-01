from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x,y,z = pos.x, pos.y,pos.z

mc.setBlocks(x-20,y,z-20,x+20,y,z+20,1)

while y >20:
    pos = mc.player.getTilePos()
    x,y,z = pos.x, pos.y,pos.z
    time.sleep(0.01)
    mc.setBlock(x,y,z,0)
    