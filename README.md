# Wi-Fi bridge
### Configuring Raspberry PI3 B as wi-fi bridge, meaning it takes internet through ethernet and shares it as wi-fi.
Follow this [link](https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/)

# Equipments
### 1. Raspberry Pi model with built-in WiFi capabilities
### 2. Micro SD Card 
To install and run the operating system (OS) and necessary software. An 8GB or larger card is usually sufficient.
### 3. Power Supply
Make sure you have a suitable power adapter for your Raspberry Pi.
### 4. Ethernet Cable
This will be used to connect the Raspberry Pi to your primary router or modem.   

After configuring RPI as wi-fi bridge and connecting it to ethernet and power supply, restart dnsmasq and hostapd services with commands  `sudo systemctl restart hostapd` and  `sudo systemctl restart dnsmasq`, check the status with `sudo systemctl status hostapd` and `sudo systemctl status dnsmasq` in case they're not configured to autorun.   

If you want to restrict specific mac address from your wi-fi bridge, follow this steps.
1. `sudo vim /etc/hostapd/hostapd.conf`
2. Add the following line to the configuration file for each MAC address you want to block:
   `deny_mac_file=/etc/hostapd/deny_mac`
3. Create a file /etc/hostapd/deny_mac and add MAC addresses line by line that you want to block.
   `sudo vim /etc/hostapd/deny_mac`
   Add MAC addresses in the format: 00:11:22:33:44:55, each in new line
4. `sudo systemctl restart hostapd`
These method should help you restrict access to your Raspberry Pi Wi-Fi bridge based on specific MAC addresses.
