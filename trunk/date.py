from normalDate import ND 
import time 

def date():
	today = ND()
	yes = today - 28 
	print today, yes
	print yes -1
	print "US", today.formatUS()
	print "add", today.add(-5)
def open_f():
	f = open('test.dat', 'r')
	data = f.readlines()
	f.close()
	return data
def write_f(data):
	z = open_f()
	f = open('test.dat', 'w') 
	data = data + '\n'
	z.append(data)
	z.sort()
	f.writelines(z)
	f.close()
class myfile:
	def __init__(self, myfile=open_f()):
		pass
	file = open_f()
	def it(self, say='hi'):
		print say 
def read_cat():
	f = open('cat.dat', 'r')
	data = f.readlines()
	f.close()
	return data
class cat_class:
	cat_no = {}
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
	else:					#validation.
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
	fmt = "%s\t%s\t%s\t%s\t%s\t%s\t%s"
	towrite = fmt % (date, UID, amt, acct_1, acct_2, cat, memo)
	write_f(towrite)
	
getdata()
#it = myfile
#it.file = open_f()
#print "Date\t\tUID\t\tAMT\tACCT\tTo/From\tCat.\tMemo"
#for items in it.file: 
#	print items, 
#it.it

class MyClass:
	"A simple example class"
	i = 12345
	def f(self):
		return 'Hello World'
	
