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

Donate me if you want:

[![NSPanel Pro](doc/assets/P_1.png)](https://www.paypal.com/paypalme/seaky77/1EUR)
[![NSPanel Pro](doc/assets/P_5.png)](https://www.paypal.com/paypalme/seaky77/5EUR)
[![NSPanel Pro](doc/assets/P_10.png)](https://www.paypal.com/paypalme/seaky77/10EUR)

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
Actual plan is to have a release in every Quarter.

### v2.2.0 (2024-Q3)
- ?

### v2.1.0 (2024-04-01)
It is now finished under testing...

#### new features (see updated manual [Manual 2.x version](#manual-2x-version) )
- [Touch gestures on dark screen](#wake-on-gesture-v21) (https://github.com/seaky/nspanel_pro_tools_apk/issues/27)
- [Wake up from Screen Saver](#wake-from-screensaver-v21) (https://github.com/seaky/nspanel_pro_tools_apk/issues/52)
- [Prevent turn off / Dim screen](#prevent-turn-off-v21) (https://github.com/seaky/nspanel_pro_tools_apk/issues/40)
- [Different Screen-on at weekdays and weekends](#screen-on-begin-on-weekdays-v21) (https://github.com/seaky/nspanel_pro_tools_apk/issues/36)
- [Switch to selected App](#switch-to-app) (https://github.com/seaky/nspanel_pro_tools_apk/issues/46)
- [Home on gesture](#home-on-gesture-v21)
- [MQTT Native Integration](#mqtt-category-v21) (https://github.com/seaky/nspanel_pro_tools_apk/issues/51,https://github.com/seaky/nspanel_pro_tools_apk/issues/10)
- [MQTT Home Assistant integration](#ha-integration) (https://github.com/seaky/nspanel_pro_tools_apk/issues/21)
- [Audio feedback](#audio-feedback-v21)

#### bugfixes
- Brightness between BELOW and ABOVE is not handled properly (https://github.com/seaky/nspanel_pro_tools_apk/issues/55)


### v2.0.1 (2024-01-28)
#### bugfixes
- Restart app after reboot does not work (https://github.com/seaky/nspanel_pro_tools_apk/issues/49)
- Display sleep time UI refresh bug (https://github.com/seaky/nspanel_pro_tools_apk/
issues/47)
- Misleading screen-on begin time calculation (https://github.com/seaky/nspanel_pro_tools_apk/issues/44)

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

> [!NOTE]
> If the version number is marked, then it is only valid for that version.

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

![NSPanel Pro](doc/assets/app/display/sc1.png)

#### Wake-on-wave
Wake up the device by hand wave. 
> [!NOTE]
> Before turning it on, set up the sensor parameters on the sensor tab.
#### Wake on touch (v2.0)
Wake up the device by a simple screen touch or tap.

#### Wake on gesture (v2.1)
Wake up the device by touch gesture. Multiple gestures can be selected the behaviour will be the same it will wakes up the device.

![NSPanel Pro](doc/assets/app/display/sc1_1.png)

#### Wake from ScreenSaver (v2.1)
Dismiss the ScreenSaver if it is active. Only works if wake-on-wave is enabled.

**** 
### brightness category
****
Category for all brightness related functions.

![NSPanel Pro](doc/assets/app/display/sc2.png)

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
Category for all (lcd) screen related functions.

![NSPanel Pro](doc/assets/app/display/sc3.png)

#### Display sleep
Set system level display sleep time. After the prescribed interval the screen will be turned off if another function does not override it, for example: Prevent turn off or Screen begin

#### Prevent turn off (v2.1)
Prevents the screen from completly turning off while retaining the dim feature

#### Screen-on time swicth
During a predefinied period it turns on the screen and it remains on untile the end of the interval.

#### Screen-on begin (v2.0)
The time when the screen-on begins. 
> [!TIP]
> If the Begin time 00:00 and End time is also 00:00 the feature is.

#### Screen-on end (v2.0)
The time when the screen-on ends.

#### Screen-on begin on weekdays (v2.1)
The time when the screen-on begins on weekdays. 

> [!TIP]
> If both begin time and end time is "00:00" it will be disabled or ignored
> If the weekend is disabled, weekdays will jump over weekends. So after friday the monday will be scheduled.
> If the weekend is enabled, after friday the weekend intervall will take effect.

#### Screen-on end on weekdays (v2.1)
The time when the screen-on ends.

#### Screen-on begin on weekends (v2.1)
The time when the screen-on begins at weekends

> [!TIP]
> If both begin time and end time is "00:00" it will be disabled or ignored
> If the weekdays is disabled, weekends will jump over weekdays. So after sunday the next saturday will be scheduled.
> If the weekdays is enabled, after sunday the weekdays intervall will take effect.

#### Screen-on end on weekends (v2.1)
The time when the screen-on ends.

![NSPanel Pro](doc/assets/app/display/sc4.png)

## sensor tab
****
### sensor proximity category
****
Category for proximity sensor related functions.

![NSPanel Pro](doc/assets/app/sensor/sc5.png)

#### Proximity sensor
Proximity sensor live value shows actual sensor value and shows the trigger when it is activated.
#### Proximity sensor trigger threshold
Above the value the trigger event will be create

****
### sensor light category
****
Category for proximity sensor related functions.

![NSPanel Pro](doc/assets/app/sensor/sc6.png)

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

![NSPanel Pro](doc/assets/app/tools/sc7.png)
#### Launch App after reboot
Launch selected application after device reboot
#### Wait for WIFI
Start selected application after WIFI connection is established
#### Switch to app
Switch to selected application

### other
****

![NSPanel Pro](doc/assets/app/tools/sc8.png)

#### Home on gesture (v2.1)
The selected gesture will switch to this application.

## integration tab (v2.1)
****

![NSPanel Pro](doc/assets/app/integration/sc10.png)
### mqtt category (v2.1)
****
Category for MQTT and HomeAssistant related settings

#### State
The current state of the connection.
#### Setup
Setup MQTT Connection
#### Enabled
If turned off the connection will be dissconnected

#### MQTT Setup
![NSPanel Pro](doc/assets/app/integration/sc11.png)
#### Enabled
If turned off the connection will be dissconnected. Turn on only if you setup connection parameters correctly
#### Connection status
The current state of the connection.
#### Publish events
You can select the messages you want to publish on this channel. Only publish those that you really need.
#### Host
MQTT server host name only non SSL is available in v2.1
#### Port
MQTT server port only non SSL is available in v2.1
#### Username
Configured username
#### Password
Configured password
#### HA Integration
Enables MQTT Integration based integration, events and diagnostics are implemented.

![NSPanel Pro](doc/assets/app/integration/sc13.png)

#### HA Integration
If enabled it sends configuration message to the proper topics
#### Device Id
Unique device id
#### Topic prefix
Topic prefix usually homeassistant the default

## settings tab
****
### general category
****

![NSPanel Pro](doc/assets/app/settings/sc14.png)
### Audio feedback (v2.1)
Plays audio on certain events such as identified touch gestures on in order to provide audio-based feedback.
### Resume on boot
Autostart NSPanelTools app after device restart
#### Reboot device
This option reboots the device
#### Hostname
Changes the device hostname
### debug category
****

![NSPanel Pro](doc/assets/app/settings/sc15.png)
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
