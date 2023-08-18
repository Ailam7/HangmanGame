# HangmanGame

A simple hangman game. You are given a hint and the length of the word at the start. You have to guess the word within 7 guesses. After each turn,
you are reminded of how many guesses you have left. The ASCII art of the noose will update after each wrong guess. 

*** 

### Credits 

The ASCII Art of the noose used in this program was taken from:

https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

***


### Words

The words used for the game are taken from the words.txt file. The file contains 270 words, from 9 different categories. Each line in the file has
the word, followed by a comma and then the category of it, which is the hint. So for example:

```
Canada, Country
```

In the above case, Canada would be the word and country would be the hint. 

***

### Adding your own words 

Adding your own words is very easy. Just add them in the same format as all the other words into the words.txt file. If you would like to add Pizza just add 

```
Pizza, Food
```

as a new line into the words.txt file. 

***

### Guesses 

You have 7 guesses. Each guess can be a character, or the word itself. Unless you're really sure of what the word is, its probably not a good idea 
to enter a word. Even a small spelling mistake means the program will take your guess as wrong. It's better to just type in letters until the word
is complete. 

Guesses are deducted only after a wrong guess. Case sensitivity is completely neglected in the program. Typing in 'A' is the same as typing in 'a'.
Guess must be alphabetic. If the guess contains any character that is not alphabetic, the program will reject that guess. 

***

### ASCII Art

ASCII art is used to visualize the noose at all stages of the game. The noose starts with the head of the stick figue, followed by his body, arms, and
legs. Once the body is complete, you are on your last guess. 

**Enjoy the program!**
