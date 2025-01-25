#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

# Lists of adjectives and nouns
adjectives = ['Happy', 'Sad', 'Fast', 'Slow', 'Red', 'Blue', 'Green', 'Yellow', 'Bright', 'Dark']
nouns = ['Tiger', 'Dragon', 'Eagle', 'Shark', 'Lion', 'Wolf', 'Panther', 'Falcon', 'Bear', 'Fox']

def generate_username(include_numbers=True, include_special_chars=True, length=None):
    """
    Generate a random username based on user preferences.

    Parameters:
    - include_numbers (bool): Whether to include numbers in the username.
    - include_special_chars (bool): Whether to include special characters in the username.
    - length (int): Desired length of the username. If None, length is determined by components.

    Returns:
    - str: Generated username.
    """
    username = random.choice(adjectives) + random.choice(nouns)

    if include_numbers:
        username += str(random.randint(0, 99))

    if include_special_chars:
        username += random.choice(string.punctuation)

    if length and len(username) > length:
        username = username[:length]

    return username

def save_usernames_to_file(usernames, filename='usernames.txt'):
    """
    Save a list of usernames to a file.

    Parameters:
    - usernames (list): List of usernames to save.
    - filename (str): Name of the file to save the usernames in.
    """
    with open(filename, 'w') as file:
        for username in usernames:
            file.write(username + '\n')

def main():
    print("Welcome to the Random Username Generator!")
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    length = input("Desired username length (press Enter for default): ").strip()
    length = int(length) if length.isdigit() else None

    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]

    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    save_option = input("\nWould you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        filename = input("Enter the filename (default is 'usernames.txt'): ").strip()
        if not filename:
            filename = 'usernames.txt'
        save_usernames_to_file(usernames, filename)
        print(f"Usernames have been saved to {filename}")

if __name__ == "__main__":
    main()


# In[ ]:




