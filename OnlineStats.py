print("DATA 51100- Fall 2022")
print("Sai Kumar Murarishetti")
print("Programming Assignment #1")

# function
def main():
    while True:
        # enter a number
        number = int(input("Enter a number: "))

        # Check if the entered number is negative, if so, exit the loop
        if number < 0:
            break

        # Initialize variables for mean (xn),variance (sn) and (i)
        xn = 1
        sn = 0
        i = 2

        # Calculated mean and variance using a while loop
        while i <= number:

            #vaiance
            sn = (((i - 2) * sn) / (i - 1)) + (((i - xn) * (i - xn)) / i)

            # Mean
            xn = xn + (i - xn) / i
            i+=1
        # Print the calculated mean and variance
        print("Mean is", xn, "Variance is", sn)

# Code is being run as the main program
if __name__ == "__main__":
    # Calling the main function if the code is executed
    main()
