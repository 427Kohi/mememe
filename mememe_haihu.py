# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
im = Image.new('RGB', (960, 960), (100, 100, 100))
draw = ImageDraw.Draw(im)
mememe = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,4,2,2,5,6,2,2,2,2,3,3,3,2,2,2,2,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,4,4,7,2,5,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,5,2,2,2,2,5,1,1,8,1,1,1,1,1,6,2,2,2,2,2,2,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,5,5,2,2,5,8,8,8,8,8,8,8,8,8,0,8,8,0,0,8,1,2,2,2,5,1,1,1,1,0,0,1,5,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,5,5,2,5,1,8,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,8,5,1,8,8,8,8,8,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,5,5,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,8,8,8,8,8,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,5,5,2,8,0,0,0,0,0,8,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,5,2,1,1,8,8,0,0,0,0,0,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,2,2,5,5,2,1,0,8,8,8,8,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,2,'a',5,2,5,8,0,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,5,4,5,2,1,8,8,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,8,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,5,2,2,2,0,8,8,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,8,8,8,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,5,2,5,2,1,8,8,8,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,8,8,8,8,8,8,0,8,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,5,5,2,1,0,8,0,1,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,1,1,1,0,0,5,0,0,0],
[0,0,0,0,0,0,2,6,2,1,0,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,5,0,0,0,0,0,0,1,0,0,0,0,0,0,0,8,8,0,8,1,1],
[0,0,0,0,0,1,2,2,2,8,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,1,0,0,1,1,8,0,8,8,8,8,8,8,0,0,8,8,8,0],
[0,0,0,0,0,2,5,2,0,8,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,5,8,8,8,8,1,8,0,0,0,0,0,0,0,0,0,8],
[0,0,0,0,0,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,2,1,8,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,8,2,5,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,8,0,0,0,8,2,2,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,2,8,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,8,2,0,0,0,0,0,0,8,1,8,0,0,0,0,8,8,8,8,0,0,0,0,1,1,1,1,1,1,1,1,1,8,8,8,8],
[0,0,0,1,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,8,8,0,0,1,0,0,0,0,0,0,8,8,8,8,8,0,0,8,8,8,8,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,2,2,0,0,8,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,8,8,0,0,0,8,0,1,0,0,0,0,0,8,8,8,1,8,1,1,1,1,1,1,1,1,1,1,8,0,0,0,0,8,0,0,8,8,8,8],
[0,0,0,2,2,0,0,8,8,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,8,8,8,0,8,1,8,0,0,0,0,0,8,8,8,1,1,1,1,1,1,1,8,8,8,8,8,5,5,5,5,5,5,5,5,1,5,1,8],
[0,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,8,8,8,8,0,8,8,8,8,8,8,8,1,0,1,1,1,1,1,1,5,5,5,5,6,5,5,5,1,5,1,1,1,1,1,5,1,1],
[0,0,0,2,0,0,0,0,8,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,8,8,8,8,8,8,'b',8,8,8,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,5],
[0,0,0,2,0,0,0,8,0,8,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,8,0,0,0,0,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
[0,0,0,5,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,8,0,8,8,8,8,8,'b',8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,8,8,8,8,8,8,8,8,'b',8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,8,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,8,0,0,0,0,0,0,8,0,8,8,0,0,0,8,8,8,8,8,8,8,8,8,8,'b',8,8,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,8,0,0,0,8,0,0,8,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,8,0,0,0,0,0,0,8,8,8,8,8,0,0,8,8,8,8,8,8,8,8,8,0,'b',8,0,1,0,0,1,1,1,1,8,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,1,1,8,0,0,0,8,8,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,8,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,8,8,8,1,1,0,0,5,5,5,'b','b','b',5,8,8,8,8,8,8,8,8,1,8,8,8,8,1],
[0,1,8,8,0,0,0,8,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,1,8,0,8,8,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,8,0,0,5,5,5,5,5,'b','b','b','b',8,8,8,0,0,0,8,8,8,1,1,1],
[0,1,0,1,0,0,0,8,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,8,8,1,0,0,0,0,0,0,8,8,8,'b',5,'b',8,8,8,8,8,8,8,8,8,8,8,0,1,8,0,1,1,5,5,5,5,5,5,'b','b',8,8,8,1,1,1,1,8,8,8,1],
[0,0,8,1,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,8,8,0,0,0,0,0,0,8,8,6,2,2,2,6,8,8,8,'b',8,'b',8,8,8,8,8,0,0,8,1,0,1,1,1,1,5,5,5,5,5,'b',8,8,8,8,1,1,1,1,1,1],
[0,0,8,8,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,0,0,0,8,0,5,6,6,2,2,5,2,8,8,8,8,8,'b','b',8,8,8,8,8,0,0,1,0,5,1,1,1,8,1,5,5,5,5,'b','b',8,8,8,1,1,1,1,1],
[1,0,1,0,0,0,0,0,0,8,0,0,0,8,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,8,8,8,0,0,0,0,0,0,0,0,0,8,8,8,8,8,0,0,2,0,5,5,8,'b',2,1,0,0,5,8,8,8,8,8,'b',8,8,8,8,0,0,8,0,0,0,5,5,5,5,8,8,8,1,1,5,5,5,5,'b',8,0,1,1,1,1],
[1,0,0,0,8,0,0,0,0,0,8,0,0,0,8,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0,8,0,0,0,0,0,0,8,0,8,8,8,0,0,8,6,'b',5,2,2,2,2,0,0,0,8,8,8,'b',8,'b',8,8,8,8,0,0,0,0,0,0,0,8,5,5,5,1,8,8,8,1,5,5,5,5,5,8,8,1,1,1],
[1,0,0,0,8,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,8,8,8,0,0,0,0,0,0,0,8,8,8,8,8,5,6,'b',6,2,2,2,6,5,2,0,0,8,8,8,8,'b',8,8,8,8,8,8,0,0,0,0,0,8,8,8,5,5,5,5,0,8,8,8,1,5,5,1,1,8,8,1,1],
[0,0,0,1,0,0,0,0,0,0,0,8,0,0,0,8,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,8,8,8,0,0,8,0,0,0,0,8,8,8,8,6,'b',2,2,2,2,5,6,'b','b',0,0,0,8,'b',8,'b',8,8,8,8,8,8,0,0,0,0,0,'b',8,8,8,5,5,5,1,0,0,1,0,1,1,5,1,1,8,8,1],
[0,0,0,0,0,1,0,0,0,0,0,8,0,0,8,0,8,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,8,8,8,0,8,0,8,8,8,8,8,8,6,2,2,2,2,2,'c',6,'b','d',8,0,0,0,8,8,'b',8,8,8,8,8,0,8,0,0,0,0,1,8,8,8,'b',5,5,5,1,8,0,0,0,8,1,1,1,1,8,1],
[0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,8,0,0,0,0,0,1,0,8,0,0,0,0,0,0,1,1,8,0,0,8,8,8,8,8,8,8,8,8,8,'b',5,0,0,5,6,2,2,6,8,8,5,0,0,0,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,1,1,8,8,5,5,5,1,1,8,8,0,0,8,1,1,'b',8,8],
[0,0,0,0,0,0,1,0,0,0,0,0,8,8,0,0,1,0,8,8,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,1,8,8,8,'b','b',8,0,8,8,8,8,1,0,6,'c',5,6,'c',6,8,'b','b',0,0,0,8,8,8,8,0,0,8,0,0,0,0,0,0,0,0,1,8,1,1,8,5,5,5,8,'b',8,0,0,0,0,1,1,8,8],
[1,0,0,0,0,1,0,1,0,0,0,0,8,8,0,0,0,8,0,8,0,8,0,0,0,8,0,0,1,0,0,0,0,0,0,0,0,0,8,0,8,8,8,8,8,8,8,8,0,0,6,'d',1,5,'c',8,8,8,0,0,0,0,0,8,8,8,0,0,0,0,0,0,0,0,0,0,0,1,8,1,8,8,8,5,5,8,8,1,8,0,0,0,8,1,1,8],
[5,0,0,0,0,8,0,0,0,0,0,0,0,8,8,0,0,0,1,0,8,0,8,8,8,8,8,8,0,0,1,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,0,0,0,0,'b',9,'d',8,8,8,1,1,0,0,0,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,'b',5,5,8,8,5,5,0,0,0,0,1,1,8],
[0,0,0,0,8,8,8,0,0,0,0,0,0,0,8,8,8,0,0,0,0,0,8,8,8,8,8,8,8,0,0,8,8,8,0,8,8,0,8,8,8,8,8,8,8,8,8,0,0,0,0,0,5,'d',8,8,5,6,0,0,0,0,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,1,8,8,5,5,1,1,1,8,0,0,0,8,1,8],
[0,0,0,0,0,8,8,1,0,8,0,0,0,8,0,8,8,8,8,8,8,8,8,8,1,8,8,8,8,8,1,0,0,0,8,0,0,0,0,0,0,8,8,8,8,8,8,0,0,0,0,0,0,0,0,1,8,0,0,0,0,0,8,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,5,5,8,1,5,1,0,0,0,0,1,8],
[0,1,0,0,8,8,8,8,1,0,1,0,8,0,0,8,8,8,8,8,0,8,0,0,8,0,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,1,8,8,8,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,'b',5,8,1,1,5,0,0,0,0,1,'b'],
[0,1,0,0,8,8,8,0,0,0,0,8,0,8,0,0,8,8,8,8,8,8,1,0,0,0,0,0,1,1,0,8,5,8,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,5,8,1,1,1,8,'b',5,8,1,5,5,8,0,0,0,0,1],
[0,0,0,0,8,8,8,0,0,0,8,8,8,0,8,0,8,8,8,8,8,8,8,0,0,0,1,0,6,2,2,2,2,6,8,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,'b',0,0,0,0,0,0,0,0,0,0,0,5,5,5,8,1,1,1,8,5,8,1,5,5,5,8,0,0,0,1],
[0,0,0,0,8,8,8,0,0,0,0,8,8,8,8,0,8,8,8,8,8,8,8,8,8,0,0,2,6,'b','b',2,2,5,1,1,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,'b',5,8,0,0,0,0,0,0,0,8,0,1,1,1,1,1,1,1,5,5,8,8,5,5,1,8,0,0,0,0],
[0,0,1,0,8,8,8,0,0,0,0,0,8,1,8,8,8,8,8,'b',8,8,8,8,8,6,6,'d','b',2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,0,0,0,8,8,'b',8,8,0,8,0,0,0,0,0,1,5,1,1,1,1,1,1,1,5,5,8,8,5,5,1,5,0,0,0,0],
[0,0,5,0,8,8,8,0,0,0,0,8,0,8,8,8,8,8,8,8,'b',8,8,8,2,'d','d',2,2,2,2,6,'c',5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,0,0,0,0,0,8,'b',8,'b',8,8,0,0,0,0,0,0,1,5,5,5,1,1,1,1,5,5,8,8,1,5,5,1,0,0,0,0],
[0,0,1,8,8,8,8,0,0,0,0,1,8,8,8,8,8,8,8,8,'b',8,8,3,6,5,5,2,2,2,2,2,5,6,'d',6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,0,0,0,0,0,0,0,0,0,5,8,6,8,8,0,0,0,0,0,8,8,5,5,5,8,1,1,1,1,5,8,8,8,5,1,1,8,8,0,0],
[0,0,0,8,8,8,8,8,8,0,8,5,1,8,8,5,8,8,8,8,8,'b',2,2,5,1,1,0,0,5,5,2,6,5,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'b',8,8,0,0,0,0,0,8,8,0,'b',5,'b',8,1,8,1,5,8,8,1,5,1,1,1,8,0,0],
[0,0,0,1,8,8,8,8,8,8,8,5,8,8,8,8,8,8,8,8,8,'b',2,2,8,1,0,1,5,6,5,6,5,'b','d','d',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'b',8,8,0,0,8,0,0,0,0,8,0,8,8,'b',8,8,1,5,'b',1,8,1,5,1,1,8,8,0],
[0,0,0,9,8,8,8,8,8,8,8,5,8,8,8,0,5,8,8,8,8,'b',8,8,6,8,0,0,5,'b',8,8,'b',8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,1,0,8,0,8,8,0,8,8,0,0,8,8,8,8,8,1,1,5,5,1,8,8,5,5,1,1,8,0],
[0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,0,0,8,8,8,8,'b',8,8,8,8,1,0,0,5,'b',8,8,8,8,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,8,8,8,8,8,8,0,8,8,8,'b',8,1,1,8,5,8,1,1,5,5,1,8,8,0],
[0,0,0,0,8,8,8,8,8,8,8,8,5,8,8,0,0,'b',8,8,8,8,'b',8,'b',8,0,0,0,0,0,5,8,8,8,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,8,8,0,8,8,8,8,8,8,8,8,0,0,1,1,1,5,1,1,8,5,5,1,1,8,8],
[0,0,0,0,8,8,8,8,0,5,0,0,0,1,8,8,0,1,8,8,8,8,8,8,8,8,8,0,0,1,0,0,1,5,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,8,8,8,8,8,8,0,0,0,0,0,5,5,1,1,8,8,5,5,1,8,8],
[0,0,0,0,8,8,8,8,1,0,0,0,0,0,8,8,0,1,8,8,8,8,8,8,'b',8,8,0,0,0,0,0,0,0,0,0,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,8,8,8,'b','b',8,8,8,0,0,0,0,0,0,0,0,1,8,8,5,5,1,1,8],
[0,0,0,0,8,8,5,0,0,0,0,0,0,0,0,8,1,1,8,8,8,8,8,8,8,8,'b',8,8,0,0,0,0,0,0,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,'b',8,0,0,0,0,0,0,0,0,0,1,1,5,5,5,1],
[0,0,0,0,5,1,0,0,0,0,0,0,0,0,0,0,1,5,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,'b',8,8,8,8,1,0,0,0,0,0,0,0,0,0,0,0,5,5,'b',1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,5,8,8,8,8,8,8,8,8,8,8,0,0,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,1,5,2,1,1,0,0,0,0,0,0,0,0,0,0,0,5,5,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,'b',8,8,8,8,8,8,8,8,8,8,8,6,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,'d',2,2,2,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,0,0,0,8,8,5,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,3,3,2,5,0,5,1,0,0,0,0,0,0,8,0,1,0,0,8],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,1,0,0,8,8,8,8,8,0,0,0,8,0,5,5,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,3,5,2,2,0,0,1,1,0,0,0,0,0,0,8,0,8,8,8],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,1,0,0,8,0,0,8,8,0,0,0,0,0,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'b',6,3,3,2,2,0,0,0,1,8,0,0,0,0,0,0,8,0,8,8],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'d',2,4,3,2,2,0,0,2,0,8,8,0,0,0,0,0,0,8,8,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,1,5,0,8,0,0,0,0,0,0,0,0,0,0,0,8,8,'b',8,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,'d',2,4,2,2,1,5,0,0,0,1,8,0,0,0,0,0,0,0,0,8],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,1,5,0,8,1,0,0,0,0,0,0,0,1,0,0,0,8,8,8,8,8,0,0,0,1,1,1,1,1,1,1,1,5,1,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,'d',2,4,2,1,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,8],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,1,0,1,8,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'d','d',2,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,8],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,'d',2,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,8,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,'d',0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,'d',0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,8,0,0,0,0,0,1,0,0,0,8,0,0,0,0,0,0,0,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,2,2,5,3,2,8,8,0,0,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,5,0,0,0,0,0,0,1,0,0,0,0,0,1,2,4,7,2,'b',0,0,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,5,0,0,0,0,0,0,0,8,0,0,0,0,0,2,2,7,2,5,0,0,0,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,8,'b',0,0,0,1,0,0,8,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,4,3,2,'b',0,0,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,2,3,4,2,'b',5,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,'d',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,4,3,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,2,2,'d','b',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,7,2,8,8,8,'b',8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,5,'b',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,4,2,8,0,0,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,2,2,'d',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,8,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,4,0,0,0,1,6,1,0,1,0,0,0,0,0,0,1,2,0,'e',2,0,0,0,0,0,0,0,0,5,2,2,2,'d',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,'a',0,0,0,0,1,8,1,8,0,0,0,6,2,5,2,2,'a','a',2,0,0,0,0,0,0,0,2,2,2,2,'b','b',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,2,1,0,0,1,2,'b',5,2,2,2,3,2,1,1,0,0,0,0,2,2,2,2,5,'b',1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,2,2,5,0,0,2,'b',2,5,2,2,1,0,1,0,0,0,5,2,2,2,2,2,'d',2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,0,0,2,2,2,1,0,1,1,1,1,2,2,2,2,2,2,2,2,'b',2,2,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,8,1,2,2,2,2,2,2,2,1,5,1,5,2,2,2,2,2,2,2,2,2,2,'b','b',2,'a',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,'b',5,2,4,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,8,'d',2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,'b','b',2,4,2,0,0,0,0,0,0,0,0,8,1,0,0,0,1,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,8,'b','d',2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,'b',5,2,4,2,5,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,8,'b','b',2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,2,4,2,2,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,8,'b','b',2,2,2,2,2,2,2,5,2,2,2,2,2,'b',2,4,3,2,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,8,8,'b','b',2,2,2,2,2,5,5,2,2,2,2,'d',2,4,3,2,0,0,0,0,0,0,0,0,0,0,1,1,8,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2]]

y1 = 0
for line in mememe:
    x1 = 0
    for masu in line:
        if masu == 1:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(128, 128, 128))
        elif masu == 2:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(30, 30, 30))
        elif masu == 3:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(0, 80, 0))
        elif masu == 4:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(70, 255, 70))
        elif masu == 5:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(102, 51, 51))
        elif masu == 6:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(102, 51, 0))
        elif masu == 7:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(102, 204, 51))
        elif masu == 8:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(255, 219, 145))
        elif masu == 9:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(255, 204, 204))
        elif masu == 'a':
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(153, 204, 51))
        elif masu == 'b':
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(255, 153, 102))
        elif masu == 'c':
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(102, 0, 102))
        elif masu == 'd':
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(255, 102, 153))
        elif masu == 'e':
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(204, 255, 153))
        else:
            draw.rectangle((x1, y1, x1 + 10, y1 + 10), fill=(245, 245, 220))
        x1 += 10
    y1 += 10
im.save('/home/mememe.jpg', quality=95)#/home/mememe.jpgの部分に保存したいフォルダーを指定してください。
