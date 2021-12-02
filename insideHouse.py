from mcpi.minecraft import Minecraft
mc = Minecraft.create()


buildX = 1
buildY = 1
buildZ = 1
width = 10
height = 5
length = 6


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
print(x)
print(y)
print(z)

if 0<x<20 and 0<z<20 and y==10:
    mc.postToChat("You are in house!")
else:
    mc.postToChat("You are not in house!")
