import sys, os, string
from support import *
from files import * 	#remove after moving last function

import time

# from reports import *
# from support import *
# from update import *

def updatemenu():
	while 1:
		print "1 Print Month \t2 Add Bill \t3 Add Payment \t4 Bill Stats\t5 Pay Stats"
		choice = raw_input(pt)
		if choice == '1':printit()
		if choice == '2':addbill()
		if choice == '3':addpayment()
		if choice == '4':billstats()
		if choice == '5':paystats()
		else:break

def addbill():
	#f = open ('debit_new.tab', 'r')
	f = open ('debit.tab', 'r')
	#mypar = f.readlines()
	#par2 = string.split(mypar(1))
	#print par2
	#for vary in mypar:
	#print mypar
	#for i, v in enumerate(mypar):
 	#	print i, v
	#for items in mypar:
	#	print mypar(items)
	#print mypar
	billline = f.readline()
	it = {} 
	while billline  <> '':
		new = billline.split()
		it = it + new
		billline = f.readline()
	#print 'addbill'
	print it 


def addpayment():
	print 'addbill'


def billstats():
	pass
def paystats():
	pass

def add_credit():
	fmt = '\n%s\t%s\t%s\t%s\t%s\t%s'
	f = open('credit.tab', 'a')	
	print 'Ref #'
	ref = raw_input(pt)
	yr = g_year()
	mo = g_month()
	day = g_day()
	rm = g_roomate()
	print 'Amt:'
	amt = raw_input(pt)
	it = (ref, yr,mo,day, rm, amt)
	them  = ('Ref', 'Year', 'Month', 'Day', 'Roomate', 'Amt')
	print fmt % them
	for x in (it):
		print '%s\t' % x,
	value = fmt % it
	print
	print '0:OK\t CR:NO'
	go = raw_input(pt)
	#print value
	if go == '0':
		f.write(value)
		print 'Added', value
	f.close()

def add_debit():
	fmt = '%s\t%s\t%s\t%s\t%s'
	f = open('debit.tab', 'a')	
	#f.write('\n')
	print 'Ref #'
	#ref = raw_input(pt)
	yr = g_year()
	mo = g_month()
	day = g_day()
	biller = g_biller()
	print 'Amt:'
	amt = raw_input(pt)
	it = (yr, mo, day, amt, biller)
	them  = ('Ref', 'Year', 'Month', 'Amt')
	value = fmt % it
	f.write(value)
	new = '1'
	while new <> '':
		new = g_roomate()
		if new <> '':
			rm = '\t%s' % new
			f.write(rm)
	#f.write('\n')
	f.close()

#updatemenu()	


def fileinfo():
	debit_fs = debit_f()
	credit_fs = credit_f()
	cr =  len(credit_fs)
	db =  len(debit_fs)
# 	print time.asctime()
# 	print  time.ctime()
# 	print time.gmtime()
# 	print time.localtime()
	x =  '\n' + str(cr) + '\t'+ str(db) + '\t'
	z = str(time.localtime())
	
	w = ''
# 	for items in z:
# 		w = w + str(items)
# 	print w
# 	print '%s %s %s %s %s %s %s %s %s %s %s' % time.localtime()
# 	print time.strftime('%Y/%m/%d %H:%M:%S',x)
	d = open('updates.dat', 'r')
	e = d.readlines()
# 	for line in e:
# 		f = line.split()
# 		print f,
# 		print len(line.split()) #'%s %s %s %s %s %s %s %s %s %s %s' % f
		
# 	d.close()
# 	print x
# 	pRint len(d)
# 	d.seek(5,2)
# 	print '-', d.readline()
# 	for line in d:
# 		print ':',line,
# 	d.close()
	d = open('updates.dat','a')
	d.write(x)
# 	print d
	d.close()
	print
