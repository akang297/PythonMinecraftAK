from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 20
z = 28
blockType = 1
mc.player.setTilePos(10,20,28)
mc.setBlock(x, y, z, blockType)