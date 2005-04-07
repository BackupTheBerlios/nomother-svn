from normalDate import ND 
import time 
import sys

#################
# Constants
################

FALSE = 0 == 1
TRUE = not FALSE

# Global Variables
ALLDONE = FALSE

#############
# Literals
#############
SEP = '-' * 79

###########################
# Prompts and othe Strings 
###########################
pt = ":>"
TRAILER = "...\n"

###############################

def Exit(Agrs):
	tprint ("Exiting" + TRAILER)
	global ALLDONE
	ALLDONE = TRUE


tprint = sys.stdout.write

#Open File
def open_f():
	f = open('test.dat', 'r')
	data = f.readlines()
	data.sort()
	f.close()
	return data
def filter_f(year="", month=""):
	data = process_f()
	year = "2004"
	year_list= []
	month_list = []
	print "filter_f 269" 
	for x in data:
		#print "%s:%s" % (x, data[x]["year"])
		if data[x]["year"] == year:
			year_list.append(x)
			if data[x]["month"] == month:
				month_list.append(x)		
def process_f():
	data = open_f()
	date = 0
	UID_no = 1
	amt_no = 2
	account_no = 3 
	payee_no =  4
	cat_no = 5
	memo_no = 6
	count = 0
	dict = {} 
	for i in data:
		temp_list = {}
		count += 1
		i_split= i.split()
		temp_list["ID"] = str(count)
		temp_list["UID"] = i_split[UID_no]
		temp_list["year"] = i_split[date][0:4]		#year 
		temp_list["month"] = i_split[date][4:6]
		temp_list["day"] = i_split[date][6:8]
		temp_list["acct"] = i_split[account_no] 
		temp_list["amt"] = float(i_split[amt_no])
		temp_list["payee"] = i_split[payee_no]
		temp_list["cat"] = i_split[cat_no]
		if len(i_split) > 6:				#This is because some lines are
			temp_list["memo"] =  i_split[memo_no]	#6 long, other 5. Maybe is we split
		else:						#it differently?  The last value 
			temp_list["memo"] = ""			#has been droping off if it is empty
		dict[str(count)] = temp_list	
	fmt2 = "%s:\t%s"	
	return dict	
def write_f(data):
	z = open_f()
	f = open('test.dat', 'w') 
	data = data + '\n'
	z.append(data)
	z.sort()
	f.writelines(z)
	f.close()
class myfile:
	def __init__(self):
		self.wholeFile = process_f()
def read_cat():
	f = open('cat.dat', 'r')
	data = f.readlines()
	f.close()
	return data
def write_cat(no, data):
	z = read_cat()
	f = open('cat.dat', 'w')
	data = no + '\t' + data + '\n'
	z.append(data)
	z.sort()
	f.writelines(z)
	f.close()
def put_cat():
	data = read_cat()
	for i in data:
		(no, name) = i.split()
		cat_class.cat_no[no] = name
def get_cat():
	put_cat()				#when should I do this?
	print "Cat Name"
	data = raw_input(':>')
	if cat_class.cat_no.has_key(data):	#this doesn't work.  I can perhaps use the name as key, and the no. as value? 
		return data			#or, let none mean enter new value, easier to test against, but it means no data
	else:					#validation. Does it matter? lets treat the cat name as a label. only the no. matters
		write_cat('6', data)
		return data
	#write_cat(data)	
 	
def print_cat():
	put_cat()				#when should I do this?
	count = 0
	for i in cat_class.cat_no:
		count = count + 1
		print '(%s) %s \t' % (i, cat_class.cat_no[i]),
		if count == 6:
			print
	print	
def getdata():
	z_class = cat_class.cat_no
	UID = str(time.time())
	date = ND()
	date_fmt = str(date.formatUS())
	date = str(date)
	print 'Default Date:', date, date_fmt 
	print 'Change Date? <enter> to accept default'
	newdate = raw_input('Change date?')
	if newdate <> '':
		date = newdate
	print 'Amount:'
	amt = raw_input(':>')
	print "Account"
	acct_1 = raw_input(":>")
	print "To/From"
	acct_2 = raw_input(":>")
	print "Category"
	print_cat()
	cat =  get_cat()
	print "Comment/Memo:"
	memo = raw_input(':>')
	if len(memo) <1:
		memo = memo + ' '
	fmt = "%s\t%s\t%s\t%s\t%s\t%s\t%s"
	towrite = fmt % (date, UID, amt, acct_1, acct_2, cat, memo)
	write_f(towrite)
	
class Account:
	def __init__(self):
		self.Bal = 0		#Current Balance
	def Credit(self, amt):		
		self.Bal += amt		#Credit the Account
	def Debit(self, amt):		
		self.Bal -= amt		#Debit the Account
		
class cat(Account):
	def __init__(self):
		self.Bal = 0

def accounts():
	f = open('accounts.dat', 'r')
	data = f.readlines()
	x = {} 
	for i in data:
		y = i.split()
		w,z = y[0],y[1]
		x[w] = z		
	return x

mytime = time.time()
#ogetdata()
#process_f()
filter_f()
def display():
	accounts()	
	print "DISPLAY()"
				### todo: read list of Catagories, make it into dictionary.
				### store category amts into dictionary.  Print it.
				### repeat with accounts. :-)  sort dictionaries, and print them.
	#print "Date\t\tUID\t\tAMT\tACCT\tTo/From\tCat.\tMemo"

				### The following dates are "static" we need to set the cate on the 
				### prompt, and redisplay based on the new values. 
				
				### We also need to print PER acct, and summarize categories
	currentDate = ND()
	stringDate = str(currentDate)
	currentYear = stringDate[0:4]
	currentMonth = stringDate[4:6]
	currentDay = stringDate[6:8]
	#print "Current month:", currentMonth
	newfile = myfile()
	accts = accounts()
	fmt = "<%s>\t%s/%s/%s %10s  %s\t $%7.2f \t $%8.2f"
	for items in accts:
			total = 0
			tprint ("\n" + "="*20 +"\t" + accts[items] +"\t"  + "="*30 + "\n")
			print "<#>\tYYYY/MM/DD   ---Cat---  PAYEE \t  --AMT--\t  --TOT.--"    
			print "=" *70
			for item in newfile.wholeFile: 
				special = FALSE
				year = newfile.wholeFile[item]["year"]
				acct = newfile.wholeFile[item]["acct"]
				month = newfile.wholeFile[item]["month"]
				if acct == accts[items]:
					amt = float(newfile.wholeFile[item]["amt"]) 
					total = total + amt
				if month == currentMonth and year == currentYear and acct == accts[items]:
					id = newfile.wholeFile[item]["ID"]
					payee = newfile.wholeFile[item]["payee"]
					cat = newfile.wholeFile[item]["cat"]
					day = newfile.wholeFile[item]["day"] 
					if day == currentDay:
						special = TRUE
					else:
						if day > currentDay:
							special = TRUE 
					if special == TRUE:
						print "-"*  70
					print fmt % (id, year,month,day, cat,  payee, amt, total)
				if month > currentMonth and year == currentYear and acct == accts[items]:
					id = newfile.wholeFile[item]["ID"]
					payee = newfile.wholeFile[item]["payee"]
					cat = newfile.wholeFile[item]["cat"]
					day = newfile.wholeFile[item]["day"]
					
					print fmt % (id, year,month,day, cat,  payee, amt, total)

			print "=" *70
#sums()
print (time.time() - mytime)


########################
# Display Data and menu
########################

#Read myfile.file()

it = myfile()

#tprint (it.wholeFile)
#print it.wholeFile
while not ALLDONE:
	display()
	tprint("ENTER to quit\n")	
	input = raw_input(pt)
	if input == '':
		ALLDONE = TRUE
######
# END
######
