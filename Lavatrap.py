import mcpi.minecraft as minecraft# you need to use this if you are using block
import mcpi.block as block
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat("Welcome to the Lava Trap")
mc.player.setPos(100,45,100)
pos = mc.player.getTilePos()

mc.setBlocks(pos.x -10, pos.y -1, pos.z -10,
             pos.x +10, pos.y -1, pos.z +10, block.WOOL.id)

#mc.setBlocks(pos.x -5, pos.y -1, pos.z -5,
             #pos.x +5, pos.y -1, pos.z +5, block.LAVA.id)
#mc.setBlock(pos.x , pos.y -1, pos.z , block.DIAMOND_BLOCK.id)


