#Daniel DeLong, Multiplication Table
import time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

#set our row and column lists for later
row=[]
column=[]
#this try: loop makes sure they input an integer
while True:
    typer("How many numbers do you want in your table (1-something)?")
    try:
        number_of_nums=int(input(""))
    except:
        continue
    else:
        break

#set some helpful variables
loop_helper=1
copy_of_nums=number_of_nums
#put the correct number of numbers in row[]
while copy_of_nums>0:
    row.append(loop_helper) #add loop_helper to the end of row[]
    loop_helper+=1 #add one to loop_helper
    copy_of_nums-=1 #subtract one from copy_of_nums

#same code as before but for column[]
loop_helper=1
copy_of_nums=number_of_nums
#put the correct number of numbers in column[]
while copy_of_nums>0:
    column.append(loop_helper)
    loop_helper+=1
    copy_of_nums-=1

print("X\t",end="") #print an X, don't go to a new line
def table_maker(loop_helper1,loop_helper2): #define a function named table_maker with parameters loop_helper1 and loop_helper2
    for number in row: #for each number in row[]:
        print(f"{number}\t",end="") #print that number, don't go to a new line
    print("") #go to a new line

    #ok so this loop is a little complicated, but basically what it is doing is it's print one number from column[], then multiply every row number with the current column number and print those before going to a new line and doing the same thing but with a different column number
    for number in column: #for each number in column[]:
        print(f"{number}\t",end="") #print that number
        for other_number in row: #then for each number in row[]:
            print(f"{row[loop_helper1]*column[loop_helper2]}\t",end="") #print a number times another number
            loop_helper1+=1 #add one to loop_helper1
        loop_helper2+=1 #then after that loop we add one to loop_helper2
        loop_helper1=0 #set loop_helper1 back to 0
        print("")

table_maker(0,0) #call the table maker function and set each argument to 0

#example of how this works:
"""
How many numbers do you want in your table (1-something)?
6
X       1       2       3       4       5       6
1       1       2       3       4       5       6
2       2       4       6       8       10      12
3       3       6       9       12      15      18
4       4       8       12      16      20      24
5       5       10      15      20      25      30
6       6       12      18      24      30      36
"""