from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
def getWoolState(color):
    """Takes a color as a string and return the wool block state for that color"""
    if color == "pink":
        return 6
    elif color != "pink":
        return random.randint(0,15)
    
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
    