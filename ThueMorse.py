#Technically all needed for our use.
def generate_thue_morse_val(n):
    return bin(n).count('1') % 2

#Staples the string of binary characters togather.
def generate_thue_morse(n):
    return [generate_thue_morse_val(i) for i in range(n)]

def main():
    #try block to get input from user for first n numbers in sequence.
    try:
        n = int(input("Enter a positive integer for the length of Thue-Morse sequence: "))
        if n <= 0:
            print("Please enter a positive number greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return

    #Builds the Thue-Morse Sequence
    sequence = generate_thue_morse(n)
    print("Thue-Morse sequence first ", n, " terms:")
    print(sequence)

if __name__ == "__main__":
    main()