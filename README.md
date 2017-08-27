# Brightness Controller

This is version 2 of Brightness Controller. Please note that it is compatible with python2 only. It supports an arbitrary number of displays!

If you like this, do not forget to give us a Star!  [![GitHub stars](https://img.shields.io/github/stars/lordamit/brightness.svg?style=flat-square)](https://github.com/lordamit/brightness/stargazers) People already did!

![](img/BrightnessController.gif)

## Installation via PPA

Thanks to package maintainer @apandada1, we have PPA repository For Ubuntu and likewise users:

```bash
sudo add-apt-repository ppa:apandada1/brightness-controller
sudo apt-get update
sudo apt-get install brightness-controller
```

## Manual Installation
First, install pyside.

```bash
sudo apt-get install python-pyside
```
Somtimes it is not enough to install and integrate pyside, so you might also try installing pyside using pip.

```bash
pip install pyside
```

Next, download the latest zip file from [here](https://github.com/lordamit/Brightness/archive/master.zip).

Extract it and open a terminal. Change directory to the `Brightness` folder. Next type this command:

```bash
python src/init.py
```

Achean also created a detailed tutorial on how to install it in Debian based on his experience. You can find it [here](https://github.com/LordAmit/Brightness/issues/98#event-1218811468).

## Features

The following features are implemented:

1. Brightness Control
1. Saving color profile
1. Loading color profile


We are working on the following features:

1. Auto-loading of color and brightness settings
2. Checking for update

It should be mentioned that through color profile Red, Green and Blue color ratios are changed in the screen.

## Dependencies
There are several dependencies:

1. python-pyside
2. xrandr support in your system
3. python2

## Bugs

Please test v2. Reporting bugs is appreciated.

## Can I have just brightness sliders - For Four displays?
We got you covered! Try version 1.2.3/simpler version of Brightness Controller.
![](img/brightness-controller-1.png)

To install, simply do this:

```bash
sudo add-apt-repository ppa:apandada1/brightness-controller
sudo apt-get update
sudo apt-get install brightness-controller-simple
```
Further details are available [here](http://lordamit.github.io/Brightness/)
