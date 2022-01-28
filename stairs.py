from mcpi.minecraft import Minecraft
mc= Minecraft.create()

pos = mc.player.getTilePos()
x,y,z = pos.x,pos.y,pos.z

stair =53

step = 0
while step <100:
    mc.setBlock(x+step,y+ step,z ,stair)
    step +=1