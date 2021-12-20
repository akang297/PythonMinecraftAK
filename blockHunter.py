from mcpi.minecraft import Minecraft
import math
import time
import random
mc = Minecraft.create()

destX = random.randint(-127 ,127)
destZ = random.randint(-127 ,127)
destY = mc.getHeight(destX, destZ)

block = 57
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Block Set")


while True:
    pos = mc.player.getPos()
    distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
    
    if distance > 100:
        mc.postToChat("Freezing")
        print(distance)
    elif distance > 50:
        mc.postToChat("Cold")
        print(distance)
    elif distance > 25:
        mc.postToChat("Warm")
        print(distance)
        
    elif distance > 12:
        mc.postToChat("On fire!")
        print(distance)
    elif distance > 0:
        print(distance)
    elif distance <=1:
        mc.postToChat("Found it")
        print(distance)
        print("Found")
        