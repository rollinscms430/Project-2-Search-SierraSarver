# Project 2 - Solving Problems by Searching: Word Ladders
# Sierra Sarver 2/26/17

def ladder(start_word, end_word):
    
    """Implement a breadth-first search technique to generate a chain of
       words that only differ in one letter until a start word and end word
       are connected"""
    
    # Open file
    file = open('words.txt')
    
    # Build dictionary storing all of the words
    # that have the same length as the start word.
    word_dict = {}
    for word in file:
        if len(word) == len(start_word) + 1:
            # Remove whitespace
            word = word.strip()
            word_dict[word[:len(start_word)]] = start_word
    
    # Variables
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    queue = [start_word]

    # Breadth-first search on the dictionary of same length words.
    # Replaces a single letter of the current word with one in the alphabet
    # until a match is found from the word dictionary that was built.
    # When match is found, add that word to the queue and output the correct
    # path that was used to find all of the matches until the end word.
    while len(queue):
        curr_word = queue[0]
        queue.pop(0)
        
        if curr_word == end_word:
            return word_dict[curr_word]
            
        for i in range(len(start_word)):
            for letter in alpha:  
                if curr_word[i] != letter:              
                    nxt = list(curr_word)            
                    nxt[i] = letter              
                    new_word = str(''.join(nxt))
                    if new_word in word_dict and word_dict[new_word] == start_word:
                        queue.append(new_word)
                        word_dict[new_word] = word_dict[curr_word] + ' ' + new_word

# Main
if __name__ == '__main__':
    print ladder('snakes', 'brains')