from PIL import Image

#create the lists
imglist =[]
pix = []
redpix =[]
greenpix=[]
bluepix=[]

#define median function
def median(list):
    length = len(list)
    sortedlist = sorted(list)
    return sortedlist[((length + 1)/2)-1]

#open images for fast pixel access
for n in range(1,10):
    imglist.append(Image.open(str(n) + ".png"))
    pix.append(imglist[n - 1].load())

#get width and height 
width,height = imglist[0].size

#make a new image
newimg = Image.new("RGB",(width,height))
newimgpix = newimg.load()

#loop that sets the pixels of our new image
for x in range(0,width):
    for y in range(0,height):
        for m in range(len(pix)):
            #print n
            redpix.append(pix[m][x,y][0])
            greenpix.append(pix[m][x,y][1])
            bluepix.append(pix[m][x,y][2])

        newimgpix[x,y] = (median(redpix),median(greenpix),median(bluepix))
        del redpix[:]
        del greenpix[:]
        del bluepix[:]
#save the image
newimg.save("newimg.png")