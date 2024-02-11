greetings = input("Greeting: ").strip().lower()
# WHAT'S THE FIRST WORd
def get_first_word():
    words = greetings.split()
    if words:
        return words[0]
    else:
        return None
first_word = get_first_word()
def get_first_letter():
    if greetings:
        return greetings[0]
    else:
        return None
first_letter = get_first_letter()

if first_word == 'hello':
    print('0')
elif first_letter == 'h':
    print('20')
else:
    print('100')



