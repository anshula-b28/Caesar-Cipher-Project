## Explanation of the program caesar_cipher.py

- Step by step explanation in Encryption:

  1.encrypted="" → Initializes an empty string to store the result.

  2.for char in message: → It loops through each character of the message.

  3.if char.isalpha(): → It checks if the character is a letter (ignores spaces, numbers, punctuation).

  4.base=ord('A') if char.isupper() else ord('a') → Determines ASCII base depending on uppercase or lowercase.

  5.encrypted+=chr((ord(char)-base+shift)%26+base) → Converts character to a number (0–25) using ord(char)-base. 
  
     Adds the shift and uses %26 to wrap around the alphabet (so Z+1 becomes A).
  
     Converts back to a character using chr(...).
  
  6.else: encrypted+=char → If not a letter, just keep it as is.

  7.return encrypted → Return the encrypted string.


- Explanation in Decryption:

  1.Purpose: Reverses the encryption process using the same shift.

  2.Works almost the same as encrypt, except it subtracts the shift instead of adding it.

  3.This ensures that letters go back to their original position in the alphabet.


- Step by step explanation in Main Program:

  1.Ask the user to enter a message.

  2.Ask the user to enter a shift value (integer).

  3.Call the encrypt function and store the result in encrypted_text.

  4.Print the encrypted message.

  5.Call the decrypt function on the encrypted text to verify it returns to the original message.

  6.Print the decrypted message.

