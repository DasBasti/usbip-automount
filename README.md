# usbip-automount
Automount devices with usbip according to their usbid.

## List of devices
To add a device to the list of devices to automatically load, add the usbid to the devices variable in the usbip.py
    
    devices = ["usbid=05dc:b051"]
  
## Run the automounter
execute usb-automount.sh as root to run the script. Don't forget to have usbipd running.
    
    usbipd -D
    ./usbip-automount.sh
