import sys, os, string
sys.path.insert(0, "files")
from support import *

# class currentdate():
# 	date 

def debit_f():
	#f = open('debit_new.tab', 'r')		#New file format?
	f = open('debit.tab', 'r')		#Old file format
	debit = f.readlines()
	z = open('debit_sorted.dat', 'w')
	that = []
	newlist = []
	y = [] 
	for line in debit:
		(year, mo, day, amt, biller, roomate) = line.split('\t', 5)
		newlist.sort
		thing = year + '\t' + mo + '\t' + day + '\t' + amt + '\t' + biller + '\t' + roomate
		that.append(thing)
	that.sort()
	z.writelines(that)
	return debit
	f.close()

def credit_f():
	f = open('credit.tab', 'r')
	credit = f.readlines()
	return credit
	f.close()

def debit_year(file, date):
	list = []
	for line in file:
		(year, mo, day, amt, biller, roomate) = line.split('\t',5)
		if year == date:
			list.append(line)
	return list
def credit_year(file, date):
	list = []
	for line in file:
		(ref, year, mo, day, roomate, amt) = line.split('\t', 5)
		if year == date:
			list.append(line)
	return list

def credit_month(file, date):
	list = []
	for line in file:
		(ref, year, mo, day, roomate, amt) =  line.split('\t', 5)
		if mo == date:
			list.append(line)
			#print line
	return list
def debit_month(file, date):
	list = []
	for line in file:
		(year, mo, day, amt, biller, roomate) = line.split('\t',5)
		if biller == '':
			pass
		else:
			if mo == date:
				list.append(line)
	return list

	
def debit_year_month(file, year, month):
	'''Takes Year and month and returns matching records'''
	if month <> '':
		i = debit_totals(debit_month(debit_year(file, year),month))
	else:
		i = debit_totals(debit_year(file, year))
	return i
def credit_year_month(file, year,month):
	if month <> '':
		i = credit_totals(credit_month(credit_year(file, year),month))
	else:
		i = credit_totals(credit_year(file, year))
	return i
	
def debit_totals(file):						#DEBITS
	(mo, day, yr, amt, bill, rm) = (0, 1, 2, 3, 4, 16) 	#Set Debit file format
	(CT, DM, MC, NS, NG, BL, JB, TB) = (0,0,0,0,0,0,0,0)		#Init Variables
	share = 0.0
	
	RM = {}
	
	for records in file:
		myline = records.split()
		group = myline[5:len(myline)]
		number = len(myline[5:len(myline)])
		share = float(myline[amt])/number
		for person in group:
			if person  == "CT":CT = share + CT
			if person  == "DM":DM = share + DM
			if person  == "MC":MC = share + MC
			if person  == "NS":NS = share + NS
			if person  == "JB":JB = share + JB
			if person  == "NG":NG = share + NG	
			if person  == "BL":BL = share + BL	
			if person  == "TB":TB = share + TB
	total = (JB+NG+CT+MC+DM+NS+BL+TB)
	return (JB,NG,CT,MC,DM,NS,BL,TB, total)
			
def credit_totals(file):						#CREDITS DONE
	(ref, yr, mo, day, rm ,amt) = (0, 1, 2, 3, 4, 5) 	#Set Credit file format
	(CT, DM, MC, NS, NG, BL, JB, TB) = (0,0,0,0,0,0,0,0)		#Init Variables
	share = 0.0
	for line in file:
		myline = line.split()
		(value, share) = (myline[rm], float(myline[amt]))
		if value  == "CT":CT = share + CT
		if value  == "DM":DM = share + DM
		if value  == "MC":MC = share + MC
		if value  == "NS":NS = share + NS
		if value  == "JB":JB = share + JB
		if value  == "NG":NG = share + NG	
		if value  == "BL":BL = share + BL	
		if value  == "TB":TB = share + TB
	total = (CT+JB+NG+MC+DM+NS+BL+TB)
	return (JB,NG,CT,MC,DM,NS,BL,TB, total)	

def diff(debit, credit):
	'''Takes the 8 values from Debit, subtracts credit and returns the result'''
	#print debit
	#print credit
 	(a, b, c, d, e, f, g, o, x, ) = debit
	(h, i, j, k ,l, m, n, p, y) = credit
	total = ((a-h), (b-i), (c-j), (d-k), (e-l), (f-m), (g-n),  (o-p), (x-y))
	return total


def biller_totals(file):
	(mo, day, yr, amt, bill, rm) = (0, 1, 2, 3, 4, 5) 	#Set Debit file format
	(CT, DM, MC, NS, NG, BL, JB, TB) = (0,0,0,0,0,0,0,0)		#Init Variables
	(Nipsco, AEP, Comcast,City,Vonage,Rent)= (0,0,0,0,0,0)
	share = 0.0

	for records in file:
		myline = records.split()
		share = float(myline[amt])
		it = myline[bill]
		if it  == "Nipsco":Nipsco = share + Nipsco
		if it == 'AEP':AEP = share + AEP
		if it == 'Comcast':Comcast = share + Comcast
		if it == 'City':City = share + City
		if it == 'Vonage':Vonage = share + Vonage
		if it == 'RENT':Rent = share + Rent
	i = (Nipsco, AEP, Comcast, City, Vonage, Rent)
	return i

 

