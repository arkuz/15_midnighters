# Night Owls Detector

Devman database stores information about who and when sent the task for verification. This script gets a list of people who have passed their homework after 24:00

# Installation

Install the virtual environment and all necessary packages from the file `requirements.txt`

```bash
git clone https://github.com/arkuz/15_midnighters.git 
virtualenv -p python3 venv
cd venv
source bin/activate
cd ..
pip install -r requirements.txt
```

# Quickstart

```bash
$ python3 seek_dev_nighters.py
Getting a list of users, please wait...
  da3c84b1d9eb403e - 05:40:50
  da3c84b1d9eb403e - 05:20:33
  РамильЯббаров - 00:04:35
  arkuz - 01:09:32
  8e94ac43ec4e4c57 - 01:09:31
  a4d7936053fc4520 - 01:06:57
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
