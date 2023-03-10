for integer in range(1,100):
  
    string =""
    
    if integer% 5 == 0:
        string = string + "Buzz"
    elif integer% 3 == 0:
        string = string + "Fizz"
    elif integer% 5 != 0 and integer% 3 != 0:
        string = string + str(integer)

    print(string)
