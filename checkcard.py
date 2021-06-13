def just_add(z):
    total = 0
    for item in range(len(z)):
        total += int(item)
    return total


def splitadd(y):
    cut =  [int(item) for item in str(y)]
    total = 0
    for item in range(len(cut)):
        total += int(item)
    return total


def validate(x):
    card = list(x)

    for i in range (14):
        if int(i) % 2 == 0:
            card[i] = int(card[i]) * 2
            if int(card[i]) > 9:
                card[i] = splitadd(card[i])
    merge = card[:14]
    final = just_add(merge) + int(card[15])
    
    if final % 10 == 0:
       return  "This card is valid!",final
    else:
        return "This card is invalid, try again",final

if __name__ == "__main__":
    while True:
        detail = input("Enter the card number: ")
        print(validate(detail))
        print(validate(detail)[1])
        if "invalid" not in validate(detail):
            break




