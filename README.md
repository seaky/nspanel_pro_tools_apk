# NSPanel Pro Tools Application
## Version history

### v1.x (planned features)
- toggle proximity and touch wakeup feature independently
- ?

### v1.0
- first production release
- support wakeup on proximity sensor trigger
- support wakeup on touch
- support autolaunch application
- new dark design
- renamed original "ProximityTool" app to "NSPanelTools" app
- moved to new repositroy

### v0.8-alpha (ProximityTool)
- first release
- support wakeup on proximity sensor trigger

## Sonoff NSPanel Pro

Sonoff NSPanel Pro is a smart home control panel which based on Android 8.1 Oreo (AOSP) system.

After gain ADB access custom applications can be installed onto this unit. See (https://blakadder.com/nspanel-pro-sideload/)

![Drag Racing](doc/assets/nspanel-pro.png)

https://itead.cc/product/sonoff-nspanel-pro-smart-home-control-panel/

## Manual for v1.0

## ADB Access
https://blakadder.com/nspanel-pro-sideload/

> **Warning**
> Consequence of gaining ADB access the device won't get any official update and the device will be marked as rooted permanently.
 
## Install
Unable to install third-part applications without gain ADB access.

- Download apk
- adb install <filename>.apk

## Features
### wakeup
This app will turn on the display.  
In order to make it turn off when not in use, you may change the display sleep settings (`Settings -> Display -> Advanced -> Sleep`).

Unfortunatelly this AOSP build does not support wakeup device which causes if official app is not running the device will go to deepsleep.
Due to the lack of power button, just a hard reset (unplug) can wake up the device.

Wake up on wave and touch feature are implemented in the app btw that was the original purpose of the app.
* activate toggle
  * activates a background service which runs even if tha app is killed
  * toggle state is presisted
  * background service activates itself is the screen goes off
  * currently this option observes the proximity sensor gestures (current unable to disable it. see next version)
* resume on boot
  * activates the background service automatically without any user interaction
  * after reboot the app may not visible in app switcher
* wake on touch
  * panel touch will also wakes up the device
  * can be turned off

### launch
This feature enables to run an application as a default app such as HomeAsistant.
* select
  * select installed application if launch on startup activated the app selection is disabled
  * always test it with test button before activates 
* launch on startup 
  * runs the selected app after reboot
* test button
  * launch the selected app
