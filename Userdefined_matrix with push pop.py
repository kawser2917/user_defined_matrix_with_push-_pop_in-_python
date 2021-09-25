import numpy as np


class state:
  
    def __init__(self,matno,parentno,mat):
        self.matno=matno
        self.parentno=parentno 
        self.mat=mat
matrix=[]
while True:
    choice=int(input("Enter your choice:"))
   
    if choice==1:
        matno=int(input("Enter matno: "))
        parento=1
        print("Enter your element for matrix:")
        mat=[[int(input())for i in range (3)] for j in range (3)]
        start=np.array(mat)
        obj=state(matno,parento,start)

        matrix.append(obj.matno)
        matrix.append(obj.parentno)
        matrix.append(obj.mat)
        print(matrix)
        print()
    elif choice==2:
        matrix.pop(0)
        matrix.pop(0)
        matrix.pop(0)
    
    elif choice==3:
        print(matrix)
    else:
        break

        

    


        




        


