# Automated Social Media Spear-Phisher Facebook Post
## Authors: 
- Abdullah Arif
- Abdullah Chattha
- Ashraf Taifour
- Mohamad Elchami
- Steve Pham

## Supervisor
    Dr. Sherif Saad Ahmed

## Adding packages
	Don't forget to `pip3 freeze > requirements.txt` - after installing packages in virtual environment

## How to run
Program has been tested on Linux

1. Setup
* Make sure you have gecko driver installed: https://github.com/mozilla/geckodriver/releases
* Also, install TOR: https://www.torproject.org/download/ 
* Extract TorFolder to program directory
2. Putting in login information
* Navigate to the secretDirectory/secret.py file and put in your email, password and username
3. Recommended step: use virtual environment
```
python3 -m venv facebookEnv
source facebookEnv/bin/activate
```
4. Install dependencies 
`pip3 install -r requirements.txt`

5. Run program
    `python3 main.py`

# What is this? 🤔
The part of the social media automated spear phisher that allows automatically posting to Facebook
