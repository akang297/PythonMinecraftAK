from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time


while True:
    
    
    
    time.sleep(30)
    blockHits= mc.events.pollBlockHits()
    blockHitsLength = len(blockHits)
    print(blockHitsLength)
    mc.postToChat("Your score is" + str(blockHitsLength))


#blockHitLength = 