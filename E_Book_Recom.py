print("\t\tWELCOME TO BOOk.NET")
print("---------------------GENRE---------------------")
types = ['FICTION','MYSTERY', 'THRILLER', 'ROMANCE', 'HORROR', 'HISTORY']

for i in types:
    print('\t\t   ' + i)
    print('\n')

genre = input("Please select the genre you need....").upper()  # Convert input to uppercase
print("LOADING...........")


def fiction():
    print("Here are some of the most recommended fictional books for you.....")
    fictional=['The Alchemist','Adventures of Sherlock Holmes','The Great Gatsby','Nineteen Eighty-Four','To Kill a Mockingbird','The Girl Who Drank The Moon']
    for j in fictional:
        print('\t\t'+j)
        print('\n')
    select=input(print("select the book you need....."))
    print(select +' is now displayed....')


def mystery():
    print("Here are some of the most recommended mystery books for you....")
    Mystery=['The Silent Patient','Gone Girl','Murder on the Orient','Express In the Woods','The Da Vinci Code','The Big Sleep']
    for j in Mystery:
       print('\t\t'+j)
       print('\n')
    select=input(print("select the book you need...."))
    print(select +' is now displayed....')

def thriller():
    print("Here are some of the most recommended thriller books for you....")
    Thriller=['The Girl on the Train', 'My Sister,the Serial Killer'  ,'The Girl with the Dragon Tattoo' , 'A Good Girls Guide to Murder' ,' Verity']
    for j in Thriller:
        print('\t\t'+j)
        print('\n')
    select=input(print("select the book you need...."))
    print(select +' is now displayed....')


def romance():
    print("Here are some of the most recommended romance books for you....")
    romantic=['Red, White & Royal' ,'Blue Beach Read', 'The Kiss Quotient' ,'The Notebook' ,'The Fault in Our Stars' ,'The Love Hypothesis']
    for j in romantic:
       print('\t\t'+j)
    print('\n')
    select=input(print("select the book you need...."))
    print(select +' is now displayed....')

def horror():
    print("Here are some of the most recommended horror books for you....")
    bhooth=['Dracula Frankenstein' ,'The Haunting of Hill House', 'The Exorcist','House of Leaves', 'It' ]
    for j in bhooth:
       print('\t\t'+j)
       print('\n')
    select=input(print("select the book you need....."))
    print(select +' is now displayed....')
def history():
    print("Here are some of the most recommended history related books for you...")
    History=['The Last Mughal' ,'The Wonder That Was India', '1776','India After Gandhi','The Age of Extremes',  'Stalins Englishman ']
    for j in History:
        print('\t\t'+j)
        print('\n')
    select=input(print("Please select the book you need....."))
    if select == History:
        print(select +' is now displayed....')
    
if genre == types[0]:
    fiction()
elif genre == types[1]:
    mystery()
elif genre == types[2]:
    thriller()
elif genre == types[3]:
    romance()
elif genre == types[4]:
    horror()
elif genre == types[5]:
    history()
else:
    print("Invalid genre selection")