def pause():myinput = raw_input('Enter to continue. ')	

pt = ':> '

ln = "%8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f\n"
hd = "%9s%9s%9s%9s%9s%9s%9s%9s%9s" % ('JB','NG','CT','MC','DM','NS','BL','TB','Total')

def g_roomate():
	print '1 JB\t2 NG\t3 DM\t4 BL\t5 NS\t6 MC\t7 CT\t 8 TB'
	input = raw_input(pt)
	if input == '1':return 'JB'
	elif input == '2':return 'NG'
	elif input == '3':return 'DM'
	elif input == '4':return 'BL'
	elif input == '5':return 'NS'
	elif input == '6':return 'MC'
	elif input == '7':return 'CT'
	elif input == '8':return 'TB'
	else:return ''
def g_biller():
        print '1 Nipsco\n2 AEP\n3 Comcast\n4 City Utilities\n5 Vonage\n6 Rent'
        input = raw_input(pt)
        if input == '1':return 'Nipsco'
        elif input == '2':return 'AEP'
        elif input == '3':return 'Comcast'
        elif input == '4':return 'City'
        elif input == '5':return 'Vonage'
        elif input == '6':return 'RENT'
        else:return ''
def g_month():
	print 'Month'
	print '  Q1\t  Q2\t  Q3\t   Q4'
	print '1 Jan \t4 Apr \t7 Jul \t10 Oct'
	print '2 Feb \t5 May \t8 Aug \t11 Nov'
	print '3 Mar \t6 Jun \t9 Sept \t12 Dec'
	input = raw_input(pt)
	if len(input)< 2:
		input = '0' + input
	return input
def g_year():
	print 'Year:'
	print '1 2001 \t2 2002 \t3 2003\t4 2004\t5 2005'
	input = raw_input(pt)
	if len(input)< 4:
		input = '200' + input
	return input
def g_day():
	print 'Day:'
	input = raw_input(pt)
	if len(input)< 2:
		input = '0' + input
	return input
def g_amt():
	print 'Amt:'
	input = raw_input(pt)
	return input
