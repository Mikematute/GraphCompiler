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

	def used_mem(self):
		# get the starting number for the meory and substract it to the current memory coutners
		counters = {}
		start = self.mem_id * 10000
		counters[0] = self.int_cont - start
		counters[1] = self.float_cont - start - 1000
		counters[2] = self.char_cont - start - 2000
		counters[3] = self.string_cont - start - 3000
		counters[4] = self.bool_cont - start - 4000
		counters[5] = self.nodes_cont - start - 5000
		counters[6] = self.arc_cont - start - 6000
		counters[7] = self.directed_cont - start - 7000
		counters[8] = self.undirected_cont - start - 8000
		return counters

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

	def print_counters(self):
		print("int: " + str(self.int_cont))
		print("flt: " + str(self.float_cont))
		print("chr: " + str(self.char_cont))
		print("str: " + str(self.string_cont))
		print("bol: " + str(self.bool_cont))
		print("nde: " + str(self.nodes_cont))
		print("arc: " + str(self.arc_cont))
		print("dir: " + str(self.directed_cont))
		print("und: " + str(self.undirected_cont))

	def get_counter_id(self, counter_id):
		if counter_id == "int":
			to_return = self.int_cont
			self.int_cont = self.int_cont + 1
			return to_return
		elif counter_id == "float":
			to_return = self.float_cont
			self.float_cont = self.float_cont + 1
			return to_return
		elif counter_id == "char":
			to_return = self.char_cont
			self.char_cont = self.char_cont + 1
			return to_return
		elif counter_id == "string":
			to_return = self.string_cont
			self.string_cont = self.string_cont + 1
			return to_return
		elif counter_id == "bool":
			to_return = self.bool_cont
			self.bool_cont = self.bool_cont + 1
			return to_return
		elif counter_id == "node":
			to_return = self.nodes_cont
			self.nodes_cont = self.nodes_cont + 1
			return to_return
		elif counter_id == "arc":
			to_return = self.arc_cont
			self.arc_cont = self.arc_cont + 1
			return to_return
		elif counter_id == "directed":
			to_return = self.directed_cont
			self.directed_cont = self.directed_cont + 1
			return to_return
		elif counter_id == "undirected":
			to_return = self.undirected_cont
			self.undirected_cont = self.undirected_cont + 1
			return to_return
		else:
			return -1

	def get_counter_num(self, counter_num):
		if counter_num == 0:
			to_return = self.int_cont
			self.int_cont = self.int_cont + 1
			return to_return
		elif counter_num == 1:
			to_return = self.float_cont
			self.float_cont = self.float_cont + 1
			return to_return
		elif counter_num == 2:
			to_return = self.char_cont
			self.char_cont = self.char_cont + 1
			return to_return
		elif counter_num == 3:
			to_return = self.string_cont
			self.string_cont = self.string_cont + 1
			return to_return
		elif counter_num == 4:
			to_return = self.bool_cont
			self.bool_cont = self.bool_cont + 1
			return to_return
		elif counter_num == 5:
			to_return = self.nodes_cont
			self.nodes_cont = self.nodes_cont + 1
			return to_return
		elif counter_num == 6:
			to_return = self.arc_cont
			self.arc_cont = self.arc_cont + 1
			return to_return
		elif counter_num == 7:
			to_return = self.directed_cont
			self.directed_cont = self.directed_cont + 1
			return to_return
		elif counter_num == 8:
			to_return = self.undirected_cont
			self.undirected_cont = self.undirected_cont + 1
			return to_return
		else:
			return -1
