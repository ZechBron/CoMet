


####
#		CoMet version 0.1
#	~ Collection of Metadata Extractor Tools ~
#		Coded By: Zech Bron
#	   https://github.com/ZechBron
#
# NOTE:
# CoMet contains two metadata extractor which is Pdf and Audio only.
# I will update this script of mine with additional stuff like mp4 metadata extractor etc...
# As of now. You might want to follow me in GitHub?
###

import os
import PyPDF2
import audio_metadata
def banner():
   os.system("clear")
   print("_______________________________________________")
   print("|===\033[0;32m          CoMet version 0.1 \033[0;0m           ===|")
   print("|= \033[0;34m~\033[0;32m Collection of Metadata Extractor Tool\033[0;0m\033[34m ~ \033[0;0m=|")
   print("|=\033[0;33m          Coded By:\033[0;0m\033[0;36m Zech Bron \033[0;0m             =|")
   print("|=\033[0;33m    GitHub:\033[0;0m\033[0;36m https://github.com/ZechBron \033[0;0m   =|")
   print("|_____________________________________________|")
   print("\n")
banner()
# Audio Metadata
def zAudio(audioFile):
   zCh = audio_metadata.load(audioFile)
   print(zCh)

# Pdf Metadata
def zPdf(zFile):
   read = PyPDF2.PdfFileReader(zFile, 'rb')
   pdf = read.getDocumentInfo()
   for i in pdf:
      print("\033[0;36m[\033[0;0m\033[0;32mZ\033[0;0m\033[0;36m]\033[0;0m " + i + ": " + pdf[i])


print("\033[0;34mWhat do you want?\033[0;0m")
print(" a. Pdf")
print(" b. Audio")
zCh = input("\033[0;36m[\033[0;0m\033[0;32mZ\033[0;0m\033[0;36m]\033[0;0m \033[0;34mPlease Choose: \033[0;0m")


if zCh == 'A' or zCh == 'a':
   zFile = input("\033[0;36m[\033[0;0m\033[0;32mZ\033[0;0m\033[0;36m]\033[0;0m \033[0;34mEnter pdf file: \033[0;0m")
   zPdf(zFile)

elif zCh == 'B' or zCh == 'b':
   audioFile = input("\033[0;36m[\033[0;0m\033[0;32mZ\033[0;0m\033[0;36m]\033[0;0m \033[0;34mEnter audio file: \033[0;0m")
   zAudio(audioFile)

else:
   print("\033[0;36m[\033[0;0m\033[0;31m!\033[0;0m\033[0;36m]\033[0;0m Wrong input")
