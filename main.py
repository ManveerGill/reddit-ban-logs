import requests
import praw
import config
import time
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Ban Log").sheet1

reddit = praw.Reddit(
    client_id = config.client_id,
    client_secret = config.client_secret,
    username = config.username ,
    password = config.password ,
    user_agent = config.user_agent)

for log in reddit.subreddit('mod').mod.log(limit = 2000):
    if (str(log.action)) == 'banuser':
        #print('Banned User: {}, Duration: {}, Details: {}, Banned by: {}, Date: {}'.format(log.target_author, log.details, log.description, log.mod, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.created_utc))))
        
        yesterday = datetime.now() - timedelta(days = 1)
        yesterday = yesterday.strftime('%d')
        reddit_day = time.strftime('%d', time.localtime(log.created_utc))

        if yesterday == reddit_day:
            sheet.insert_row((str(log.target_author), str(log.details), str(log.description), str(log.mod), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.created_utc))), 2)
            time.sleep(1)



