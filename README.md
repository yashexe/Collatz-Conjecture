# Collatz-Conjecture

The Collatz Conjecture is a mathematical problem that involves an iterative process applied to a positive integer. Here's how it works:

1. Take any positive integer **n**.
2. If **n** is even, divide it by 2. If **n** is odd, multiply it by 3 and add 1.
3. Repeat this process with the resulting integer.

The conjecture is that no matter what positive integer you start with, you will always eventually reach the number 1.

The examples in this repository are the collatz conjecture sequence of a starting number 10.

## Usage

To use this code, run it in a Python interpreter and enter a positive integer when prompted. The Collatz Conjecture sequence will be generated and plotted. The plot will be saved as an image file called **conjecture.png**.

## Code breakdown

**collatz(hailstone_number)**: This function takes in a positive integer and generates the Collatz Conjecture sequence for that integer. It saves the sequence to a text file called sequence.txt. It then reads the sequence from the text file and returns it as a list of floats.

**plotHailstone(Data)**: This function takes in the Collatz Conjecture sequence as a list of floats and plots it as a series of parabolas. It saves the plot as an image file called conjecture.png and displays it to the user.

if __name__ == "__main__": This block of code is run when the script is executed. It first clears the contents of the sequence.txt file, then generates the Collatz Conjecture sequence by calling the collatz() function. It then plots the sequence by calling the plotHailstone() function.
