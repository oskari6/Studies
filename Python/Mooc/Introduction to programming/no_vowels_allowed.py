# Write your solution here
# Write your solution here
def no_vowels(word):
    chars = "aeiou"
    for c in chars:
        word = word.replace(c, "") 
    return word

if __name__ == "__main__":
    word = "hi everybody!"
    print(no_vowels(word))