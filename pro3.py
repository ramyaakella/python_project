a=[['___','___','___'],['___','___','___'],['___','___','___']]
b=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
import random
def inputa():
     c=random.sample(b,1)
     x=c[0][0]
     y=c[0][1]
     a[x][y]=' X '
     b.remove([x,y])
   
def outputa():
    for i in a :
        print(*i)
        print("\n\n")
def inputau():
    while True :
        x=int(input("enter the x co-ordinate "))
        y=int(input("enter the y co-ordinate "))
        if [x,y] in b :
            a[x][y]=' O '
            b.remove([x,y])
            break
        else :
            print("Please enter the co-ordinates again ")
def res():
    if a[0]==[' X ',' X ',' X '] or a[1]==[' X ',' X ',' X '] or a[2]==[' X ',' X ',' X '] :
     print("player 2 wins !!!!")
     return 1
    elif ((a[0][0]==' X ' and a[1][0]==' X ' and a[2][0]==' X ') or (a[0][1]==' X ' and a[1][1]==' X ' and a[2][1]==0) or (a[0][2]==' X ' and a[1][2]==' X ' and a[2][2]==' X ')):
     print("player 2 wins !!!!")
     return 1
    elif (a[0][0]==' X ' and a[1][1]==' X ' and a[2][2]==' X ') :
      print("player 2 wins !!!!")
      return 1
    elif a[0][2]==' X ' and a[1][1]==' X ' and a[2][0]==' X ' :
     print("player 2 wins !!!!")
     return 1
    elif a[0]==[' O ',' O ',' O '] or a[1]==[' O ',' O ',' O '] or a[2]==[' O ',' O ',' O '] :
     print("player 1 wins !!!!")
     return 1
    elif ((a[0][0]==' O ' and a[1][0]==' O ' and a[2][0]==' O ') or (a[0][1]==' O ' and a[1][1]==' O ' and a[2][1]==' O ') or (a[0][2]==' O ' and a[1][2]==' O ' and a[2][2]==' O ')):
     print("player 1 wins !!!!")
     return 1
    elif (a[0][0]==' O ' and a[1][1]==' O ' and a[2][2]==' O ') :
      print("player 1 wins !!!!")
      return 1
    elif a[0][2]==' O ' and a[1][1]==' O ' and a[2][0]==' O ' :
      print("player 1 wins !!!!")
      return 1
    else:
      return 0
i=1;j=0
h=input("enter your name : ")
print( 'hi',h ,'\n', "welcome! let's play the game","\n\n"," TIC TAC TOE")  
z=0
outputa()
while i<=9 :
    if i%2==0 :
        print("Player 2")
        inputa()
    else :
        print("Player 1")
        inputau()
    outputa()
    z=res()
    if z==1:
        j=1
        break
    i=i+1
if j==0 :
     print("Draw")

