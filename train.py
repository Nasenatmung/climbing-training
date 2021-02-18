# coding=UTF-8

# Will create a single session training plan for climbing with randomly selected exercises
# All exercises are chosen from input files. You can easily adjust them to your needs.

import getinput as getinput
import selectexercises as selectex 
import random
import sys

inptrainplan=getinput.getinput()
traintype=inptrainplan.choose()
#print (traintype)
exlist=inptrainplan.chooseexc(traintype)
#print (exlist)

gettrainplan=selectex.selectex(exlist)
gettrainplan.create()


