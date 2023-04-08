# Copyright (c) 2023.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Project: social_media_data_acquisition
# @FileName: app.py
# @Author：hz157
# @DateTime: 10/1/2023 下午9:55
from Database.Mysql import Mysql
from Model.models import Article, User, Media, DictConvertORM
from Network.Files import DownloadWeiboVideo, DownloadWeiboImage
from Network.Sina import *
from Utils import timeutlis
from Utils.clean import CleanData
from Utils.logutils import LogUtils

logutils = LogUtils()


def main(keyword, outType):
    logutils.info("Spider Start Working")
    pages = getArticlePagesByKeyword(keyword)
    for page in range(pages):
        mids = getArticleMidsByKeyword(keyword, page)
        if mids is None:
            logutils.error("pc cookie invalid")
        for mid in mids:
            # Random delay 1-10s 随机延时1-3s
            timeutlis.sleep(1, 3)
            response = getArticlePageInfo(mid)
            if response is None:
                logutils.error("Weibo mobile cookie invalid")
                return
            UserInfo = getUserInfo(response)
            ArticleInfo = getArticleInfo(response)
            Images = getArticleImage(response)
            Video = getArticleVideo(response)
            if len(Images) != 0:
                for image in Images:
                    imagePath = DownloadWeiboImage(ArticleInfo['id'], image)
                    if imagePath is not None:
                        print(f'Images Download Success, path: {imagePath}')
            # Judge whether there are video  判断是否有视频
            if Video is not None:
                videoPath = DownloadWeiboVideo(ArticleInfo['id'], Video)
                if videoPath is not None:
                    print(f'Video Download Success, path: {videoPath}')
            try:
                ArticleInfo['spider_keyword'] = keyword
                ArticleInfo['server_name'] = config.server_name
                ArticleInfo['clean_text'] = CleanData(ArticleInfo['text'])
            except Exception as e:
                logutils.error(e)
            if outType == 'datebase':
                database(UserInfo, ArticleInfo, Images, Video)
            else:
                cli(UserInfo, ArticleInfo, Images, Video)
            # Query whether there is article data in the database   查询数据库中是否有文章数据


def database(userInfo, articleInfo, imagesInfo, videoInfo):
    session = Mysql()
    if session.query(Article).filter(Article.id == articleInfo['id']).first() is None:
        # Construct article orm object - Article    构造文章ORM对象
        article = DictConvertORM(articleInfo, table="article")
        try:
            # Query whether there is user data in the database  查询数据库中是否有用户数据
            user = session.query(User).filter(User.id == userInfo['id']).first()
            if user is None:
                # Construct user ORM object 构造用户ORM对象
                user = DictConvertORM(userInfo, table='user')
                session.add(user)
            session.add(article)
            # Judge whether there are pictures  判断是否有图片
        except Exception as e:
            logutils.error(e)
    session.commit()
    session.close()


def cli(userInfo, articleInfo, imagesInfo, videoInfo):
    print(f"""
    userInfo:
    {userInfo}
    articleInfo:
    {articleInfo}
    imagesInfo:
    {imagesInfo}
    videoInfo:
    {videoInfo}
    """)
    # a = input('Press any key to go to the next one')


if __name__ == '__main__':
    main()
