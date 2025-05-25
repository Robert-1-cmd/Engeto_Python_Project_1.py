'''
project_1.py: the first project for the Engeto Online Python Academy

author: Robert Půža
email: puza.robert@seznam.cz
'''

# THE text
'''
author =
'''
from collections import Counter



TEXTS = [
 '''Situated about 10 miles west of Kemmerer,
 Fossil Butte is a ruggedly impressive
 topographic feature that rises sharply
 some 1000 feet above Twin Creek Valley
 to an elevation of more than 7500 feet
 above sea level. The butte is located just
 north of US 30 and the Union Pacific Railroad,
 which traverses the valley.''',
 '''At the base of Fossil Butte are the bright
 red, purple, yellow and gray beds of the Wasatch
 Formation. Eroded portions of these horizontal
 beds slope gradually upwards from the valley floor
 and steepen abruptly. Overlying them and extending
 to the top of the butte are the much steeper
 buff-to-white beds of the Green River Formation,
 which are about 300 feet thick.''',
 '''The monument contains 8198 acres and protects
 a portion of the largest deposit of freshwater fish
 fossils in the world. The richest fossil fish deposits
 are found in multiple limestone layers, which lie some
 100 feet below the top of the butte. The fossils
 represent several varieties of perch, as well as
 other freshwater genera and herring similar to those
 in modern oceans. Other fish such as paddlefish,
 garpike and stingray are also present.'''
]

name = "bob"
print("username : bob")
password = 123
print("password : 123")
user = "bob : 123"
cara = "-" * 40
print(cara)
 
 # soubor Regist.user
user = {
    "bob" : "123",
    "ann" : "pass123",
    "nike" : "password",
    "liy" : "pass123"
    }



num_texts = len(TEXTS)

if name in user and password == user[name]:
    print(f"Welcome to the app, {name}")
    print(f"We have {num_texts} texts to be analyzed.")
    print(cara)
else:
     print(f"Welcome to the app, {name}")
     print(f"We have {num_texts} texts to be analyzed.")
     print(cara)
    
    
    
    # Uživatelský vstup
choice = input("Enter a number btw. 1 and 3 to select: ")

if not choice.isdigit():
    print("You must enter a number. Exiting.")
    

choice_int = int(choice)

if not 1 <= choice_int <= len(TEXTS):
    print("Number out of range. Exiting.")
    

selected_text = TEXTS[choice_int - 1]

user_input = 1  # Should be 1, 2, or 3

def text_analyzer(text):
    words = text.split()
    clean_words = [word.strip(".,!?") for word in words]

    titlecase_words = [word for word in words if word.istitle()]
    uppercase_words = [word for word in words if word.isupper()]
    lowercase_words = [word for word in words if word.islower()]
    number_strings = [word for word in words if word.isdigit()]
    number_sum = sum(int(num) for num in number_strings)
    word_lengths = [len(w) for w in clean_words if w.isalpha()]
    length_counts = dict(Counter(word_lengths))

    result = {
        'word_count': len(words),
        'titlecase_words': len(titlecase_words),
        'uppercase_words': len(uppercase_words),
        'lowercase_words': len(lowercase_words),
        'number_strings': len(number_strings),
        'number_sum': number_sum,
        'length_counts': length_counts
    }

    return result

def print_text_stats(result):
    print("-" * 40)
    print(f"There are {result['word_count']} words in the selected text.")
    print(f"There are {result['titlecase_words']} titlecase words.")
    print(f"There are {result['uppercase_words']} uppercase words.")
    print(f"There are {result['lowercase_words']} lowercase words.")
    print(f"There are {result['number_strings']} numeric strings.")
    print(f"The sum of all the numbers is {result['number_sum']}")

def print_length_histogram(length_counts):
    print("-" * 40)
    print("LEN| OCCURENCES       |NR.")
    print("-" * 40)
    for length in sorted(length_counts):
        count = length_counts[length]
        stars = '*' * count
        print(f"{str(length).rjust(3)}|{stars.ljust(18)}|{count}")

# --- Example usage ---
if __name__ == "__main__":
    selected_text = TEXTS[0]  # or TEXTS[int(input()) - 1] for user choice
    result = text_analyzer(selected_text)
    print_text_stats(result)
    print_length_histogram(result['length_counts'])

    # Výpis pod sebou
def print_result_items(result):    
 for key, value in result.items():
    if key != "length_counts":
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
        print(f"{key}: {value}")
        
if name in user and password == user[name]:
   name = 'marek'
   print("user_name: marek")
   password = 123
   print("password: 123")
   print("Unregistered user, terminating the program.")
else:
    print("username: marek")
    print("password: 123")
    print("Unregistered user, terminating the program.")