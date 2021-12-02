from mcpi.minecraft import Minecraft
mc=Minecraft.create()

answer =input("Create a crater? Y/n")
if answer =="Y" or answer == "y":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x +20, pos.y +10, pos.z +20, pos.x-20 ,pos.y-30, pos.z-20,0)
    mc.postToChat("BOOM!")
