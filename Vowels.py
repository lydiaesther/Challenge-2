def vowel(text):
    vowels = "aeiou"
    print([letter for letter in text if letter in vowels])
    print(len([letter for letter in text if letter in vowels]))
vowel('drinking water');


