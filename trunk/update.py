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
	f = open ('debit.tab', 'r')
	billline = f.readline()
	it = {} 
	while billline  <> '':
		new = billline.split()
		it = it + new
		billline = f.readline()
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
	amt = g_amt() 
	it = (ref, yr,mo,day, rm, amt)
	them  = ('Ref', 'Year', 'Month', 'Day', 'Roomate', 'Amt')
	print fmt % them
	for x in (it):
		print '%s\t' % x,
	value = fmt % it
	print
	print '0:OK\t CR:NO'
	go = raw_input(pt)
	if go == '0':
		f.write(value)
		print 'Added', value
	f.close()

def add_debit():
	fmt = '%s\t%s\t%s\t%s\t%s'
	f = open('debit.tab', 'a')	
	print 'Ref #'
	yr = g_year()
	mo = g_month()
	day = g_day()
	biller = g_biller()
	amt = g_amt() 
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
	f.close()

#updatemenu()	


def fileinfo():
	debit_fs = debit_f()
	credit_fs = credit_f()
	cr =  len(credit_fs)
	db =  len(debit_fs)
	x =  '\n' + str(cr) + '\t'+ str(db) + '\t'
	z = str(time.localtime())
	
	w = ''
	d = open('updates.dat', 'r')
	e = d.readlines()
		
	d = open('updates.dat','a')
	d.write(x)
	d.close()
	print
