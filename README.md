
# Image-To-Ascii
Draw the given image to the console using the ascii characters.


## Prerequisites
Don't forget that you should be importing 
* **google_images_download** 


```terminal
$ pip install google_images_download
```
or for more information --> https://github.com/hardikvasa/google-images-download

## Using the script
After you install google_images_download you can run the script in the terminal.

```terminal
$ cd {drawToConsole.py Location}
$ python drawToConsole.py
```

Now you can simply write the word for the image you would like to see.

### Example #1

Entered input: **Saturn**

Result: ![alt text](https://github.com/emrebicer/Image-To-Ascii/blob/master/Screenshots/saturn.png)

### Example #2

Entered input: **Micheal Jackson**

Result: ![alt text](https://github.com/emrebicer/Image-To-Ascii/blob/master/Screenshots/mj.png)

### Example #3

Entered input: **Yin yang**

Result: ![alt text](https://github.com/emrebicer/Image-To-Ascii/blob/master/Screenshots/yin%20yang.png)


## Cont'd
Also, you can make the script draw your local files.
Using the command (in the script),

```terminal
LOCAL {imageName.png} // Could be any image extension.
```

Before drawing the image, the script changes to width and height of the image to fit it to the console screen.Don't forget that the bigger the width and height more quality you will get and more realistic the ascii characters will look.
For me the optimal width of the image should be 50 pixels to fit the maximized console screen well, but you can change the desired width with the given command(in the script),

```terminal
width 30 // Changes the width to 30 pixels.
```

**Note that;** The height of the original image is resized according to desired width.
E.g;An image with 300x150 is converted to 50x25.
