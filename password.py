import random
len_of_pass = int(input("Enter the length of the password  "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ''.join(random.sample(s,len_of_pass)) 
print(password)