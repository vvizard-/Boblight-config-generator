#!/usr/bin/python

# Number of LED's per side
top = 71
left = 41
bottom = 70
right = 41

# Name of this device
device = "Teensy"

# Color scan depth in percent (default: 15)
depth = 20 

#======================= DO NOT EDIT BELOW THIS LINE ===========================
lightCount = 1
vscan = 0.0
hscan = 0.0

topScanSpan = float(100)/float(top)
leftScanSpan = float(100)/float(left)
bottomScanSpan = float(100)/float(bottom)
rightScanSpan = float(100)/float(right)

#============================== PRINT LIGHTS ===================================
for num in range(1,top+1):
	if num == 1: scan = 0

	print "[light]"
	print "name top%s" % num 
	print "color red %s %d" % (device, lightCount)
	lightCount += 1
	print "color green %s %d" % (device, lightCount)
	lightCount += 1
	print "color blue %s %d" % (device, lightCount)
	lightCount += 1
	print "hscan %.1f %.1f" % (scan, scan+topScanSpan)
	print "vscan %.1f %.1f" % (0, float(depth))
	print
	scan = scan + topScanSpan

for num in range(1,right+1):
	if num == 1: scan = 0
	print "[light]"
	print "name right%s" % num 
	print "color red %s %d" % (device, lightCount)
	lightCount += 1
	print "color green %s %d" % (device, lightCount)
	lightCount += 1
	print "color blue %s %d" % (device, lightCount)
	lightCount += 1
	print "hscan %.1f %.1f" % (100-float(depth), 100)
	print "vscan %.1f %.1f" % (scan, scan+rightScanSpan)
	print
	scan = scan + rightScanSpan

for num in range(1,bottom+1):
	if num == 1: scan = 100
	print "[light]"
	print "name bottom%s" % num 
	print "color red %s %d" % (device, lightCount)
	lightCount += 1
	print "color green %s %d" % (device, lightCount)
	lightCount += 1
	print "color blue %s %d" % (device, lightCount)
	lightCount += 1
	print "hscan %.1f %.1f" % (scan-bottomScanSpan, scan)
	print "vscan %.1f %.1f" % (100-float(depth), 100)
	print
	scan = scan - bottomScanSpan

for num in range(1,left+1):
	if num == 1: scan = 100
	print "[light]"
	print "name left%s" % num 
	print "color red %s %d" % (device, lightCount)
	lightCount += 1
	print "color green %s %d" % (device, lightCount)
	lightCount += 1
	print "color blue %s %d" % (device, lightCount)
	lightCount += 1
	print "hscan %.1f %.1f" % (0.0, float(depth))
	print "vscan %.1f %.1f" % (scan-leftScanSpan, scan)
	print
	scan = scan - leftScanSpan




