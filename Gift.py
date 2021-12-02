from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=10
y=11
z=12

gift = mc.getBlocks(x,y,z)

if gift == mc.getBlocks(x,y,z):
    mc.postToChat("It is diamond!")
else:
    mc.postToChat("Bring a gift to" + str(x)+","+str(y)+","+str(z))