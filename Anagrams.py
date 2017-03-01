# Project 2 - Solving Problems by Searching: Anagrams
# Sierra Sarver 2/26/17

"""Implement a dictionary to keep track of the anagrams
   or words that contain the same set of letters."""

# Open text file
file = open('words.txt')
   
# The sorted letters of each word will be the keys
# A list of words having those keys will be the values
anagrams = {}

# Loop through file
for line in file:
    
    # Remove whitespace
    line = line.strip()
    
    # Use tuple to create immutable list of the sorted letters
    sorted_letters = tuple(sorted(line))
    
    # If letter sequence is unique, create new dictionary entry
    if sorted_letters not in anagrams:
        anagrams[sorted_letters] = []
        
    # Else append the mattching letter sequence to list of anagrams
    anagrams[sorted_letters].append(line)
    
# Print all words with matches
for words in anagrams:
    if len(anagrams[words]) > 1:
      print anagrams[words]