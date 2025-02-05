#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def main():
    """Main function to handle user input and display the word count."""
    print("Word Counter Program")
    print("--------------------")
    
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()


# In[ ]:




