!/bin/bash

echo "_______________________________________"
echo "|===          CoMet version 0.1            ===|"
echo "|= ~ Collection of Metadata Extractor Tool ~ =|"
echo "|=          Coded By: Zech Bron              =|"
echo "|=    GitHub: https://github.com/ZechBron    =|"
echo "|_____________________________________________|"



echo -e "Please Chooose: "
echo -e " 1. Termux"
echo -e " 2. Ubuntu"
echo -e " 3. Other"
read zCh

if [ $zCh = 1 ]; then
pkg install python -y
pip install --upgrade pip
pip install -U audio-metadata
pip install PyPDF2

elif [ $zCh = 2 ]; then
apt-get install python3 -y
apt-get install python3-pip -y
apt-get install python-pip3 -y
pip install --upgrade pip
pip install -U audio-metadata
pip install PyPDF2

elif [ $zCh = 3 ]; then
apt install python3 -y
apt install python3-pip -y
apt install python-pip3 -y
pip install --upgrade pip
pip install -U audio-metadata
pip install PyPDF2

else
echo -e "\e[91mWrong input\e[0m"
fi
