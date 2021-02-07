x = int(input('Type a number: \n'))

if x > 0:
    for i in range(2,10):
        y = x%i
        notPrime = 0
        if y == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")
        
    
        


    

    