adb shell am broadcast -a com.android.settings.wifi.action.ADD_NETWORK --es ssid "WiFi_SSID" --es password "WiFi_Password"
adb shell svc wifi enable
adb shell svc wifi connect "WiFi_SSID" --password "WiFi_Password"
adb shell dumpsys wifi
