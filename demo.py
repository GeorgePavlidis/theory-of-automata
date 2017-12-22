
import platform
import sys
import copy as copy
import os


__author__ = 'Pavlidis Georgios'

Total_nodes = 0
initial_nodes = []
final_nodes = []
current_nodes = []
edges = [] # [source_node, 'conditions', destination_node]

def readFile(importFile):
	global Total_nodes, initial_nodes, final_nodes, current_nodes, edges

	Total_nodes = 0
	initial_nodes = []
	final_nodes = []
	current_nodes = []
	edges = [] # [source_node, 'conditions', destination_node]
	

	with open(importFile,"r+") as file:
		#total number of nodes
		Total_nodes = int(file.readline())
		#initialize edges
		for i in range (0, Total_nodes):
			edges.append([])
			initial_nodes.append(0)
			final_nodes.append(0)

		try:	
			#read the starting nodes
			for x in file.readline().split(' '):
				initial_nodes[int(x)]=1
		except:
			print( "you have problem with your INITIAL nodes, please check it and try again!")
			return False


		#read the final nodes
		try:	
			#read the starting nodes
			for x in file.readline().split(' '):
				final_nodes[int(x)]=1
		except:
			print( "you have problem with your FINAL nodes, please check it and try again!")
			return False



		#read the edges of this model
		# the numbers of {GP} nodes are represented as integer	
		# and conditions are represented as string
		for line in file:
			edge = line[:len(line)-1].split(' ')
			x = []
			try:

				x.append(edge[1])
				x.append(int(edge[2]))
			except:
				print ("You have problem with edge at line", line)
				return False

			edges[int(edge[0])].append(x)

		return True


#GP read char from terminal without press the <ENTER> 
def read_char():
	if 'Windows' == platform.system():
		import msvcrt
<<<<<<< HEAD
		input_char = getch.getch()
=======
		input_char = msvcrt.getch()
		print input_char,
>>>>>>> eb21be4c622b65f551a48b2a503992f8b623bc3f

	else:
		import tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			input_char = sys.stdin.read(1)
			print input_char,
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	return input_char






<<<<<<< HEAD
def check(current_nodes, input_char='@'):
	while True:
		new_current_nodes = []
=======
def check(current_nodes, input_char):
	while True:

		new_current_nodes=[]
>>>>>>> eb21be4c622b65f551a48b2a503992f8b623bc3f
		#for each current node..
		for node in current_nodes:

			# for each edge of this node..
			for x in edges[node]:
			
				#check if the input char is condition for this edge 
				#or if there is the empty word
<<<<<<< HEAD
			 	if x[0]=='@':
			 		if(current_nodes.count(x[1])==0):
			 			new_current_nodes.append(x[1])
			 		# if input_char=='@' and new_current_nodes.count(node)==0:
			 		# 	print "im in", input_char, 
			 		# 	new_current_nodes.append(node)

		#GP if the new and the old list are the same it mean that all pollible and suitable nodes are in there
		if not all(element in current_nodes for element in new_current_nodes):
			current_nodes = list(current_nodes+new_current_nodes)
		else:
			break
	

	new_current_nodes = []
	if not input_char=='@':
		for node in current_nodes:

			# for each edge of this node..
			for x in edges[node]:
	
				#check if the input char is condition for this edge 
				#or if there is the empty word
			 	if x[0]==input_char:

			 		if(new_current_nodes.count(x[1])==0):
			 			new_current_nodes.append(x[1])	

		return new_current_nodes
	return current_nodes

=======
			 	if x[0]==input_char or x[0]=='@':
			 		if(new_current_nodes.count(x[1])==0):
			 			new_current_nodes.append(x[1])

		#GP if the new and the old list are the same it mean that all pollible and suitable nodes are in there
		if(not current_nodes==new_current_nodes):
			current_nodes = new_current_nodes
		else:
			return current_nodes
>>>>>>> eb21be4c622b65f551a48b2a503992f8b623bc3f



def model():
	global current_nodes
<<<<<<< HEAD
	print ('Press <ENTER> to begin:\n')
=======
	print ('Entrer your characters:\n')
>>>>>>> eb21be4c622b65f551a48b2a503992f8b623bc3f
	input_char='s'

	#GP initialize the current nodes
	for i in range(0,Total_nodes):
		if initial_nodes[i]==1:
			current_nodes.append(i)
<<<<<<< HEAD
			current_nodes = check(current_nodes)


	print current_nodes
=======
		 	for x in edges[i]: 
			 	if x[0]=='@':
			 		if(current_nodes.count(x[1])==0):
			 			current_nodes.append(x[1])


>>>>>>> eb21be4c622b65f551a48b2a503992f8b623bc3f
	while True:

		#read the next character
		input_char= read_char()
		
		#repeat until <ENTER> be pressed
		if input_char ==chr(13):
			break

		#create the new list of current nodes
		current_nodes = check(current_nodes, input_char)

		#if threre are not other node, break.
		if(current_nodes==[]):
			break
		#print current_nodes,

	
	for node in current_nodes:
		if final_nodes[node]==1:
			print ('\nYES')
			return True
	print ('\nNO')
	return False
		


def print_des():
		print("GP_15112")
		os.system("clear")
		print ("The description must follow the format bellow: ")
		print(" ")
		print ("	line 1: Total_number_of_nodes")
		print ("	line 2: initial_node")
		print ("	line 3: final_nodes : split with <SPACE>")
		print ("	line 4 and bellow: edges as ")
		print ("		[source_node, 'conditions', destination_node]:")
		print ("			split with <SPACE>")
		print ("	last line: empty line (very important!!!)")
		print ("Example: ")
		print ("	line 1: 3 ")
		print ("	line 2: 0 ")
		print ("	line 3: 1 2 ")
		print ("	line 4: 0 a 1 ")
		print ("	line 5: 0 b 2 ")
		print ("	line 6: ")


if __name__ == "__main__":
	flag = False
	print_des()
	while(not flag):

		file = raw_input ("Entrer the name of file with description of model: ")
		#file = "example1.txt"
		try:
			flag = readFile(file)
			if not flag: 
				print_des()
		except IOError as e:
			print( "File not found...")
			print(" please try again")
		


	#print ("Total_nodes ", Total_nodes)
	#print ("initial_nodes ", initial_nodes)
	#print ("final_nodes ", final_nodes)
	#print ("edges", edges) 
	while True:
		model()
		k = raw_input ("Would you like to try again ??(Y/N) ")
		if ( k.upper()=='N'):
			break
