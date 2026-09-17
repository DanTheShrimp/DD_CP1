#Daniel DeLong, Crew Shares
import time,random
def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

while True:
    typer("My system memory has been wiped. Please input the number of crew on Yondu's ship.")
    try:
        number_of_crew=int(input(""))
    except:
        time.sleep(0.75)
    else:
        break

loop_helper=1
list_of_names=[]
while number_of_crew>0:
    stringed_loop_helper=str(loop_helper)
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1]
    if last_number=="1":
        typer(f"What is the name of the {loop_helper}st crew member?")
    elif last_number=="2":
        typer(f"What is the name of the {loop_helper}nd crew member?")
    elif last_number=="3":
        typer(f"What is the name of the {loop_helper}rd crew member?")
    else:
        typer(f"What is the name of the {loop_helper}th crew member?")
    name=input("").title().strip()
    list_of_names.append(name)
    loop_helper+=1
    number_of_crew-=1
    time.sleep(0.75)

credits=random.randint(2000,8000)
yondu_share=round(credits*0.13,2)
credits-=yondu_share
peter_share=round(credits*0.11,2)
credits-=peter_share