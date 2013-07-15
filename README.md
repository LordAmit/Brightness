Brightness Controller
==========

## What is it?

Brightness Controller allows you to control Brightness of your **internal AND external monitor** with the help of *xrandr* in Linux. The controller is created using *python*, which in the back end calls *os.system* commands to execute system commands.

## What good is it?

It allows you to control the brightness of your monitor to a better extent. For example, my laptop's monitor brightness can be controlled using hardware keys at discrete values, such as 20%, 40%, 60% ... 100%. Brightness Controller allows you to change the brightness to a better degree of control, ranging from 1% to 100%! It should be mentioned that it changes the present brightness value set via hardware control of your monitor. For example, if you set your Monitor's brightness to 50% using hardware buttons, then that will be the 100% value in Brightness controller. 

## How do I run it? 

- Download the <a href="https://github.com/lordamit/Brightness/archive/master.zip">Latest version</a> to your home folder. 
- Extract it. 
- In the src folder, set the permission of the brightness.py file as executable. 
- Find the brightness.desktop in the src folder and open it with gedit text editor.
- Replace 'path/to' with the original path of brightness.py in line 4 and brightness.desktop in line 7.
- Mark brightness.desktop as executable.
- Now brightness.desktop would turn into 'Brightness Controller' and would have an icon.
- Double-click Brightness Controller and the app would run. You can even pin it to Unity launcher.

## What are the requirements / dependencies / things I need to run it?

I have found only three requirements till now.

1. Python - Linux should have it by default
2. Python WxWidgets

    >sudo apt-get install python-wxgtk2.8
3. xrandr - that's what the program uses in the backend to control the brightness of your monitor!

## It does not detect my monitors properly.

Kindly make an issue in the github project and submit the output of this command:

> xrandr -q

## I have more than two monitors, and this program only shows two. What's happening?

In a word, *jealousy*. Because I never had more than two monitors simultaneously, I decided to give support for up to two monitors only. So no, it can not support your third (or fourth, or fifth...) monitor.

## Screenshot

<a href="http://www.flickr.com/photos/lordamit/9035113863/" title="Brightness Controller_018 by lordamit, on Flickr"><img src="http://farm4.staticflickr.com/3760/9035113863_3f34176caa.jpg" width="306" height="127" alt="Brightness Controller_018"></a>

# Misc.

Random questions that might show up here are answered here in advance.

## The coding style is not exactly.. pythonlike.
 
Because it is my first python code that exceeds 10 lines. I have not used Python before, but I decided to use it for this project for no particular reason.

## Why is it here?

I wrote it because I could not find any other similar software available **in Linux** that provides an easy to use UI for changing brightness. There are still room for improvement, specially in the coding style. I hope due to its open source nature, people will come forward and will help it become a better brightness controller.

## Help! It broke my computer!

*Erm, that's not exactly supposed to happen. Still, use at your own risk. I won't allow myself to be held responsible even if it turns your monitor into a black hole, sucks you in and kills you in the process.
But still, let me know if something goes wrong by reporting it in the issues section.*

On a more serious note, Brightness Controller does nothing that can break your computer. It simply provides a graphical user interface you can use with a mouse to control brightness easily. It does not execute any command or does not do anything to change your system. So, feel free to use it :)
