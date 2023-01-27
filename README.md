# Overview
This is a small script designed to send a Telegram message to myself, once a day, at 8am, letting myself know whether the *Brew Metric Watch (Silver)* is available. <br>
The script utilises a basic web scraper to scan the main body of watch description, and checks if it contains the **Sold out** phrasing. <br>
Using Pyinstaller, the script has been converted to an **executable** file. <br>
The specific Telgram bot token has been redacted for privacy reasons


## Tech
  - Python
  - Beautiful Soup
  - Telegram Bot API
  - Pyinstaller

## Cronjob
```
* 8 * * * ~/documents/repos/watch-out/dist/main
```
