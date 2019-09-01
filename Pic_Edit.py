from PIL import Image, ImageDraw
a=str(input("Enter image file name with extension to edit :- "))
ip = Image.open(a)
ips = ip.load()
n=int(input("Press 1 for Sobel Horizontal\nPress 2 for Sobel Vertical\nPress 3 for Laplacian Operation\nPress 4 for Gaussian Blur\n"))
if(n==1):
    kernel = [[-1,-2,-1],
              [0,0,0],
              [1,2,1]]
if(n==2):
    kernel = [[-1, 0, 1],
              [-2,0,2],
              [-1, 0,1]]
if(n==3):
    kernel = [[1, 1,1],
              [1,-8,1],
              [1,1,1]]
if(n==4):
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
