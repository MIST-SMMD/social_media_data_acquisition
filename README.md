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

## Implementation:
We use Python to write scripts to simulate user requests for search on Sina Weibo,
and utilize the beautifulsoup4 library to parse web pages and extract relevant data.


### List of Supported Libraries
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
- logs (运行日志)
- Model
  - models.py (ORM Database Models)
- Network
  - Files.py (Media File Operations)
  - Sina.py (Sina Weibo API Operations)
- static
  - images (Default Image Storage Location)
  - video (Default Video Storage Location)
  - output
- Utils
  - clean.py (Data Cleaning Module)
  - convert.py (Data Format Conversion Module)
  - logutils.py (Logging Module)
  - timeutils.py (Time Module)
- venv (Python Environment)
- app.py (Main Function of the Program)
- cli.py (Command-Line Interface (CLI) Program)

