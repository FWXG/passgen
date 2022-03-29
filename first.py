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

    

        
