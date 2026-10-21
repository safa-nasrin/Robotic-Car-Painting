from robodk.robolink import *
from robodk.robomath import *
RDK = Robolink()

tool = RDK.Item('Generic Paint Sprayer', ITEM_TYPE_TOOL)
obj = RDK.Item('Nissan Altima 2013', ITEM_TYPE_OBJECT)

RDK.Spray_Clear()

# Using 50mm cubes limits the "itching" slightly while still overlapping
options = "PROJECT PARTICLE=CUBE(50,50,50) STEP=6x6"

# The 800s make the spray cone massive enough to hit every curve
close_p = [0, 0, 0,    100, 0, 0,    0, 100, 0,    0, 1, 0, 1] 
far_p   = [0, 0, 1000, 800, 0, 0,    0, 800, 0,    0, 1, 0, 1]

RDK.Spray_Add(tool, obj, options, Mat([close_p, far_p]).tr())
RDK.Spray_SetState(SPRAY_ON)
