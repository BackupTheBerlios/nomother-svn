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
# 		print "%20s %20s %20s %30s" % ('1 Yearly  Bal.','2 Yearly Totals','3 Db&Cr/Mo Person','4 Debits/Month Roomates TWO')
# 		print '1 Yearly  Bal.\t2 Yearly Totals\t3 Db&Cr/Mo Person\t4 Debits/Month Roomates TWO'
# 		print "%d %15s %20s %20s %30s"% 5, 'Acct Bal.','6 Print Month','7 Biller/Month','8 Debits/Month Billers TWO')
# # 		print "5 Acct Bal.\t6 Print Month\t7 Biller/Month\t\t8 Debits/Month Billers TWO"
# 		print '9 Add Credit\t10 Add Debit'
		print 'Totals:\t1 Balances\t2 Yearly\t3 Monthly'
		print 'Debits:\t4 Roomates\t5 Bills \t6 Monthly Bills'
		print 'Show:\t7 Month\t\t71 All Months\t72 Invoices'
		print 'Add:\t8 Credit\t9 Debit'
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

