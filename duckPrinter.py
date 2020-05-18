def create_quack(text):
	# Top text box border
	print("    ----------------------------    ")

	# Creates a text box with 18 chars per line
	# Plus 4 chars padding and "<>" at borders
	for i in range(len(text)):
		## Padding at the start of every line and "<" border delimiter 
		if i % 18 == 0:
			print("   <     {}".format(text[i]), end="")

		# When the end of line is reached, create some padding and a ">" border
		elif i % 18 == 17 and i != 1:
			print("{}     >    \n".format(text[i]), end="")
		
		# Prints each character of the current line
		else:
			print(text[i], end="")


		# Adds final padding and border ">"
		# Needed because sometimes the text doesn't reach the 18 chars
		if i == len(text) - 1 and len(text) % 18:
			for j in range(18 - i % 18):
				print(" ", end="")
			print("    >\n", end="")

	# Printing bottom border on the screen	
	print("    ----------------------------    ")

	# Prints a very cool duck
	print("""                     ^
              ..    /
             ( '`< /
              )(
       ( ----'  '.
       (         ;
        (_______,' 
jgs~^~^~^~^~^~^~^~^~^~^~""")


text = input()

create_quack(text)
