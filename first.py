import random

def _main(length):
    count = 0
    res = ""
    while count < length:
        res += chr(random.randint(33,125))
        count += 1
    return res

def _save(my_pass,pass_for):
    path = pass_for
    with open("all_pass/{}.txt".format(path), "w") as file:
        file.write(my_pass)

    
used_for = input()
_save(_main(random.randint(15,30)), used_for)
print("Ready")
input("Tab any key to close")
