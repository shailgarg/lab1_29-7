def count(text):
    
    vowels = "aeiouAEIOU"
    
    
    vowel = 0
    consonant = 0
    
    
    for char in text:
        if char.isalpha():  
            if char in vowels:  
                vowel += 1
            else:  
                consonant += 1
    
    return vowel, consonant


string = input("Enter a string: ")


vowels, consonants = count(string)


print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
