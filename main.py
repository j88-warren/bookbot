import sys
from stats import get_book_text, count_words, sorted_character_count

def main(): #defining the main function, which takes no arguments
	if len(sys.argv) <2:
		print("'Usage: python3 main.py <path_to_book>'")
		sys.exit(1) #gets the book path from command line arguments or exits if not provided

	book_path = sys.argv[1] #gets the first command-line argument (the file path) and assigns it to variable book_path
	text = (get_book_text(book_path)) #Assigns the results from get_books_text function with the contents of the file "books/frankenstein.txt" to the variable text
	print("============ BOOKBOT ============") #prints the title "BOOKBOT" with equal signs for decoration
	print(f"Analyzing book found at {book_path}...") #prints a message indicating the book being analyzed
	print("----------- Word Count -----------") #prints a header for the word count section
	print(f"Found {count_words(text)} total words") #print function calls the count_words function with the variable text and prints the result from that function
	print("-------- Character Count --------") #prints a header for the character count section
	sorted_character_count(text) #calls the sorted_character_count function with the variable text to display the character counts in sorted order
	print("============= END ===============") #prints the footer "END" with equal signs for decoration


main ()	#calls the main function to execute the program