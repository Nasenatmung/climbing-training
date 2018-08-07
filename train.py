# coding=UTF-8

import random
import sys

def selectexercises(length,num,fin,fout):
    liste = []
    x=(random.randint(1,length))
    liste.append(x)
    j=0
    for line in fin:
       j=j+1
       if x == j:
         fout.write(line)
    fin.seek(0)
    # select a new exercise and check if it is already on the list
    for i in range(0,num-1):
       k=1
       while k < 2:
          k = 1
          x=(random.randint(1,length))
          for l in range(0,len(liste)):
             if x == liste[l]:
               k = k - 1
          liste.append(x)
          k = k + 1
     # choose exercise from file
       j=0
       for line in fin:
          j=j+1
          if x == j:
            fout.write(line)
       fin.seek(0)
    del liste[:]

# choose type of training
traintype = raw_input("Do you want to make climbing specific or balance training?\n")
climbing = False
balance = False
if traintype == "1" or traintype == "climbing specific" or traintype == "specific" or traintype == "climbing":
  climbing = True
if traintype == "2" or traintype == "balance training" or traintype == "balance":
  balance = True

# section for climbing specific training
if climbing:
  print("\n= Great, you chose to make climbing specific training! =\n")

  cnum=input("Request Number of Climbing Specific Exercises\n")
  fcin=open('upper.inp','r')
  clength=0
  # evaluate number of exercises in each file
  for line in fcin:
     clength = clength + 1
  # rewind files
  fcin.seek(0)
  if cnum >= clength:
    print clength
    sys.exit("ERROR: Number of requested climbing specific exercises equals or is larger than the number of exercises in file!")
  fout=open('workoutplan','w')
  fout.write('=========== climbing specific ========\n')
  selectexercises(clength,cnum,fcin,fout)

# section for balance training
elif balance:
  print("\n= Great, you chose to make balance training! =\n")

  knum=input("Request Number of Lower Body Exercises\n")
  rnum=input("Request Number of Middle Body Exercises\n")
  onum=input("Request Number of Upper Body Exercises\n")
  fkin=open('lower.inp','r')
  frin=open('middle.inp','r')
  foin=open('upper.inp','r')
  klength=0
  rlength=0
  olength=0

  # evaluate number of exercises in each file
  for line in fkin:
     klength = klength + 1
  for line in frin:
     rlength = rlength + 1
  for line in foin:
     olength = olength + 1

  # rewind files
  fkin.seek(0)
  frin.seek(0)
  foin.seek(0)

  if knum == klength:
    sys.exit("ERROR: Number of requested lower exercises equals or is larger than the number of exercises in file!")
  if rnum == rlength:
    sys.exit("ERROR: Number of requested middle body exercises equals or is larger than the number of exercises in file!")
  if onum == olength:
    sys.exit("ERROR: Number of requested upper body exercises equals or is larger than the number of exercises in file!")

  fout=open('workoutplan','w')

  # knee exercises
  fout.write('============= Lower body =============\n')
  selectexercises(klength,knum,fkin,fout)
  fout.write('============= Middle body ============\n')
  selectexercises(rlength,rnum,frin,fout)
  fout.write('============= Upper Body =============\n')
  selectexercises(olength,onum,foin,fout)

else:
  sys.exit("ERORR: Please choose what kind of training you want!")

print "'Genuegend Kraft ist ein Zustand, den es nicht gibt.' (Wolfgang Guellich)"
fout.write("\n'Genuegend Kraft ist ein Zustand, den es nicht gibt.' (Wolfgang Guellich)")
