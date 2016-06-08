from mylib import print_dict_sorted, inv_to_assign, solved_inv_per_qm, inv_to_assign_per_qm
from collections import OrderedDict
invs = {}
# investigations = OrderedDict()

for x in range(501,532):
	invs[x] = {'qm_id':None}

for x in range(501,510):
	invs[x]['qm_id']=201
for x in range(520,524):
	invs[x]['qm_id']=202

qm_in_this_week = {
	201:{'name':'AS'},
	202:{'name':'SR'},
	203:{'name':'AS'},

}
num_qms = len(qm_in_this_week)
total_invs = len(invs)
inv_to_assign = inv_to_assign(invs)
num_inv_to_assign = len(inv_to_assign)
solved_inv_per_qm = solved_inv_per_qm(invs, qm_in_this_week)
print(num_inv_to_assign)
print(solved_inv_per_qm)

inv_to_assign_per_qm(qm_in_this_week, solved_inv_per_qm, total_invs)
# print (inv_to_assign)
# print(total_invs)
# print(num_qms)
# print(print_dict_sorted(invs))
# print(len(invs))
# print(invs.keys())	
# print(sorted(invs))
# print(qm_in_this_week)

