from colorama import Fore
def arrays_multyplay():
    try:
        a=input(Fore.CYAN+'Enter your  first array : '+Fore.RESET)
        b=input(Fore.CYAN+'Enter your second array : '+Fore.RESET)
        print((Fore.GREEN+'your first array is :  {}'+Fore.RESET).format(a))
        print((Fore.GREEN+'your second array is : {}'+Fore.RESET).format(b))
        c= a[0]*b[0] + a[1]*b[2] , a[0]*b[1] + a[1]*b[3] , a[2]*b[0] + a[3]*b[2] , a[2]*b[1] + a[3]*b[3]
        print(((Fore.BLUE+'your multyplay array is : {} ')+Fore.RESET).format(c))
    except KeyboardInterrupt:
		print (Fore.RED+"\nABORTED PROGRAM....!!" +Fore.RESET)
def arrays_Divisiony():
    try:
        a=input(Fore.CYAN+'enter your array : '+Fore.RESET)
        print((Fore.GREEN+'your  array is :  {}'+Fore.RESET).format(a))
        dlta = float(a[0]*a[3] - a[1]*a[2])
        print((Fore.RED+'your Dlta is : {}'+Fore.RESET).format(int(dlta)))
        j = float(a[3]/dlta) , float(-a[1]/dlta) , float(-a[2]/dlta) , float(a[0]/dlta)
        print((Fore.BLUE+' your  Divisiony array is : {}'+Fore.RESET).format(j))
    except KeyboardInterrupt:
		print (Fore.RED+"\nABORTED PROGRAM....!!" +Fore.RESET)
def arrays_Divisiony_G():
    try:
        a=input(Fore.CYAN+'Enter your  first array : '+Fore.RESET)
        b=input(Fore.CYAN+'Enter your second array : '+Fore.RESET)
        print((Fore.GREEN+'your first array is :  {}'+Fore.RESET).format(a))
        print((Fore.GREEN+'your second array is : {}'+Fore.RESET).format(b))
        dlta = float(a[0]*a[3] - a[1]*a[2])
        print(((Fore.RED+'your Dlta is : {}')+Fore.RESET).format(int(dlta)))
        j = (float(a[3]/dlta) , float(-a[1]/dlta) , float(-a[2]/dlta) , float(a[0]/dlta))
        print((Fore.BLUE+'your  Divisiony array is : {}'+Fore.RESET).format(j))
        l = j[0]*b[0] + j[1]*b[2] , j[0]*b[1] + j[1]*b[3] , j[2]*b[0] + j[3]*b[2] , j[2]*b[1] + j[3]*b[3]
        print((Fore.RED+'your New array is : {}'+Fore.RESET).format(l))
    except KeyboardInterrupt:
		print (Fore.RED+"\nABORTED PROGRAM....!!" +Fore.RESET)
def finsh_array():
        print  (Fore.GREEN+("      / \        _   _  __  |  \/  | __ _ _ __  _   _ "))
	print  ("     / _ \ _____| | | |/ _` | |\/| |/ _` | '_ \| | | |")
	print  ("    / ___ \_____| |_| | (_| | |  | | (_| | | | | |_| |")
	print  ("   /_/   \_\     \__, |\__,_|_|  |_|\__,_|_| |_|\__, |")
	print  ("                 |___/                          |___/ ")+Fore.RESET
	print (Fore.CYAN+'1: arrays_multypay'+Fore.RESET)
	print (Fore.CYAN+'2: arrays_Divisiony'+Fore.RESET)
	print (Fore.CYAN+'3: A * B = G'+Fore.RESET)
	print (Fore.YELLOW+"Press ctrl+c to exit..." +Fore.RESET)
	try:
		def yam():
			opt = int(raw_input('Enter choice : '))
			if opt == 1	:
				arrays_multyplay()
				return yam()
			elif opt == 2:
				arrays_Divisiony()
				return yam()
			elif opt == 3:
				arrays_Divisiony_G()
				return yam()
			else :
				print (Fore.RED+"\nEnter correct choice...!!" +Fore.RESET)
				return yam()
		yam()
	except KeyboardInterrupt:
		print(Fore.RED+"\nABORTED PROGRAM....!!" +Fore.RESET)
finsh_array()
