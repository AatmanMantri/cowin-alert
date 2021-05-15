# cowin-alert
A simple python script to alert when slot for a particular pincode is free for the age 18+

For setting up python virtual env (optional but recommended):
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Installing dependencies:
`pip install requests`
`pip install playsound`
`pip install PyObjC` (only required for MacOS)

Command to run:
`python3 <pincode> <refresh interval (in seconds)> <alert_sound (tested with mp3)>`
eg: `python3 313603 60 song.mp3`
