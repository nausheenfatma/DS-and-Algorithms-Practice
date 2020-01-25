ip_addresses={}


def check_conditions(comp_str):

	leading_zero_flag=len(str(int(comp_str)))==len(comp_str)

	

	if int(comp_str) <= 255 and int(comp_str) != 0 and leading_zero_flag:
		return True
	else:
		return False


def makeIp(ipstring, component_count, ip_address):

	# basecase
	if component_count > 3 and len(ipstring)!=0:
		return

	if len(ipstring)==0 and component_count==4:
		ip_addresses[ip_address[:-1]]=0	
		return
	#

	#break ip 

	left_one=ipstring[0]
	right_one=ipstring[1:]


	if check_conditions(left_one):
		makeIp(right_one, component_count+1, ip_address+left_one+".")



	left_two=ipstring[0:2]
	right_two=ipstring[2:]	

	if check_conditions(left_two):
		makeIp(right_two, component_count+1, ip_address+left_two+".")


	left_three=ipstring[0:3]
	right_three=ipstring[3:]	


	if check_conditions(left_three):
		makeIp(right_three, component_count+1, ip_address+left_three+".")


makeIp("2552551113", 0, "")
	

print ip_addresses.keys()

	
