#WORKING WITH STRINGS
#Ask user their name
name = input("Whats your name? ").strip().title()
#split users name into first name and second name
first,last = name.split(" ")
#Remove Whitespace from string and capitalize
#name=name.strip().title()
#capitalize the name
#name=name.capitalize()#just the first letter
#name=name.title() capitalize first letterof word

#Say hello to user using different formats
print("Hello " + first)
#print(f"Hello,{name}")
#print("Hello",name)
#print automatically moves the cursor to the bottom line
#official documentation for print
#print(*object,sep='',end="\n")
#the end makes it to move to the next line automatically
#You can edit this if you want to change that.
#Escaping characters

