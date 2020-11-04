import string
import random
import pyperclip as pc

set_1 = string.ascii_lowercase
set_2 = string.ascii_uppercase
set_4 = string.digits
set_3 = string.punctuation

pwdLength = int(input("How long do you want your password:\t"))
pwd = []
pwd.extend(list(set_1))
pwd.extend(list(set_2))
pwd.extend(list(set_3))
pwd.extend(list(set_4))

random.shuffle(pwd)
print("Your password is:")
copyPwd = "\t\t" + "".join(pwd[0:pwdLength])
print(copyPwd)
pc.copy(copyPwd)
print("Password is copied to clipboard")



