import re

students = {'meirzhan': 'meir'}
# info = {'Meirzhan': {'full-name'} }
admins = {'admin' : 'admin'}
categories = ["sneakers" , "clothers"]


sneakers = {'yeezy boast 700' : 30000 , 'nike air jordan' : 35000 , 'Nike Air Force 1' : 27900 ,
 'Nike React Miler 2' : 19900 , 'Nike Air Max 90' : 25990, 'Adidas Ozweego': 18990 , 'Adidas Superstar 2': 31900 }

clothers = {'t-shirt adidas' : 5000, 'hoodie nike' : 12000 , 'shorts nike': 15900 , 'shorts adidas' : 15000 , 'socks h&m' : 890 }

basket = {}
admin_keys = admins.keys()
dict_keys = students.keys()


exi = False


def add():
    
    mdl = input('Write a model: ')
    price = int(input('Write a price: ')) 

# --------------------admin----------------------------
def admin(login):
    bool_1 = False
    if login in admin_keys:
        pas = input('Password:(if you want go back, write exi): ')
        
        if pas == admins[login]:
            bool_1 = True
            conf = 'admin'
            return conf
       
        elif pas.lower() == 'exi' or  pas.lower() == 'no':
            conf = 'exi' 
            return conf

        else:
            while not bool_1:
                n_pass = input('Wrong password:')
                if n_pass == admins[login]:
                    bool_1 = True
                    conf = 'admin'
                    return conf



# def update_model():
	



# ---------------------------------------------------------------

# def show_admin():
# 	bool_1 = True
# 	exi = True
# 	qwer = int(input('1.Models\n2.Users\nYour choice: '))
# 	while not bool_1:
		# if qwer == 1:






# ------------------------Log in ----------------ca-----------------------------------------------
def Log_in(login):
	bool_2 = False
	bool_1 = False
	exi = False
	
	while not exi:

        
		if login in dict_keys:
			password = input('Password:(if you want go back, write exi): ')
			
			if password == students[login]:
				bool_2 = True
				exi = True
				conf = 'joined'
				return conf

			elif password.lower() =='exi' or password.lower() == 'exit':
				exi = True
				conf = 'exi'
				return conf
			else:

				while not bool_2:
					n_pass = input('Wrong password:')

					if n_pass == students[login]:
						bool_2 = True
						exi = True
						conf = 'joined'
						return conf

		elif login.lower() == 'exi' or login.lower() == 'exit':
			conf = 'exi'
			return conf

		elif login in admin_keys:
			password = input('Password:(if you want go back, write exi): ')
			
			if password == admins[login]:
				exi = True
				conf = 'admin'
				return conf

			elif password.lower() =='exi' or password.lower() == 'exit':
				exi = True
				conf = 'exi'
				return conf
			else:

				while not bool_2:
					n_pass = input('Wrong password:')

					if n_pass == students[login]:
						bool_2 = True
						exi = True
						conf = 'joined'
						return conf
		else:
			while not bool_1:
				n_login = input('Wrong login, write again pls(if you want go back, write exi): ')		
				
				if n_login in dict_keys:
					n_pass = input('Password:')

					if n_pass == students[n_login]:
						bool_2 = True
						bool_1 = True
						exi = True
						conf = 'joined'
						return conf

					else:

						while not bool_2:
							n_pass = input('Wrong password:')

							if n_pass == students[n_login]:
								bool_1 = True
								bool_2 = True
								exi = True
								conf = 'joined'
								return conf

							else:
								bool_2 = False


				elif n_login.lower() == 'exi' or  n_login.lower() =='exit':
					conf = 'exi'
					return conf

# --------------------------------------------------------------------------------------------------
# -------------------Registretion--------------------------------------------------------------------------
def regist(login):
	exi = False

	while not exi:
		conf_log = input('Confirm your login: ')
		bool_2 = False

		if conf_log == login:
			ad_pass = input('Write password: ')
			conf_pass = input('Write again: ')
			bool_1 = True

			if ad_pass == conf_pass:
				bool_2 = True
				conf = 'did'
				return conf

			else:
				while not bool_2:
					added_pass = input('You have incorrectly confirmed your password, confirm again pls: ')
					confed_pass = input('Confirm again, correctly: ')

					if confed_pass == added_pass:
						bool_2 = True
						students[login] = confed_pass
						conf = 'did'
						return conf
					
					elif confed_pass.lower() == 'exi':
						conf = 'exi'
						bool_2 = True
						exi = True
						return conf

		elif conf_log == 'exi':
			exi = True
			conf = 'exi'
			return conf



# ----------------------------------------------------------------------------------------------------------


# ---------------categery-------------------------
def category(len):
	count = 0

	while count <=len :
		count+=1
		print(f"{count}.{categories[count-1]}")

		if count ==  len:
			cat_ans = int(input('Your choice:'))
			retrn = {categories[cat_ans-1]}
			print(retrn)
			return retrn

# -------------------------------------------------

# -------------------------------model list ---------------------------------
def models(cat_choice):
	if cat_choice == {'sneakers'}:
		answer = input('Do you want watch models? ')
		if answer.lower() == 'yes' or answer.lower() == 'y':
			i = 0
			for key in sneakers.keys():
				i+=1
				print(f"{i}.'{key}' - {sneakers[key]} tg")
				
				
			return sneakers
		elif answer.lower() == 'no' or answer.lower() == 'exi':
			print('thank you for you attention!')
			return answer
		# exi = input('')
		
		else:
			models(cat_choice)
			
	elif cat_choice == {'clothers'}:
		answer = input('Do you want watch models? ')

		if answer.lower() == 'yes' or answer.lower() == 'y':
			i = 0
			for key in clothers.keys():
				i+=1
				print(f"{i}.'{key}' - {clothers[key]} tg")
				
			return clothers

		elif answer.lower() == 'no' or answer.lower() == 'exi':
			print('thank you for you attention!')
			return answer
		
		else:
			models(cat_choice)
			
# --------------------------------------------------------------------------


main = False

while not main:
	print('------------------------------------------------------------------------')
	print("\n  -'MTB'- shop\n")
	# print('\n')
	answer = int(input('  1.Log in \n  2.Need an account\n  3.Watch products\n- Your answer: '))
	print('\n')
	print('------------------------------------------------------------------------')

	if answer == 1:

		login = input('Login(if you want go back, write exi): ')
		confirm = Log_in(login)
        
		exi = False
		stop_buy= False
		while not exi:
            
            	
			if confirm == 'joined':
				main = False
				print('')			
				print("   | 'MTB'- shop |")
				print('   ---------------')
				print('')
				n_ans = int(input('1.categeries\n2.basket\n3.log out\n '))
				print('\n------------------------------------------------------------------------')
				if n_ans == 1:
					exi = True
					len_category = len(categories)
					cat_choice = category(len_category)
					dict_model = models(cat_choice)
					stop_buy= False

					if dict_model == 'no' or 'n' or 'exi':
						stop_buy= True
						exi = False
						print('\n')
					
					# print(len(dict_model))
					stop_buy= False
					while not stop_buy:
						answer = input("Do you want buy(if yes,write the id of the products,else write no or exi): ")
						numer = answer.isnumeric()

						
						# if answer.isdigit():
						if numer == True:
							if int(answer) < len(dict_model) or int(answer) == len(dict_model):
								keys = []
								answer = int(answer)
								for i in dict_model.keys():
									keys.append(i)
								
								basket[str(keys[answer-1])] = dict_model[str(keys[answer-1])]


								print(f'{basket} bought   ')
						

					
						else:

							if answer.lower() == 'exi' or answer.lower() == 'no':
								exi = False
								main = True
								stop_buy= True
								i = input()


							else:
								exi = False



				elif n_ans == 2:
					i = 0
					exi = True
					b_basket = False
					empty_basket = not bool(basket)

					if empty_basket == True:
						print("        Your basket is 'empty'.")
						i = input('')
						exi = False
					else:

						while not b_basket:
							i = 0
							for key in basket.keys():
								i+=1
								print(f"{str(i)}.'{key}' - {basket[key]} tg")
							
							
							# if empty_basket == False:
							value = 0 
							i=0
							keys = []
								
							for i in basket.keys():
								keys.append(i)

							for i in range(len(keys)):
								value += int(basket[str(keys[i])])

							print(f"             'Total: {str(value)} tg' ")
							answer = input("Do you want to pay or delete some things or clear(for clear write word 'clear') the basket: ")
							numer = answer.isnumeric()



							if answer.lower() == 'yes' or answer.lower() == 'y':
								print('Thank you!!!')
								basket.clear()
								b_basket = True
								exi = False



							elif numer == True:
								if int(answer) < len(basket) or int(answer) == len(basket):
									keys = []
									answer = int(answer) 
								

									for i in basket.keys():
										keys.append(i)
							
									basket.pop(str(keys[answer-1]))
									b_basket = False
							elif answer.lower() == 'clear' or answer.lower() == 'cl':
								basket.clear()
								qw = input("Your basket was cleared! ")
								b_basket = True
								exi = False

							elif answer.lower() == 'exi' or 'no':
								b_basket = True
								exi = False


				elif n_ans ==3:
					print('You logged out!')
					exi = True

				else:
					exi = False


			elif confirm == 'admin':
				print('admin')
				main = False
				exi = True
				# print('')			
				# print("   | 'MTB'- shop(admin) |")
				# print('   ---------------')
				# print('')
				# n_ans = int(input('1.categeries\n2.accounts\n3.log out\n '))
				# print('\n------------------------------------------------------------------------')
				# 	if n_ans = 1:

			elif confirm == 'exi':
				main = False
				exi = True
						

    




								


				



	elif answer == 2:
		login = input('Write new login, pls: ')
		confirm = regist(login)




		if confirm == 'did':
			print(students)

		elif confirm == 'exi':
			main = False
			exi = True

	elif answer ==3:
		len_category = len(categories)
		cat_choice = category(len_category)

		list_model = models(cat_choice)
		exi = input('')

		# if cat_choice == {'sneakers'}:
		# 	answer = input('Do you want watch models? ')
		# 	if answer.lower() == 'yes':
		# 		i = 0
		# 		for key in sneakers.keys():
		# 			i+=1
		# 			print(f"{i}.{key} - {sneakers[key]}")
			

		# 	elif answer.lower() == 'no' or answer.lower() == 'exi':
		# 		print('thank you for you attention!')

		# 	exi = input('')

		# elif cat_choice == {'clothers'}:
		# 	answer = input('Do you want watch models? ')

		# 	if answer.lower() == 'yes':
		# 		i = 0
		# 		for key in clothers.keys():
		# 			i+=1
		# 			print(f"{i}.{key} - {clothers[key]}")
			

		# 	elif answer.lower() == 'no' or answer.lower() == 'exi':
		# 		print('thank you for you attention!')

		# 	exi = input('')
			
		
		
