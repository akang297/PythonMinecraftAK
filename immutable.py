from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Do you want blocks to be Immutable? Y/N")

if answer == "Y" or answer == "y":
    mc.setting("world_immutable",True)
    mc.postToChat("World is immutable")
else:
    mc.setting("world_immutable",False)
    mc.postToChat("World is mutable")