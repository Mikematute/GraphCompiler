from table import Table
from oracle import consult
from memory import Memory
from algorithmQuadruple import Algorithm_Quadruple
import sys
import networkx as nx
'''
FG = nx.DiGraph()

FG.add_node(0)
FG.add_node(1)
FG.add_node(2)
FG.add_node(3)
FG.add_node(N)

// Regresa la cantidad de conexiones en el camino
nx.shortest_path_length(FG, init, dest)

// Regresa el valor del camino mas corto
nx.dijkstra_path_length(FG, init, dest)

// Siempre hacer la comprobacion para no escribir dos arcos
FG.has_edge(init, dest)
    FG.remove_edge(init, dest)
    FG.add_edge(init, dest, weight=0.0)
fALSE
    FG.add_edge(init, dest, weight=0.0)

// siempre hacer la comprobacion de que exista un camino
nx.has_path(FG, init, dest)
nx.shortest_path(FG, init, dest)

// siempre hacer la comprobacion de que no se borre un arco inexistente
FG.has_edge(init, dest)
FG.remove_edge(init, dest)



'''

class Virtual_Machine:
    def __init__(self, g_mem = Memory(1), l_mem = Memory(2), t_mem = Memory(3),
                c_mem = Memory(4), g_vars = Table(), quad = Algorithm_Quadruple()):
        self.global_mem     = g_mem
        self.local_mem      = l_mem
        self.temporal_mem   = t_mem
        self.constant_mem   = c_mem
        self.globalVars     = g_vars
        self.quadruples     = quad
        self.aux_function   = "main"
        self.s_context      = []
        self.s_local        = []
        self.s_temporal     = []
        self.aux_local      = Memory(2)
        self.aux_temporal   = Memory(3)
        self.instruction_pointer = 0
        self.int_to_operator = {0  : '+',
                                1  : '-',
                                2  : '*',
                                3  : '/',
                                4  : '=',
                                5  : '%',
                                6  : '&&',
                                7  : '||',
                                8  : '<',
                                9  : '>',
                                10 : '<=',
                                11 : '>=',
                                12 : '!=',
                                13 : '==',
                                14 : '!',
                                15 : 'print'}

    def start(self):
        print("Starting VM")
        # Start "instruction_pointer" on 0
        self.instruction_pointer = 0
        # Save the the instruction located in the quadruple by the "instruction_pointer"
        current_quad = self.quadruples.lst_quadruples[self.instruction_pointer]

        # Read the quadruples until there is one with the "END" instruction
        while(current_quad.operation != "END"):
            self.perform_operation(current_quad)
            current_quad = self.quadruples.lst_quadruples[self.instruction_pointer]
            

    def perform_operation(self, quad):
        operation = quad.operation
        #--------------------------- a d d i t i o n ---------------------------
        if operation == 0:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            if isinstance(l_op, str):
                l_op = l_op.strip("\"")
                r_op = r_op.strip("\"")
            result = l_op + r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ s u b s t r a c t i o n ----------------------
        if operation == 1:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op - r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------------------- p r o d u c t ----------------------------
        if operation == 2:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op * r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #--------------------------- d i v i s i o n ---------------------------
        if operation == 3:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op / r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------- a s s i g n a t i o n -----------------------
        if operation == 4:
            # Get the left operator
            if str(quad.element_1)[0] == "(":
                memory_id = self.search_in_memory(int(str(quad.element_1)[1:-1]))
            else:
                memory_id = quad.element_1
            # Get the right operator
            value = self.search_in_memory(quad.result)
            # Cast the result into the appropiate type according to the oracle
            # Save the result in the left operator
            self.save_in_memory(memory_id, value)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #----------------------------- m o d u l o -----------------------------
        if operation == 5:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op % r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------------- a n d --------------------------------
        if operation == 6:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op and r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #--------------------------------- o r ---------------------------------
        if operation == 7:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op or r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------- l e s s    t h a n --------------------------
        if operation == 8:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op < r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------- m o r e    t h a n --------------------------
        if operation == 9:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op > r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ l e s s  e q  t h a n ------------------------
        if operation == 10:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op <= r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ m o r e  e q  t h a n ------------------------
        if operation == 11:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op >= r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------- d i f f e r e n t --------------------------
        if operation == 12:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op != r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ e q u a l ------------------------------
        if operation == 13:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op == r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------------- n o t --------------------------------
        if operation == 14:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Perform the operation
            result = not l_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ p r i n t ------------------------------
        elif operation == 15:
            # Get the operator
            l_op = self.search_in_memory(quad.element_1)
            # Perform the operation
            print(str(l_op).strip("\""))
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------- g o t o -------------------------------
        elif operation == 'GOTO':
            # Skip the instruction pointer to the number indicated
            self.instruction_pointer = quad.result - 1
        #------------------------------ g o t o v ------------------------------
        elif operation == 'GOTOV':
            # Get the boolean expression
            l_op = self.search_in_memory(quad.element_1)
            # Evaluate if the expression is TRUE
            result = l_op == True
            # If the expression is TRUE then move the instruction pointer to the
            # specified jump in the result field (indicated in the quadruple)
            if result:
                self.instruction_pointer = quad.result - 1
            else:
                self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ g o t o f ------------------------------
        elif operation == 'GOTOF':
            # Get the boolean expression
            l_op = self.search_in_memory(quad.element_1)
            # Evaluate if the expression is FLASE
            result = l_op == False
            # If the expression is FLASE then move the instruction pointer to the
            # specified jump in the result field (indicated in the quadruple)
            if result:
                self.instruction_pointer = quad.result - 1
            else:
                self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------------- e r a --------------------------------
        elif operation == 'ERA':
            # Saves the current instruction pointer
            # allocate memory for new function
            self.aux_function = quad.element_1
            self.aux_local = Memory(2)
            self.aux_temporal = Memory(3)

            for x in range(self.globalVars.table_functions[self.aux_function].variables + 10):
                self.aux_local.save_memory_value("", 0)
                self.aux_local.save_memory_value("", 1)
                self.aux_local.save_memory_value("", 2)
                self.aux_local.save_memory_value("", 3)
                self.aux_local.save_memory_value("", 4)

            for x in range(self.globalVars.table_functions[self.aux_function].temporal + 10):
                self.aux_temporal.save_memory_value("", 0)
                self.aux_temporal.save_memory_value("", 1)
                self.aux_temporal.save_memory_value("", 2)
                self.aux_temporal.save_memory_value("", 3)
                self.aux_temporal.save_memory_value("", 4)

            # Advance the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ p a r a m ------------------------------
        elif operation == 'PARAM':
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # save operator on the memory space given
            keys = list(self.globalVars.table_functions[self.aux_function].vars_table.keys())
            param = int(quad.result[-1])
            mem = self.globalVars.table_functions[self.aux_function].vars_table[keys[param]].direction
            self.aux_local.save_to_memory(l_op, mem)
            # Advance the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ g o s u b ------------------------------
        elif operation == 'GOSUB':
            # Get the name of the function to be called
            function_name = quad.element_1
            # Get the instruction number where the function starts
            function_ip = self.globalVars.table_functions[function_name].init_quadruple
            # Stack current memory and place function in current context
            self.s_local.append(self.local_mem)
            self.s_temporal.append(self.temporal_mem)

            self.local_mem = self.aux_local
            self.temporal_mem = self.aux_temporal
            # Save the next instruction pointer in the stack of IPs, so the program
            # can return to the next instruction
            self.quadruples.push_ip(self.instruction_pointer + 1)
            self.quadruples.push_function(function_name)
            # Change the instruction pointer to that function
            self.instruction_pointer = function_ip - 1
        #----------------------------- r e t u r n -----------------------------
        elif operation == 'RETURN':
            # Get the left operator
            memory_id = self.search_for_memory(self.quadruples.peek_function())
            # Get the right operator
            value = self.search_in_memory(quad.element_1)
            # Cast the result into the appropiate type according to the oracle
            # Save the result in the left operator
            self.save_in_memory(memory_id, value)

            # Retrieve the last instruction pointer added to the functions stack
            last_ip = self.quadruples.pop_ip()
            self.quadruples.pop_function()
            # Return the instruction pointer
            self.instruction_pointer = last_ip
        #---------------------------- e n d p r o c ----------------------------
        elif operation == 'ENDPROC':
            # return stack memory
            self.local_mem = self.s_local.pop()
            self.temporal_mem = self.s_temporal.pop()
            # Retrieve the last instruction pointer added to the functions stack
            last_ip = self.quadruples.pop_ip()
            self.quadruples.pop_function()
            # Return the instruction pointer
            self.instruction_pointer = last_ip
        #------------------------------- V E R F -------------------------------
        elif operation == 'VERF':
            # Get the index and the upper/lower limits to be evaluated
            index = self.search_in_memory(quad.element_1)
            lower_lim = quad.element_2
            upper_lim = quad.result
            # verify that the value of the index is in between the lower and upper
            # bounds
            if lower_lim <= index and index < upper_lim:
                # Advance the instruction pointer
                self.instruction_pointer = self.instruction_pointer + 1
            else:
                self.print_error("array outbounds", True)
        #------------------------ c o n s t r u c t o r ------------------------
        elif operation == 'CONSTCT':
            # Get the size of the graph
            graph_size = quad.element_1
            # Get The address where the graph data will be stored
            graph_address = quad.result
            # Build a blank graph object
            new_graph = nx.DiGraph()
            # Add blank nodes to the graph object
            for i in range(graph_size):
                new_graph.add_node(i)

            # Save the result in the specified address
            self.save_in_memory(graph_address, new_graph)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------------------- a d d n o d e ----------------------------
        elif operation == 'ADDNODE':
            # Retrieve the value of the node
            node_value = self.search_in_memory(quad.element_1)
            # Retrieve the index to which the node will be added
            node_index = self.search_in_memory(quad.element_2)
            # Retrieve the graph memory address
            graph_address = quad.result
            # Retrieve the real node memory address to which the value will be saved
            node_address = self.get_node_address(graph_address, node_index)
            # Save the value of the node in the given address
            self.save_in_memory(node_address, node_value)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------------------- g e t n o d e ----------------------------
        elif operation == 'GETNODE':
            # Retrieve the index to which the node will be looked for
            node_index = self.search_in_memory(quad.element_1)
            # Retrieve the graph memory address
            graph_address = quad.element_2
            
            # Retrieve the real node memory address to which the value will be retrieved
            node_address = self.get_node_address(graph_address, node_index)

            # Retrieve the value stored in that node
            node_value = self.search_in_memory(node_address)

            # Save the value of the node in the given temporal address
            self.save_in_memory(quad.result, node_value)

            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------------------- n o d e m e m ----------------------------
        elif operation == 'NODEMEM':
            # Get the graph address
            graph_address = quad.element_1
            memory_type = int(int(graph_address) / 10000)

            if memory_type == 1:
                graph_address =  self.global_mem.get_memory_value(graph_address)

            elif memory_type == 2:
                graph_address = self.local_mem.get_memory_value(graph_address)
            
            # Strip the ( ) parenthesis from the node
            graph_address = int(str(graph_address)[1:-1])
            
            # Get the index 
            node_index = self.search_in_memory(quad.element_2)
            
            # Retrieve the address that points to the begining of the edges
            node_address = int(graph_address) + (2 * int(node_index)) + 1
            
            # Save that address in the temporal asigned
            self.save_in_memory(quad.result, node_address)

            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------------------- a d d c o n n ----------------------------
        elif operation == 'ADDCONN':
            # Retrieve the content of the temporal value
            temp_value = self.search_in_memory(quad.element_1)
            # Retrive the content of the index
            index = self.search_in_memory(quad.element_2)
            # Retrieve the content of the weight
            weight = self.search_in_memory(quad.result)


            edge_start = self.search_in_memory(temp_value)
            edge_start = int(str(edge_start)[1:-1])

            #print("temporal vlaue: " + str(temp_value) + ", index: " + str(index) + ", weight: " + str(weight))
            #print("Edge     vlaue: " + str(edge_start) + ", index: " + str(index) + ", weight: " + str(weight))

            edge_header = int(edge_start) + (2 * int(index))
            edge_destiny = int(edge_start) + (2 * int(index)) + 1
            node_destiny = "X"

            # Save in memory the destiny of the connection
            self.save_in_memory(edge_header, weight)
            # Save in memory the weight of the connection
            self.save_in_memory(edge_destiny, index)

            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #--------------------- g r a p h    a d d n o d e ----------------------
        elif operation == 'GADDCON':
            # Get the origin of the connection
            node_init = self.search_in_memory(quad.element_1)
            # Get the destiny of the conenction
            node_dest = self.search_in_memory(quad.element_2)
            # Get the address of the graph object
            graph_address = int(quad.result) + 1
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
            
            # Get the new quadruple of that instructino pointer
            new_quad = self.quadruples.lst_quadruples[self.instruction_pointer]
            # Get the weight of the connection
            con_weight = self.search_in_memory(new_quad.element_1)
            # Retrieve the graph object from the graph address
            graph = self.search_in_memory(graph_address)
            # Look if there is already a connection between the given nodes
            if graph.has_edge(node_init, node_dest):
                # There is a coonection, delete it
                graph.remove_edge(node_init, node_dest)

            # Build a new connection between the nodes with the given weight
            graph.add_edge(node_init, node_dest, weight=con_weight)

            # Save the new graph in the given address
            self.save_in_memory(graph_address, graph)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------- g r a p h    a d d w e i g h ---------------------
        elif operation == 'NODEMEM':
            # Get the graph address
            graph_address = quad.element_1
            memory_type = int(int(graph_address) / 10000)

            if memory_type == 1:
                graph_address =  self.global_mem.get_memory_value(graph_address)

            elif memory_type == 2:
                graph_address = self.local_mem.get_memory_value(graph_address)
            
            # Strip the ( ) parenthesis from the node
            graph_address = int(str(graph_address)[1:-1])
            
            # Get the index 
            node_index = self.search_in_memory(quad.element_2)
            
            # Retrieve the address that points to the begining of the edges
            node_address = int(graph_address) + (2 * int(node_index)) + 1
            
            # Save that address in the temporal asigned
            self.save_in_memory(quad.result, node_address)

            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------ p r i n t    c o n n e c t i o n s -----------------
        elif operation == 'PRINTCO':
            # Get the starting node inside the graph address
            node_header = self.search_in_memory(quad.element_1)
            node_header = int(str(node_header)[1:-1])
            # Get the size of the graph
            graph_size = quad.element_2
            # Get the index node where we will check the connections 
            index = self.search_in_memory(quad.result)

            # Get the header name of the node on the left side
            node_header = int(node_header) + (int(index) * 2)
            node_start = self.search_in_memory(node_header)
            node_connections = int(node_header) + 1
            node_connections = self.search_in_memory(node_connections)
            node_connections = int(str(node_connections)[1:-1])
            #print(node_connections)

            # Go through all the possible connections that a node can have
            for i in range(graph_size):           
                # Get the connection weight
                weight = int(node_connections) + (i * 2)
                weight = self.search_in_memory(weight)
                # If the weight is different from an empty string
                if (weight != ""):
                    # Get the header name of the node on the right side
                    node_end = int(node_connections) + (i * 2) + 1
                    node_end = self.search_in_memory(node_end)
                    node_begin= self.search_in_memory(quad.element_1)
                    node_begin= int(str(node_begin)[1:-1])
                    node_end =  node_begin + (int(node_end) * 2 )
                    node_end = self.search_in_memory(node_end)

                    # Display the result
                    weight = str(weight)
                    node_start = str(node_start)
                    node_end = str(node_end)
                    print('{0:15} ==> {1:3} ==> {2:15}'.format(node_start, weight, node_end))

            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------- w e i g h t   o f   s h o r t p a t h ----------------
        elif operation == 'SHORTWE':
            # Get the origin of the connection
            node_init = self.search_in_memory(quad.element_1)
            # Get the destiny of the connection
            node_dest = self.search_in_memory(quad.element_2)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
            # Get the new quadruple of that instruction pointer
            new_quad = self.quadruples.lst_quadruples[self.instruction_pointer]
            # Get the graph memory address
            graph_address = int(new_quad.element_1) + 1
            # Get the temporal address
            temp_address = new_quad.result
            # REtrieve the graph object
            graph = self.search_in_memory(graph_address)
            # Look if there exists a path from one node to another
            if nx.has_path(graph, node_init, node_dest):
                # Perform the operation of shortpath
                result = nx.dijkstra_path_length(graph, node_init, node_dest)
            else:
            # There was no short path, return -1
                result = -1

            result = int(result)
            # Save the result on the temporal assigned
            self.save_in_memory(temp_address, result)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------- w e i g h t   o f   s h o r t p a t h ----------------
        elif operation == 'SHORTNO':
            # Get the origin of the connection
            node_init = self.search_in_memory(quad.element_1)
            # Get the destiny of the connection
            node_dest = self.search_in_memory(quad.element_2)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
            # Get the new quadruple of that instruction pointer
            new_quad = self.quadruples.lst_quadruples[self.instruction_pointer]
            # Get the graph memory address
            graph_address = int(new_quad.element_1) + 1
            # Get the temporal address
            temp_address = new_quad.result
            # REtrieve the graph object
            graph = self.search_in_memory(graph_address)
            # Look if there exists a path from one node to another
            if nx.has_path(graph, node_init, node_dest):
                # Perform the operation of shortpath
                result = nx.shortest_path(graph, node_init, node_dest)
                # Retrieve the names of those nodes
                for i in range(len(result)-1):
                    node_beg = result[i]
                    node_end = result[i+1]
                    node_beg = self.get_node_address(graph_address-1, node_beg)
                    node_end = self.get_node_address(graph_address-1, node_end)
                    node_beg = self.search_in_memory(node_beg)
                    node_end = self.search_in_memory(node_end)
                    print('{0:15} ==> {1:15}'.format(node_beg, node_end))
            else:
            # There was no short path, return -1
                result = -1

            
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------ d e l e t e    c o n n e c t i o n -----------------
        elif operation == 'DELETEC':
            # Get the origin of the connection
            node_init = self.search_in_memory(quad.element_1)
            # Get the destiny of the connection
            node_dest = self.search_in_memory(quad.element_2)
            # Get the graph memory address
            graph_address = quad.result
            # Retrieve the graph object
            graph = self.search_in_memory(int(graph_address) + 1)

            # Look if there exists a connection from one node to another
            if graph.has_edge(node_init, node_dest):
                # Delete such connection on the graph object
                graph.remove_edge(node_init, node_dest)
                # Get both addresses that contain the connection of a node
                edge_header_address = self.get_address_for_edgeheader(graph_address, node_init, node_dest)
                edge_pointer_address = int(edge_header_address) + 1
                # Delete the data from the nedge memory
                self.save_in_memory(edge_header_address, "")
                self.save_in_memory(edge_pointer_address, "")
                
            # Save the modified graph on the graph_memory
            self.save_in_memory((int(graph_address) + 1), graph)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ d e l e t e    n o d e -----------------------
        elif operation == 'DELETEN':
            # Get the index of the node to be deleted
            node_index = self.search_in_memory(quad.element_1)
            # Get the graph memory address
            graph_address = quad.result
            # Get the graph size
            graph_size = quad.element_2
            # Retrieve the graph object
            graph = self.search_in_memory(int(graph_address) + 1)
            # Remove the node from the graph
            graph.remove_node(node_index)
            # Add the node again
            graph.add_node(node_index)
            # Remove the node edges data
            for i in range(graph_size):
                edge_header_address = self.get_address_for_edgeheader(graph_address, node_index, i)
                edge_pointer_address = int(edge_header_address) + 1
                self.save_in_memory(edge_header_address, "")
                self.save_in_memory(edge_pointer_address, "")
            
            # Remove from other nodes the edges that reach the node
            for n in range(graph_size):
                # Do this for all the connections except for the ones of th node
                # we already reseted
                if n != node_index:
                    # Get the edge memory addresses
                    edge_header_address = self.get_address_for_edgeheader(graph_address, n, node_index)
                    edge_pointer_address = int(edge_header_address) + 1
                    # Delete the information form those addresses
                    self.save_in_memory(edge_header_address, "")
                    self.save_in_memory(edge_pointer_address, "")

            # Remove the header from the node
            
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ n o d e    d e g r e e -----------------------
        elif operation == 'DEGREE':
            # Get the graph address
            graph_address = quad.element_2
            # Get the index of the node to be evaluated
            node_index = self.search_in_memory(quad.element_1)
            # Get the temporal address where the result will be saved
            temp_address = quad.result
            # Retrieve the graph object address
            graph_address = int(graph_address) + 1
            # Retrieve the graph object
            graph = self.search_in_memory(graph_address)
            # Perform the operation and save the result
            degree = graph.degree(int(node_index))
            # Save the result in the specified temporal memory
            self.save_in_memory(temp_address, degree)
            # Move the instruction pointer
            self.instruction_pointer = self.instruction_pointer + 1


    def search_in_memory(self, memory_id):
        # Verify escape int 
        if str(memory_id)[0] == '$':
            return int(str(memory_id)[1:])
        else:
            if str(memory_id)[0] == '(':
                aux_mem = int(str(memory_id)[1:-1])
                # Obtains the first digit to know which memory the ID belongs to
                mem_type = int(aux_mem / 10000)

                # If the result is 1, it is the global memory
                if mem_type == 1:
                    new_mem = self.global_mem.get_memory_value(aux_mem)
                # If the result is 2, it is the local memory
                elif mem_type == 2:
                    new_mem = self.local_mem.get_memory_value(aux_mem)
                # If the result is 3, it is the temporal memory
                elif mem_type == 3:
                    new_mem = self.temporal_mem.get_memory_value(aux_mem)
                # If the result is 4, it is the constant memory
                elif mem_type == 4:
                    new_mem = self.constant_mem.get_memory_value(aux_mem)
            else:
                new_mem = memory_id
            
            # Obtains the first digit to know which memory the ID belongs to
            memory_type = int(new_mem / 10000)

            # If the result is 1, it is the global memory
            if memory_type == 1:
                return self.global_mem.get_memory_value(new_mem)
            # If the result is 2, it is the local memory
            elif memory_type == 2:
                return self.local_mem.get_memory_value(new_mem)
            # If the result is 3, it is the temporal memory
            elif memory_type == 3:
                return self.temporal_mem.get_memory_value(new_mem)
            # If the result is 4, it is the constant memory
            elif memory_type == 4:
                return self.constant_mem.get_memory_value(new_mem)


    def search_for_memory(self, variable):
        # Search on every table and retrieve the variable object
        variable_obj = self.globalVars.search_variable_by_id(variable)
        # Send back the variable memory address
        return variable_obj.direction


    def save_in_memory(self, memory_id, result):
        memory_type = int(memory_id / 10000)

        # If the result is 1, then save the result in the global memory
        if memory_type == 1:
            self.global_mem.save_to_memory(result, memory_id)
        # If the result is 2, then save the result in the local memory
        elif memory_type == 2:
            self.local_mem.save_to_memory(result, memory_id)
        # If the result is 3, then save the result in the temporal memory
        elif memory_type == 3:
            self.temporal_mem.save_to_memory(result, memory_id)
        # If the result is 4, then save the result in the constant memory
        elif memory_type == 4:
            self.constant_mem.save_to_memory(result, memory_id)


    def cast_to_type(self, quadruple, value):
        '''
        # Retrive the type of the left operand involved in the operation
        type_left = quadruple.element_1
        type_left = self.globalVars.search_variable_by_memory(type_left)
        type_left = type_left.type
        # Retrive the type of the right operand involved in the operation
        type_right = quadruple.element_2
        type_right = self.globalVars.search_variable_by_memory(type_right)
        type_right = type_right.type
        # Retrieve the operation being performed
        operation = quadruple.operation
        # Consult the oracle to get the type of the result
        result_type = consult(operation, type_left, type_right)
        '''
        memory_type = int(quadruple.result / 10000)
        data_type = quadruple.result - (memory_type * 10000)
        data_type = int(data_type / 1000)
        result_type = data_type

        # Return the result casted to that type
        if result_type == 0:
            return int(value)
        elif result_type == 1:
            return float(value)
        elif result_type == 2:
            return chr(value)
        elif result_type == 3:
            return str(value)
        elif result_type == 4:
            return bool(value)


    def print_error(self, error_type, program_stop, variable=""):

        if error_type == "array outbounds":
            print("Index exceeds dimensions of array")
            if program_stop:
                sys.exit("Ending program due to errors")


    def get_node_address(self, graph_address, index):
        # Get the memory address where the graph points (the initial node)
        node_address = self.search_in_memory(int(graph_address))
        
        # Strip the ( ) parenthesis
        node_address = str(node_address)[1:-1]
        
        # Add to the initial node address, twice the index variable
        node_address = int(node_address) + (int(index) * 2)
        
        # Return that address
        return node_address

    def get_address_for_edgeheader(self, graph_address, index_init, index_dest):

        node_init_address = self.search_in_memory(int(graph_address))
        node_init_address = str(node_init_address)[1:-1]
        
        edge_init_address = int(node_init_address) + (2 * index_init) + 1
        edge_init_address = self.search_in_memory(edge_init_address)
        edge_init_address = str(edge_init_address)[1:-1]

        return int(edge_init_address) + (2 * int(index_dest))

    def get_address_for_edgepointer(self, graph_address, index_init, index_dest):

        node_init_address = self.search_in_memory(int(graph_address))
        node_init_address = str(node_init_address)[1:-1]
        
        edge_init_address = int(node_init_address) + (2 * index_init) + 1
        edge_init_address = self.search_in_memory(edge_init_address)
        edge_init_address = str(edge_init_address)[1:-1]

        return int(edge_init_address) + (2 * int(index_dest)) + 1




