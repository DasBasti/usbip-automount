#!/bin/bash
modprobe usbip_core
modprobe usbip_host
modprobe vhci_hcd
python usb.py
