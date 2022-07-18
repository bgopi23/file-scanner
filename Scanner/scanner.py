# to run command-line/terminal prompts in python
import subprocess


# user guide
print('Either Drag and Drop your file into the terminal or type the file pathname in the space below')
print('_____________________________________________________________________________________________')
# gather user input
Cybersierra_File = input("Enter your File Pathname: ")


# update ClamAV virus database
subprocess.run(["freshclam"])
# scan inputted file using ClamAV 
subprocess.run(["clamscan" ,Cybersierra_File])


