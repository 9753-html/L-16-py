try:
    num=int(input("Enter any Number:"))
    print(num)

except ValueError as e:
    print("Error=",e)