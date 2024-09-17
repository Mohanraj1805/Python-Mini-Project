import random
# importing random elements in the password
password='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@!#._+:;*&^%$~`=[}'
length_password=int(input('Enter the length of password: '))#the length of the password depends on the user input
a=''.join(random.sample(password,length_password))#sample is a functions in random
print('your password is: '+a)
