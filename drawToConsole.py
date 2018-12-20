#github.com/emrebicer

from __future__ import print_function
from PIL import Image
import os
from google_images_download import google_images_download

#CHARS	= [' ', ' ', '.', ':', '!', '+', '*', 'e', '$', '@', '8']

desiredWith = 50


def getRandomImage(keyw):
    response = google_images_download.googleimagesdownload()

    keyword = keyw + ' black and white'
    absolute_image_paths = response.download({"keywords":keyword,"limit":1})
    return absolute_image_paths[keyword]


def resizeIMG(width,img):
    basewidth = width
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    return img

def returnRecPixelDensityForTransparant(p):
    try:
        if p[0]*0.299 + p[1]*0.587 + p[2]*0.114 != 0:
            return p[0]*0.299 + p[1]*0.587 + p[2]*0.114
        else:
            return p[3]
    except:
        return 255
def returnRecPixelDensity(p):
    try:
        return p[0]*0.299 + p[1]*0.587 + p[2]*0.114
    except:
        return 255


def print1(pix,j,i):
    if(returnRecPixelDensity(pix[j,i]) > 230):
        print('8 ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 205:
        print('@ ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 180:
        print('$ ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 155:
        print('e ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 130:
        print('* ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 105:
        print('+ ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 80:
        print('! ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 55:
        print(': ', end='')
    elif returnRecPixelDensity(pix[j,i]) > 20:
        print('. ', end='')
    else:
        print('  ', end='')


def print1ForTransparant(pix,j,i):
    if(returnRecPixelDensityForTransparant(pix[j,i]) > 230):
        print('8 ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 205:
        print('@ ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 180:
        print('$ ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 155:
        print('e ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 130:
        print('* ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 105:
        print('+ ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 80:
        print('! ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 55:
        print(': ', end='')
    elif returnRecPixelDensityForTransparant(pix[j,i]) > 20:
        print('. ', end='')
    else:
        print('  ', end='')




def drawWithParameter(para):
    global keyw
    keyw = para
    try:
        im = Image.open(keyw)
    except:
        print('Can\'t open image:'+keyw)
        return

    #Check if the image has transparant value
    isTransparant = False
    im = resizeIMG(50,im)
    pix = im.load()
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            #pix[i,j] = (100,100,100)
            try:
                p = pix[i,j][0]*0.299 + pix[i,j][1]*0.587 + pix[i,j][2]*0.114
            except:
                #Cant read the rgb value so there is a alpha value.
                isTransparant = True
                break


    if isTransparant:
        im = im.convert("RGBA")
        im = resizeIMG(desiredWith,im)
        pix = im.load()
        print(str(im.size) + "(Transparant img)")
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                #pix[i,j] = (100,100,100)
                print1ForTransparant(pix,j,i)
            print()
    else:
        im = resizeIMG(desiredWith,im)
        pix = im.load()
        print(str(im.size) + "(Nontransparant img)")
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                #pix[i,j] = (100,100,100)
                print1(pix,j,i)
            print()


def drawGivenInput():
    imageLocation = str(getRandomImage(keyw))
    localLocation = './downloads/'+keyw+" black and white/"
    try:
        fileN = os.listdir(localLocation)
        localLocation = localLocation + fileN[0]
    except:
        print("Error getting the image with the path:"+localLocation)
        drawGivenInput()

    im = Image.open(localLocation)

    #Check if the image has transparant value
    isTransparant = False
    im = resizeIMG(50,im)
    pix = im.load()
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            #pix[i,j] = (100,100,100)
            try:
                p = pix[i,j][0]*0.299 + pix[i,j][1]*0.587 + pix[i,j][2]*0.114
            except:
                #Cant read the rgb value so there is a alpha value.
                isTransparant = True
                break


    if isTransparant:
        im = im.convert("RGBA")
        im = resizeIMG(desiredWith,im)
        pix = im.load()
        print(str(im.size) + "(Transparant img)")
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                #pix[i,j] = (100,100,100)
                print1ForTransparant(pix,j,i)
            print()
    else:
        im = resizeIMG(desiredWith,im)
        pix = im.load()
        print(str(im.size) + "(Nontransparant img)")
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                #pix[i,j] = (100,100,100)
                print1(pix,j,i)
            print()

print('+--------------------------------------------+')
print('|   Welcome, type help to get information!   |')
print('+--------------------------------------------+')

while 1:
    global keyw
    keyw = raw_input("What should i draw?")

    commands = keyw.split(' ')

    if keyw.lower() == 'help':
        for i in range(3):
            print('')
        print(' - Enter the keyword to draw an image found at google images.')
        print(' - To draw a local image enter the command as \' LOCAL myimage.png \'. ')
        print(' - Default width for the images is 50 to change width type \'width {newwidth}\'. ')
        print(' - To clear the console type \'clear\'. ')
        print(' - Exit or Quit commands will exit the application.')
        for i in range(3):
            print('')
    elif commands[0] == 'LOCAL':
        #draw a local img.
        print('Drawing local image : '+str(commands[1]))
        drawWithParameter(commands[1])
    elif (keyw.lower() == 'quit') | (keyw.lower() == 'exit'):
        break
    elif commands[0].lower() == 'clear':
        for i in range(100):
            print('')
    elif commands[0].lower() == 'width':
        try:
            desiredWith = int(commands[1])
            print('Image width has set to '+str(commands[1]) + '.')
        except:
            print('Invalid input!Width must be an integer.')
    else:
        drawGivenInput()
