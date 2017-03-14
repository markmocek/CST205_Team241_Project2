def helper(message, shift):
    #Set string to lower case
	message = message.lower()
	#Set string to hold characters
	code = ""
	
	#Encrypt String
	for c in message:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			# wrap list if necessary
			if num > ord("z"):
				num -= 26
			elif num < ord("a"):
				num += 26
			code = code + chr(num)
		#Only modify letters
		else:
			code = code + c
	return code

#Encrypts the string and returns the result.
def encrypt(message):
	return helper(message, 3)

#Decrypts the string and returns the result.
def decrypt(message):
	return helper(message, -3)

#Collect string to encrypt
msg = input("Enter string: ")
if len(msg) > 0:
	#Place encrypted message in code variable
	code = encrypt(msg)
	print("Encrypted message is: ", code)
else:
	#Empty string, prompt user with new line
	code = input("Enter message to decode: ")
	if len(code) > 0:
	    #Place decrypted message in code variable
		msg = decrypt(code)
		print("The decrypted message is:", msg)
