from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    
    mc.setBlocks(x+2, y+2, z+2,x-2 ,y+3 , z-2, 18)
    mc.setBlocks(x+1, y+4, z,x-1,y+4,z, 18)
    mc.setBlocks(x, y+4, z+1,x,y+4,z-1, 18)
    mc.setBlocks(x+1, y+5, z,x-1,y+5,z, 18)
    mc.setBlocks(x, y+5, z+1,x,y+5,z-1, 18)
    mc.setBlocks(x+1, y+4, z-1,x+1,y+4,z-1, 18)
    mc.setBlocks(x, y, z,x,y+2,z ,17)


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z


growTree(x + 1, y, z)

