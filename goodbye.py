# Ask user if they want to go to Japan
opinion = input("Do you want to go to Japan?").strip().title()

#split user's name into first name and last name
first, last=opinion.split(" ") 



# say hello to the user's opinion
print(f"hello, {first}")

