again_boolean  = False
not_prime = True

while True :
    try :
        if again_boolean == True :
            input = int(input("What is your number, REALLY?\n"))
        else :
            input = int(input("What is your number?\n"))
    except :
        print("Invalid input. Must input an integer 2 or greater.")
        again_boolean = True
        continue
    break

if input < 2 :
    quit()

factors = list()
newnumber = input

while not_prime == True :
    for number in range(2, newnumber + 1) :
        if newnumber % number == 0 :
            factors.append(number)
            newnumber = int(newnumber/number)
            if newnumber == 1 :
                not_prime = False
            break

        if number == newnumber :
            not_prime = False

print(factors)
