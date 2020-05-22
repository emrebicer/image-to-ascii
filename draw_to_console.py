""" Converts the given image into text format,
    reproduces the pixels using special characters

    Emre Biçer
    github.com/emrebicer
    emreee.bicer@gmail.com
"""

import sys
import os
import math
from PIL import Image
from google_images_download import google_images_download

SPECIAL_CHARS = [' ', ' ', '.', ':', '!', '+', '*', 'e', '$', '@', '8']
desired_width = 50


def download_random_image(keyword):
    """ Download the image from the google images,
        save it to the local disk
    """

    response = google_images_download.googleimagesdownload()
    keyword = keyword + ' black and white'
    try:
        absolute_image_paths, _ = response.download(
            {"keywords": keyword, "limit": 1})
    except Exception as e:
        print('Couldn\'t download image:', str(e))
        return -1

    if absolute_image_paths[keyword] == []:
        print('\nCouldn\'t download image\n')
        return -1

    return absolute_image_paths[keyword]


def resize_image(target_width, img):
    """ Resize the image based on given width,
        keep the aspect ratio
    """

    ratio = (target_width/float(img.size[0]))
    target_height = int((float(img.size[1])*float(ratio)))
    return img.resize((target_width, target_height),
                      Image.ANTIALIAS)


def get_pixel_density(pixel):
    """ Calculate the pixel density based on rgba channels
        of the given pixel
    """

    # Check if the alpha value is < 0.5
    if len(pixel) >= 4 and pixel[3] < 255 / 2:
        return 255
    else:
        try:
            return pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114
        except Exception as _:
            return 255


def print_pixel(pixel):
    """ Print a single char based on the given pixel
    """

    # Calculate the pixel density
    density = get_pixel_density(pixel)

    # Map the density to special chars length
    # and find the matched characters
    found_index = math.floor((len(SPECIAL_CHARS)-1) * (255 - density) / 255)
    if found_index > len(SPECIAL_CHARS) - 1:
        found_index = len(SPECIAL_CHARS) - 1
    print(f'{SPECIAL_CHARS[found_index]} ', end='')


def draw_local_image(image_path, desired_width):
    """ Flushes the given image to the console
        using ascii characters
    """

    try:
        im = Image.open(image_path)
    except Exception as _:
        print('Can\'t open image:' + str(image_path))
        return

    im = im.convert("RGBA")
    im = resize_image(desired_width, im)
    pixels = im.load()

    for i in range(im.size[1]):
        for j in range(im.size[0]):
            print_pixel(pixels[j, i])
        print()


def command_line_interface():
    global desired_width
    print('+--------------------------------------------+')
    print('|   Welcome, type help to get information!   |')
    print('+--------------------------------------------+')

    while True:

        keyw = input("What should i draw:")

        commands = keyw.split(' ')

        if keyw.lower() == 'help':
            print('\n'*3)
            print(' - Enter the keyword to draw an image \
                found at google images.')
            print(' - To draw a local image enter the command as\
                \' LOCAL myimage.png \'. ')
            print(' - Default width for the images is 50 to change\
                width type \'width {newwidth}\'. ')
            print(' - To clear the console type \'clear\'. ')
            print(' - Exit or Quit commands will exit the application.')
            print('\n'*3)
        elif commands[0].lower() == 'local':
            # Draw a local img
            print('Drawing local image : '+str(commands[1]))
            draw_local_image(commands[1], desired_width)
        elif (keyw.lower() == 'quit') | (keyw.lower() == 'exit'):
            # Stop the script
            break
        elif commands[0].lower() == 'clear':
            print('\n'*100)
        elif commands[0].lower() == 'width':
            try:
                desired_width = int(commands[1])
                print('Image width has set to '+str(commands[1]) + '.')
            except Exception as _:
                print('Invalid input! Width must be an integer.')
        else:
            # Download image from google then draw
            downloaded_image_path = download_random_image(commands[0])
            if downloaded_image_path != -1:
                draw_local_image(downloaded_image_path, desired_width)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        draw_local_image(str(sys.argv[1]), 50)
    else:
        command_line_interface()
