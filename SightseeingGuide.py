from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places ={}

choice =""
while choice != "exit":
    choice = input("Enter a location('exit to close): ")
    if choice in places:
        location = x+choice
        x,y,z = 10,10,10
        mc.player.setTilePos(x,y,z)