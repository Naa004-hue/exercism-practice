"""Functions for creating, transforming, and adding prefixes to strings."""
def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un"+word
    
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string  """
    return (" :: " + vocab_words[0]).join(vocab_words[0:])
    
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    if "iness" in word :
        return word.replace("iness","y")
    return word.replace("ness","")
    
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words=sentence.split()
    if "." in words[index]:
        return words[index].replace(".","en")
    return words[index]+"en"