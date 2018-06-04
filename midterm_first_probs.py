def vowel_count(word):
    """
    Returns the number of vowels in a word (including y).
    :param word: the word to search for vowels

    >>> vowel_count('Harry')
    2
    >>> vowel_count('HAIRY')
    3
    """

    n = 0
    vowels = 'aeiouyAEIOUY'
    for char in word:
        if char in vowels:
            n += 1

    return n


def syllable_count(word):
    """
    Returns the number of syllables in the word.
    For this exercise, assume that syllables are determined as follows:
       Each sequence of vowels a e i o u y, except for the last e in a word, is a vowel.
       However, if that algorithm yields a count of 0, change it to 1.

    :param word: the word whose syllables are being counted.

    >>> syllable_count('Harry')
    2
    >>> syllable_count('HAIRY')
    2
    >>> syllable_count('hare')
    1
    >>> syllable_count('the')
    1
    """

    n = 0
    vowels = 'aeiouyAEIOUY'

    for x, char in enumerate(word, 1):
        if char in vowels:
            n += 1

    for i in range(len(word)-1):

        if str(word[i]) in vowels and str(word[i + 1]) in vowels:
            n -= 1

    if word.endswith('e') or word.endswith('E'):
        n -= 1

    if n == 0:
        n += 1

    return n

def filter_dict(filename, min, max):
    """
    From the specified dictionary file containing 1 word per line,
    return a list of words whose lengths are within the user-specified
    bounds. So for instance, if the min is 3 and max is 7,
    then only words with length >= 3 and length <= 7 will be
    returned in the list.

    :param filename: the dictionary file containing 1 word per line
    :param min: the min length (inclusive) of words to return
    :param max: the max length (inclusive) of words to return

    >>> filter_dict('small_dict.txt', 3, 5)
    ['acted', 'bios', 'coder', 'find', 'gore', 'knife', 'racer']

    >>> filter_dict('small_dict.txt', 7, 10)
    ['debased', 'shameful']
    """

    filteredWord = []

    with open(filename, 'r') as f:
        words = [line.strip() for line in f]
        for x in words:
            if len(x) >= min and len(x) <= max:
                filteredWord.append(x)

    return filteredWord



def gematria(word_to_match, filename):
    """
    Takes a word and the name of a dictionary file, and then
    returns (a list of) all the entries from the dictionary that
    Gematrically match the given word.

    "Gematria is the act of assigning numeric values to letters in an
     alphabet"
       -- (https://en.wikipedia.org/wiki/Gematria,
        last access 10/7/2017).
    Once each letter is assigned a value you can compute the value of
    a word or phrase by simply summing the values of each letter in
    the word/phrase. Using a mapping of a=1, b=2, c=3, ..., z=26,
    "Phil" has a value of P=16 + h=8 + i=9 + l=12 == 45.
    Note that the case of a letter does not change its value.

    :param word_to_match: the word for which you are trying to find a Gematric match
    :param filename: the dictionary file containing other candidate words

    >>> gematria('Phil', 'small_dict.txt')
    ['bios', 'coder', 'gore', 'knife', 'racer']
    """

    count = 0
    z = 0
    result = []

    value = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
             "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
             "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    nw = word_to_match.lower()
    for i in nw:
        if i in value:
            z += value[i]

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

        c = len(lines)

        for i in range(c):

            wordx = lines[i]
            wordx = wordx.lower()

            for c in wordx:
                if c in value:
                    count += value[c]

            if count == z:
                result.append(wordx)

            count = 0

    return result

