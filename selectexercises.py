class selectex:

    def __init__(self,exnum):
        self.__exnum=exnum

    def create(self):
        select=selectex(self.__exnum)
        fout=open("workoutplan","w")

        # for every traintype select the exercises 
        i=0
        while i < len(self.__exnum):
            fin=self.__exnum[i]
            num=self.__exnum[i+1]
            select.selectexercises(num,fin,fout)
            i=i+2
        fout.close()


    def selectexercises(self,num,fopen,fout):
        import random    
        liste = []
        fin=open(fopen,'r')
        length=0
        for line in fin:
            length=length+1
        fin.seek(0)
        # select the first exercise
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
        fin.close()
        
