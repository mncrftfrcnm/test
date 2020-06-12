import math
RR = True
wert = False
uuuu = True
from random import*
from turtle import *
yyyyyyyyyyyy = randint(1,48)
while wert == False:
    trar = input("choose: 1)+ 2)/ 3)* 4)- 5)** 6)sqrt 7)modf 8)log1p 9)hypot 10)number pi 11)number e 12)frexp 13)tan 14)fmod 15)gamma 16)lgamma 17)copysign 18)factorial 19)atan2 20)atan 21)copysign 22)exp 23)fabs 24)frexp 25)pow 26)draw 27)shipher 28)turtle 29)game 30)translate from alien language 31)1 spiral 32)2 spiral 33)text quest 34)happy 35)generator of stories 36)new game 37)game of words 38)square 39)mega squere 40)saperv 41)vidiogames 42)do you like robots 43)age 44)spiral s 45)alarm 46)your age is...  47)your random story 48)random 49)house(if you want to stop game print False):")
        
    if yyyyyyyyyyyy == 1 or trar ==  "1":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"+", tre, "=", ert +  tre)
    if yyyyyyyyyyyy == 2 or trar ==  "2" or yyyyyyyyyyyy == 2:
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"/", tre, "=", ert / tre)
    if  yyyyyyyyyyyy == 3 or trar ==  "3":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"*", tre, "=", ert * tre)
    if  yyyyyyyyyyyy == 4 or  trar ==  "4" :
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"-", tre, "=", ert - tre)









    if  yyyyyyyyyyyy == 5 or trar ==  "5":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"**", tre, "=", ert**tre)
    if  yyyyyyyyyyyy == 6 or trar ==  "6" :
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = ert ** (1./tre)
        print(ert,"**", tre, "=", retw) 
    
    if  yyyyyyyyyyyy == 7 or trar ==  "7":
        ert = int(input("choose number:"))
        retw = math.modf(ert)
        print(retw)

    if  yyyyyyyyyyyy == 8 or trar ==  "8":
        ert = int(input("choose number:"))
        retw = math.log1p(ert)
        print(retw)

    if  yyyyyyyyyyyy == 9 or  trar ==  "9":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.hypot(ert,tre)
        print(retw)

    if  yyyyyyyyyyyy == 10 or trar ==  "10":
        retw = math.pi
        print(retw)
    
    if  yyyyyyyyyyyy == 11 or  trar ==  "11":
        retw = math.e
        print(retw)
    if  yyyyyyyyyyyy == 12 or trar ==  "12":
        ert = int(input("choose number:"))
        retw = math.frexp(ert)
        print(retw)
    if  yyyyyyyyyyyy == 13 or trar ==  "13":
        ert = int(input("choose number:"))
        retw = math.tan(ert)
        print(retw)

    if  yyyyyyyyyyyy == 14 or trar ==  "14":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.fmod(ert,tre)
        print(retw)

    if yyyyyyyyyyyy == 15 or trar ==  "15":
        ert = int(input("choose number:"))
        retw = math.gamma(ert)
        print(retw)

    if  yyyyyyyyyyyy == 16 or trar ==  "16":
        ert = int(input("choose number:"))
        retw = math.lgamma(ert)
        print(retw)
    if  yyyyyyyyyyyy == 17 or trar ==  "17":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.copysign(ert,tre)
        print(retw)

    if  yyyyyyyyyyyy == 18 or trar ==  "18":
        ert = int(input("choose number:"))
        retw = math.factorial(ert)

        print(retw)
    if  yyyyyyyyyyyy == 19 or trar ==  "19":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.atan2(ert,tre)
        
        
        print(retw)

    if  yyyyyyyyyyyy == 20 or trar ==  "20":
        ert = int(input("choose number:"))
        retw = math.atan(ert)

    if  yyyyyyyyyyyy == 21 or trar ==  "21":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.copysign(ert,tre)
        print(retw)

    if  yyyyyyyyyyyy == 22 or trar ==  "22":

        tre = int(input("choose number:"))
        retw = math.exp(tre)
        print(retw)

    if  yyyyyyyyyyyy == 23 or trar ==  "23":

        tre = int(input("choose number:"))
        retw = math.fabs(tre)
        print(retw)

    if  yyyyyyyyyyyy == 24 or trar ==  "24":

        tre = int(input("choose number:"))
        retw = math.frexp(tre)
        print(retw)

    if  yyyyyyyyyyyy == 25 or trar ==  "25":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.pow(ert,tre)
        print(retw)

    if  yyyyyyyyyyyy == 26 or trar ==  "26" and RR == True:
        from tkinter import *
        yty = int(input("1)stop game 2)do not stop game")) 
        if yty == 1:
            RR = False            
            
        mm = Tk()
        g = Canvas(mm, width=750, height=500, bg="white")
        g.pack()
        lx, ly = 0,0
        g.create_line(80,0,80,1000)
        colline = "black"
        wtext=1

        def sj(event):
            global lx, ly
            lx = event.x
            ly = event.y
            if (lx<=80): 
                lx = 80

        def onc(event):
            sj(event)

        def od(event):
            if event.x<=80:
                event.x=80
            g.create_line(lx,ly,event.x,event.y,fill=colline,width=wtext)
            sj(event)

        g.bind("<Button-1>",onc)
        g.bind("<B1-Motion>",od)

        ri = g.create_rectangle(10,10,30,30,fill="red")
        bli = g.create_rectangle(10,35,30,55,fill="blue")
        bi = g.create_rectangle(10,60,30,80,fill="black")
        wi = g.create_rectangle(10,85,30,105,fill="white")
        pi = g.create_rectangle(10,110,30,130,fill="purple")
        unit = g.create_rectangle(10,135,30,155,fill="#DD00DD")
        gre = g.create_rectangle(10,160,30,180,fill="green")
        el = g.create_rectangle(10,185,30,205,fill="#00EE00")

        w1i=g.create_rectangle(10,285,30,305,fill="white")
        w2i=g.create_rectangle(10,310,30,330,fill="white")
        w3i=g.create_rectangle(10,335,30,355,fill="white")
        w1txt=g.create_text(20,294,text='1',font="Calibri 14")
        w2txt=g.create_text(20,319,text='2',font="Calibri 14")
        w3txt=g.create_text(20,344,text='3',font="Calibri 14")

        cleari=g.create_rectangle(10,435,57,455,fill="white")
        clearitxt=g.create_text(33,444,text='clear',font="Calibri 14")

        def clearhh(event):
            g.create_rectangle(80,0,1000,1000,fill="white")

        def w1(event):
            global wtext
            wtext = 1

        def w2(event):
            global wtext
            wtext = 5

        def w3(event):
            global wtext
            wtext = 9
        def uuu(event):
            g.create_rectangle(80,0,1000,1000,fill="white")



        def sr(event):
            global colline
            colline="red"
        def sbl(event):
            global colline
            colline="blue"
        def sb(event):
            global colline
            colline="black"
        def sw(event):
            global colline
            colline="white"

        def sp(event):
            global colline
            colline="purple"
        def sy(event):
            global colline
            colline="#00EE00"

        def un(event):
            global colline
            colline="#DD00DD"

        def ug(event):
            global colline
            colline="green"

#        yty = int(input("1)stop game 2)do not stop game")) 
#        if yty == 1:
#            RR = False
        g.tag_bind(ri,"<Button-1>",sr)
        g.tag_bind(bli, "<Button-1>",sbl)
        g.tag_bind(bi, "<Button-1>",sb)
        g.tag_bind(wi, "<Button-1>",sw)
        g.tag_bind(pi, "<Button-1>",sp)
        g.tag_bind(unit, "<Button-1>",un)
        g.tag_bind(gre, "<Button-1>",ug)
        g.tag_bind(el, "<Button-1>",sy)
        g.tag_bind(w1i, "<Button-1>",w1)
        g.tag_bind(w2i, "<Button-1>",w2)
        g.tag_bind(w3i, "<Button-1>",w3)
        g.tag_bind(w1txt, "<Button-1>",w1)
        g.tag_bind(w2txt, "<Button-1>",w2)
        g.tag_bind(w3txt, "<Button-1>",w3)
        g.tag_bind(cleari, "<Button-1>",clearhh)
        g.tag_bind(clearitxt, "<Button-1>",uuu)

        yty = int(input("1)stop game 2)do not stop game")) 
        if yty == 1:
            RR = False
#            break
        mm.mainloop()
        yty = int(input("1)stop game 2)do not stop game")) 
        if yty == 1:
            RR = False
#            break
    if  yyyyyyyyyyyy == 27 or trar ==  "27":
        ab = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        se = input("please enter a message to encrypt: ")
        sa = int(input("please enter a whole number from 1-25 to be your key: "))
        es = ""
        for eryb in se:
            p = ab.find(eryb)
            np = p + sa
            es = es + ab[np]
            print("your message is ",es)
    if  yyyyyyyyyyyy == 28 or trar ==  "28":
        from turtle import *
        tb = input("shape = (turtle or arrow):")
        bt = int(input("print speed from 1 to 10:"))
        y = int(input("where do you WANT TO GO(x):"))
        d =  int(input("where do you WANT TO GO(y):"))

        xt = str(tb)
        shape(xt)
        speed(bt)
        goto(y,d)
    if  yyyyyyyyyyyy == 29 or trar ==  "29":
        aliens = 5
        password = "ALIENS"
        print("quickly! aliens are invading the planet")
        print("you need to activate defence platforms")
        print("hope you know the password")
        print()
        print("-----------------------------------------------------------------------------------------------")
        print("                             WELCOME TO THE DEFENCE NETWORK"                                    )
        print("-----------------------------------------------------------------------------------------------")
        print()
        guess = input("please enter the password: ").upper()
        if guess == password:
            print("YOU WIN")
        while guess != password:
            aliens = aliens**2
            print("there are", aliens, "aliens, try again")
        #    if aliens > 74000000000:
        #        break
            print("password hint things attack you now")
            guess = input("please enter the password: ").upper()
            if aliens > 74000000000:
                print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO YOU LOSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
            if guess == password:
                print("YOU WIN")
    if  yyyyyyyyyyyy == 30 or trar ==  "30":
                
        ad = {"we":"vorag","come":"thang", "in":"zon","peace":"argh", "helo":"kodar","can":"znak","i":"az","borrow":"liftit","some":"zum"}
        eg = input("what do you want to translate:")
        ew = eg.lower().split()
        aw = []
        for w in ew:
            if w in ad:
                aw.append(ad[w])
            else:
                aw.append(w)
            print("in alien say ","".join(aw))
    if  yyyyyyyyyyyy == 31 or trar ==  "31":
        from turtle import *
        from random import *
            
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')
        cf = [clrname.upper()]
        for x in range(1,90):
                
            clr = randint(0x0,0xFFFFFF)
                
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')
            cf.append(clrname.upper())

            
        t = Pen()
        t.speed(0)
        bgcolor("black")
        for x in range(500):
            t.pencolor(cf[x%89])
            t.width(x/100 +1)
            t.forward(x)
            t.left(59)
    if  yyyyyyyyyyyy == 32 or trar ==  "32":
        from turtle import *
        from random import *
        t=Pen()
        t.speed(0)
        #t.hideturtle()

        for x in range(40):
            rey = randint(1,5)
        #    t.pensize(rey)
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')

            t.color(clrname.upper())
        #    rer = randint(20,100)
        
            t.circle(x)
            t.left(45)
        for x in range(40):
            t.color("white")
            t.circle(x)
            t.left(45)

    if  yyyyyyyyyyyy == 33 or trar ==  "33":
        #        from turtle import *print("you are in dark room")
        print("you see 4 doors")
        pc = input("choose  1,2,3 or 4: ")
        if pc == "3": 
            print("you can either")
            print("1)you can run away ")
            print("2)try to steal some gold")
            dc = input("choose 1 or 2:")
            if dc == "2":
                print("you lose")
            elif dc == "1":
                print("you lose")
            else:
                print("you lose")


        elif pc == "2":
            print("you lose")
        elif pc == "4":
            import random
            nur = random.randint(1,10)
            go = int(input("choose number from 1 to 10: "))
            if go == nur:
                    print("you win")
                    
            if go < nur:
                print("you lose")
            else:
                print ("you lose")
                    
        elif pc == "1":
                    print("you lose")
                        
        else:
            print("you lose")
    if  yyyyyyyyyyyy == 34 or trar ==  "34":
                
        print("Create your charecter")
        name = input("What is his name?")
        age = input("How old is he?")
        power = input("what is he strengths?")
        weakness = input("what is he weakness?")
        print("he is",name)
        print("he is",age, "years old")
        print("power:",power)
        print("weakness:",weakness)
        print(name,"Says thanks for creating me!!!!!!!!!!!!!!!!!")
    if  yyyyyyyyyyyy == 35 or trar ==  "35" and uuuu == True:
        import random
        woman =["a queen","a pirate","a big rabbit","dragon","princess bublgum"]
        man = ["killer","robot","mario","human","Finn"] 
        place = ["at the super market","on pluto", "in the vidiogame","at the adveture time"]
        shewore =["bag", "fairy wings", "robot","ring","dress"]
        hewore = ["purple suit", "a shark costume","Mario costume","pajama","Finn costum"]
        womansay = ["who are you?","how many beans make five","why","do you want to play vidiogame","are you ise king"]
        masay = ["beep boop","don't eat frogs","are you stupid","yes","no I am not"]
        ws = ["eat frogs", "hi is stupid", "she is stupid","me to","he is ice king "]
        do = [" fight to the end","woman and man got married", "run away","play vidio game","punch Finn"]
        ret = ["happy", "weird", "ill","flaffy","hungry"]
        rig = ["got married", "play vidiogames", "eat frogs","run away","win Finn"]
        ring = ["walk", "play with cat", "eat frogs","go to pluto","win princess"]
        w = True
        while w == True:
            print(random.choice(woman),"met",random.choice(man), random.choice(place))
            print("she was wearing",random.choice(shewore))
            print("he was wearing",random.choice(hewore))
            print("she said",random.choice(womansay))
            print("he said",random.choice(masay))
            print("world said",random.choice(ws))
            print("they are", random.choice(do))
            print("they are", random.choice(ret))
            print("she is want to", random.choice(rig))
            print("he is want to", random.choice(ring))
            rt = input("if you want to stop game print F(else print enter):")
            if rt == "F":
                w = False
                break
    if  yyyyyyyyyyyy == 36 or trar ==  "36" and uuuu == True:
        from time import *
        from tkinter import *
        w = Tk()
        WinWidth=750
        Wincenter=WinWidth/2
        g = Canvas(w, width=WinWidth, height=500, bg="white")
        g.pack()
        answ = 0

        #Clear screen
        def Clear_all():
            g.create_rectangle(0,0,1000,1000,fill="white")

        #Play again
        def Play_again():
            playag=g.create_rectangle(Wincenter-37,250,Wincenter+57,270,fill="white")
            playagtxt=g.create_text(Wincenter+10,259,text='Play again',font="Calibri 14")
            def playagev(event):
                Clear_all()
                Question1()
                Play_again()
            g.tag_bind(playag,"<Button-1>",playagev)
            g.tag_bind(playagtxt,"<Button-1>",playagev)


        def Question1():
            #Making questions
            question=g.create_text(Wincenter,20,text="You see 2 doors",font="Calibri 16")
            question=g.create_text(Wincenter,40,text="Choose 1 or 2",font="Calibri 16")
            #
            #Making answers
            answ1i=g.create_rectangle(Wincenter,70,Wincenter+20,90,fill="white")
            answ1txt=g.create_text(Wincenter+10,79,text='1',font="Calibri 14")
            answ2i=g.create_rectangle(Wincenter,100,Wincenter+20,120,fill="white")
            answ2txt=g.create_text(Wincenter+10,109,text='2',font="Calibri 14")
            #
            #Making events
            def answ1ev(event):
                Gamesay=g.create_text(Wincenter,200,text="YOU LOSE!",font="Calibri 20")
            def answ2ev(event):
                Clear_all()
                Play_again()
                Question2()
            g.tag_bind(answ1i,"<Button-1>",answ1ev)
            g.tag_bind(answ1txt,"<Button-1>",answ1ev)
            g.tag_bind(answ2i,"<Button-1>",answ2ev)
            g.tag_bind(answ2txt,"<Button-1>",answ2ev)

        def Question2():
            #Making questions
            question=g.create_text(Wincenter,20,text="You see 3 doors",font="Calibri 16")
            question=g.create_text(Wincenter,40,text="Choose 1 or 2 or 3",font="Calibri 16")
            #
            #Making answers 
            answ1i=g.create_rectangle(Wincenter,70,Wincenter+20,90,fill="white")
            answ1txt=g.create_text(Wincenter+10,79,text='1',font="Calibri 14")
            answ2i=g.create_rectangle(Wincenter,100,Wincenter+20,120,fill="white")
            answ2txt=g.create_text(Wincenter+10,109,text='2',font="Calibri 14")

            answ3i=g.create_rectangle(Wincenter,130,Wincenter+20,150,fill="white")
            answ3txt=g.create_text(Wincenter+10,139,text='3',font="Calibri 14")
            #
            #Making events
            def answ1ev(event):
                Gamesay=g.create_text(Wincenter,200,text="YOU LOSE!",font="Calibri 20") 
            def answ2ev(event):
                Gamesay=g.create_text(Wincenter,200,text="YOU LOSE!",font="Calibri 20")
            def answ3ev(event):
                Gamesay=g.create_text(Wincenter,200,text="YOU WIN!",font="Calibri 20")
                
            g.tag_bind(answ1i,"<Button-1>",answ1ev)
            g.tag_bind(answ1txt,"<Button-1>",answ1ev)   
            g.tag_bind(answ2i,"<Button-1>",answ2ev)
            g.tag_bind(answ2txt,"<Button-1>",answ2ev)   
        
            g.tag_bind(answ3i,"<Button-1>",answ3ev)
            g.tag_bind(answ3txt,"<Button-1>",answ3ev)

        #Main program
        ###################
        Question1()
        
        tt = input("if you want to stop game print F")
        if tt == "F":
            uuuu = False
#            break
        Play_again()
        tt = input("if you want to stop game print F")
        if tt == "F":
            uuuu = False
#            break
        w.mainloop()
    if  yyyyyyyyyyyy == 37 or trar ==  "37":
            
        from random import *
        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = clr
        #clrname = clrtxt.replace('0x','#')
            
        #while len(clrname) != 7:
        #    clrname = clrname.replace('#','#0')
        uu = input("print a code")
        su = uu
        if clr == su:
            print("you win")
        else:
            print("you lose, the correct word is", clr)
    if  yyyyyyyyyyyy == 38 or trar ==  "38":
        tgh = True
        while tgh == True:
            yuj = int(input("choose orthic axe of the triangle:"))
            jui = int(input("choose base of the triangle:"))
            hhru = jui*yuj/2
            print(hhru)
            r = input("if you want to stop game print F:")
            if r == "F":
                tgh = False
                break
    if  yyyyyyyyyyyy == 39 or trar ==  "39":
        from math import *
        from tkinter import *
        WinTk = Tk()
        WinWidth=750
        hh=0

        Canv = Canvas(WinTk, width=WinWidth, height=500, bg="white")
        Canv.pack()

        def MathObjects():
            Canv.create_rectangle(0,100,1000,1000,fill="lightgrey")
            Tr = Canv.create_polygon(50,90,100,20,140,90,fill="blue")
            Sq= Canv.create_polygon(170,90,170,20,240,20,240,90,fill="green")
            Cir=Canv.create_oval(270,20,340,90,fill="yellow")
            Canv.tag_bind(Tr, "<Button-1>",trisngle)
            Canv.tag_bind(Sq, "<Button-1>",gle)
            Canv.tag_bind(Cir, "<Button-1>",ci)

        #Triangle
        def trisngle(event):
            Canv.delete("all")
            MathObjects()
            TboxHeight=Entry(Canv)
            TboxBase=Entry(Canv)
            Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
            Canv.create_text(WinWidth/2,200,text="Input height of the triangle:",font="Calibri 14")
            Canv.create_window(WinWidth/2,220,window=TboxHeight)
            Canv.create_text(WinWidth/2,240,text="Input base of the triangle:",font="Calibri 14")
            Canv.create_window(WinWidth/2,260,window=TboxBase)


            clearitxt=Canv.create_text(WinWidth/2,300,text='Square',font="Calibri 14")
            def ll(event):
                Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
                global hh
                HeightTr=TboxHeight.get()
                BaseTr=TboxBase.get()
                hh = float(HeightTr)*float(BaseTr)/2
                Canv.create_text(WinWidth/2,320,text=hh,font="Calibri 14")
            Canv.tag_bind(clearitxt, "<Button-1>",ll)

        #Rectangle
        def gle(event):
            Canv.delete("all")
            MathObjects()
            TboxHeight=Entry(Canv)
            TboxBase=Entry(Canv)
            Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
            Canv.create_text(WinWidth/2,200,text="Input height of the rectangle:",font="Calibri 14")
            Canv.create_window(WinWidth/2,220,window=TboxHeight)
            Canv.create_text(WinWidth/2,240,text="Input width of the rectangle",font="Calibri 14")
            Canv.create_window(WinWidth/2,260,window=TboxBase)


            clearitxt=Canv.create_text(WinWidth/2,300,text='Square',font="Calibri 14")
            def ll(event):
                Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
                global hh
                HeightTr=TboxHeight.get()
                BaseTr=TboxBase.get()
                hh = float(HeightTr)*float(BaseTr)
                Canv.create_text(WinWidth/2,320,text=hh,font="Calibri 14")
            Canv.tag_bind(clearitxt, "<Button-1>",ll)

        #Circle    
        def ci(event):
            Canv.delete("all")
            MathObjects()
            TboxHeight=Entry(Canv)
            Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
            Canv.create_text(WinWidth/2,200,text="Input radius of the circle:",font="Calibri 14")
            Canv.create_window(WinWidth/2,220,window=TboxHeight)






            clearitxt=Canv.create_text(WinWidth/2,300,text='Square',font="Calibri 14")
            def ll(event):
                Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
                global hh
                HeightTr=TboxHeight.get()
                hh = pi*float(HeightTr)*float(HeightTr)
                Canv.create_text(WinWidth/2,320,text=hh,font="Calibri 14")
            Canv.tag_bind(clearitxt, "<Button-1>",ll)

        MathObjects()
        ggg = input("if you want to stop game print F")
        if ggg == "F":
            break
        WinTk.mainloop()





















    if  yyyyyyyyyyyy == 40 or trar ==  "40":
        from tkinter import *
        from random import *
        score = 0
        gameOver = False
        squaresToClear = 0
        def play_bombdodger():
            create_bombfield(bombfield)
            window = Tk()
            layout_window(window)
            window.mainloop()
        bombfield = []
        def create_bombfield(bombfield):
            global squaresToClear
            for row in range(0,10):
                rowlist = []
                for colown in range(0,10):
                    if randint(1,100) < 20:
                        rowlist.append(1)
                    else:
                        rowlist.append(0)
                        squaresToClear = squaresToClear + 1
                bombfield.append(rowlist)
            printfield(bombfield)
        def printfield(bombfield):
            for rowlist in bombfield:
                print(rowlist)
        #play_bombdodger()
        def layout_window(window):
            for rownumber, rowlist in enumerate(bombfield):
                for columnNumber, columnEntry in enumerate(rowlist):
                    if randint(1,100) < 25:
                        square = Label(window, text="    ", bg="darkgreen") 
                    elif randint(1,100) > 75:
                        square = Label(window, text="    ", bg="seagreen")
                    else:
                        square = Label(window, text="    ", bg="green")
                    square.grid(row=rownumber,column=columnNumber)
                    square.bind("<Button-1>", on_click)
        #play_bombdodger()
        def on_click(event):
            global score
            global gameOver
            global squaresToClear
            square = event.widget
            row = int(square.grid_info()["row"])
            column = int(square.grid_info()["column"])
            currenttext = square.cget("text")
            if gameOver == False:
                if bombfield[row][column] == 1:
                    gameOver == True
                    square.config(bg="red")
                    print("game over!")
                    print("your score is ",score)
                elif currenttext =="    ":
                    square.config(bg="brown")
                    totalbombs = 0
                    if row < 9:
                        if bombfield[row+1][column] == 1:
                            totalbombs = totalbombs + 1
                    if row > 0:

                        if bombfield[row-1][column] == 1:
                            totalbombs = totalbombs + 1
                    if column > 0:

                        if bombfield[row][column-1] == 1:
                            totalbombs = totalbombs + 1
                    if column < 9:

                        if bombfield[row][column-1] == 1:
                            totalbombs = totalbombs + 1
                    if row > 0 and column > 0:

                        if bombfield[row-1][column-1] == 1:
                            totalbombs = totalbombs + 1
                    if row < 9 and column > 0:

                        if bombfield[row+1][column-1] == 1:
                            totalbombs = totalbombs + 1        
                    if row > 0 and column < 9:

                        if bombfield[row-1][column+1] == 1:
                            totalbombs = totalbombs + 1
                    if row < 9 and column < 9:

                        if bombfield[row+1][column+1] == 1:
                            totalbombs = totalbombs + 1
                    
                    square.config(text=" "+ str(totalbombs) +" ")
                    squaresToClear = squaresToClear-1
                    score = score+1
                    if squaresToClear == 0:
                        gameOver = True
                        print("you win")
                        print("your score is",score)
        play_bombdodger()
    
    if  yyyyyyyyyyyy == 42 or trar ==  "42":
        
        ute = input("Do you like robots?")
        if ute == "yes":
            print("robots like you to!")
        elif ute == "maybe":
            print("make up your mind human!")
        elif ute == "no":
            print("are you stupid?!")
        else:
            print("are you stupid")
                    




    if  yyyyyyyyyyyy == 41 or trar ==  "41":
        import nintendo

    if  yyyyyyyyyyyy == 43 or trar ==  "43":
        age = input("How old are you? ")
        agenextyear =  int(age) + 1
        print("i am ", age)
        print("you will be", agenextyear,"next birthday." )




    if  yyyyyyyyyyyy == 44 or trar ==  "44":
        t=Pen()
        ii = randint(0,10)
        t.speed(0)
        t.hideturtle()

        for x in range(400):
            ii = randint(0,10)
            t.speed(0)
            rey = randint(1,5)
            t.pensize(rey)
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')

            t.color(clrname.upper())
            rer = randint(1,1000)

            t.circle(x)
            t.left(25)
        e = input("ys")




    if  yyyyyyyyyyyy == 45 or trar ==  "45":
        jjj = int(input("how many time do you want to sleep:"))
        for x in range(jjj):
            print(jjj-x)
            
            time.sleep(1)
        PlaySound("C:\windows\media\Ring04.wav",False)
        PlaySound("C:\windows\media\Ring01.wav",False)
        PlaySound("C:\windows\media\Ring02.wav",False)
        PlaySound("C:\windows\media\Ring03.wav",False)
        PlaySound("C:\windows\media\Ring05.wav",False)
        PlaySound("C:\windows\media\Ring06.wav",False)
        PlaySound("C:\windows\media\Ring07.wav",False)
        PlaySound("C:\windows\media\Ring08.wav",False) 
        PlaySound("C:\windows\media\Ring09.wav",False)
        PlaySound("C:\windows\media\Ring10.wav",False)
        PlaySound("C:\windows\media\Alarm01.wav",False)
        PlaySound("C:\windows\media\Alarm02.wav",False)
        PlaySound("C:\windows\media\Alarm03.wav",False)
        PlaySound("C:\windows\media\Alarm04.wav",False)
        PlaySound("C:\windows\media\Alarm05.wav",False)
        PlaySound("C:\windows\media\Alarm06.wav",False)
        PlaySound("C:\windows\media\Alarm07.wav",False)
        PlaySound("C:\windows\media\Alarm08.wav",False)
        PlaySound("C:\windows\media\Alarm10.wav",False)
        PlaySound("C:\windows\media\Alarm09.wav",False)
    if  yyyyyyyyyyyy == 46 or trar ==  "46":
        ertl = 0
        oiks = True
        while oiks == True:
            
            uitv = print("your age is")
            ujl = print(ertl)
            uit = input("y or n:")
            if uit == "y":
                oiks == False
                break
            else:
                ertl = ertl+1
    
    if  yyyyyyyyyyyy == 47 or trar ==  "47":
        rruir = []
        tttt = []
        yty5ht4 = True
        while yty5ht4 == True:
            popoiop = input("your hero is:")
            popoio = input("your 2 hero is:")
            rruir.append(popoiop)
            tttt.append(popoio)                           
            gnb = input("is it all (y or n):")
            if gnb == "y":
                print(choice(rruir),"met",choice(tttt))
    if  yyyyyyyyyyyy == 48 or trar ==  "49":
        from turtle import *
        from random import *
        t = Pen()
        t.hideturtle()
        height = randint(100,300)
        bgb = randint(100,300)
        yty = bgb/2
        yt = height/2
        ii = randint(0,10)
        t.pensize(ii)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(0,height)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(bgb,height)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')
        t.pensize(ii)
        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(bgb,0)

        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(0,0)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(0,height)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')
        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(bgb/2,height+40)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(bgb,height)
        t.penup()
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(yty,yt)
        t.pendown()
        t.goto(yty,yt+yt/2)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
        t.pensize(ii)
        t.goto(yty+yty/2+20,yt+yt/2)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())

        t.goto(yty+yty/2+20,yt)
        clr = randint(0x0,0xFFFFFF)
            
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
                
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())

        t.goto(yty,yt)
        #goto(bgb,height)
        uji = input("uj:")

    if  yyyyyyyyyyyy == 48 or trar ==  "49":
        from tkinter import *
        from random import *
        import tkinter.messagebox
        import time
        import random
        import winsound
        from winsound import PlaySound,SND_ASYNC,Beep
        import threading
        from threading import Timer,Thread
        from time import sleep
        import turtle
        from turtle import *
        import sys
        from PIL import Image
        q = Screen()
        t = Turtle()
        listen()
        t2 = Turtle()
        t.pu()
        t2.pu()
        t.speed(0)
        t.goto(0,90)
        t2.speed(0)
        t2.goto(90,0)
        t2.shapesize(10)
        t3 = Turtle()
        t4 = Turtle()
        t3.pu()

        t4.pu()
        t3.speed(0)
        t3.goto(-123,43)
        t4.speed(0)
        t3.goto(-90,0)
        t4.shapesize(10)
        def fight(cha):
            
            if cha == 't':
                global far
                e = Turtle()
                e.pu()
                e.forward(-30)
                l = 10
                far = 100
                def j():
                    global far
                    x,y = t.pos()
                    t.speed(1)
                    t.goto(x,y+100)
                    t.goto(x,y)
                    t.speed(0)
                    iu = t.distance(e)
                    if iu <= 10:
                        far = far - 1
                        print(far)
                def f():
                    global far
                    x,y = t.pos()
                    t.speed(1)
                    t.goto(x+1,y)
                    iu = t.distance(e)
                    if iu <= 10:
                        far = far - 1
                        print(far)
                def b():
                    global far
                    x,y = t.pos()
                    t.speed(1)
                    t.goto(x-1,y)
                    iu = t.distance(e)
                    if iu <= 10:
                        far = far - 1
                        print(far)
                q.onkey(j,'Up')
                q.onkeypress(f,'Left')
                q.onkeypress(b,'Right')
            if cha == 't2':
        #      global far
                e = Turtle()
                e.pu()
                e.forward(-30)
                l = 10
                far = 100
                def j():
                    global far
                    x,y = t.pos()
                    t.speed(1)
                    t.goto(x,y+100)
                    t.goto(x,y)
                    t.speed(0)
                def f():
                    global far
                    x,y = t.pos()
                    t.speed(1)
                    t.goto(x+1,y)

                def b():
                    global far
                    x,y = t.pos()
                    t.speed(1)
                    t.goto(x-1,y)
                def ata():
                    global far
                    t1 = t.clone()
                    for m in range(100):
                        t1.forward(1)
                        iu = t1.distance(e)
                        if iu <= 10:
                            far = far - 1
                            print(far)
                    t1.ht()
                q.onkey(j,'Up')
                q.onkeypress(f,'Left')
                q.onkeypress(b,'Right')
                q.onkey(ata,'w')

        def cd():
            Screen().bgcolor("black")
            t2.goto(700,700)
            t3.goto(700,700)
            t4.goto(700,700)
            #t2.goto(700,700)
            
            Screen().bgcolor("white")
        def fort(x,y):


            cd()
            t.goto(0,0)

            fight('t')
        t.onclick(fort)
        def fort2(x,y):


            cd()
            t.goto(0,0)

            fight('t2')
        t2.onclick(fort2)    
        mainloop()
    if trar ==  "False":
        wert = True
#        break
