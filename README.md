# Brightness Controller

This is version 2.4 of Brightness Controller for Linux. It supports an arbitrary number of displays and also allows changing the color temperature across displays!

If you like this, do not forget to give us a Star! That's the only way we can estimate whether people are using it or not since we do not collect any data, at all. [![GitHub stars](https://img.shields.io/github/stars/lordamit/brightness.svg?style=flat-square)](https://github.com/lordamit/brightness/stargazers) People already did!

![](img/BrightnessController.gif)

## Installation via Pip

```sh
pip install brightness-controller-linux
```

Requires at least `python3.8` or above, and `PyQt5` or above. This installation method is fairly new, so will really appreciate if you let us know if everything is working as intended or not at your end. :)

## Installation via package managers

### Ubuntu and derivatives
Thanks to package maintainer @apandada1, we have [PPA](https://launchpad.net/~apandada1/+archive/ubuntu/brightness-controller/) repository For Ubuntu and likewise users:

```bash
sudo add-apt-repository ppa:apandada1/brightness-controller
sudo apt update
sudo apt install brightness-controller
```
### Arch and derivatives
Thanks to @yochananmarqos, a package for Arch and derivatives is available in the [AUR](https://aur.archlinux.org/packages/brightness-controller-git).

```bash
yay -S brightness-controller-git
```

## Dev Docs

Want to look at source code? Want to get started? Or want to download the source code and run it from there after building things yourself? Details are available right [here!](brightness-controller-linux/README.md)

## Features

The following features are implemented:

1. Brightness Control
1. Saving color profile
1. Loading color profile

Brightness Controller changes Red, Green and Blue color ratios  in the screen through color profile at software level using `xrandr`.

We might implement the following features in the future:

1. Rewriting GUI to integrate both Brightness Controller simple and normal
2. Auto-loading of color and brightness settings based on profile
3. Checking for update

We work on this in our spare time, so can not really promise when the v3 will be released. The current version available is stable and should work as intended.

## Bugs

Please test v2.4. Reporting bugs is appreciated.

### Wayland Bugs

Wayland does not provide a way to control the brightness of primary/external displays, so Brightness Controller won't work. It has been reported several times, and we are aware about it. Really, it is out of our hands.

### Brightness and/or Color set by Brightness Controller keeps getting reset

This is something [we keep getting notified about](https://github.com/LordAmit/Brightness/issues?q=reset), but do not consider as a bug. Here is why.

Brightness is a shared property that can be accessed by any number of applications e.g., Brightness Controller, Adaptive Brightness of Ubuntu/Linux, Night Shift, f.lux, and looks like Skype too). 

If any of the other, aggressive apps choose not to play nice and override existing brightness settings, Brightness Controller really can not gatekeep them away. Sure, we can think of a way that will result in Brightness Controller forcibly setting Brightness every 5 seconds or so, but that'd just result in a tug of war later on with an arbitrary number of applications trying to control Brightness (with unpredictable side effects). 

The simpler solution is just to disable the brightness resetting function of the aggressive app instead. 

## Can I have just brightness sliders - For Controlling Four displays at the same time?

Try version 1.2.8/simpler version of Brightness Controller. It was written in Python2, which has been deprecated, and some of its dependencies (e.g. WxGTK for Python2) are not available in recent versions of Ubuntu. It is only available for Ubuntu 20.04 and previous versions.

![](img/brightness-controller-1.png)

To install, simply do this:

```bash
sudo add-apt-repository ppa:apandada1/brightness-controller
sudo apt-get update
sudo apt-get install brightness-controller-simple
```

Further details are available [here](http://lordamit.github.io/Brightness/)

Please note that the simple version may not work properly in newer versions of Linux. Unfortunately we can not provide any more updates to the simple version.
