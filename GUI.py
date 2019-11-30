from tkinter import *
from PIL import Image,ImageTk,ImageDraw
import pygame.camera
import pygame.image
import sys,select
import os 
app=Tk()
a=StringVar()
a.set("no-preview.jpg")
def SobHor():
    ip = Image.open(a.get())
    ips = ip.load()
    kernel = [[-1,-2,-1],
              [0,0,0],
              [1,2,1]]
    op = Image.new("RGB",ip.size)
    draw = ImageDraw.Draw(op)
    for x in range(1,ip.width-1):
        for y in range(1,ip.height-1):
            q=[0,0,0]
            for i in range(3):
                for j in range(3):
                    x1 = x+i-1
                    y1 = y+j-1
                    pixel = ips[x1, y1]
                    q[0]+=pixel[0]*kernel[i][j]
                    q[1]+=pixel[1]*kernel[i][j]
                    q[2]+=pixel[2]*kernel[i][j]
            draw.point((x,y),(int(q[0]),int(q[1]),int(q[2])))        

    op.show()

def SobVer():
    ip = Image.open(a.get())
    ips = ip.load()
    kernel = [[-1, 0, 1],
              [-2,0,2],
              [-1, 0,1]]
    op = Image.new("RGB",ip.size)
    draw = ImageDraw.Draw(op)
    for x in range(1,ip.width-1):
        for y in range(1,ip.height-1):
            q=[0,0,0]
            for i in range(3):
                for j in range(3):
                    x1 = x+i-1
                    y1 = y+j-1
                    pixel = ips[x1, y1]
                    q[0]+=pixel[0]*kernel[i][j]
                    q[1]+=pixel[1]*kernel[i][j]
                    q[2]+=pixel[2]*kernel[i][j]
            draw.point((x,y),(int(q[0]),int(q[1]),int(q[2])))        

    op.show()

def LapOpr():
    ip = Image.open(a.get())
    ips = ip.load()
    kernel = [[1, 1,1],
              [1,-8,1],
              [1,1,1]]
    op = Image.new("RGB",ip.size)
    draw = ImageDraw.Draw(op)
    for x in range(1,ip.width-1):
        for y in range(1,ip.height-1):
            q=[0,0,0]
            for i in range(3):
                for j in range(3):
                    x1 = x+i-1
                    y1 = y+j-1
                    pixel = ips[x1, y1]
                    q[0]+=pixel[0]*kernel[i][j]
                    q[1]+=pixel[1]*kernel[i][j]
                    q[2]+=pixel[2]*kernel[i][j]
            draw.point((x,y),(int(q[0]),int(q[1]),int(q[2])))        
    
    op.show()

def GauBlr():
    ip = Image.open(a.get())
    ips = ip.load()
    kernel = [[1/16,1/8,1/16],
              [1/8,1/4,1/8],
              [1/16,1/8,1/16]] 
    op = Image.new("RGB",ip.size)
    draw = ImageDraw.Draw(op)
    for x in range(1,ip.width-1):
        for y in range(1,ip.height-1):
            q=[0,0,0]
            for i in range(3):
                for j in range(3):
                    x1 = x+i-1
                    y1 = y+j-1
                    pixel = ips[x1, y1]
                    q[0]+=pixel[0]*kernel[i][j]
                    q[1]+=pixel[1]*kernel[i][j]
                    q[2]+=pixel[2]*kernel[i][j]
            draw.point((x,y),(int(q[0]),int(q[1]),int(q[2])))        

    op.show()

def initi(self):
    tmp_img=Image.open(a.get())
    def_img=tmp_img.resize((300,300), Image.ANTIALIAS)
    pic=ImageTk.PhotoImage(def_img)
    photolabel=Label(app,image=pic,bg='white')
    photolabel.grid(row=3,column=0,columnspan=3,rowspan=10,padx=9,pady=(20,4))
    mainloop()

def nigga():
    pygame.camera.init()
    cameras = pygame.camera.list_cameras()
    webcam = pygame.camera.Camera(cameras[0])
    webcam.start()
    img = webcam.get_image()
    WIDTH = img.get_width()
    HEIGHT = img.get_height()
    screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
    pygame.display.set_caption("pyGame Camera View")
    while True :
        for e in pygame.event.get() :
            if e.type == pygame.QUIT :
                sys.exit()
        screen.blit(img, (0,0))
        pygame.display.flip()    
        img = webcam.get_image()
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            pygame.image.save(img, "photo.jpg")
            a.set("photo.jpg")
            pygame.camera.quit()
            tmp_img=Image.open(a.get())
            def_img=tmp_img.resize((300,300), Image.ANTIALIAS)
            pic=ImageTk.PhotoImage(def_img)
            photolabel=Label(app,image=pic,bg='white')
            photolabel.grid(row=3,column=0,columnspan=3,rowspan=10,padx=9,pady=(20,4))
            mainloop()
            break

app.title("Filtering")
app.geometry('795x447+200+100')
piclist=['no-preview.jpg','photo1.jpg','photo2.jpeg','photo3.jpeg','photo4.jpeg']
l1=Label(app,text="Availabe Filters:",height =2)
l2=Label(app,text="Preview")
b1=Button(app,text='Sobel Horizontal',width=19,command= SobHor)
b2=Button(app,text='Sobel Vertical',width=19,command= SobVer)
b3=Button(app,text='Laplacian Operation',width=19,command=LapOpr)
b4=Button(app,text='Gaussian Blur',width=19,command=GauBlr)
b5=OptionMenu(app,a,*piclist,command=initi)
b6=Button(app,text='Take from Camera',width=19,command=nigga)
b7=Button(app,text="Crop",width=19)
tmp_img=Image.open('no-preview.jpg')
def_img=tmp_img.resize((300,300), Image.ANTIALIAS)
pic=ImageTk.PhotoImage(def_img)
photolabel=Label(app,image=pic,bg='white')
l1.grid(row = 0, column = 1 , columnspan = 2, rowspan=2)
b1.grid(row = 2,column=0,padx=9)
b2.grid(row = 2,column=1,padx=9)
b3.grid(row = 2,column=2,padx=9)
b4.grid(row = 2,column=3,padx=9)
b5.grid(row=11,column=3,padx=9)
b6.grid(row=12,column=3,padx=9,pady=6)
b7.grid(row=4,column=3,padx=9,pady=6)

photolabel.grid(row=3,column=0,columnspan=3,rowspan=10,padx=9,pady=(20,4))
l2.grid(row=13,column=0,columnspan=3)

app.mainloop()
