# Flash-Card-App
Flash Card App made with Python and Tkinter.

This app allows the user to study/review any topics. In my case, I programmed this app with the idea of easing my Cantonese study.
I first tested the app with some French/English words, before jumping to Cantonese/English words.

The program will display a flashcard with a Cantonese word (including the Jyutping pronounciation). Then after 3 seconds, the card will flip and 
will show the English translation. If the user knew the translation, he/she can simply press the green check mark, if he didn't knew or forgot 
the translation, he can just press the red X. Pressing the green check mark will result in the word known to be removed from the list of words
and considered for learning. In fact, this app will focus on words the user has trouble remembering or knowing.

Therefore after the first iteration of the program, a new csv file will appear in the data folder, namely "words_to_learn.csv". This will include all
the words the user didn't press the green check mark on. These are the words that the user should therefore focus on, and the next time the user will
run the program, the words displayed on the flashcards will be coming from the "words_to_learn.csv" file and not from the original "cantonese_words.csv" file.

The user can always delete manually the "words_to_learn.csv" if he wants to start anew.

This program can split into 4 steps:

1. Making the UI with Tkinter  
2. Creating new flash cards by accessing the data from a csv file and using it to fill the Canvas object in our UI  
3. Flipping the cards by making a delay of 3 seconds, then calling a function to that effect that will modify our canvas
4. Saving the user's progress by removing the words that the user knows and the saving the words the user doesn't know into a csv file, that will then be used for all future study.
