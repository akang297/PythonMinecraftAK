import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
#mc.postToChat("Hello world")
#mc.player.setPos(-125,100,64)
while True:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y,p.z, block.STONE)
    

    
