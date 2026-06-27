def rotate(text, key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    new=''
    for char in text :
        if char.isupper() and char.isalpha():
            new=new+ alphabet[(alphabet.find(char.lower()) + key) % 26].upper()
        elif char.islower() and char.isalpha():
            new=new+ alphabet[(alphabet.find(char) + key) % 26].lower()
        else :
            new=new+char
    return new
