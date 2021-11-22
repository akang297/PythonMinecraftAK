from mcpi.minecraft import Minecraft
mc = Minecraft.create()

firstName= "Charles"
lastName = "Christopher"
print(firstName ,lastName)
myGoldenApples = 10
print("My not-so-secret golden apple stash:" + str(myGoldenApples))

print("The year is " + str(19) + str(84))

message = input("Enter your message: ")
mc.postToChat(message)