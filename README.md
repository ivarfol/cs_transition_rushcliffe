	# A level Computer Science transition work

by Varfolomeev Iaroslav

- Task 4 - Linear search programming task [search/](https://github.com/ivarfol/cs_transition_rushcliffe/tree/main/search)
	- programs use array "Florida","Georgia","Delaware","Alabama","California"
	- programs ask the user to input a state to find
	- if the state is in the array, the program reports the position in array it was found at
	- if the state is not found in the array the program reports "Item not found" to the screen
	- Linear search [linear_search.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/search/linear_search.py)
		- uses linear search algorithm to locate the index of the state
	- Optimised search [search.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/search/search.py)
		- uses .index() method to locate the index of the state
- Task 5 - Guessing game programming task [guessing_game.py](https://github.com/ivarfol/cs_transition_rushcliffe/tree/main/guessing_game)
	- program generates a random number between 0000 and 9999
	- lets the user choose the number of guesses between 5 and 20
	- after each guess displays the correct numbers in green, the correct but in the wrong place in yellow and the incorrect in white
	- to use the program remove the .example from the [guessing_game.yaml.example](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/guessing_game/guessing_game.yaml.example)
	- config [guessing_game.yaml.example](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/guessing_game/guessing_game.yaml.example)
		- allows to turn off wordle extension
		- allows to turn off wordle extension by default
		- allows to turn on the mode to guess several number simultaneously, like in quardle
		- allows to change the number of numbers being guessed simultaneously by default
		- allows to turn off the input for the number of guesses
		- allows to change the number of guesses by default
- Programming Extension Tasks:
	1. Prime Number Checker [prime_number_checker.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/prime_number_checker.py)
		- program checks if an integer is a prime number
		- program can check numbers for being prime ina range
		- program is optimised by using sqrt of the number
	2. Palindrome Detector [palindrome_detector.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/palindrome_detector.py)
		- program checks if a phrase is a palindrome
		- program ignores the punctuation
		- program handles case insensitive palindromes
	3. Hangman Game [hangman.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/hangman.py)
		- program chooses a random word from a list
		- program allows to guess letters
		- program reveals correctly guessed letters and tracks the incorrect guesses
	4. Student Grade Tracker [grade_tracker](https://github.com/ivarfol/cs_transition_rushcliffe/tree/main/grade_tracker)
		- [grade_tracker.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/grade_tracker/grade_tracker.py) allows to input commands to
			- add students
			- add scores
			- revert the last score
			- remove a student
			- rename a student
			- seve or exit without saving
		- config [config_grade_tracker.yaml.example](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/grade_tracker/config_grade_tracker.yaml.example)
			- allows to change the path to the file you want to load the results from by default
			- allows to change whether the program asks if you want to create a new dictionary
			- allows to change the path to the file you want to save the results to by default
	5. File Encryption/Decryption [encription.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/encription.py)
		- program encrypts or decrypts files or texts using a key
		- program supporst encryption of binary files
		- program supports Caeser cipher
		- to encript/decript a file enter the path to the file you want to encript/decript and the path to the file you want to write the result in
