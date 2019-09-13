# allows user to input name
Name = input()

#looks at the first character of the name
char = Name[0]

#creates a for loop
for c in range(len(Name)):
    
    #if there is a "dash"
    if Name[c] == "-":
        
        #...look to the next character after it
        char += Name[c+1]
        
        #...and print that charachter
print(char)
