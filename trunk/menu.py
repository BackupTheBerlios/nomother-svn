#!/usr/bin/python
import sys, os, string
sys.path.insert(0, "files")
#from payments import *
#from charges import *
import time
from reports import *
from support import *
from update import *

def menu():
	while 1:
		t1 = time.clock()
		fmt = '%10s: (%2s)%10s  (%2s)%11s (%2s)%15s'
		print fmt % ('Totals', '1', 'Balances', '2', 'Yearly','3','Monthly')
		print fmt % ('Debits','4',  'Roomates', '5', 'Bills', '6','Monthly Bills') 
		print fmt % ('Show', '7', 'Month', '71', 'All Months', '72','Invoices')
		print fmt % ('Add', '8', 'Crediti', '9', 'Debit', '10','Misc')

		choice = raw_input( pt)
		if choice == '1':acct_summary()
		elif choice == '2':yearly_totals()
		elif choice == '3':monthly_totals()
		elif choice == '4':roomate_totals()
		elif choice == '5':biller_month_totals()
		elif choice == '6':biller_month_totals2()
		elif choice == '7':print_mo('','')
		elif choice == '71':printMo()
		elif choice == '8':add_credit()
		elif choice == '9':add_debit()
		elif choice == '10':print hd, '\n', ln % diff(debit_totals(debit_f()),credit_totals(credit_f()))
		elif choice == '11':fileinfo()		
		#elif choice == '9':biller_sums()	
		elif choice == '72':invoice()				
		else:break
		t2 = time.clock()
		print 'Compute time:', t2-t1
menu()
