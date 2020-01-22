# reddit-ban-logs
A simple script that documents all of the users banned today onto a Google sheet for future reference. Works with communities you moderate.

## Requirements
* [praw](https://praw.readthedocs.io/en/latest/)
* [gspread](https://gspread.readthedocs.io/en/latest/)
* [oauth2client](https://github.com/googleapis/oauth2client)

## Usage
Clone repository and ensure that you have installed all of the required modules as listed above. Fill out 'config.py' with your reddit API credentials. Follow [this video](https://www.youtube.com/watch?v=cnPlKLEGR7E) to setup your Google API and to download your 'creds.json' file. 