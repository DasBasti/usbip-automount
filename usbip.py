import subprocess
from time import sleep

devices = ["usbid=05dc:b051"]

def bind2usbip(id, dev):
	print "look for", dev, "@", id
	#check for local binding of usb device
	l = subprocess.Popen(['usbip', 'list', '-r', '127.0.0.1'], stdout=subprocess.PIPE)
	out = l.communicate()
	if dev in out[0]:
		#print "found. skipping"
		pass
	else:
		print "bind USB device @ ", id
		subprocess.Popen(['usbip', 'bind', '-b', id])
		sleep(1)
		subprocess.Popen(['usbip', 'attach', '-r', '127.0.0.1', '-b', id])
		sleep(1)
		subprocess.Popen(['usbip', 'detach', '-p', '0'])	
		sleep(1)

while(1):
	print "scan..."

	p = subprocess.Popen(['usbip', 'list', '-p',  '-l'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()

	for dev in out.split('\n'):
		dev = dev.split('#')
		if len(dev) == 3 and dev[1] in devices:
			print dev
			bind2usbip(dev[0].split('=')[1], dev[1].split('=')[1])
	
	sleep(2) #wait 2 sec
