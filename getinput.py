class getinput:
#   designedplans=0

    def __init__(self):
        self.__traintype="x"
        self.__exnum=[]
#       getinput.designedplans+=1
    
#   def __del__(self):
#       getinput.designedplans-=1

    def choose(self):
        import sys
        traintype = input("Do you want to make climbing specific or balance training?\n")
        if traintype == "1" or traintype == "climbing specific" or traintype == "specific" or traintype == "climbing":
            print("\n= Great, you chose to make climbing specific training! =\n")
            self.__traintype = "climbing"
        elif traintype == "2" or traintype == "balance training" or traintype == "balance":
            print("\n= Great, you chose to make balance training! =\n")
            self.__traintype = "balance"
        else:
            sys.exit("ERROR: choose >>1<<, >>climbing specific<<, >>specific<<, or >>climbing<< for climbing specific or >>2<<, >>balance training<< or >>balance<< for balance training")
        return self.__traintype
           
    def chooseexc(self,traintype):
        import sys
        check=getinput()
        if traintype == "climbing":
            cstr=input("Request Number of Climbing Specific Exercises\n")
            cnum=int(cstr)
            check.checkinput(cnum,"climbing.inp")
            fstr=input("Request Number of Finger Strength Exercises\n")
            fnum=int(fstr)
            check.checkinput(fnum,"finger.inp")
            self.__exnum.append("climbing.inp")
            self.__exnum.append(cnum)
            self.__exnum.append("finger.inp")
            self.__exnum.append(fnum)
            return self.__exnum
        if traintype == "balance":
            kstr=input("Request Number of Lower Body Exercises\n")
            knum=int(kstr)
            check.checkinput(knum,"lower.inp")
            rstr=input("Request Number of Middle Body Exercises\n")
            rnum=int(rstr)
            check.checkinput(rnum,"middle.inp")
            ostr=input("Request Number of Upper Body Exercises\n")
            onum=int(ostr)
            check.checkinput(onum,"upper.inp")
            self.__exnum.append("lower.inp")
            self.__exnum.append(knum)
            self.__exnum.append("middle.inp")
            self.__exnum.append(rnum)
            self.__exnum.append("middle.inp")
            self.__exnum.append(onum)
            return self.__exnum

    def checkinput(self,exnum,exercise):
        import sys
        fin=open(exercise,'r')
        flength=0
        for line in fin:
            flength=flength+1
        if exnum >= flength:
            sys.exit(("ERROR: Number of requested exercises", exnum, "equals or is larger than the number of exercises", flength, "in file",exercise))
        fin.close()    

