# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, possible_anagrams):
        sorted_possible_anagrams = [sorted(possible_anagram.lower()) for possible_anagram in possible_anagrams]

        matches = [anagram for anagram in possible_anagrams if sorted_possible_anagrams[possible_anagrams.index(anagram)] == self.word]

        return matches
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))