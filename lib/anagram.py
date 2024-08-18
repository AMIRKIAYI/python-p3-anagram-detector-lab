class Anagram:
    def __init__(self, word):
        # Store the sorted version of the word for easy comparison
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, word_list):
        # Find and return all anagrams in the list
        return [word for word in word_list if sorted(word) == self.sorted_word]

# Testing the implementation
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # Output: ['inlets']
