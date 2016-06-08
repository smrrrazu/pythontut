def print_dict_sorted(dict):
    for key in sorted(dict):
        print (key, dict[key])

def inv_to_assign(invs):
	not_solved_invs= {}
	for inv in invs:
		if invs[inv]['qm_id'] == None:
			not_solved_invs[inv] = {'qm_id': None}

	return not_solved_invs

def solved_inv_per_qm(invs, qms):
	inv_per_qm= {}
	for qm in qms:
		counter = 0
		for inv in invs:
			if invs[inv]['qm_id'] == qm:
				counter +=1
		if counter != 0:
			inv_per_qm[qm] = counter
	return inv_per_qm

def inv_to_assign_per_qm(qms, solved_inv_per_qm, total_invs):
	num_qm= len(qms)
	num_inv_per_qm = total_invs // num_qm
	reminder = total_invs % num_qm
	inv_to_assign_per_qm = {}
	print(num_inv_per_qm,':',reminder)
	for qm in qms:
		num_to_assign = num_inv_per_qm
		if qm in solved_inv_per_qm:
			num_to_assign = num_inv_per_qm - solved_inv_per_qm[qm]
			if num_to_assign < 0:
				num_inv_per_qm = total_invs // (num_qm-1)
				continue
		print(num_to_assign)	
