from normalDate import ND 
import time 

print "time:   \t", time.time()
print "asctime:\t", time.asctime()
print "clock:  \t", time.clock()
print "ctime:  \t", time.ctime()
print "gmtime: \t", time.gmtime()
print "strftime:\t", time.strftime('%a %b %d %H:%M%S %Y')
today = ND()
yes = today - 28 
print today, yes
print yes -1
print "US", today.formatUS()
print "add", today.add(-5)
#z = today - 20050310
