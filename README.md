Brightness Controller
==========

## What is it?

Brightness Controller allows you to control Brightness of your **internal AND external monitor** with the help of *xrandr* in Linux. The controller is created using *python*, which in the back end calls *os.system* commands to execute system commands.

## What good is it?

It allows you to control the brightness of your monitor to a better extent. For example, my laptop's monitor brightness can be controlled using hardware keys at discrete values, such as 20%, 40%, 60% ... 100%. Brightness Controller allows you to change the brightness to a better degree of control, ranging from 1% to 100%! It should be mentioned that it changes the present brightness value set via hardware control of your monitor. For example, if you set your Monitor's brightness to 50% using hardware buttons, then that will be the 100% value in Brightness controller. 

## How do I run it? 

Just set the permission of the brightness.py file as executable. Double click on it, and it will run. 

## How do I know my Monitor name?

Easy, open terminal and then paste this command.

> xrandr -q | grep -w connected

I am given this output,

> **LVDS1** connected 1366x768+0+0 (normal left inverted right x axis y axis) 309mm x 173mm

So that means the name of my primary ( or connected ) monitor is **LVDS1**. In your case, it might be VGA1, HDMI1 or even DP1!

## What are the requirements / dependencies / things I need to run it?

I have found only three requirements till now.

1. Python - Linux should have it by default)
2. WxWidgets - the UI was written using Python WxWidgets)
3. xrandr - that's what the program uses in the backend to control the brightness of your monitor!

# Misc.

Random questions that might show up here are answered here in advance.

## The coding style is not exactly.. pythonlike.
 
Because it is my first python code that exceeds 10 lines. I have not used Python before, but I decided to use it for this project for no particular reason.

## Why is it here?

I wrote it because I could not find any other similar software available **in Linux** that provides an easy to use UI for changing brightness. There are still room for improvement, specially in the coding style. I hope due to its open source nature, people will come forward and will help it become a better brightness controller.

## Help! It broke my computer!

Erm, that's not exactly supposed to happen. Still, use at your own risk. I won't allow myself to be held responsible even if it turns your monitor into a black hole, sucks you in and kills you in the process.
But still, let me know if something goes wrong by reporting it in the issues section.

