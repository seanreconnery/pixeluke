# PixeLuke
hastily thrown together PixelKnot password cracker, utilizing F5.jar (from f5-steganography)

Utilizes f5.jar to attempt passwords from your supplied list.

# Usage:
python3 pixeluke.py pk-luke.jpg passlist.txt


# A few words of warning...
Because PixelKnot only uses the last 1/3rd of the password to unlock the file portion, we are prone to incorrect passwords if they have the same "last 1/3rd" as the ACTUAL password.
EXAMPLE:  the password for the pk-luke.jpg image is "abc123" with PixelKnot.  However, using f5.jar, you only have to enter "23" (the last 1/3rd) of the password to unlock the embedded file.
Now.. here's the tricky part..
The file that this unlocks is STILL encrypted.  But it unlocks the file, and you can verify it IS the right password by loading the image into PixelKnot and inputting the FULL password.
Obviously, if PixelKnot spits out a message at you... yay!  You've done it!
If PK tells you "no dice" though.. then we know you have the LAST 3rd correct, but we need to fix the beginning part of the password somehow.

Happy Hunting!
