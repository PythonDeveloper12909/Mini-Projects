import colorama
from colorama import Fore,Style
import random,re
colorama.init()
print(f'{Fore.CYAN} Hello im TravelBot!{Style.RESET_ALL}')
user_name=input(f'{Fore.RED}Your Name?:{Style.NORMAL}')
if not user_name:
     user_name="Agent"
print(f'{Fore.CYAN} nice to meet you,{user_name}{Style.RESET_ALL}')
print(f'{Fore.LIGHTMAGENTA_EX} i can:\n-Suggest travel spots(say"recommendation")\n-Offer packing tips(say"packing")\n-Tell a joke(say"joke"){Style.RESET_ALL}')
print(f'{Fore.GREEN}Type "exit" or "bye" to end{Style.RESET_ALL}')
destinations={"mountains":["Swiss Alphes","Rocky Mountains","Himalayas"],"beaches":["Bali","Maldieves","Phuket"],"cities":["Tokyo","Paris","New York"]}
jokes=["why do travellers always feel hot? because of their hot spots!","why do programmers dont like nature?Too many bugs!","why did the computer go to the doctor? because it had too many bugs!"]
conservation_history=[]
while True:
    user_input=input(f'{Fore.CYAN}{user_name}:{Style.BRIGHT}')
    joke=random.choice(jokes)
    destination=user_input.lower().strip()
    if user_input.lower().strip()=="recommendation" or user_input.lower().strip()=="suggest":
        conservation_history.append("recommendation")
        print(f'{Fore.GREEN}TravelBot:Where would you like to go?(beaches/mountains/cities){Style.RESET_ALL}') 
    elif user_input.lower().strip()=="joke" or user_input.lower().strip()=="funny":
         conservation_history.clear()
         conservation_history.append("joke")
         print(f'{Fore.LIGHTMAGENTA_EX}TravelBot:{joke}{Style.RESET_ALL}')
         if "recommendation" in conservation_history:
              conservation_history.remove("recommendation")
    elif user_input.lower().strip()=="packing" or user_input.lower().strip()=="pack":
         conservation_history.clear()
         print(f'{Fore.CYAN}TravelBot:Where to?{Style.RESET_ALL}')
         conservation_history.append('packing')
         if user_input.lower().strip()=="maldieves":
              destination="maldieves"
         elif user_input.lower().strip()=="phuket":
              destination="phuket"
         elif user_input.lower().strip()=="bali":
              destination="bali"
    elif user_input.lower().strip()==destination and "packing" in conservation_history:
         conservation_history.clear()
         print(f'{Fore.GREEN}TravelBot:How many days?:{Style.RESET_ALL}')
         try:
              days=int(input(f'{Fore.CYAN}{user_name}:{Style.BRIGHT}'))
              if not days==str:
                    conservation_history.append(days)
              elif days==str:
                    days=user_input
                    conservation_history.append(days)
         except ValueError:
              print(f'{Fore.GREEN}TravelBot:Please choose valid days{Style.BRIGHT}')
         if days in conservation_history:
              if destination=="maldieves" or destination=="bali" or destination=="phuket":      
                print(f'{Fore.GREEN}TravelBot:packing tips for {days} days in {destination}\n-Pack versatile clothes\n-Bring chargers/adapters\n-Check weather forecast{Style.RESET_ALL}')
              else:
                   print(f"{Fore.LIGHTCYAN_EX}TravelBot:Sorry,We dont have that kind of destination!{Style.BRIGHT}")  
    elif user_input.lower().strip()=="beaches" and "recommendation" in conservation_history:
            conservation_history.clear()
            print(f"{Fore.GREEN}TravelBot:where would u like to go to? (maldieves,phuket,bali){Style.RESET_ALL}")
            conservation_history.append("beaches")  
    elif user_input.lower().strip()=="maldieves" and "beaches" in conservation_history:
         print(f'{Fore.GREEN}TravelBot:ohh nice!enjoy your maldieves trip!{Style.RESET_ALL}')
         break
    elif user_input.lower().strip()=="bali" and "beaches" in conservation_history:
        print(f'{Fore.GREEN}TravelBot:ohh nice! enjoy your bali trip!{Style.RESET_ALL}')
        break  
    elif user_input.lower().strip()=="phuket" and "beaches" in conservation_history:
         print(f"{Fore.GREEN}TravelBot:ohh nice! enjoy your phuket trip!{Style.RESET_ALL}")
         break
    elif user_input.lower().strip()=="mountains" and "recommendation" in conservation_history:
         conservation_history.clear()
         print(f'{Fore.GREEN}TravelBot:Where would you like to go?(swiss alphes,rocky mountains,himalayas){Style.RESET_ALL}')
         conservation_history.append("mountains")
    elif user_input.lower().strip()=="swiss alphes" and "mountains" in conservation_history:
         print(f'{Fore.GREEN}TravelBot:ohh nice! enjoy your trip to swiss alphes!{Style.RESET_ALL}')
         break        
    elif user_input.lower().strip()=="rocky mountains" and "mountains" in conservation_history:
         print(f'{Fore.GREEN}TravelBot:ohh nice! enjoy your trip to rocky mountains{Style.RESET_ALL}')
         break
    elif user_input.lower().strip()=="himalayas" and "mountains" in conservation_history:
         print(f'{Fore.GREEN}TravelBot:ohh nice! enjoy your trip to himalayas{Style.RESET_ALL}')
         break
    elif user_input.lower().strip()=="cities" and "recommendation" in conservation_history:
         conservation_history.clear()
         print(f'{Fore.GREEN}TravelBot:Where would you like to go to?(tokyo,paris,new york){Style.RESET_ALL}')
         conservation_history.append("cities")
    elif user_input.lower().strip()=="tokyo" and "cities" in conservation_history:
         print(f'{Fore.GREEN}TravelBot:ohh nice! enjoy your trip to tokyo{Style.RESET_ALL}')
         break
    elif user_input.lower().strip()=="new york" and "cities" in conservation_history:
         print(f"{Fore.GREEN}TravelBot:ohh nice!enjoy your trip to new york{Style.RESET_ALL}")
         break
    elif user_input.lower().strip()=="paris" and "cities" in conservation_history:
         print(f'{Fore.GREEN}TravelBot:ohh nice! enjoy your trip to paris{Style.RESET_ALL}')
         break
    elif user_input.lower().strip()=="exit" or user_input.lower().strip()=="bye":
               break
    else:
         print(f'{Fore.LIGHTCYAN_EX}TravelBot:sorry,i couldnt understand!{Style.BRIGHT}')
        