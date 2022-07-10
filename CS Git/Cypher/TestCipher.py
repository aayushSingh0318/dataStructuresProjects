
#  Description: Decode and encode different cyphers. 


from operator import index
from re import T
import string
import sys
from typing import Counter

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ): #Aayush Code
  rows, cols = (int(key), len(strng))
  zigzag_array = [['-' for i in range(cols)] for j in range(rows)]
  cur_row = 0
  up = True
  word = ""
  for i in range(len(strng)):
    zigzag_array[cur_row][i] = strng[i]
    if up:
      cur_row += 1
    else:
      cur_row -= 1
    if cur_row == key - 1:
      up = False
    elif cur_row == 0:
      up = True
  for a in range(rows):
    for b in range(cols):
      if zigzag_array[a][b]!= '-':
        word = word + str(zigzag_array[a][b])

  return word
  

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ): #Aayush Code
  rows, cols = (int(key), len(strng))
  zigzag_array = [['-' for i in range(cols)] for j in range(rows)]
  cur_row = 0
  up = True
  word = ""
  for i in range(len(strng)):
    zigzag_array[cur_row][i] = 'x'
    if up:
      cur_row += 1
    else:
      cur_row -= 1
    if cur_row == key - 1:
      up = False
    elif cur_row == 0:
      up = True
      
  letter = 0
  for a in range(rows):
    for b in range(cols):
      if zigzag_array[a][b]== 'x':
        zigzag_array[a][b] = strng[letter]
        letter += 1
      
  up_reverse= True
  cur_row_reverse = 0
  for z in range(len(strng)):
    word = word + zigzag_array[cur_row_reverse][z] 
    if up_reverse:
      cur_row_reverse += 1
    else:
      cur_row_reverse -= 1
    if cur_row_reverse == key - 1:
      up_reverse = False
    elif cur_row_reverse == 0:
      up_reverse = True
  return word
  
  

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ): #Aayush Code
  only_letters = ''
  for chars in strng:
    if (ord(chars) >= 97 and ord(chars) <= 122) or (ord(chars) >= 65 and ord(chars) <= 90):
      chars = chars.lower()
      only_letters +=  chars
    else:
      pass
  return only_letters

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s): #Danny Code
  x = ord(p) + (ord(s) - 97) 
  if x > 122:
    y = 96 + abs(122 - x)
  else:
    y = x
  z = chr(y)
  return z

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s): #Danny Code
  x = ord(s) - ord(p) + 97 
  if x < 97:
    y = 123 - (ord(p) - ord(s))
  else:
     y = x
  z = chr(y)
  return z

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def pass_string(filteredStrng, p): #Danny Code
  if len(filteredStrng) == len(p):
    return p
  else:
    x = int(abs(len(filteredStrng) - len(p)))
    for i in range(x):
      p += p[i]
  return p 

def vigenere_encode ( strng, phrase ): #Danny Code
  passPhrase = pass_string(strng, phrase)
  encoded = ''
  for i in range(len(strng)):
        #print(passPhrase[i], strng[i])
    encoded += encode_character(passPhrase[i], strng[i])
    #find phrase and set output to var 
    #string to store result and return string 
    #loop encode strng times 
    return encoded



#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ): #Danny Code
  passPhrase = pass_string(strng, phrase)
  decoded = ''
  for i in range(len(strng)):
    #print(passPhrase[i], strng[i])
    decoded += decode_character(passPhrase[i], strng[i])
  return decoded


def main():
    # COMMENT OUT NEXT LINE 
    #sys.stdin = open('cipher.in.txt', 'r')
  # NEXT 4 LINES ARE PLACEHOLDERS SO I CAN TEST 
    rail_fence_plain = sys.stdin.readline().strip()
    rail_fence_key = (sys.stdin.readline())
    print(rail_fence_plain)
    print(rail_fence_key)
  # read the key from stdin
    
  # encrypt and print the encoded text using rail fence cipher

  # NEXT 4 LINES ARE PLACEHOLDERS SO I CAN TEST 
    rail_fence_encoded = sys.stdin.readline().strip()
    rail_fence_encoded_key = (sys.stdin.readline())
    print(rail_fence_encoded)
    print(rail_fence_encoded_key)

  # read the key from stdin

  # decrypt and print the plain text using rail fence cipher

  # read the plain text from stdin

  # read the pass phrase from stdin
  # encrypt and print the encoded text using Vigenere cipher
  #DANNY CODE STARTS HERE IN MAIN 
    print("Vigenere Cipher")
    plainText = filter_string(sys.stdin.readline().strip())
    passPhrase = sys.stdin.readline().strip()
    print('')
    print("Plain Text:", plainText)
    print("Pass Phrase:", passPhrase)
    print("Encoded Text:", vigenere_encode(plainText, passPhrase))
  # read the encoded text from stdin

  # read the pass phrase from stdin

  # decrypt and print the plain text using Vigenere cipher
    print('')
    print("Encoded Text:", vigenere_encode(plainText, passPhrase))
    print("Pass Phrase:", passPhrase)
    print("Decoded Text:", vigenere_decode (vigenere_encode(plainText, passPhrase), passPhrase))
  

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
