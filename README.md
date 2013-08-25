# Brightness Controller

Brightness Controller allows you to control Brightness of your **Primary and Secondary Display** with the help of `xrandr` in Linux. It is a software based dimmer. The controller is created using Python, which in the back end calls `os.system` commands to execute system commands.

It allows you to control the brightness of your monitor to a better extent. For example, my laptop's monitor brightness can be controlled using hardware keys at discrete values, such as 20%, 40%, 60%, ... 100%. Brightness Controller allows you to change the brightness to a better degree of control, ranging from 1% to 100%! It should be mentioned that it changes the present brightness value set via hardware control of your monitor. For example, if you set your Monitor's brightness to 50% using hardware buttons, then that will be the 100% value in Brightness controller.

## Installation 

There are mainly two options available. One is the easy installation method, involving installers designed for your distro, or a bash script based installer for all platforms. 

### Easy Installers

**For users:**
- [Ubuntu Software Center](https://apps.ubuntu.com/cat/applications/brightness-controller/)
- [Debian](https://dl.dropboxusercontent.com/u/84627545/brightness_1.0_all.deb)
- [Experimental RPM](https://dl.dropboxusercontent.com/u/84627545/brightness-1.0-2.noarch.rpm)
- [Script*](https://gist.github.com/lordamit/6134441/download)

Script gives you the latest changes made in the repository. You can execute it to even update your Brightness Controller.

**For developers:**
- [Git clone Bash script](https://gist.github.com/ZDroid/d2cfb2c26be2dd1a706c/download)

It should be mentioned that Script gives you the latest Brightness Controller.

## Dependencies

Three dependencies only.

1. **Python** - Linux should have it by default

2. **Python WxWidgets**
```bash
$ sudo apt-get install python-wxgtk2.8
```
3. **`xrandr`** - that's what the program uses in the backend to control the brightness of your monitor!

## Screenshots

Apperance is subject to change based on the theme you are using. These screenshots were taken in Linux Mint environment.

![Screenshot 1](https://raw.github.com/lordamit/Brightness/master/img/screenshot-1.png)

![Screenshot 2](https://raw.github.com/lordamit/Brightness/master/img/screenshot-2.png)

## FAQ

Random questions that might show up here are answered here in advance.

### Why is it here?

I wrote it because I could not find any other similar software available **in Linux** that provides an easy to use UI for changing brightness. There are still room for improvement, specially in the coding style. I hope due to its open source nature, people will come forward and will help it become a better brightness controller.

### It doesn't detect my displays properly

Kindly make an issue in the GitHub project and submit the output of this command:
```bash
$ xrandr -q
```

### I have more than two displays, but this program only shows two.

In a word, *jealousy*. Because I never had more than two displays simultaneously, I decided to give support for up to two displays only. So no, it can not support your third (or fourth, or fifth...) display.
