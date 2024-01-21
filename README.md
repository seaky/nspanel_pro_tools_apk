# NSPanel Pro Tools Application

This application is a custom developed apk which allows devices running on the 
- Smatek T6E variants
  - Sonoff NSPanel Pro
  - Zemismart T6E
  - Avatto T6E
  - Tuya T6E
- or similar architecture 
  
to leverage certain features such as proximity sensor, light sensor, and Home Assistant integration.

Application mainly tested on NSPanel Pro but may works on other devices.

## Table of contents

- [App version history](#app-version-history)
- [NSPanel Pro device info](#sonoff-nspanel-pro)
- [NSPanel Pro device rooting and sideload](#device-rooting-and-sideload)
- [Install custom launcher](#install-custom-launcher)
- [Install custom webview](#install-custom-webview)
- [Install app](#install-app)
- [Manual for v2.x](#manual-2x-version)
- [Manual for v1.x](#manual-1x-version)


## App Version history

### v2.x (2024-Q1)
- HA/HASS integration
- Gesture based HASS events
- Gesture based wake-up

### v2.0 (2024-01-21)
#### new features (see manual [Manual 2.x version](#manual-2x-version) )
- code has been fully redesigned (see [Backward compatibility](#backward-compatibility))
  - a lot easier to add new capabilites
  - enables to add internal event listeners and therby make MQTT/HASS integration 
- new Preference based UI
  - a lot easier to add new UI elemens. Due to the small screen a scrollable view is much more convenient or usable
- screen always on/off feature (https://github.com/seaky/nspanel_pro_tools_apk/issues/5, https://github.com/seaky/nspanel_pro_tools_apk/issues/14)
- reboot device from app (https://github.com/seaky/nspanel_pro_tools_apk/issues/6)
- change hostname from app (https://github.com/seaky/nspanel_pro_tools_apk/issues/8)
- system display sleep time setting from app
- predefinied brightness scenarios based on lightsensor trigger events
- now automatically launched apps can wait for established wifi connection

#### bugfixes
- touch-screen reader memoryleak fixed
- request exclude app from battery optimization, helps to prevent app kill by system
- wake-on-wave can be turned off

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

![NSPanel Pro](doc/assets/nspanel-pro-small.png)

Device info:
https://itead.cc/product/sonoff-nspanel-pro-smart-home-control-panel/

## Device rooting and sideload

### Gaining ADB access

- Download [ADB drivers](https://developer.android.com/studio/run/win-usb) and install.
- Download [Android platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) unzip it to a folder.
- Get device ip address (if you dont know what is ip-address and dont know how to find it do not root the device, you will mess the device up)
> [!TIP]
> You'll find the ip address within Sonoff app settings or in your router dhcp clients view

- Registrate your device with the eWeLink app just follow the device registration process
- To gain ADB access tap on the device id quickly multiple times to enable developer mode
- after you consider the adb agreement you will able to acces device through the adb command
> [!WARNING]
> If you accept the agreement you won't be able to revert it.Your device will be rooted forever. You wont get any new future updates forever. 

> [!TIP]
> With my [RootTool](https://github.com/seaky/nspanel_pro_roottool_apk) app you can update your device

- connect to device with adb

start adb listen:
```
adb tcpip 5555
```

list devices
```
adb devices -l
```

connect device
```
adb connect <ip-address>
```
- Install a custom Launcher (see [Install Launcher](#install-custom-launcher))

### Usefull ADB commands

connect device
```
adb connect <ip-address>
```

list devices
```
adb devices -l
```

press home button
```
adb shell input keyevent 3
```

press power button
```
adb shell input keyevent 26
```

show notifications
```
adb shell cmd statusbar expand-notifications
```

install app
```
adb install <apk>
```

## Install custom launcher

To handle the device more easily, you need to install a custom launcher.

Download [UltraSmall Launcher](https://drive.google.com/file/d/1iW6vWaGAjNTUO_Cs-2r-18j_468mU3oK/view?usp=drive_link)
- install and simulate home key press
- select set "Launcher" as default

## Install custom webview

If you want to use Home Assistant companion app you must update factory provided webview component.

> [!TIP]
> You dont need to instal Xposed root firmware as blackadder mentioned.

Just simple download com.android.webview_108.0.5359.128.apk or any new version which supporst arm64-v8, armeabi-v7a on firmware above 1.5 **Lineageos version** can be installed!

[WebView 108 for firmware >=1.5 ](https://drive.google.com/file/d/1fAO5daUOnUtNlg10KSUmz5feRImZaU9M/view?usp=drive_link)

Under frimware version 1.5 you have two options, update firmware by my frimware updater or simply install this resigned version below.

[WebView 108 for firmware <1.5 ](https://drive.google.com/file/d/1SL7e6uCesPOvakz_LmD829_IFYwK09kC/view?usp=drive_link)

install webview apk
```
adb install -r <webview>
```


## Install App

- Download apk from releases section
- adb install -r [filename.apk]

## Manual 2.x version
### backward compatibility
version 2.x supports all v1.x features. Except the automatic brightness change which was experimental and replaced by light-level triggered brightness control see [Brightness category]
(#brightness-category).
> [!NOTE]
> All configuration for v1.x is obsolete in 2.x therefore 2.x app must be reconfigured before use.

### main switch
Main switch allows for the complete disabling of the application's functions. Controls the background activities. Purpose of being able to disable the whole app without uninstall.
* active toggle
  * activates a background service which runs even if the app is "killed" from app-switcher
  * off state turns all app features off including "launch app after reboot"

## display tab
This tab groups all screen or display related configurations and features. Such as how and when to turn on and off or how bright is it. etc

****
### wakeup category
****
Category for all wake-up related functions.

Unfortunatelly this [AOSP 8.1](https://source.android.com/) build does not support wakeup device which causes that if official app is not running the device will go to deepsleep.
Due to the lack of power button, just a hard reset (unplug) can wake up the device.

#### Wake-on-wave
Wake up the device by hand wave. 
> [!NOTE]
> Before turning it on, set up the sensor parameters on the sensor tab.
#### Wake on touch
Wake up the device by a simple screen touch or tap.

**** 
### brightness category
****
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
****
### screen category
****
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

****
### sensor proximity category
****
Category for proximity sensor related functions.
#### Proximity sensor
Proximity sensor live value shows actual sensor value and shows the trigger when it is activated.
#### Proximity sensor trigger threshold
Above the value the trigger event will be create

****
### sensor light category
****
Category for proximity sensor related functions.
#### Light sensor
Light sensor live value shows actual sensor value and shows the trigger when it is activated.
#### Light sensor trigger below
Below the value the trigger event will be created
#### Light sensor trigger above
Above the value the trigger event will be created

## tools tab
****
### autostart category
****
Autostart or launch other app after device restart
#### Launch App after reboot
Launch selected application after device reboot
#### Wait for WIFI
Start selected application after WIFI connection is established

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
