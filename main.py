import random
import time

type_dict = {1: {"type": "0123456789", "len": 6},
             2: {"type": "abcdefghijklmnopqrstuvwxyz", "len": 8},
             3: {"type": "abcdefghijklmnopqrstuvwxyz0123456789", "len": 10},
             4: {"type": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "len": 12},
             5: {"type": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*+-?@^~", "len": 18},
             6: {"type": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@["
                         "\\]^_`{|}~",
                 "len": 24}}


def rand_pass(inp):
    password_d = []
    password = ""
    for i in range(type_dict[inp]["len"]):
        password_d += random.choices(type_dict[inp]["type"])

    for i in password_d:
        password += str(i)

    print("Generated password : " + str(password))

    log = str(time.strftime("%H:%M:%S ==> ", time.localtime())) + str("Generated password : " + str(password))
    my_file = open("data.log", "a")
    my_file.write(str(log) + "\n")
    my_file.close()


def enter_num(x):
    print("1.very_simple (6 character)\n2.simple (8 character)\n3.medium (10 character)\n4.difficult (12 character)\n5.very_difficult (18 character)\n6.very_very_difficult (24 character)\n")
    try:
        inp = int(input(x))
        print("\n")
        rand_pass(inp)
        print("")
    except ValueError:
        print("\n")
        enter_num("Just enter the number : ")


if __name__ == '__main__':
    enter_num("Enter password type number : ")
