

class Proconlist:
	def __init__(self, decision):
		self.decision = decision
		self.prolist = []
		self.conlist = []
	def add_pro(self, reason):
		self.reason = reason
		self.prolist.append(reason)
	def add_con(self, reason):
		self.reason = reason
		self.conlist.append(reason)
	def make_priority(self, pro_or_con, number_in_list, reason):
		if pro_or_con == "con":
			self.conlist.remove(conlist[number_in_list])
			self.conlist.insert(0, reason)
		elif pro_or_con == "pro":
			self.prolist.remove(conlist[number_in_list])
			self.prolist.insert(0, reason)

def new_pro():
	print "Okay, so what's another positive aspect of this decision?"
	this_pro = raw_input("Well, it might . . .")
	list_name.add_pro(this_pro)
	user_decision()

def new_con():
	print "Okay, so what's another negative aspect of this decision?"
	this_con = raw_input("Well, it might . . .")
	list_name.add_con(this_con)
	user_decision()

def user_decision():
	print "Do you want to add a pro or a con?"
	user_choice = raw_input("Type 'pro' or 'con' or 'no' >>> ")
	if user_choice == 'pro':
		new_pro()
	elif user_choice == 'con':
		new_con()
	else:
		show_list()
		
def show_list():
	print "Okay, so you're looking to figure out whether to" + list_name.decision + "!"
	print "That sounds hard! Here are some reasons that sounds like a good idea:"
	for reason in list_name.prolist:
		print "It might " +reason +"\n"
	print "And here are some reasons it's more complicated than that:"
	for reason in list_name.conlist:
		print "It might " +reason +"\n"


print "Let's make a list. What should we call it?"
list_name = raw_input("Let's call this list . . .")
print "That's a great name. So, what decision are you agonizing over?"
decision = raw_input("I wonder if I should. . .")
print "That's a tough one! What's one good reason you should do it?"
pro1 = raw_input("It might. . .")
print "That makes sense. Now, what's stopping you?"
con1 = raw_input("It might. . .")
list_name = Proconlist(decision)
list_name.add_pro(pro1)
list_name.add_con(con1)
print "Okay, so you wonder whether you should" + list_name.decision
print "One positive outcome is that it might" + list_name.prolist[0] 
print "One negative possibility is that it might" + list_name.conlist[0]
user_decision()
