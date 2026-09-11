
import time,random

while True:
    number_to_print=random.randint(0,1)
    print(number_to_print,end="")
    do_new_line=random.randint(1,75)
    if do_new_line==1:
        print("")
    time.sleep(0.0001)