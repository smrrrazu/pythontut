def add_number(*args):
	total = 0
	for a in args:
		total +=a
	print (total)

add_number (1,2,3,4)


def health_calculator(age, apple_ate, cigs_smoked):
	answer = (100-age) + (apple_ate*3.5) - (cigs_smoked*2)
	print(answer)

list_test = [35,2,0]

health_calculator(list_test[0],list_test[1],list_test[2])
health_calculator(*list_test)

#health_calculator(**kwargs)

def test_fun(**kwargs):
	print (kwargs)


test_fun(age=25,name='razu',locatioin='cph')



