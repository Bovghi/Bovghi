print("tris")
p=1
v=3
g=0
h=1
p1=1
p2=2
p3=3
p4=4
p5=5
p6=6
p7=7
p8=8
p9=9
print("the game starts!")
while h!=0 and v!=1 and v!=2:
  if p==1:
    print("player 1 turn")
    print(p1,p2,p3)
    print(p4,p5,p6)
    print(p7,p8,p9)
    g=int(input("insert position: "))
    if p1==g and p1==1:
      p1="X"
    elif p2==g and p2==2:
      p2="X"
    elif p3==g and p3==3:
      p3="X"
    elif p4==g and p4==4:
      p4="X"
    elif p5==g and p5==5:
      p5="X"
    elif p6==g and p6==6:
      p6="X"
    elif p7==g and p7==7:
      p7="X"
    elif p8==g and p8==8:
      p8="X"
    elif p9==g and p9==9:
      p9="X"
    else:
      print("turn lost because you didn't insert a valid position")
      
  if p==2:
    print("player 2 turn")
    print(p1,p2,p3)
    print(p4,p5,p6)
    print(p7,p8,p9)
    g=int(input("insert position: "))
    if p1==g and p1==1:
      p1="O"
    elif p2==g and p2==2:
      p2="O"
    elif p3==g and p3==3:
      p3="O"
    elif p4==g and p4==4:
      p4="O"
    elif p5==g and p5==5:
      p5="O"
    elif p6==g and p6==6:
      p6="O"
    elif p7==g and p7==7:
      p7="O"
    elif p8==g and p8==8:
      p8="O"
    elif p9==g and p9==9:
      p9="O"
    else:
      print("turn lost because you didn't insert a valid position")
  if p==1:
    p=2
  else:
    p=1
  if p1==p2==p3=="X":
    v=1
  elif p4==p5==p6=="X":
    v=1
  elif p7==p8==p9=="X":
    v=1
  elif p1==p4==p7=="X":
    v=1
  elif p2==p5==p8=="X":
    v=1
  elif p3==p6==p9=="X":
    v=1
  elif p1==p5==p9=="X":
    v=1
  elif p3==p5==p7=="X":
    v=1

  if p1==p2==p3=="O":
    v=2
  elif p4==p5==p6=="O":
    v=2
  elif p7==p8==p9=="O":
    v=2
  elif p1==p4==p7=="O":
    v=2
  elif p2==p5==p8=="O":
    v=2
  elif p3==p6==p9=="O":
    v=2
  elif p1==p5==p9=="O":
    v=2
  elif p3==p5==p7=="O":
    v=2

  if p1=="O" or p1=="X":
    if p2=="O" or p2=="X":
      if p3=="O" or p3=="X":
        if p4=="O" or p4=="X":
          if p5=="O" or p5=="X":
            if p6=="O" or p6=="X":
              if p7=="O" or p7=="X":
                if p8=="O" or p8=="X":
                  if p9=="O" or p9=="X":
                    h=0

if v==1:
  print("player 1 wins")
elif v==2:
  print("player 2 wins")
elif h==0:
  print("it's a draw")
print(p1,p2,p3)
print(p4,p5,p6)
print(p7,p8,p9)
