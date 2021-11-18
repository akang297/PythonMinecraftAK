from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 10.0
y= 110.0
z=12.0


mc.player.setTilePos(x,y,z)
time.sleep(10)

x = 100.0
y= 110.0
z=1.0


mc.player.setTilePos(x,y,z)