# Brightness Controller

This is version 2 of Brightness Controller. Please note that it is compatible with python2 only. It supports an arbitary number of displays!

If you like this, do not forget to give us a <!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/lordamit/brightness" data-icon="octicon-star" data-size="large" aria-label="Star lordamit/brightness on GitHub">Star</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>
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

## Version 1

You can find details and installers of the publicly released Brightness Controller version 1.2.2 from [here](http://lordamit.github.io/Brightness/)
