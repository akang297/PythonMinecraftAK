from mcpi.minecraft import Minecraft
mc= Minecraft.create()

import time

pos = mc.player.getTilePos()
x=pos.x+1
y=pos.y
z=pos.z
blocks=[20,20,20,20,20,20,20,20,20,20]
barBlock = 22
inc =0
count = 0

while count < len(blocks):
    mc.setBlock(x,y+inc ,z, blocks[inc])
    blocks.pop(len(blocks)-1)
    blocks.insert(0,barBlock)
    time.sleep(1)
    count = count +1
    inc = inc +1
count = 0
inc = 0
while count < len(blocks):
    mc.setBlock(x,y+inc ,z, blocks[inc])
    time.sleep(1)
    count = count +1
    inc = inc +1
   