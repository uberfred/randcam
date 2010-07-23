#!/usr/bin/python
import sane

def grab_image(cam):
	cam.mode = 'color'
	cam.start()
	return cam.snap()

sane.init()
webcam = sane.open('v4l:/dev/video0')
ones = 0
zeroes = 0
bstring = ''
for i in range(100):
	img = grab_image(webcam)
	data = list(img.getdata())
	for value in data:
		if value[2]%2 == 0:
			zeroes += 1
			bstring += '0'
		else:
			ones += 1
			bstring += '1'
		if len(bstring) == 32:
			print int(bstring, 2)
			bstring = ''
webcam.close()
sane.exit()

