name = ""
name = input("Please input your name \n").capitalize()
while name == "":
    name = input("Please input your name \n").capitalize()        

def parse_adventure_response(reply):
    reply_lower = reply.lower()
    response_array = reply_lower.split()
    if "yes" not in response_array:
        return("well this was all a bit pointless...")    
    return ("Excellent choice! Space cat approves!")


adventure_response = input("Welcome {name} Would you like to go on an adventure? (yes/no) \n".format(name = name))
print(parse_adventure_response(adventure_response))



# if adventure_response.lower() == "no":
#     print ("Seriously?!? OK have a nice day!")
# elif adventure_response.lower() == "yes":
#     adventurer = input("Great stuff, now choose your character: \n 1 = Pirate \n 2 = Space cat \n")
#     if adventurer == 1:
#         print("good choice, lets go!")
#     else:
#         print("Space cats only sleep they dont go on adventures! :D")


