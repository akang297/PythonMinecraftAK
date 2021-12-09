from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
floorx = pos.x-2
floory= pos.y-1
floorz = pos.z -2
width = 5
length = 5
block = 41

mc.setBlocks(floorx, floory,floorz,floorx+width,floory,floorz+length,block)

while True:
    pos = mc.player.getTilePos()
    while floorx <= pos.x <= floorx+width and floorz <= pos.z <= floorz + length:
        if block ==41:
            block = 57
            mc.setBlocks(floorx, floory,floorz,floorx+width,floory,floorz+length,block)
            pos = mc.player.getTilePos()
            time.sleep(0.5)
        else:
            block=41
            mc.setBlocks(floorx, floory,floorz,floorx+width,floory,floorz+length,block)
            pos = mc.player.getTilePos()
            time.sleep(0.5)
