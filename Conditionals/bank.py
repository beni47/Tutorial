greetings = input("Greeting: ").strip().lower()

# WHAT'S THE FIRST WORD
def get_first_word():
    words = greetings.split()
    if words:
        return words[0]
    else:
        return None  # Return None if there are no words

# Call the get_first_word function and store the result
first_word = get_first_word()

# Check conditions and print messages accordingly
if first_word == 'hello' or first_word == 'hello,':
    print('0')
elif first_word.startswith('h'):
    print('20')
else:
    print('100')
