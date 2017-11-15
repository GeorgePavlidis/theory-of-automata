
import platform
import sys, tty, termios

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

		#read the starting nodes
		for x in file.readline().split(' '):
			initial_nodes.append(int(x))

		#validity check
		for node in initial_nodes:
			if node<0 or node>=Total_nodes:
				print( "you have problem with your INITIAL nodes, please check it and try again!")
				return False


		#read the final nodes
		for x in file.readline().split(' '):
			final_nodes.append(int(x))

		#validity check
		for node in final_nodes:
			if node<0 or node>=Total_nodes:
				print( "you have problem with your FINAL nodes, please check it and try again!")
				return False


		#read the edges of this model
		# the numbers of nodes are represented as integer	
		# and conditions are represented as string
		for line in file:
			edge = line[:len(line)-1].split(' ')
			x = []
			try:
				x.append(int(edge[0]))
				x.append(edge[1])
				x.append(int(edge[2]))
			except:
				print ("You have problem with edge at line", line)
				return False

			edges.append(x)

		return True


def model():
	print ('Press <ENTER> to begin:\n')
	input_char='s'
	stri = ""
	if 'Windows' == platform.system():
		input_char = getch.getch()

	else:
		while not input_char.upper() == chr(13):
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				input_char = sys.stdin.read(1)
				print input_char,
				stri+=input_char
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	print stri
	if input_char.upper() == chr(13): 
		print ('YES')


def print_des():
		print(" ")
		print ("The description must follow the format bellow ")
		print(" ")
		print ("	line 1: Total_number_of_nodes")
		print ("	line 2: initial_node")
		print ("	line 3: final_nodes : split with <SPACE>")
		print ("	line 4 and bellow: edges as ")
		print ("		[source_node, 'conditions', destination_node]:")
		print ("			split with <SPACE>")
		print ("Example: ")
		print ("	line 1: 3 ")
		print ("	line 2: 0 ")
		print ("	line 3: 1 2 ")
		print ("	line 4: 0 a 1 ")
		print ("	line 5: 0 b 2 ")


if __name__ == "__main__":
	flag = False
	print_des()
	while(not flag):

		#file = raw_input ("Entrer the name of file with description of model: ")
		file = "example1.txt"
		try:
			flag = readFile(file)
			if not flag: 
				print_des()
		except IOError as e:
			print( "File not found...")
			print(" please try again")
		


		print ("Total_nodes ", Total_nodes)
		print ("initial_nodes ", initial_nodes)
		print ("final_nodes ", final_nodes)
		print ("edges", edges) 
		#sys.argv[1]
		model()