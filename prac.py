import tkinter as tk
import hangman as hng
import sys
#class test_gui():
window=tk.Tk()
window.title('Hangman')
window.resizable(height=False,width=False)
window.geometry('500x500')
frame=tk.Frame(window,height=100,width=250,bg='black')
frame.pack(expand=True,side='bottom',fill='both')
frame_1=tk.Frame(window,height=100,width=250,bg='black')
frame_1.pack(expand=True,side='top',fill='both')

hint_1='ghh'
ob1=hng.hangman()
def hint():
	hint_1=ob1.display()
	frame_2=tk.Frame(window,height=100,width=250,bg='black')
	frame_2.pack(expand=True,side='top',fill='both')
	global label_hint
	label_hint=tk.Label(frame_2,text=hint_1,bg='white')
	label_hint.grid(row=0,column=0)

c1=tk.Canvas(frame_1,bg='black')
c1.pack(fill='both')
c1.create_rectangle(350,215,450,265,fill='white')
c1.create_rectangle(400,215,407,55,fill='white')
c1.create_rectangle(320,55,400,62,fill='white')
c1.create_rectangle(320,62,323,92,fill='white')

	#c1.create_line(,0,200,200,fill='white')
par='a'
loop=True
#global lives
#global lives_1
lives=10
lives_1=10
prac='a'
score_1=0
hint()
def func(par):
    x=par
    global lives
    global lives_1
    global score_1
    print(x)
    c1.create_text(100,0,fill='white',text=par)
    score_1,lives=ob1.read(x,lives_1,score_1)
    lives_1=lives
    if lives==9:
         c1.create_oval(310,92,330,120,outline='white')
    if lives==8:
         c1.create_line(320,120,320,130,fill='white')
    if lives==7:
         c1.create_line(310,130,330,130,fill='white')
    if lives==6:
         c1.create_line(310,130,295,145,fill='white')
    if lives==5:
         c1.create_line(330,130,345,145,fill='white') 	
    if lives==4:
         c1.create_line(320,120,320,160,fill="white")
    if lives==3:
         c1.create_line(320,160,300,190,fill="white")
    if lives==2:
         c1.create_line(320,160,340,190,fill="white")
    if lives==1:
         c1.create_line(300,190,295,190,fill="white")
    
         
    if lives<=0:
        c1.create_line(340,190,345,190,fill="white")
        print("game over")
        print("score = " +str(ob1.score))
        sys.exit()
        #print("PLAY AGAIN?(y/n)")
    if score_1+1==ob1.score:
        if label_hint:
            label_hint.destroy()
            hint()
	#if score==0:
		#print("game over")
		#print("score = " +str(hangman.score))
   		
	
#top=t.Frame(window,height=100,width=250,bg='blue').grid(side='right')
#size=t.Frame(width=100,height=100)
#bottom.iconify()
#def inpt():
a=tk.Button(frame,text='a',height=1,width=1,command=lambda :func('a'),padx=20)	
a.grid(row=1 ,column=0)
b=tk.Button(frame,text='b',height=1,width=1,command=lambda :func('b'),padx=20)
b.grid(row=1 ,column=1)
c=tk.Button(frame,text='c',height=1,width=1,command=lambda :func('c'),padx=20)
c.grid(row=1 ,column=2)
d=tk.Button(frame,text='d',height=1,width=1,command=lambda :func('d'),padx=20)
d.grid(row=1 ,column=3)
e=tk.Button(frame,text='e',height=1,width=1,command=lambda :func('e'),padx=20)
e.grid(row=1 ,column=4)
f=tk.Button(frame,text='f',height=1,width=1,command=lambda :func('f'),padx=20)
f.grid(row=1 ,column=5)
g=tk.Button(frame,text='g',height=1,width=1,command=lambda :func('g'),padx=20)
g.grid(row=1 ,column=6)
h=tk.Button(frame,text='h',height=1,width=1,command=lambda :func('h'),padx=20)
h.grid(row=1 ,column=7)
i=tk.Button(frame,text='i',height=1,width=1,command=lambda :func('i'),padx=20)
i.grid(row=1 ,column=8)
j=tk.Button(frame,text='j',height=1,width=1,command=lambda :func('h'),padx=20)
j.grid(row=2 ,column=0)
k=tk.Button(frame,text='k',height=1,width=1,command=lambda :func('k'),padx=20)
k.grid(row=2 ,column=1)
l=tk.Button(frame,text='l',height=1,width=1,command=lambda :func('l'),padx=20)
l.grid(row=2 ,column=2)
m=tk.Button(frame,text='m',height=1,width=1,command=lambda :func('m'),padx=20)
m.grid(row=2 ,column=3)
n=tk.Button(frame,text='n',height=1,width=1,command=lambda :func('n'),padx=20)
n.grid(row=2 ,column=4)
o=tk.Button(frame,text='o',height=1,width=1,command=lambda :func('o'),padx=20)
o.grid(row=2 ,column=5)
p=tk.Button(frame,text='p',height=1,width=1,command=lambda :func('p'),padx=20)
p.grid(row=2 ,column=6)
q=tk.Button(frame,text='q',height=1,width=1,command=lambda :func('q'),padx=20)
q.grid(row=2 ,column=7)
r=tk.Button(frame,text='r',height=1,width=1,command=lambda :func('r'),padx=20)
r.grid(row=2 ,column=8)
s=tk.Button(frame,text='s',height=1,width=1,command=lambda :func('s'),padx=20)
s.grid(row=3 ,column=0)
t=tk.Button(frame,text='t',height=1,width=1,command=lambda :func('t'),padx=20)
t.grid(row=3 ,column=1)
u=tk.Button(frame,text='u',height=1,width=1,command=lambda :func('u'),padx=20)
u.grid(row=3 ,column=2)
v=tk.Button(frame,text='v',height=1,width=1,command=lambda :func('v'),padx=20)
v.grid(row=3 ,column=3)
w=tk.Button(frame,text='w',height=1,width=1,command=lambda :func('w'),padx=20)
w.grid(row=3 ,column=4)
x=tk.Button(frame,text='x',height=1,width=1,command=lambda :func('x'),padx=20)
x.grid(row=3 ,column=5)
y=tk.Button(frame,text='y',height=1,width=1,command=lambda :func('y'),padx=20)
y.grid(row=3 ,column=6)
z=tk.Button(frame,text='z',height=1,width=1,command=lambda :func('z'),padx=20)
z.grid(row=3 ,column=7)
space=tk.Button(frame,text='space',height=1,width=1,command=lambda :func(" "),padx=20)
space.grid(row=3 ,column=8)
#par="a"
#while lives>0:
#	inpt()
	
window.mainloop()
		
	
	
	############################################################################
	

	


	
