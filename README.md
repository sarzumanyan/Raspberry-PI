# Wi-Fi bridge
Follow this [link]((https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/)https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/)

### Configuring Raspberry PI3 B as wi-fi bridge, meaning it takes internet through ethernet and shares it as wi-fi.
After connecting RPI to ethernet and power supply, restart dnsmasq and hostapd services with commands  `sudo systemctl restart hostapd` and  `sudo systemctl restart dnsmasq`, check the status with `sudo systemctl status hostapd` and `sudo systemctl status dnsmasq` in case they're not configured to autorun.
