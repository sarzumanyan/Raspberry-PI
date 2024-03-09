# Wi-Fi bridge
### 1. Update your Raspberry Pi:
`sudo apt upgrade`
### 2. Install hostapd and dnsmasq:
`sudo apt install hostapd dnsmasq`
### 3. Configure hostapd:
Edit the hostapd configuration file:
`sudo vim /etc/hostapd/hostapd.conf`
Add the following lines to the file:
```bash
interface=wlan0
driver=nl80211
ssid=YourSSID
hw_mode=g
channel=6
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
```
Replace YourSSID with the desired name for your Wi-Fi network.
### 4. Configure dnsmasq:
`sudo vim /etc/dnsmasq.conf`
Add these lines
```bash
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```
### 5. Enable IP forwarding:
`sudo vim /etc/sysctl.conf`
Uncomment the line 
`net.ipv4.ip_forward=1`
Save the file and type command `sudo sysctl -p`
### 6. Restart services
`sudo service hostapd restart
`
`
sudo service dnsmasq restart
`
