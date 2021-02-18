# coding=UTF-8

# All exercises are chosen from input files. You can easily adjust them to your needs.

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
traintype = input("Do you want to make climbing specific or balance training?\n")
climbing = False
balance = False
if traintype == "1" or traintype == "climbing specific" or traintype == "specific" or traintype == "climbing":
  climbing = True
if traintype == "2" or traintype == "balance training" or traintype == "balance":
  balance = True

# section for climbing specific training
if climbing:
  print("\n= Great, you chose to make climbing specific training! =\n")

  inpcnum=input("Request Number of Climbing Specific Exercises\n")
  inpfnum=input("Request Number of Finger Strength Exercises\n") 
  cnum=int(inpcnum)
  fnum=int(inpfnum)
  fcin=open('upper.inp','r')
  ffin=open('finger.inp','r')
  clength=0
  flength=0

  # evaluate number of exercises in each file
  for line in fcin:
     clength = clength + 1
  for line in ffin:
     flength = flength + 1

  # rewind files
  fcin.seek(0)
  ffin.seek(0)

  if cnum >= clength:
    print (clength)
    sys.exit("ERROR: Number of requested climbing specific exercises equals or is larger than the number of exercises in file!")
  if fnum >= flength:
    print (flength)
    sys.exit("ERROR: Number of requested finger strength exercises equals or is larger than the number of exercises in file!")

  # select exercises
  fout=open('workoutplan','w')
  fout.write('============ Finger Strength =========\n')
  selectexercises(flength,fnum,ffin,fout)
  fout.write('=========== Climbing Specific ========\n')
  selectexercises(clength,cnum,fcin,fout)

  ffin.close()
  fcin.close()

# section for balance training
elif balance:
  print("\n= Great, you chose to make balance training! =\n")

  inpknum=input("Request Number of Lower Body Exercises\n")
  inprnum=input("Request Number of Middle Body Exercises\n")
  inponum=input("Request Number of Upper Body Exercises\n")
  knum=int(inpknum)
  rnum=int(inprnum)
  onum=int(inponum)
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

  if knum >= klength:
    print (klength)
    sys.exit("ERROR: Number of requested lower exercises equals or is larger than the number of exercises in file!")
  if rnum >= rlength:
    print (rlength)
    sys.exit("ERROR: Number of requested middle body exercises equals or is larger than the number of exercises in file!")
  if onum >= olength:
    print (olength)
    sys.exit("ERROR: Number of requested upper body exercises equals or is larger than the number of exercises in file!")

  # select exercises
  fout=open('workoutplan','w')
  fout.write('============= Lower Body =============\n')
  selectexercises(klength,knum,fkin,fout)
  fout.write('============= Middle Body ============\n')
  selectexercises(rlength,rnum,frin,fout)
  fout.write('============= Upper Body =============\n')
  selectexercises(olength,onum,foin,fout)

  fkin.close()
  frin.close()
  foin.close()

else:
  sys.exit("ERORR: Please choose what kind of training you want!")

print ("'Genuegend Kraft ist ein Zustand, den es nicht gibt.' (Wolfgang Guellich)")
fout.write("\n'Genuegend Kraft ist ein Zustand, den es nicht gibt.' (Wolfgang Guellich)")
fout.close()
