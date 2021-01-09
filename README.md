# PaintBot

Python script that generates an AHK script that draws an image

Here is an example of an input image.

![](imgs/flowers.png)


This image is read at pixel level and the algorithm maps each fittest neighbour pixel based on a tolerance input number (from 0 to 255, zero being exactly the same)

> python main.py "imgs/flowers.png" 64 > flowers64.ahk

After generating a AHK script, the later opens a "paint" window, adjust its window a automatically draws the input image:

![](gifs/flowers1.gif)


Here is also another example:

![](gifs/school_of_athens.gif)


TODO List:

- Create a user interface
- Find a way to adjust "paint" window size. So far the window position must be previously and manually calibrated
