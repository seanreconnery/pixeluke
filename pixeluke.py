# Really janky PixelKnot password cracker I tossed together to help out.
# PROBLEM ---	since PixelKnot uses the last 1/3rd of the password to encrypt, we only try the LAST 3rd..
#		However... this is a slight problem in the case of:  abc123 & 1723
#		both of these will result in the cracker trying "23" as the password.
#		so, you may need to do some error mitigation after finding a possible password.
# USE:  python3 pixeluke.py image.jpg wordlist.txt
# Happy Hunting!

import os, sys, subprocess, math

img = sys.argv[1]		# file path to the image
pwlist = sys.argv[2]		# file path to a list of passwords

if not img:
	print("No image specified.")
	print("USAGE:  python3 pixeluke.py image.jpg wordlist.txt")

if not pwlist:
	print("No password list specified.")
	print("USAGE:  python3 pixeluke.py image.jpg wordlist.txt")


with open(pwlist) as pw:	# open the file
	pword = pw.readline().strip()	# read a line in
	cnt = 1			# set our COUNTER to the 1st position

	while pword:	
		# while we have a password to try, we keep trying.
		# grab the last 1/3rd of the password
		passlen = len(pword) / 3
		last_third = math.ceil(passlen)
		negthird = -1 * last_third
		passw = pword[negthird:].strip()

		# build our command as an array of values
		comm = [ 'java', '-jar', 'f5.jar', 'x', '-p', passw, img ]

		# output the progress to our user
		print("Try # {}: Password:  {} \n   Last 1/3: {}".format(cnt, pword.strip(), passw))	

		# run our command and pipe the output back to a variable we'll call RESULT
		result = subprocess.Popen( comm, stdout=subprocess.PIPE ).communicate()[0]
		
		if str(result).find("only") > 0:
			#print("wrong password.")
			pword = pw.readline().strip()	# set the next line
			cnt += 1			# increase the counter

		else:
			# holy crap, we found something!!
			with open('output.txt', 'r') as f:
				file_check = f.read()

			print("")
			print("------- !!!FOUND PASSWORD!!! -------")
			print("")
			print("Password:    [  " + str(pword) + "  ]")
			print("Try # " + str(cnt))
			print("")
			print(str(file_check))
			print("")
			pword = ""		# clear this variable and break out of our loop.


print("------- CRACKING COMPLETE -------")

