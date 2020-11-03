SECURE = (('a', '@'), ('s', '$'), ('i', '1'), ('and', '&'), ('or', '|'), ('o', '0'))

def securePwd(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == '__main__':
    userInputPwd = input("Enter your password: \n")
    x = securePwd(userInputPwd)
    print(x)
