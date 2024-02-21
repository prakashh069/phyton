letter_template = '''Dear {name}, you are selected! 
The orientation session is scheduled for {date}.
Congratulations!'''

name= input('Enter the name: ')
date= input('Enter the date: ')

fill_tempelate=letter_template.format(name=name, date= date)

print(fill_tempelate)