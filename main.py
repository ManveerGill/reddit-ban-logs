import praw
import config
import time
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] # Scope for Google Drive/Sheets API
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) # JSON file containing Google API credentials 
client = gspread.authorize(creds)

SHEET = client.open("YOUR SHEET NAME HERE").sheet1 # Edit your sheets name

reddit = praw.Reddit(
    client_id = config.client_id,
    client_secret = config.client_secret,
    username = config.username ,
    password = config.password ,
    user_agent = config.user_agent)

for log in reddit.subreddit('mod').mod.log(limit = 2000): # Loop through 2000 moderator log actions
    if (str(log.action)) == 'banuser': # Find actions that lead to a user being banned
        yesterday = datetime.now() - timedelta(days = 1) # Script runs at 12:05am EST daily, so it needs to only focus on users that were banned on the last calendar day
        yesterday = yesterday.strftime('%d')
        reddit_day = time.strftime('%d', time.localtime(log.created_utc))

        if yesterday == reddit_day:
            SHEET.insert_row((str(log.target_author), str(log.details), str(log.description), str(log.mod), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.created_utc))), 2) # Insert a new row onto our Google Sheet at row 2, pushing the other rows down
            time.sleep(1) # Wait 1 second before proceeding, Google tends to rate limit causing the script to crash



