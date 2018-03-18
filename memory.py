################################################################################
#                               Memory Class                                   #
# Class used for the simulation of different memory chaches on the sistem.     #
# For now only used as an assosiation of numbers							   #
################################################################################

class Memory:
	def __init__(self, memid):
		# actual way we will track how many values we currently have and assign each to a “space in memory”
		self.mem_id = memid
		start = self.mem_id * 10000
		self.int_cont = start
		self.float_cont = start + 1000
		self.char_cont = start + 2000
		self.string_cont = start + 3000
		self.bool_cont = start + 4000
		self.nodes_cont = start + 5000
		self.arc_cont = start + 6000
		self.directed_cont = start + 7000
		self.undirected_cont = start + 8000

	def reset_cont(self):
	    # All cont to 0
		start = self.mem_id * 10000
		self.int_cont = start
		self.float_cont = start + 1000
		self.char_cont = start + 2000
		self.string_cont = start + 3000
		self.bool_cont = start + 4000
		self.nodes_cont = start + 5000
		self.arc_cont = start + 6000
		self.directed_cont = start + 7000
		self.undirected_cont = start + 8000

	def p_counters(self):
		print("int: " + str(self.int_cont))
		print("flt: " + str(self.float_cont))
		print("chr: " + str(self.char_cont))
		print("str: " + str(self.string_cont))
		print("bol: " + str(self.bool_cont))
		print("nde: " + str(self.nodes_cont))
		print("arc: " + str(self.arc_cont))
		print("dir: " + str(self.directed_cont))
		print("und: " + str(self.undirected_cont))

