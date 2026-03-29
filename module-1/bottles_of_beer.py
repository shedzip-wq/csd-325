# Sheridan Dela Cruz
# March 28, 2026
# Module 1.3

# Bottles of Beer Countdown Program
# Asks user for a stating number, counts down using a function,
# and prints a final message when finished.

def countdown(n):
    """
    Counts down from n to 0 while printing the song lyrics
    Handles plural and singular bottle cases.
    """
    
    # Loop for plural bottles
    while n>1:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print("Take one down, pass it around...")
        n-=1
        print(f"{n} bottles of beer on the wall.\n")

    # Final bottle(singular)
    if n==1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down, pass it around...")
        print("No more bottles of beer on the wall!\n")
    
# Main Program

num_bottles = int(input("How many bottles of beer are on the wall?"))
countdown(num_bottles)
print("Time to buy more beer!")
    
