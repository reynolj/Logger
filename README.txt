This script reads a text file to log you into your accounts.
The file is not encrypted in any way, this is for convenience. 

Prerequisites are: 
- Install the chromedriver.exe from https://chromedriver.chromium.org/downloads
- Install selenium
  - pip3 install selenium
- Create a file with lines formatted as: <SITE> <USER_ELEMENT_NAME> <PASSWORD_ELEMENT_NAME> <USERNAME> <PASSWORD> <OPTIONAL_REDIRECT>

This is a command line script that requires arguments.
The format is: 
  logger.py -f <filename>

This script does not work on websites that redirect you at the start or require you to agree with something prior to login
