################################################################################
#                               Memory Class                                   #
# Class used for the simulation of different memory chaches on the sistem.     #
# For now only used as an assosiation of numbers							   #
################################################################################

from memoryArray import Memory_Array

class Memory:
	def __init__(self, memid):
		# actual way we will track how many values we currently have and assign each to a “space in memory”
		self.mem_id = memid
		start = self.mem_id * 10000
		self.int_memory 		= Memory_Array(start)
		self.float_memory 		= Memory_Array(start + 1000)
		self.char_memory 		= Memory_Array(start + 2000)
		self.string_memory 		= Memory_Array(start + 3000)
		self.bool_memory 		= Memory_Array(start + 4000)
		self.node_memory 		= Memory_Array(start + 5000)
		self.arc_memory 		= Memory_Array(start + 6000)
		self.directed_memory 	= Memory_Array(start + 7000)
		self.undirected_memory 	= Memory_Array(start + 8000)

	def used_mem(self):
		# get the starting number for the meory and substract it to the current memory coutners
		counters = {}
		start = self.mem_id * 10000
		counters[0] = self.int_memory.counter 		- start
		counters[1] = self.float_memory.counter 	- start - 1000
		counters[2] = self.char_memory.counter 		- start - 2000
		counters[3] = self.string_memory.counter 	- start - 3000
		counters[4] = self.bool_memory.counter 		- start - 4000
		counters[5] = self.node_memory.counter 		- start - 5000
		counters[6] = self.arc_memory.counter 		- start - 6000
		counters[7] = self.directed_memory.counter	- start - 7000
		counters[8] = self.undirected_memory.counter- start - 8000
		return counters

	def reset_cont(self):
	    # All cont to 0
		start = self.mem_id * 10000
		self.int_memory 		= Memory_Array(start)
		self.float_memory 		= Memory_Array(start + 1000)
		self.char_memory 		= Memory_Array(start + 2000)
		self.string_memory 		= Memory_Array(start + 3000)
		self.bool_memory 		= Memory_Array(start + 4000)
		self.node_memory 		= Memory_Array(start + 5000)
		self.arc_memory 		= Memory_Array(start + 6000)
		self.directed_memory 	= Memory_Array(start + 7000)
		self.undirected_memory 	= Memory_Array(start + 8000)

	def print_counters(self):
		print("int: " + str(self.int_memory.counter))
		print("flt: " + str(self.float_memory.counter))
		print("chr: " + str(self.char_memory.counter))
		print("str: " + str(self.string_memory.counter))
		print("bol: " + str(self.bool_memory.counter))
		print("nde: " + str(self.node_memory.counter))
		print("arc: " + str(self.arc_memory.counter))
		print("dir: " + str(self.directed_memory.counter))
		print("und: " + str(self.undirected_memory.counter))

	def get_counter(self, counter_id):
		if counter_id == "int" or counter_id == 0:
			to_return = self.int_memory.counter
			self.int_memory.increment_counter()
			return to_return
		elif counter_id == "float" or counter_id == 1:
			to_return = self.float_memory.counter
			self.float_memory.increment_counter()
			return to_return
		elif counter_id == "char" or counter_id == 2:
			to_return = self.char_memory.counter
			self.char_memory.increment_counter()
			return to_return
		elif counter_id == "string" or counter_id == 3:
			to_return = self.string_memory.counter
			self.string_memory.increment_counter()
			return to_return
		elif counter_id == "bool" or counter_id == 4:
			to_return = self.bool_memory.counter
			self.bool_memory.increment_counter()
			return to_return
		elif counter_id == "node" or counter_id == 5:
			to_return = self.node_memory.counter
			self.node_memory.increment_counter()
			return to_return
		elif counter_id == "arc" or counter_id == 6:
			to_return = self.arc_memory.counter
			self.arc_memory.increment_counter()
			return to_return
		elif counter_id == "directed" or counter_id == 7:
			to_return = self.directed_memory.counter
			self.directed_memory.increment_counter()
			return to_return
		elif counter_id == "undirected" or counter_id == 8:
			to_return = self.undirected_memory.counter
			self.undirected_memory.increment_counter()
			return to_return
		else:
			return -1

	def get_memory_value(self, memory_id):
		data_type = memory_id - (self.mem_id * 10000)
		data_type = int(data_type / 1000)

		index = memory_id - (self.mem_id * 10000)
		index = index - (data_type * 1000)

		if data_type == 0:
			return self.int_memory.get_value(index)
		elif data_type == 1:
			return self.float_memory.get_value(index)
		elif data_type == 2:
			return self.char_memory.get_value(index)
		elif data_type == 3:
			return self.string_memory.get_value(index)
		elif data_type == 4:
			return self.bool_memory.get_value(index)
		elif data_type == 5:
			return self.node_memory.get_value(index)
		elif data_type == 6:
			return self.arc_memory.get_value(index)
		elif data_type == 7:
			return self.directed_memory.get_value(index)
		elif data_type == 8:
			return self.undirected_memory.get_value(index)

	def save_memory_value(self, value, type):
		if type == 0 or type == 'int':
			self.int_memory.add_value(value)
		elif type == 1 or type == 'float':
			self.float_memory.add_value(value)
		elif type == 2 or type == 'char':
			self.char_memory.add_value(value)
		elif type == 3 or type == 'string':
			self.string_memory.add_value(value)
		elif type == 4 or type == 'bool':
			self.bool_memory.add_value(value)
		elif type == 5 or type == 'node':
			self.node_memory.add_value(value)
		elif type == 6 or type == 'arc':
			self.arc_memory.add_value(value)
		elif type == 7 or type == 'directed':
			self.directed_memory.add_value(value)
		elif type == 8 or type == 'undirected':
			self.undirected_memory.add_value(value)

	def save_to_memory(self, value, memory_id):
		memory_type = int(memory_id / 10000)

		data_type = memory_id - (memory_type * 10000)
		data_type = int(data_type / 1000)

		index = memory_id - (memory_type * 10000) - (data_type * 1000)

		if data_type == 0:
			self.int_memory.add_value_at_index(value, index)
		elif data_type == 1:
			self.float_memory.add_value_at_index(value, index)
		elif data_type == 2:
			self.char_memory.add_value_at_index(value, index)
		elif data_type == 3:
			self.string_memory.add_value_at_index(value, index)
		elif data_type == 4:
			self.bool_memory.add_value_at_index(value, index)
		elif data_type == 5:
			self.node_memory.add_value_at_index(value, index)
		elif data_type == 6:
			self.arc_memory.add_value_at_index(value, index)
		elif data_type == 7:
			self.directed_memory.add_value_at_index(value, index)
		elif data_type == 8:
			self.undirected_memory.add_value_at_index(value, index)
