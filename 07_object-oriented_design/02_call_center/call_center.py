"""
Imagine you have a call center with three levels of employees: respondent,
manager, and director. An incoming telephone call must be first allocated
to a respondent who is free. If the respondent can't handle the call, he
or she must escalate the call to a manager. If the manager is not free or
not able to handle it, then the call should be escalated to a director.
Design the classes and data structures for this program. Implement a method
dispatchCall() which assigns a call to the first available employee.
"""


class Staff_Queue():
	employee_type = {0: 'Respondent', 1: 'Manager', 2: 'Director'}

	def __init__(self, level):
		self.level = level
		self.employees_available = []
		self.assigned_calls = {}  # assigned_calls[call_id] = staff_assigned
		self.calls_on_hold = []


	def __str__(self):
		queue_str = '\t\t{0}s:\n'.format(self.employee_type[self.level])

		for call in self.assigned_calls.keys():
			active_call = 'Call #{0} is received by Employee #{1}\n'\
				.format(call, self.assigned_calls[call])
			queue_str += active_call

		queue_str += '***\n'
		queue_str += 'Employees available: {0}\n'.format(self.employees_available)
		queue_str += 'Num of calls on hold: {0}\n'.format(self.calls_on_hold)
		return queue_str


	def add_employee(self, new_employee):
		self.employees_available.append(new_employee)


	def assign_call(self, call_id):
		assigned_employee = None

		if len(self.employees_available) > 0:
			assigned_employee = self.employees_available.pop(0)
			self.assigned_calls[call_id] = assigned_employee
		else:
			self.calls_on_hold.append(call_id)

		return (call_id, self.level, assigned_employee)


	def end_call(self, call_id):
		employee = self.assigned_calls[call_id]
		self.employees_available.append(employee)
		del self.assigned_calls[call_id]

		return (call_id, self.level, employee)


	def can_answer_call(self):
		if len(self.employees_available) > 0:
			return True
		else:
			return False


	def have_calls_on_hold(self):
		if len(self.calls_on_hold) > 0:
			return True
		else:
			return False


	def get_call_on_hold(self):
		if len(self.calls_on_hold) > 0:
			return self.calls_on_hold.pop(0)




class Call_Center():
	def __init__(self):
		self.call_id = 1
		self.employee_id = 1
		self.assigned_calls = {}  # assigned_calls[call_id] = staff_level
		self.staff_levels = [Staff_Queue(0), Staff_Queue(1), Staff_Queue(2)]
		self.print_summary = True


	def __str__(self):
		staff_summary = ''

		for staff_list in self.staff_levels:
			staff_summary += str(staff_list)
			staff_summary += '\n'

		return staff_summary


	def add_employee(self, level=0):
		self.staff_levels[level].add_employee(self.employee_id)
		self.employee_id += 1


	def new_call(self):
		# This function is publicly called.
		call_id = self.call_id
		self.call_id += 1
		return self.dispatch_call(call_id, False)


	def end_call(self, call_id, escalate):
		# This function is publicly called.
		# escalate is True or False
		return self.dispatch_call(call_id, escalate)


	def dispatch_call(self, call_id, escalate=False):
		# This function is privately called by new_call() and end_call().

		# New calls.
		if call_id not in self.assigned_calls:
			self.assigned_calls[call_id] = 0
			assignment = self.staff_levels[0].assign_call(call_id)

			if self.print_summary:
				self.print_call_assignment(0, assignment)

		# Call ends or escalates.
		else:
			prev_level = self.assigned_calls[call_id]
			end_call_result = self.staff_levels[prev_level].end_call(call_id)

			if escalate:
				# Only level 0 or 1 calls can escalate.

				# Information about who escalated the call.
				if self.print_summary:
					self.print_call_assignment(2, end_call_result)


				# assignment_type = 3 is normal escalation.
				# assignment_type = 4 is if the manager queue is full.
				assignment_type = 3

				if prev_level == 0:
					# If the manager is not free or not able to handle it,
					# then the call should be escalated to a director.
					if self.staff_levels[1].can_answer_call():
						next_level = prev_level + 1
					else:
						next_level = prev_level + 2
						assignment_type = 4

				elif prev_level == 1:
					next_level = prev_level + 1

				self.assigned_calls[call_id] = next_level
				assignment = self.staff_levels[next_level].assign_call(call_id)

				if self.print_summary:
					self.print_call_assignment(assignment_type, assignment)

			else:
				del self.assigned_calls[call_id]

				if self.print_summary:
					self.print_call_assignment(1, end_call_result)


			# After a call ends, check and assign calls on hold.
			if self.staff_levels[prev_level].have_calls_on_hold():
				# next_call should be a call_id.
				next_call = self.staff_levels[prev_level].get_call_on_hold()
				assignment = self.staff_levels[prev_level].assign_call(next_call)

				if self.print_summary:
					self.print_call_assignment(5, assignment)


	def print_call_assignment(self, assignment_type, assignment):
		# Normal call assignment.
		if assignment_type == 0:
			call_num, assigned_level, assigned_employee = assignment

			if assigned_employee is None:
				print('Level {0}: Call {1} is on hold.'
					.format(assigned_level, call_num))
			else:
				print('Level {0}: Call {1} is picked up by employee {2}.'
					.format(assigned_level, call_num, assigned_employee))

		# Call ends with no escalation.
		elif assignment_type == 1:
			call_num, prev_level, available_employee = assignment
			print('Level {0}: Employee {1} ended call {2}.'
				.format(prev_level, available_employee, call_num))

		# Which employee escalated the call?
		elif assignment_type == 2:
			call_num, prev_level, available_employee = assignment
			print('Level {0}: Employee {1} escalated call {2}.'
				.format(prev_level, available_employee, call_num))

		# Normal escalation.
		elif assignment_type == 3:
			call_num, assigned_level, assigned_employee = assignment

			print('Call {0} is escalated to level {1}.'
				.format(call_num, assigned_level))

			self.print_call_assignment(0, assignment)

		# Escalating straight from respondent to directors.
		elif assignment_type == 4:
			print('Manager queue is full. Escalating to directors.')
			self.print_call_assignment(0, assignment)

		# Call on hold being picked up.
		elif assignment_type == 5:
			call_num, assigned_level, assigned_employee = assignment
			print('Level {0}: Call on hold {1} is picked up by employee {2}.'
				.format(assigned_level, call_num, assigned_employee))









