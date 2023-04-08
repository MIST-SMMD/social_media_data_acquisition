# MIST-SMMD: Social media data acquisition implementation

> The content of this repository contains the implementation source code for social media data acquisition in the MIST-SMMD project.

![introduce](/static/images/intro.gif)


## Introduction
This project uses Sina Weibo as a data source platform for research. 
Sina Weibo is an internet-based social media platform, launched by Sina Corporation in 2009 as a microblogging service. 
Users can post short texts, images, videos, and other multimedia content on Sina Weibo, 
as well as interact with other users through actions such as following, commenting, reposting, and liking. 
As one of the most important and popular social media platforms in China, 
Sina Weibo has a wide-ranging influence in Chinese society, 
serving as a significant platform for news dissemination, 
information sharing, opinion expression, and social interaction.

## Demo
You only need to clone this repository and install third-party support libraries to use.
```
git clone https://github.com/MIST-SMMD/social_media_data_acquisition.git
pip install -r requirements.txt
python cli.py
```
If you use a database, you need to install MySQL database yourself. Weibo cookie needs to be obtained by yourself.（See the following steps for How to Obtain Weibo Cookie.）.


## Implementation:
We use Python to write scripts to simulate user requests for search on Sina Weibo,
and utilize the beautifulsoup4 library to parse web pages and extract relevant data.

### Data clean - character clean
The code repository uses character matching and regular expression matching
to preprocess and clean noisy data in Weibo messages for efficient text data processing. 
Character-level cleaning includes removing topic tags, zero-width spaces (ZWSP), 
mentions to other users, Emoji emoticons, HTML tags, and other noise in the text data.

[Implementation code](/Utils/clean.py)

### Media file acquisition
The data returned from the request URL for Weibo posts includes image id (unique identifiers) and video URL information.
These addresses are parsed and requests are made to retrieve media files.
**It is important to note that not every Weibo post contains media data.**

**Note: As of April 8, 2023, during testing, there was an HTTP 403 error in response to image requests,
which are currently unavailable for use.**


### List of Support Libraries
| Lib            | Version | Function        | 
|----------------|---------|-----------------|
| SQLAlchemy     | 2.0.9   | Database        |
| PyMySQL        | 1.0.3   | Database Driver |
| beautifulsoup4 | 4.12.1  | Parsing Data    |
| loguru         | 0.6.0   | Logging Module  |
| requests       | 2.28.2  | Network Request |

You can also use the following commands to quickly install these third-party supporting libraries.
```bash
pip install -r requirements.txt
```

## How to Obtain Weibo Cookie
### pc
- Open https://s.weibo.com/weibo?q=暴雨 ('暴雨' is not a unique parameter)
- Open the browser developer console (F12) and view the request's headers. Find the Cookie
![developer console](/static/images/20230407221120.png)
### mobile 
- Open https://m.weibo.cn/detail/4886532286323175 (4886532286323175 is not a unique parameter)
- Open the browser developer console (F12) and view the request's headers. Find the Cookie
![developer console](/static/images/20230407221334.png)

## Project Structure
- Config
  - config.ini (Configuration Information, Cookie/Database Connection Information)
  - config.py (Configuration File)
- Database
  - Mysql.py (Database Connection Engine)
- logs (Run Log)
- Model
  - models.py (ORM Database Models)
- Network
  - Files.py (Media File Operations)
  - Sina.py (Sina Weibo API Operations)
- static
  - media (Default Media Storage Location)
  - output
- Utils
  - clean.py (Data Cleaning Module)
  - convert.py (Data Format Conversion Module)
  - logutils.py (Logging Module)
  - timeutils.py (Time Module)
- venv (Python Environment)
- app.py (Main Function of the Program)
- cli.py (Command-Line Interface (CLI) Program)

