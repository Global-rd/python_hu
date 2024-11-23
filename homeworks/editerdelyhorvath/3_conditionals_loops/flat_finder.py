'''
3. házi feladat

Feladat 1: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra
(if-elif-else, operátorok)
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_helpers')))

from terminal_clearer import clear_terminal

clear_terminal()

# Ask the user for input
city = input("Enter the city: ").strip().upper()
usd = int(input("Enter the monthly price (in USD): ").strip())

# Analysis of conditions
if city == "CHICAGO" or ((city == "NEW YORK" or city == "SAN FRANCISCO") and usd < 4000):
    can_move = True
elif city != "WASHINGTON" and usd < 3000:
    can_move = True
else: 
    can_move = False

# Print the result based on the conditions
if can_move:
    print(f"Yes, we can move to {city.title()} for {usd} USD.")
else:
    print(f"No, we cannot move to {city.title()} for {usd} USD.")
