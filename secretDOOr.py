from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x= 110
y= 6
z= 67
air = 0
gift = mc.getBlock(x, y, z)
pos = mc.player.getTilePos()
if gift == 0:
    mc.setBlocks(pos.x -5, pos.y -1, pos.z -5,pos.x +5, pos.y -1, pos.z +5, air)
else:
    mc.postToChat("Place an offering on the pedestal.")
    mc.setBlocks(x,y,z,x,y+1,z, air)