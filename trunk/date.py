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
def write_cat(data):
	z = read_cat()
	f = open('cat.dat', 'w')
	data = data + '\n'
	z.append(data)
	z.sort()
	f.writelines(z)
	f.close()

def get_cat():
	print "Cat Name"
	data = raw_input(':>')
	write_cat(data)	
	
def print_cat():
	data = read_cat()
	for items in data:
		print items, 
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
	print get_cat()
	print "Comment/Memo:"
	memo = raw_input(':>')
	fmt = "%s\t%s\t%s\t%s\t%s\t%s\t%s"
	towrite = fmt % (date, UID, amt, acct_1, acct_2, cat, memo)
	write_f(towrite)
	
getdata()
it = myfile
it.file = open_f()
print "Date\t\tUID\t\tAMT\tACCT\tTo/From\tCat.\tMemo"
for items in it.file: 
	print items, 
#it.it

class MyClass:
	"A simple example class"
	i = 12345
	def f(self):
		return 'Hello World'
	
