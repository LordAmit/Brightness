# Brightness Controller

## What is it?

Brightness Controller allows you to control Brightness of your **Primary and Secondary Display** with the help of `xrandr` in Linux. It is a software based dimmer. The controller is created using Python, which in the back end calls `os.system` commands to execute system commands.

## What good is it?

It allows you to control the brightness of your monitor to a better extent. For example, my laptop's monitor brightness can be controlled using hardware keys at discrete values, such as 20%, 40%, 60%, ... 100%. Brightness Controller allows you to change the brightness to a better degree of control, ranging from 1% to 100%! It should be mentioned that it changes the present brightness value set via hardware control of your monitor. For example, if you set your Monitor's brightness to 50% using hardware buttons, then that will be the 100% value in Brightness controller. 

## Installation 

There are various options available.
The Debian, RPM and Ubuntu Software Center methods are for easy installing, whereas the bash script and the source method gives you a geeky feeling and the latest version of Brightnes Controller.

- [Ubuntu Software Center](https://apps.ubuntu.com/cat/applications/brightness-controller/)
- [Debian](https://dl-web.dropbox.com/get/brightness_1.0_all.deb?w=AACghuGBHKdubl0-3npV9RphiYyiMhNGyy-vA5ZBeadXlQ&dl=1)
- [Experimental RPM](https://dl-web.dropbox.com/get/brightness-1.0-2.noarch.rpm?w=AABT4bXl_KuZxAVrMx2xEduZuk1GSjGR5t_9dNTsyEDFSA&dl=1)
- [Good old bash script](https://gist.github.com/lordamit/6134441)

<h3>Instructions for compiling from the source code.</h3>

- Download the [Latest version](https://github.com/lordamit/Brightness/archive/master.zip) to your home folder.
- Extract it.
- Open the `src/brightness.desktop` with your favourite text editor.
- Replace `path/to...` with the original path of `brightness.py` in line 4 and `brightness.svg` in line 7.
- Now `brightness.desktop` looks like 'Brightness Controller' and should have an icon.
- Double-click Brightness Controller and the app should run.

## What are the requirements / dependencies / things I need to run it?

Three dependencies only.

1. Python - Linux should have it by default

2. Python WxWidgets
```bash
$ sudo apt-get install python-wxgtk2.8
```
3. `xrandr` - that's what the program uses in the backend to control the brightness of your monitor!

## It doesn't detect my displays properly

Kindly make an issue in the GitHub project and submit the output of this command:
```bash
$ xrandr -q
```

## I have more than two displays, and this program only shows two. What's happening?

In a word, *jealousy*. Because I never had more than two displays simultaneously, I decided to give support for up to two displays only. So no, it can not support your third (or fourth, or fifth...) display.

## Screenshot

![Brightness Controller screenshot](http://farm3.staticflickr.com/2829/9290314985_725f94cb98.jpg)

# Misc

Random questions that might show up here are answered here in advance.

## The coding style is not exactly... Python-like
 
Because it is my first Python code that exceeds 10 lines. I have not used Python before, but I decided to use it for this project for no particular reason.

## Why is it here?

I wrote it because I could not find any other similar software available **in Linux** that provides an easy to use UI for changing brightness. There are still room for improvement, specially in the coding style. I hope due to its open source nature, people will come forward and will help it become a better brightness controller.

## Help! It broke my computer!

*Erm, that's not exactly supposed to happen. Still, use at your own risk. I won't allow myself to be held responsible even if it turns your display into a black hole, sucks you in and kills you in the process.  
But still, let me know if something goes wrong by reporting it in the issues section.*

On a more serious note, Brightness Controller does nothing that can break your computer. It simply provides a graphical user interface you can use with a mouse to control brightness easily. It does not execute any command or does not do anything to change your system. So, feel free to use it. :)
