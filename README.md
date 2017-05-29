# Brightness Controller

<svg height='20' width='80' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns='http://www.w3.org/2000/svg'>
  <linearGradient id='a' x2='0' y2='100%'>
    <stop offset='0' stop-color='#fff' stop-opacity='.7'></stop>
    <stop offset='.1' stop-color='#aaa' stop-opacity='.1'></stop>
    <stop offset='1' stop-opacity='.5'></stop>
  </linearGradient>
  <rect fill='#555' height='20' rx='3' width='80'></rect>
  <rect fill='#4c1' height='20' rx='3' width='43' x='37'></rect>
  <path d='M37 0h4v20h-4z' fill='#4c1'></path>
  <rect fill='url(#a)' height='20' rx='3' width='80'></rect>
  <g fill='#fff' font-family='DejaVu Sans,Verdana,Geneva,sans-serif' font-size='11' text-anchor='middle'>
    <a id='link' target='_new' xlink:href='https://github.com/lordamit/Brightness'>
      <text fill-opacity='.3' fill='#010101' x='19.5' y='15'>star</text>
      <text fill='#fff' x='19.5' y='14'>star</text>
    </a>
    <a id='count-link' target='_new' xlink:href='https://github.com/lordamit/Brightness/stargazers'>
      <text fill-opacity='.3' fill='#010101' id='count' x='57.5' y='15'>128</text>
      <text fill='#fff' id='count' x='57.5' y='14'>128</text>
    </a>
  </g>
</svg>

This is version 2 of Brightness Controller. Please note that it is compatible with python2 only. It supports an arbitary number of displays!

If you like this, do not forget to give us a Star!

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
