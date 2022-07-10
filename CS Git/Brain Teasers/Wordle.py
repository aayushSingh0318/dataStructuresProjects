
#  Description: Given a dictionary Wordle solver

import sys
from typing import List, Tuple

# # Example:
# guesses = [
#    [
#        ('A', 'B'),
#        ('D', 'Y'),
#        ('O', 'Y'),
#        ('P', 'Y'),
#        ('T', 'B')
#    ],
#    [
#        ('D', 'G'),
#        ('O', 'G'),
#        ('C', 'B'),
#        ('K', 'B'),
#        ('S', 'B')
#    ]
# ]
# dictionary = 
# [
# 'ADOPT',
# 'DOING',
# 'DOPEY',
# 'PODGY'
# ]
# wordle(guesses, dictionary) , , ). 'G' = green, 'Y' = yellow, 'B'
# = black.
# # 
# # `dictionary` is the list of all of possible words to narrow 
# # down.
# # 
# # Output:
# # The subset of words in `dictionary` that can be the answer
# # based on previous guesses. Return an empty list if no words in 
# # the
# # dictionary are possible.

def includeWord(word, greens, yellows, blacks):
    
    for letter, index in greens:
        if word[index] != letter:
            return False
    
    for letter, index in yellows:
        if word[index] == letter or letter not in word: 
            return False
        
    for letter in blacks:
        if letter in word:
            return False
        
    return True
    


def wordle(guesses: List[List[Tuple[str, str]]], dictionary: List[str]) -> List[str]:
    
    greens = []
    yellows = []
    blacks = []
    
    potentialWords = []
    
    for guess in guesses:
        for i in range(5):
            color = guess[i][1]
            letter = guess[i][0]
            if color == 'G':
                greens.append((letter, i))
            elif color == 'Y':
                yellows.append((letter, i))
            else:
                blacks.append(letter)
    
        
    for word in dictionary:
        if includeWord(word, greens, yellows, blacks):
            potentialWords.append(word)
    return potentialWords
    
    
            
            
            
        

    
    
def main():
   
   # Helper functions for reading in input.
   LINES = sys.stdin.read().splitlines()[::-1]
   def input(): return LINES.pop()
   
   mul = lambda: map(int,input().strip().split())
   strng = lambda: input().strip()
   
   # First two numbers correspond to the number of words in the 
# dictionary
   # and the number of guesses respectively.
   num_dictionary, num_guesses = mul()
   
   dictionary = [strng().upper() for _ in range(num_dictionary)]
   guesses = []
   
   # Following lines contain the word guessed and the colors.
   for _ in range(num_guesses):
       # Advance reader (skip blank line).
       input()
       guess = strng()
       colors = strng()
       
       assert len(guess) == len(colors)
       guesses.append([(letter.upper(), color) for letter, color 
in zip(list(guess), list(colors))])
   
   # Call `wordle` function.
   filtered = wordle(guesses, dictionary)
   
   if len(filtered) == 0:
       print('No matches.')
   else:
       print(' '.join(filtered))
if __name__ == "__main__":
   main()
