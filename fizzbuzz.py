for integer in range(1,100):
    st =""
    if integer% 3 == 0:
        print("Fizz")
    elif integer% 5 == 0:
        print("Buzz")
    elif integer% 5 != 0 and integer% 3 != 0:
        st = st + str(integer)

    print(st)



