# Brightness Controller

This is version 2 of Brightness Controller (beta). It is completely stable and we are working on some more features to be integrated before release.

## Installation
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
2. Reversing Brightness control for primary and secondary monitor in case you want to flip the controls.
1. Saving color profile
2. Loading color profile

We are working on the following features:

1. Auto-loading of color and brightness settings
2. Checking for update

It should be mentioned that through color profile Red, Green and Blue color ratios are changed in the screen.

## Dependencies
There are several dependencies:

1. python-pyside
2. xrandr support in your system

## Bugs

Please test v2. Reporting bugs is appreciated.

## Version 1

You can find details and installers of the publicly released Brightness Controller version 1.2.2 from [here](http://lordamit.github.io/Brightness/)
