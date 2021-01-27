cart_list = []
final_response = ""
menu = ['egg', 'bread', 'french toast','avocado','sweet potato']


while final_response.lower() != 'quit':
    
    if cart_list == []:
        print('\nYour shopping cart is currently empty')
    add_again = input('Would you like to add anything to your cart?\n'
                      'Yes or No?        ')
    while add_again.lower() != "yes" and add_again.lower() != "no":
                print('\nSorry, that is not an option')
                add_again= input('Would you like to add anything to your cart?\n'
                                 'Yes or No?        ')
                
                
    while add_again.lower() == 'yes':
        print('\nWe currently have the following items available\n')
        for food_item in menu:
            print('-' + food_item)
        cart_addition = input('What would you like to add?        ')
        
        
        if cart_addition != int and cart_addition in menu:
            cart_list.append(cart_addition)
            print('\nBelow is the list of items in your shopping cart \n')
            for i in set(cart_list): 
                print(str(cart_list.count(i)) + " " + i + '(s)')
            
            add_again = input('Would you like to add anything else? \n'
                                 'Yes or No?        ')
            
            while add_again.lower() != "yes" and add_again.lower() != "no":
                print('\nSorry, that is not an option')
                add_again= input('Would you like to add anything else?\n'
                                 'Yes or No?        ')
            
            
        else:
            print('\nThat is not in the list of options') 
            add_again = input('Would you like to try again? \n'
                              'Yes or No?       ')
            
            while add_again.lower() != "yes" and add_again.lower() != "no":
                print('Sorry, That is not an option')
                add_again = input('Would you like to try again? \n'
                              'Yes or No?       ')

    if cart_list == []:
        print('\nThank you for shopping with us') 
        break
    
    cart_del_quest1 = input("Would you like to remove anything from your cart? \n"
                            'Yes or No?           ')
    
    while cart_del_quest1.lower() != "yes" and cart_del_quest1.lower() != "no":
                print('Sorry, That is not an option')
                cart_del_quest1 = input("Would you like to remove anything "
                                        "from your cart? \n"
                                        'Yes or No?           ')
    
    while cart_del_quest1.lower() != int: 
    
        if cart_del_quest1.lower() == "yes":
            print('\nBelow are the list of items in your shopping cart \n')
            
            if cart_list == []:
                print('Your shopping cart is currently empty')
                break

            else:
                for i in set(cart_list):
                    print(str(cart_list.count(i)) + " " + i + '(s)')
                cart_del_quest2 = input('What would you like to remove?    ')

                
                if cart_del_quest2 in cart_list:
                    cart_list.remove(cart_del_quest2)
                    cart_del_quest1 = input("Would you like to remove anything "
                                            "else from your cart? \n"
                                            'Yes or No?       ')
                    
                else:
                    print('\nSorry, That is not in your shopping cart ')
                    cart_del_quest1 = input("Would you like to remove anything "
                                            "from your cart? \n"
                                            'Yes or No?      ')
                    
                    while cart_del_quest1.lower() != "yes" and cart_del_quest1.lower() != "no":
                        print('\nSorry, That is not an option')
                        cart_del_quest1 = input('Would you like to try again? \n'
                                          'Yes or No?       ')
                
            
    
    
        elif cart_del_quest1.lower() == "no":
            print('\nBelow is the list of items in your shopping cart \n')
            for i in set(cart_list):
                print(str(cart_list.count(i)) + " " + i + '(s)')
            break
                
        else:
            print('\nSorry, That is not an option')
            cart_del_quest1 = input("Would you like to remove anything "
                                        "from your cart? \n"
                                        'Yes or No?         ')
            
            while cart_del_quest1.lower() != "yes" and cart_del_quest1.lower() != "no":
                print('\nSorry, That is not an option')
                cart_del_quest1 = input('Would you like to try again? \n'
                              'Yes or No?       ')
            
    print("\nType 'quit' to keep shopping or type 'continue' to go on")
    final_response = input('>>>>>     ')
        
    while final_response.lower() != 'quit' and final_response.lower() != 'continue':
        print('\nSorry, That is not an option')
        print("\nType 'quit' to keep shopping or type 'continue' to go on")
        final_response = input('>>>>>     ')

if cart_list != []:
    print('\nThank you for shopping with us')  
    print('\nBelow is the list of items in your shopping cart \n')
    for i in set(cart_list):          
        print(str(cart_list.count(i)) + " " + i + '(s)')
        
else:
    print("\n We are sad to see that you could not buy anything today. Come again next time.")
    