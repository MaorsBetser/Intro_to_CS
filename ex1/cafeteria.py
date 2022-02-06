
def process_amount(cash):
    if cash % 50 == 0 and cash >= 50:
        return "don't you have smaller cash?"
    elif cash < 50 and cash % 10 == 0 and cash != 0:
        return "ok"
    elif cash <= 0:
        return "no service"
    else:
        return "Total: " + str(cash)
def main():
    cash  = int(input("How much cash recived\n"))
    print(process_amount(cash))
main()