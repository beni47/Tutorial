
def hello(to="world"):
    print("hello", to)
name=  input("whats your name? ")
hello(name)
hello()


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


def parity():
    n = int(input("Enter n: "))
    remainder = n % 2
    if remainder > 0:
        print("Odd")
    else:
        print("Even")

parity()