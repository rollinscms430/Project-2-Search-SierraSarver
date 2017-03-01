# Project 2 - Solving Problems by Searching: Boggle
# Sierra Sarver 2/26/17

"""Implement recursive technique to find words from boggle board utilizing
   dictionaries, lists, and tuples."""

# 8 possible direction list
directions = [( 1,  0),   # right
              ( 1,  1),   # down-right
              ( 0,  1),   # down
              (-1,  1),   # down-left
              (-1,  0),   # left
              (-1, -1),   # left-up
              ( 0, -1),   # up
              ( 1, -1)]   # up-right

# Variables to be set and initialized
wordlist = set()
prefix_dictionary = {}
grid = ['unth', 
        'gaes', 
        'srtr',
        'hmia']

def find_words(x0, y0, prefix, visited, node):
    """Finds words starting from most top left node using the given prefix string
       and excluding the grid positions from a tuple that has already been visited."""
    words = set()
    for dx, dy in directions:
        # Validate current position 
        # Not valid: (too far off sides, bottom/top, or already visited)
        x = x0 + dx
        if x < 0 or x >= 4 :
            continue  # done if we go off the grid
        y = y0 + dy
        if y < 0 or y >= 4:
            continue  # done if we go off the grid
        if (x, y) in visited:
            continue  # done if this position has already been visited
        
        # Get the letter from this current position
        letter = grid[y][x]
        # Combine the prefix and letter in that position to create some word
        word = prefix + letter
        # If that word is in our wordlist, then add it to found words for a match.
        if word in wordlist:
            words.add(word)
        
        # If the letter of the current position is a prefix still but needs
        # to check for more letters for longer words, then recursively find
        # those other words from this prefix then add it to our found words for match.
        if letter in node:
            words.update(find_words(x, y, word, visited + ((x, y),), node[letter]))
    
    return words


def search():
    """Search our grid and return a set of all the found words using 
       our find words method."""
    words = set()
    for y0 in xrange(4):
        for x0 in xrange(4):
            letter = grid[y0][x0]
            words.update(find_words(x0, y0, letter, ((x0, y0),), prefix_dictionary[letter]))
    return words


def open_wordlist():
    """Open our text file wordlist."""
    with open('words.txt') as file:
        wordlist = set(line.strip() for line in file if len(line.strip()) >= 2)
    return wordlist


def build_prefix_dictionary(word_list):
    """Build our prefix dictionary based on the matching letters from wordlist."""
    dictionary = {}
    for word in wordlist:
        node = dictionary
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
    return dictionary

# Main
if __name__ == '__main__':
    # Set our wordlist with appropriate method
    wordlist = open_wordlist()
    # Create our prefix dictionary from that generated wordlist
    prefix_dictionary = build_prefix_dictionary(wordlist)
    print '\n'

    # Print the given grid
    print 'Current Boggle Grid:'
    for row in grid:
        print row
    print '\n'

    # Call search and print the found matches
    words = search()
    print 'Found Words:'
    print ' '.join(sorted(words))