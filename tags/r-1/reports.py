#  
# import sys, os, string
# sys.path.insert(0, "files")
# from support import *
# #from payments import *
# #from charges import *
# from update import *
from files import *
from support import *
# from new import *
# from reports import *
import time
def acct_summary():	
	h = 'acct_summary\n'							#Report Title
	(CT, DM, MC, NS, NG, BL, JB, TB) = (0,0,0,0,0,0,0,0)			#Init Roomate Variables
# 	print '\tJB\tNG\tCT\tMC\tDM\tNS\tBL\tTB\tTotal'			#Print Name Headed
# 	temp = '\t',hd
# 	holding.append(temp)
	h = h + '\t'+ hd + '\n'
	h = h + '\t'+ '-'*32 + 'Debits'+ '-'*32				#Print Type Header
	h = h + '\n'
	years = ('0000', '2002', '2003', '2004','2005')
	(debit_fs,credit_fs) = (debit_f(),credit_f())			#Read Files ONCE
	
	for j in years:							#Print Debits 
		h = h + j+ '\t'+ ln %  debit_totals(debit_year(debit_fs, j))	#Totals	
	h = h + 'TOTAL'+ '\t'+ ln % debit_totals(debit_fs)
	h = h + '\t'+ '-'*32 + 'Credits'+ '-'*31 + '\n'

	for j in years:							#Print Credits
		#(JB,NG,CT,MC,DM,NS,BL,TB, total) = credit_totals(credit_year(credit_fs, j))
		h = h + j+'\t'+ln % credit_totals(credit_year(credit_fs, j))
	h = h + 'TOTAL'+ '\t'+ln % credit_totals(credit_fs)		#Totals
	h = h + '\t'+ '-'*32 + 'Sums'+ '-'*34 + '\n'							#Header
	h = h +  '\t'+ln % diff(debit_totals(debit_fs),credit_totals(credit_fs))		#Running Totals
# 	h = h + '\n'
	print h
	m = diff(debit_totals(debit_fs),credit_totals(credit_fs))
	print '/6 Mo\t',
	for items in m:
		print '%8.2f' % (float(items)/6),
	print
	print '/1 Yr\t',
	for items in m:
		print '%8.2f' % (float(items)/12),
	print
	print '/2 Yrs\t',
	for items in m:
		print '%8.2f' % (float(items)/24),
	print
	print '/3 Yrs\t',
	for items in m:
		print '%8.2f' % (float(items)/36),
	print
	print '/4 Yrs\t',
	for items in m:
		print '%8.2f' % (float(items)/48),
	print
	print '/5 Yrs\t',
	for items in m:
		print '%8.2f' % (float(items)/60),
	print
	print time.asctime()	
	print 

def monthly_totals():
	print 'Monthly Totals'	,time.asctime()				#Report Title
	(CT, DM, MC, NS, NG, BL, JB,TB) = (0,0,0,0,0,0,0,0)			#Init Roomate Variables
	(debit_fs,credit_fs) = (debit_f(),credit_f())			#Read Files ONCE
	years = ('0000', '2002', '2003', '2004', '2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	rm = {'JB':1, 'NG':2, 'CT':3, 'MC':4, 'DM':5, 'NS':6, 'BL':7,'TB':8, 'Total':9}
	
	print '-'*30,'Debits','-'*30
	for i in years:
		print i, hd
		for j in months:
			print j, 'db',ln % debit_year_month(debit_fs, i, j),
			print '   cr',ln % credit_year_month(credit_fs, i, j),
		print 
# 	print time.asctime()	
	print
def yearly_totals():
	print 'yearly totals',time.asctime()				#Report Title
	years = ('0000', '2002', '2003', '2004', '2005')
	(debit_fs,credit_fs) = (debit_f(),credit_f())
# 	date = time.asctime()
	fname = 'yearly_totals'
	f = open(fname,'w')
	f.write(time.asctime())
	for i in years:
		it =  '\n'+ i+hd+'\n'
		print it,
		f.write(str(it))
		it =  '  db:'+ ln % debit_totals(debit_year(debit_fs, i))	#Totals	
		print it,
		f.write(it)
		it =  '  cr:'+ ln % credit_totals(credit_year(credit_fs,i))
		print it,
		f.write(it)
		it = ' Tot:'+ ln % diff(debit_totals(debit_year(debit_fs, i)), credit_totals(credit_year(credit_fs,i)))
		print it,
		f.write(it)
# 		print
	print 	
	it = ' Bal:' + ln % diff(debit_totals(debit_fs),credit_totals(credit_fs))
	print it
	it = '\n' + it
	f.write(it)

	f.close()
# # 	print
	
def roomate_totals():
	print 'roomate totals'								#Report Title
# 	t1 = time.clock()
	(debit_fs,credit_fs) = (debit_f(),credit_f())
	years = ('0000', '2002', '2003', '2004', '2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	rm = {'JB':0, 'NG':1, 'CT':2, 'MC':3, 'DM':4, 'NS':5, 'BL':6, 'TB':7}
	h = ''
# # # 	h = h + '-'*10+'Debits'+'-'*10
	print '-'*10+'Debits'+'-'*10
	for i in rm.keys():

# 		h = h + '\n' 
# 		print i, rm[i] ,'    jan     feb     mar     apr     may     jun     jul     aug     sep     oct     nov     dec'
# # # 		h =  h +'\n\n'+ i + str(rm[i]) +'    jan     feb     mar     apr     may     jun     jul     aug     sep     oct     nov     dec'
		print '\n', i , str(rm[i]) ,'   jan     feb     mar     apr     may     jun     jul     aug     sep     oct     nov     dec'
		for y in years:
# # # 			h = h + '\n' + y
			print y,
# 			print '%d' % debit_totals(debit_year(debit_fs, y))[int(rm[i])]
			#z = debit_year(debit_fs,y)
			for m in months: 
# # # 				h = h + '%8.2f' % debit_year_month(debit_fs, y, m)[int(rm[i])]
				print '%7.2f' % debit_year_month(debit_fs, y, m)[int(rm[i])],
				#w = debit_month(z,m)[rm[i]]
				#print w,
				#print '%7.2f' % w,
# 				h = h + '\n'
# 				print '.',
			print
# # # 	print h
	print time.asctime()	
	print


def biller_month_totals2():
	print 'biller_month totals2'							#Report Title
	(CT, DM, MC, NS, NG, BL, JB, TB) = (0,0,0,0,0,0,0,0)				#Init Roomate Variables
	(debit_fs,credit_fs) = (debit_f(),credit_f())				#Read Files ONCE
	years = ('2002', '2003', '2004','2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	rm = {'JB':1, 'NG':2, 'CT':3, 'MC':4, 'DM':5, 'NS':6, 'BL':7,'TB':8, 'Total':9}
	bl = {'Nipsco':0, 'AEP':1, 'Cable':2,'City':3,'Vonage':4,'Rent':5}
	h = ''
	for i in bl.keys():
		h = h + i + '\t jan     feb     mar     apr     may     jun     jul     aug     sep     oct     nov     dec\n'
# 		print 'Billers'.center(80)
		for y in years:
			h = h + y
# 			print ((biller_totals(debit_month(debit_year(debit_fs,y), '01'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'02'))[bl[i]]),	(biller_totals(debit_month(debit_year(debit_fs, y),'03'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'04'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'05'))[bl[i]]),	(biller_totals(debit_month(debit_year(debit_fs, y),'06'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'07'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'08'))[bl[i]]),	(biller_totals(debit_month(debit_year(debit_fs, y),'09'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'10'))[bl[i]]),(biller_totals(debit_month(debit_year(debit_fs, y),'11'))[bl[i]]),	(biller_totals(debit_month(debit_year(debit_fs, y),'12'))[bl[i]]))
			z = debit_year(debit_fs, y)
			for m in months:
				x = biller_totals(debit_month(z,m))
				h = h + '%8.2f' % x[bl[i]]
			h = h + '\n'
		h = h + '\n'
	print h
	print time.asctime()	
	print	
	
def biller_month_totals():
	print 'biller month totals'							#Report Title
	(CT, DM, MC, NS, NG, BL, JB) = (0,0,0,0,0,0,0)				#Init Roomate Variables
	(debit_fs,credit_fs) = (debit_f(),credit_f())				#Read Files ONCE
	years = ('2002', '2003', '2004','2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	rm = {'JB':0, 'NG':1, 'CT':2, 'MC':3, 'DM':4, 'NS':5, 'BL':6, 'Total':7}
	
	print 'Billers'.center(80)
	for i in years:
		print i, '  Nipsco      AEP    Cable     City    Phone     Rent    Total      Per'
		for j in months:
			#print j, 'db',ln  % debit_year_month(debit_fs, i, j)
			print j, '  %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f' % (biller_totals(debit_month(debit_year(debit_fs, i),j))),
			total = add(biller_totals(debit_month(debit_year(debit_fs, i), j)))
			print '%8.2f %8.2f' % (total, total/3)  
		print
	print time.asctime()	
	print

def add(it):
	(a, b, c, d, e, f) = it
	return (a+b+c+d+e+f)
def invoice():
	years = ('2002', '2003', '2004','2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
# 	rm = {'JB':0, 'NG':1, 'CT':2, 'MC':3, 'DM':4, 'NS':5, 'BL':6,'TB':7, 'Total':8}
	
	
	
	print 'Invoice'
# 	t1 = time.clock()
	(debit_fs,credit_fs) = (debit_f(),credit_f())
	years = ('0000', '2002', '2003', '2004','2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	rm = {'JB':0, 'NG':1, 'CT':2, 'MC':3, 'DM':4, 'NS':5, 'BL':6}
	h = ''
# # # 	h = h + '-'*10+'Debits'+'-'*10
	print '-'*10+'Balances'+'-'*10
	for i in rm.keys():
		temp = '-'*20+'Debits:  ' + time.asctime() +'-'*20
		print '\n', i , str(rm[i]) ,'      jan    feb    mar    apr    may    jun    jul    aug   sep     oct    nov    dec  total'
		temp = temp + '\n'+ i + ' '+ str(rm[i]) +'        jan      feb      mar      apr      may      jun      jul      aug     sep       oct      nov      dec    total'
		for y in years:
			deb = 0
			print y, 'db',
			temp = temp + '\n'+ y + ' db'
			for m in months: 
				m = float(debit_year_month(debit_fs, y, m)[int(rm[i])])
				deb = deb + m
				print '%6d' % m,
				temp = temp + '%9.2f' % m 
			temp = temp + '%9.2f' % deb + '\n'
			print '%6d' % deb
			temp = temp + '     cr'
			print '     cr',
			cred = 0
			for m in months:
				m =  float(credit_year_month(credit_fs, y, m)[int(rm[i])])
				cred = cred + m
				print '%6d' % m,
				temp = temp + '%9.2f' % m
			temp = temp + '%9.2f' % cred + '\n'
			print '%6d' % cred
			print '   Tot:',
			temp = temp + '   Tot:'
			tot = 0
			for m in months:
				m = float((credit_year_month(credit_fs, y, m)[int(rm[i])])-(debit_year_month(debit_fs, y, m)[int(rm[i])]))
				tot = tot + m
				print '%6d' % m,
				temp = temp + '%9.2f' % m
			temp = 	temp + '%9.2f' % tot + '\n'
			print '%6d' % tot
		print	
		temp = temp + '\n'
		deb = -1*float(debit_totals(debit_fs)[rm[i]])
		cred = float(credit_totals(credit_fs)[rm[i]])
		print 'Debits:  $%9.2f' % deb 
		print 'Credits: $%9.2f' % cred
		print 'Balance: $%9.2f' % float(deb+cred)
		temp = temp + 'Debits:  $%9.2f' % deb + '\n'
		temp = temp + 'Credits: $%9.2f' % cred + '\n'
		temp = temp + 'Balance: $%9.2f' % float(deb+cred) + '\n'
# 		temp = '<html><head><title></title><meta content=""><style></style></head><body>' + temp + '</body></html>'
		
		
		filename =  'invoice_' + i  +'.txt'
		file = open(filename, 'w')
		file.write(temp)
# 		print temp
		temp = ''
		
		print  
# 	print '*'*40
# 	filename = i + '_invoice.html'
# # 	file = open(filename, 'w')
# 	file.write(temp)
# 	print temp
	temp = ''		
	print time.asctime()	
	print	
	
def print_mo(yr,mo):
# 	if y =='' and m == '':
	yr = g_year()
	mo = g_month()
	x = debit_month(debit_year(debit_f(), yr),mo)
	y = credit_month(credit_year(credit_f(), yr),mo)
	#x = x.split()
	#y = y.split()
	z = 0
	total = 0
	print yr, mo
	print 'Debits'
	for row in x:
		print ':',x[z],	
		total = total +  float(x[z].split()[3])
# 		print '!', total
		z = 1 + z
	print
	print 'Total: $%.2f /2= $%.2f /3= $%.2f /2p4w= $%.2f /3p4w= $%.2f' %  (total, total/2,total/3, total/8, total/12)
	print
	print 'Credits'
	z = 0
	total = 0
	for row in y:
		print ':',y[z],
		total = total + float(y[z].split('\t')[5])
# 		print '!', total
		z = 1 + z
	#print
	#print 'Total: $%.2f /2= $%.2f /3= $%.2f' %  (total, total/2,total/3)
	#print	
	
def printMo():
	print 'Print Months', time.asctime()						#Report Title
	years = ('2002', '2003', '2004','2005')
	months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	for y in years:
		for m in months:
			print '-'*40
			print y, m
			print_mo(y,m)
			
	print '-'*40	
	
