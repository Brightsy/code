import turtle
import random
t=turtle.Turtle()
u=turtle.Turtle()
a=70
bgcolor='pale turquoise'
#treecolor='saddle brown'
treecolor='black'
turtle.setworldcoordinates(-a,-a,a,a)
turtle.bgcolor(bgcolor)
turtle.tracer(0)
u.fillcolor('white')
u.pencolor('white')
u.penup()
u.backward(90)
u.right(90)
u.forward(35)
u.pendown()
u.begin_fill()
u.forward(55)
u.left(90)
u.forward(180)
u.left(90)
u.forward(55)
u.left(90)
u.pencolor('black')
u.pensize(3)
u.goto(0,-32)
u.goto(-90,-35)
u.end_fill()
u.pencolor('white')
u.penup()
for i in range(1,400):
    x=random.uniform(-a,a)
    y=random.uniform(-a+40,a)
    u.goto(x,y)
    u.dot(5,"white")
def tree(branch_len,width):
    #print(branch_len)
    nowpos=t.pos()
    nowangle=t.heading()
    
        
    newwidth=width*0.618
    angle1=random.uniform(15,30)
    angle2=random.uniform(25,30)
    angle3=random.uniform(15,30)
    #"""
    if branch_len>20:
        branch_len1=branch_len*random.uniform(0.5,0.6)
        branch_len2=branch_len*random.uniform(0.55,0.65)
        branch_len3=branch_len*random.uniform(0.5,0.6)
    else:
        branch_len1=branch_len*random.uniform(0.7,0.8)
        branch_len2=branch_len*random.uniform(0.7,0.8)
        branch_len3=branch_len*random.uniform(0.7,0.8)
    #"""
    if branch_len>2:
        t.pensize(width)
        t.pencolor(treecolor)
        t.penup()
        f1=random.uniform(0,1)
        f2=random.uniform(0,width)
        f3=random.uniform(0,branch_len)
        
        if f1>0.5:
            t.left(90)
            t.forward(f2)
            t.right(90)
            t.forward(f3)
            t.dot(5,'white')
            t.backward(f3)
            t.left(90)
            t.backward(f2)
            t.right(90)
        else:
            t.right(90)
            t.forward(f2)
            t.left(90)
            t.forward(f3)
            t.dot(5,'white')
            t.backward(f3)
            t.right(90)
            t.backward(f2)
            t.left(90)
        t.pendown()
        
        if branch_len==35:
            t.forward(20)
            angle1=random.uniform(15,20)
            angle2=random.uniform(15,20)
            angle3=random.uniform(15,20)
        elif branch_len<35*0.6 and branch_len>35*0.5:
            branch_len=15
            t.forward(15)
        else:
            t.forward(branch_len)
        t.pendown()
        
        if nowangle<90:
            t.penup()
            t.goto(nowpos)
            t.left(90)
            t.forward(width*0.9/7)
            t.right(90)
            t.pencolor('white')
            if width<2:
                snowwidth=2
            else:
                snowwidth=width/3
            t.pensize(snowwidth)
            t.forward(branch_len/10)
            t.pendown()
            t.forward(branch_len*9*1.05/10)
            t.penup()
            t.pencolor(treecolor)
            t.goto(nowpos)
            t.forward(branch_len)
            t.pendown()
        
        if nowangle>90:
            t.penup()
            t.goto(nowpos)
            t.right(90)
            t.forward(width*0.9/7)
            t.left(90)
            t.pencolor('white')
            if width<1.5:
                snowwidth=1.5
            elif width<5:
                snowwidth=3
            else:
                snowwidth=width/3
            t.pensize(snowwidth)
            t.forward(branch_len/10)
            t.pendown()
            t.forward(branch_len*9/10)
            t.penup()
            t.pencolor(treecolor)
            
            t.goto(nowpos)
            t.forward(branch_len)
            t.pendown()
        t.right(angle1)
        tree(branch_len1,newwidth)
        t.left(angle2)
        if(branch_len<20):
            tree(branch_len2,newwidth)
        t.left(angle3)
        tree(branch_len3,newwidth)
        t.right(angle3+angle2-angle1)
        t.penup()
        t.backward(branch_len)
        t.pendown()

t.penup()
t.left(90)
t.backward(45)
t.pendown()
t.pencolor(treecolor)
tree(35,30)
t.penup()

t.hideturtle()
u.hideturtle()
turtle.update()
turtle.done()


