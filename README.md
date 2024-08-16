# A level Computer Science transition work

by Varfolomeev Iaroslav

- Task 4 - Linear search programming task [search/](https://github.com/ivarfol/cs_transition_rushcliffe/tree/main/search)
	- programs uses array "Florida","Georgia","Delaware","Alabama","California"
	- programs asks the user to input a state to find
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
		- allows to turn on the mode to guess several number silmantaniously, like in quardle
		- allows to change the number of numbers being guessed silmantaniously by default
		- allows to turn off the input for the number of guesses
		- allows to change the number of guesses by default
- Programming Extension Tasks:
	1. Prime Number Checker [prime_number_checker.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/prime_number_checker.py)
	2. Palindrome Detector [palindrome_detector.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/palindrome_detector.py)
	3. Hangman Game [hangman.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/hangman.py)
	4. File Encription/Decription [encription.py](https://github.com/ivarfol/cs_transition_rushcliffe/blob/main/encription.py)
