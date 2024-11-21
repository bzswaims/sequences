import math

#Used to find the parity, 0 for even, 1 for odd, likely need to flip this
#I cant remember if 0 = negative and 1 = positive or the reverse.
def parity(n):
    return n % 2

#Generates the nth Lucas Number using the explicit formula
#L_n = ((1 + sqrt(5)) / 2)^n + ((1 - sqrt(5)) / 2)^n
def generate_lucas_val(n):
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio
    psi = (1 - math.sqrt(5)) / 2  # Conjugate of the golden ratio
    return round(math.pow(phi, n) + math.pow(psi, n))

def generate_lucas(n):
    return [generate_lucas_val(i) for i in range(n)]

def main():
    #try block to get input from user for first n numbers in sequence.
    try:
        n = int(input("Enter a positive integer for the length of Lucas sequence: "))
        if n <= 0:
            print("Please enter a positive number greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return

    #Builds the Thue-Morse Sequence
    sequence = generate_lucas(n)
    print("Lucas sequence first ", n, " terms:")
    print(sequence)

if __name__ == "__main__":
    main()