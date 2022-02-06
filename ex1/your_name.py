

def print_name(name):
    for letter in name:
        if letter != " ":
            print(letter, end="")
        else:
            print()
    print()

def main():
    print_name("Maor Betser")
main()