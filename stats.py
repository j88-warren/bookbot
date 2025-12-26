def get_book_text(path_to_file): #defining a function that takes a file path as an argument
	with open(path_to_file) as f: #opens the file and assigns it to variable f
		   return f.read() #returns the contents of the variable f	

def count_words(text): #defining a function that takes text as an argument
	words = text.split() #splits the text into words based on whitespace and assigns it to variable words
	return len(words) #returns the number of words by calculating the length of the words list

def count_characters(text): #defining a function that takes the result of get_book_text function as an argument
	character_count = {} #creates an empty dictionary to store character counts
	for char in text: #iterates through each character in the text
		if char.isalpha(): #checks if the character is an alphabet letter
			char = char.lower() #converts the character to lowercase
			if char in character_count: #checks if the character is already in the dictionary
				character_count[char] += 1 #increments the count for that character up 1
			else:
				character_count[char] = 1 #initializes the count for that character to 1
	return character_count #returns the dictionary containing character counts

def sorted_character_count(text): #defining a function that takes text as an argument
	character_count = count_characters(text) #calls the count_characters function with the text and assigns the result to variable character_count
	sorted_character_count = dict(sorted(
		character_count.items(), #gets the items (key-value pairs) from the character count dictionary as a tuple
		key=lambda x: x[1], #specifies that the sorting should be based on the second element of the tuple (the value/count)
		reverse=True)) #sorts the character count dictionary items based on the count in descending order
	for char, count in sorted_character_count.items(): #iterates through each character and its count in the sorted character count dictionary
		character_count = (f"{char}: {count}") #formats the character and its count as a string
		print(character_count) #prints the formatted string showing the character and its count

