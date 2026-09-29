#Daniel DeLong, Multiplication Table
import time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

row=[]
column=[]
while True:
    typer("How many numbers do you want in your table (1-something)?")
    try:
        number_of_nums=int(input(""))
    except:
        continue
    else:
        break

loop_helper=1
copy_of_nums=number_of_nums
#put the correct number of numbers in row[]
while copy_of_nums>0:
    row.append(loop_helper)
    loop_helper+=1
    copy_of_nums-=1

loop_helper=1
copy_of_nums=number_of_nums
#put the correct number of numbers in column[]
while copy_of_nums>0:
    column.append(loop_helper)
    loop_helper+=1
    copy_of_nums-=1

print("X\t",end="")
def table_maker(loop_helper1,loop_helper2):
    for number in row:
        print(f"{number}\t",end="")
    print("")
    for number in column:
        print(f"{number}\t",end="")
        for other_number in row:
            print(f"{row[loop_helper1]*column[loop_helper2]}\t",end="")
            loop_helper1+=1
        loop_helper2+=1
        loop_helper1=0
        print("")

table_maker(0,0)
