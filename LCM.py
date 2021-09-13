# ************************* Finding LCM ****************************8

# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input("Enter the Number 1: "))
            num2 = int(input("Enter the Number 2: "))
        except Exception as E:
            print("Only integers are allowed...!")
        else:
            try:
                print("The L.C.M. is", compute_lcm(num1, num2))
            except Exception as E:
                print(f"Can't Find LCM of {num1} and {num2}")
        continue
