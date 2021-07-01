#house.py 
from mcpi.minecraft import Minecraft
from mcpi import block



ip = "10.183.3.20"
mc = Minecraft.create(ip, 4711)
x, y, z = mc.player.getPos() 



# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-19,-1,-19,30,64,19,air) # clear some air   
#mc.setBlocks(x+100,y,z-100,x+100,y+640,+100,0)                                            
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
print(xyzString)



mc.setBlock(0,8,4,5,17)
mc.setBlock(0,8,5,5,17)


mc.setBlock(0,7,3,5,17)
mc.setBlock(0,7,4,5,17)
mc.setBlock(0,7,5,5,17)
mc.setBlock(0,7,6,5,17)

mc.setBlock(0,6,3,5,17)
mc.setBlock(0,6,4,5,17)
mc.setBlock(0,6,5,5,17)
mc.setBlock(0,6,6,5,17)
mc.setBlock(0,6,7,5,17)

mc.setBlock(0,5,1,5,17)
mc.setBlock(0,5,2,5,17)
mc.setBlock(0,5,3,5,17)
mc.setBlock(0,5,4,20,17)
mc.setBlock(0,5,5,20,17)
mc.setBlock(0,5,6,20,17)
mc.setBlock(0,5,7,5,17)
mc.setBlock(0,5,8,5,17)
mc.setBlock(0,5,9,5,17)


mc.setBlock(0,4,1,5,17)
mc.setBlock(0,4,2,5,17)
mc.setBlock(0,4,3,5,17)
mc.setBlock(0,4,4,20,17)
mc.setBlock(0,4,5,20,17)
mc.setBlock(0,4,6,20,17)
mc.setBlock(0,4,7,5,17)
mc.setBlock(0,4,8,5,17)
mc.setBlock(0,4,9,5,17)


mc.setBlock(0,3,1,5,17)
mc.setBlock(0,3,2,5,17)
mc.setBlock(0,3,3,5,17)
mc.setBlock(0,3,4,20,17)
mc.setBlock(0,3,5,20,17)
mc.setBlock(0,3,6,20,17)
mc.setBlock(0,3,7,5,17)
mc.setBlock(0,3,8,5,17)
mc.setBlock(0,3,9,5,17)

mc.setBlock(0,2,1,5,17)
mc.setBlock(0,2,2,5,17)
mc.setBlock(0,2,3,5,17)
mc.setBlock(0,2,4,5,17)
mc.setBlock(0,2,5,5,17)
mc.setBlock(0,2,6,5,17)
mc.setBlock(0,2,7,5,17)
mc.setBlock(0,2,8,5,17)
mc.setBlock(0,2,9,5,17)

mc.setBlock(0,1,1,5,17)
mc.setBlock(0,1,2,5,17)
mc.setBlock(0,1,3,5,17)
mc.setBlock(0,1,4,5,17)
mc.setBlock(0,1,5,5,17)
mc.setBlock(0,1,6,5,17)
mc.setBlock(0,1,7,5,17)
mc.setBlock(0,1,8,5,17)
mc.setBlock(0,1,9,5,17)


mc.setBlock(0,5,1,35,15)
mc.setBlock(0,4,1,35,15)
mc.setBlock(0,3,1,35,15)
mc.setBlock(0,2,1,35,15)
mc.setBlock(0,1,1,35,15)
mc.setBlock(0,0,1,35,15)
mc.setBlock(0,0,2,35,15)
mc.setBlock(0,0,3,35,15)
mc.setBlock(0,0,4,35,15)
mc.setBlock(0,0,5,35,15)
mc.setBlock(0,0,6,35,15)
mc.setBlock(0,0,7,35,15)
mc.setBlock(0,0,8,35,15)
mc.setBlock(0,0,9,35,15)
mc.setBlock(0,1,9,35,15)
mc.setBlock(0,2,9,35,15)
mc.setBlock(0,3,9,35,15)
mc.setBlock(0,4,9,35,15)
mc.setBlock(0,5,9,35,15)
mc.setBlock(0,6,2,35,15)
mc.setBlock(0,7,3,35,15)
mc.setBlock(0,8,4,35,15)
mc.setBlock(0,9,5,35,15)
mc.setBlock(0,8,6,35,15)
mc.setBlock(0,7,7,35,15)
mc.setBlock(0,6,8,35,15)


mc.setBlock(1,5,1,35,15)
mc.setBlock(1,4,1,35,15)
mc.setBlock(1,3,1,35,15)
mc.setBlock(1,2,1,35,15)
mc.setBlock(1,1,1,35,15)
mc.setBlock(1,0,1,35,15)
mc.setBlock(1,0,2,35,15)
mc.setBlock(1,0,3,35,15)
mc.setBlock(1,0,4,35,15)
mc.setBlock(1,0,5,35,15)
mc.setBlock(1,0,6,35,15)
mc.setBlock(1,0,7,35,15)
mc.setBlock(1,0,8,35,15)
mc.setBlock(1,0,9,35,15)
mc.setBlock(1,1,9,35,15)
mc.setBlock(1,2,9,35,15)
mc.setBlock(1,3,9,35,15)
mc.setBlock(1,4,9,35,15)
mc.setBlock(1,5,9,35,15)
mc.setBlock(1,6,2,35,15)
mc.setBlock(1,7,3,35,15)
mc.setBlock(1,8,4,35,15)
mc.setBlock(1,9,5,35,15)
mc.setBlock(1,8,6,35,15)
mc.setBlock(1,7,7,35,15)
mc.setBlock(1,6,8,35,15)

mc.setBlock(2,5,1,35,15)
mc.setBlock(2,4,1,35,15)
mc.setBlock(2,3,1,35,15)
mc.setBlock(2,2,1,35,15)
mc.setBlock(2,1,1,35,15)
mc.setBlock(2,0,1,35,15)
mc.setBlock(2,0,2,35,15)
mc.setBlock(2,0,3,35,15)
mc.setBlock(2,0,4,35,15)
mc.setBlock(2,0,5,35,15)
mc.setBlock(2,0,6,35,15)
mc.setBlock(2,0,7,35,15)
mc.setBlock(2,0,8,35,15)
mc.setBlock(2,0,9,35,15)
mc.setBlock(2,1,9,35,15)
mc.setBlock(2,2,9,35,15)
mc.setBlock(2,3,9,35,15)
mc.setBlock(2,4,9,35,15)
mc.setBlock(2,5,9,35,15)
mc.setBlock(2,6,2,35,15)
mc.setBlock(2,7,3,35,15)
mc.setBlock(2,8,4,35,15)
mc.setBlock(2,9,5,35,15)
mc.setBlock(2,8,6,35,15)
mc.setBlock(2,7,7,35,15)
mc.setBlock(2,6,8,35,15)


mc.setBlock(3,5,1,35,15)
mc.setBlock(3,4,1,35,15)
mc.setBlock(3,3,1,35,15)
mc.setBlock(3,2,1,35,15)
mc.setBlock(3,1,1,35,15)
mc.setBlock(3,0,1,35,15)
mc.setBlock(3,0,2,35,15)
mc.setBlock(3,0,3,35,15)
mc.setBlock(3,0,4,35,15)
mc.setBlock(3,0,5,35,15)
mc.setBlock(3,0,6,35,15)
mc.setBlock(3,0,7,35,15)
mc.setBlock(3,0,8,35,15)
mc.setBlock(3,0,9,35,15)
mc.setBlock(3,1,9,35,15)
mc.setBlock(3,2,9,35,15)
mc.setBlock(3,3,9,35,15)
mc.setBlock(3,4,9,35,15)
mc.setBlock(3,5,9,35,15)
mc.setBlock(3,6,2,35,15)
mc.setBlock(3,7,3,35,15)
mc.setBlock(3,8,4,35,15)
mc.setBlock(3,9,5,35,15)
mc.setBlock(3,8,6,35,15)
mc.setBlock(3,7,7,35,15)
mc.setBlock(3,6,8,35,15)

mc.setBlock(4,5,1,35,15)
mc.setBlock(4,4,1,35,15)
mc.setBlock(4,3,1,35,15)
mc.setBlock(4,2,1,35,15)
mc.setBlock(4,1,1,35,15)
mc.setBlock(4,0,1,35,15)
mc.setBlock(4,0,2,35,15)
mc.setBlock(4,0,3,35,15)
mc.setBlock(4,0,4,35,15)
mc.setBlock(4,0,5,35,15)
mc.setBlock(4,0,6,35,15)
mc.setBlock(4,0,7,35,15)
mc.setBlock(4,0,8,35,15)
mc.setBlock(4,0,9,35,15)
mc.setBlock(4,1,9,35,15)
mc.setBlock(4,2,9,35,15)
mc.setBlock(4,3,9,35,15)
mc.setBlock(4,4,9,35,15)
mc.setBlock(4,5,9,35,15)
mc.setBlock(4,6,2,35,15)
mc.setBlock(4,7,3,35,15)
mc.setBlock(4,8,4,35,15)
mc.setBlock(4,9,5,35,15)
mc.setBlock(4,8,6,35,15)
mc.setBlock(4,7,7,35,15)
mc.setBlock(4,6,8,35,15)

mc.setBlock(5,5,1,35,15)
mc.setBlock(5,4,1,35,15)
mc.setBlock(5,3,1,35,15)
mc.setBlock(5,2,1,35,15)
mc.setBlock(5,1,1,35,15)
mc.setBlock(5,0,1,35,15)
mc.setBlock(5,0,2,35,15)
mc.setBlock(5,0,3,35,15)
mc.setBlock(5,0,4,35,15)
#mc.setBlock(5,0,5,35,15)
mc.setBlock(5,0,6,35,15)
mc.setBlock(5,0,7,35,15)
mc.setBlock(5,0,8,35,15)
mc.setBlock(5,0,9,35,15)
mc.setBlock(5,1,9,35,15)
mc.setBlock(5,2,9,35,15)
mc.setBlock(5,3,9,35,15)
mc.setBlock(5,4,9,35,15)
mc.setBlock(5,5,9,35,15)
mc.setBlock(5,6,2,35,15)
mc.setBlock(5,7,3,35,15)
mc.setBlock(5,8,4,35,15)
mc.setBlock(5,9,5,35,15)
mc.setBlock(5,8,6,35,15)
mc.setBlock(5,7,7,35,15)
mc.setBlock(5,6,8,35,15)

mc.setBlock(5,8,4,5,17)
mc.setBlock(5,8,5,5,17)


mc.setBlock(5,7,3,5,17)
mc.setBlock(5,7,4,5,17)
mc.setBlock(5,7,5,5,17)
mc.setBlock(5,7,6,5,17)

mc.setBlock(5,6,3,5,17)
mc.setBlock(5,6,4,5,17)
mc.setBlock(5,6,5,5,17)
mc.setBlock(5,6,6,5,17)
mc.setBlock(5,6,7,5,17)

mc.setBlock(5,5,1,5,17)
mc.setBlock(5,5,2,5,17)
mc.setBlock(5,5,3,5,17)
mc.setBlock(5,5,4,5,17)
mc.setBlock(5,5,5,5,17)
mc.setBlock(5,5,6,5,17)
mc.setBlock(5,5,7,5,17)
mc.setBlock(5,5,8,5,17)
mc.setBlock(5,5,9,5,17)


mc.setBlock(5,4,1,5,17)
mc.setBlock(5,4,2,5,17)
mc.setBlock(5,4,3,5,17)
mc.setBlock(5,4,4,5,17)
mc.setBlock(5,4,5,5,17)
mc.setBlock(5,4,6,5,17)
mc.setBlock(5,4,7,5,17)
mc.setBlock(5,4,8,5,17)
mc.setBlock(5,4,9,5,17)


mc.setBlock(5,3,1,5,17)
mc.setBlock(5,3,2,5,17)
mc.setBlock(5,3,3,5,17)
mc.setBlock(5,3,4,5,17)
mc.setBlock(5,3,5,5,17)
mc.setBlock(5,3,6,5,17)
mc.setBlock(5,3,7,5,17)
mc.setBlock(5,3,8,5,17)
mc.setBlock(5,3,9,5,17)

mc.setBlock(5,2,1,5,17)
mc.setBlock(5,2,2,5,17)
mc.setBlock(5,2,3,5,17)
mc.setBlock(5,2,4,5,17)
mc.setBlock(5,2,5,5,17)
mc.setBlock(5,2,6,5,17)
mc.setBlock(5,2,7,5,17)
mc.setBlock(5,2,8,5,17)
mc.setBlock(5,2,9,5,17)

mc.setBlock(5,1,1,5,17)
mc.setBlock(5,1,2,5,17)
mc.setBlock(5,1,3,5,17)
mc.setBlock(5,1,4,5,17)
mc.setBlock(5,1,5,71,17)
mc.setBlock(5,1,6,5,17)
mc.setBlock(5,1,7,5,17)
mc.setBlock(5,1,8,5,17)
mc.setBlock(5,1,9,5,17)


mc.setBlock(5,5,1,35,15)
mc.setBlock(5,4,1,35,15)
mc.setBlock(5,3,1,35,15)
mc.setBlock(5,2,1,35,15)
mc.setBlock(5,1,1,35,15)
mc.setBlock(5,0,1,35,15)
mc.setBlock(5,0,2,35,15)
mc.setBlock(5,0,3,35,15)
mc.setBlock(5,0,4,35,15)
mc.setBlock(5,0,5,35,15)
mc.setBlock(5,0,6,35,15)
mc.setBlock(5,0,7,35,15)
mc.setBlock(5,0,8,35,15)
mc.setBlock(5,0,9,35,15)
mc.setBlock(5,1,9,35,15)
mc.setBlock(5,2,9,35,15)
mc.setBlock(5,3,9,35,15)
mc.setBlock(5,4,9,35,15)
mc.setBlock(5,5,9,35,15)
mc.setBlock(5,6,2,35,15)
mc.setBlock(5,7,3,35,15)
mc.setBlock(5,8,4,35,15)
mc.setBlock(5,9,5,35,15)
mc.setBlock(5,8,6,35,15)
mc.setBlock(5,7,7,35,15)
mc.setBlock(5,6,8,35,15)


