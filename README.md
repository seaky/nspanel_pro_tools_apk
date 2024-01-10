# NSPanel Pro Tools Application
## Version history

### v2.x (2024-Q1)
- HA/HASS integration
- Gesture based HASS events
- Gesture based wake-up

### v2.0 (2024-01-xx - under testing)
#### new features (see manual [Manual 2.x version](#manual-2x-version) )
- 
- code has been fully redesigned (easier to add new capabilites)
- new Preference based UI (easier to add new capabilites)
- screen allways on/off feature (https://github.com/seaky/nspanel_pro_tools_apk/issues/5, https://github.com/seaky/nspanel_pro_tools_apk/issues/14)
- reboot device (https://github.com/seaky/nspanel_pro_tools_apk/issues/6)
- change hostname (https://github.com/seaky/nspanel_pro_tools_apk/issues/8)
- display sleep time setting
- automatic brightness change based on lightsensor

#### bugfixes
- touch screen reader memoryleak fixed
- request exclude app from battery optimization, helps to prevent app kill by system

### v1.1 (2023-02-02)
- added light sensor feature
  - auto adjust brightness (experimental)
- added set brightness
  - adjust brightness
- optimized toggle operations  
  - preparation for future updates
  - main switch called "active" fully turn off all features of the app including app launch
  - all features can be set independently
- note switch defaults are still off (will be changed in 1.2)
- known bugs
  - trigger label sometimes permanently visible solution: navigate between menus
  - auto adjust brightness level can be very low
  - light menu icon is wrong
> **Note**
> Don't forget to activate main switch


### v1.0 (2023-01-22)
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

## Manual
## ADB Access
https://blakadder.com/nspanel-pro-sideload/

> **Note**
> In order to make the display turn off when not in use, you may change the display sleep settings (`Settings -> Display -> Advanced -> Sleep`).

> **Warning**
> Consequence of gaining ADB access the device won't get any official update and the device will be marked as rooted permanently.
 
## Install
Unable to install third-part applications without gain ADB access.

- Download apk
- adb install -r <filename>.apk

## Manual 2.x version
### main switch
Main switch allows for the complete disabling of the application's functions. Controls the background activities. Purpose of being able to disable the whole app without uninstall.
* active toggle
  * activates a background service which runs even if the app is "killed" from app-switcher
  * off state turns all app features off including launch app after reboot

## display tab
### wakeup category
Category for all wake-up related functions.

Unfortunatelly this [AOSP](https://source.android.com/) build does not support wakeup device which causes that if official app is not running the device will go to deepsleep.
Due to the lack of power button, just a hard reset (unplug) can wake up the device.

#### Wake-on-wave
Wake up the device by hand wave. 
> [!NOTE]
> Before turning it on, set up the sensor parameters on the sensor tab.

#### Wake on touch
Wake up the device by screen touch.

### brightness category
Category for all brightness related functions.
#### Brightness
Set system level display brightness. On certain cases it is used to set if no light change event is triggered.
#### Brightness on light-below switch
Set brightness to the given value if light-below event is triggered. 
> [!NOTE]
> Before turning it on, set up the sensor parameters on the sensor tab.

#### Brightness on light-below seekbar
Set brightness to the prescribed value.

#### Brightness on light-above switch
Set brightness to the given value if light-above event is triggered. 
> [!NOTE]
> Before turning it on, set up the sensor parameters on the sensor tab.

#### Brightness on light-above seekbar
Set brightness to the prescribed value.

### screen category
Category for all screen related functions.
#### Display sleep
Set system level display sleep time. 
#### Screen-on time swicth
During a predefinied period it turns on the screen and it remains on untile the end of the interval.
#### Screen-on begin
The time when the screen-on begins. 
> [!TIP]
> If the Begin time 00:00 and End time is also 00:00 the feature is.


#### Screen-on end
The time when the screen-on ends.

## sensor tab
### sensor proximity
Category for proximity sensor related functions.
#### Proximity sensor
Proximity sensor live value shows actual sensor value and shows the trigger when it is activated.
#### Proximity sensor trigger threshold
Above the value the trigger event will be create

### sensor light
Category for proximity sensor related functions.
#### Light sensor
Light sensor live value shows actual sensor value and shows the trigger when it is activated.
#### Light sensor trigger below
Below the value the trigger event will be created
#### Light sensor trigger above
Above the value the trigger event will be created

## settings tab
### Resume on boot
Autostart NSPanelTools app after device restart
#### Reboot device
This option reboots the device
#### Hostname
Changes the device hostname
#### Debug mode
Changes log level to debug
#### Verbos mode
Changes log level to verbose


## Manual 1.x version

### main switch
Switch controls the background activities. Purpose of being able to disable the whole app without uninstall.
* active toggle
  * activates a background service which runs even if the app is "killed" from app-switcher
  * off state turns all app features off including launch app after reboot

### wake up
Unfortunatelly this AOSP build does not support wakeup device which causes if official app is not running the device will go to deepsleep.
Due to the lack of power button, just a hard reset (unplug) can wake up the device.

Wake up on wave and touch feature are implemented in the app btw that was the original purpose of the app.
* wake-on-wave
  * toggle state is presisted
  * feature activates itself if the screen goes off
  * this option observes the proximity sensor gestures
* wake-on-touch
  * panel touch will also wakes up the device
  * feature activates itself if the screen goes off
  * this option observes the panel touch
* resume on boot
  * start the selected app after reboot automatically
  * feature activates itself after reboot
  * after the reboot this app may not visible in app switcher, nonetheless the background service will be active  

### launch
This feature enables to run an application as a default app such as HomeAsistant.
* select
  * select installed application if launch on startup activated the app selection is disabled
  * always test it with test button before activates 
* launch on startup 
  * runs the selected app after reboot
* test button
  * launch the selected app

### light
This feature enables utilization of light sensor. 
* set brightness
  * panel brightness can be changed manually
  * if auto adjust is turned on it shows the calculated brightness value in relatime
* auto adjust brightness
  * automatically calculates and adjust the brightness based on sensed lux 
