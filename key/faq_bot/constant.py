#!/bin/bash python3
# -*- coding: UTF-8 -*-
"""
constants.py Defining the constant used for a project.
"""

import os
from conf.config import *
# ---------------------------------------------------------------------
# Constants and global variables
# ---------------------------------------------------------------------

# ROOT PATH
ABSDIR_OF_SELF = os.path.dirname(os.path.abspath(__file__))
ABSDIR_OF_PARENT = os.path.dirname(ABSDIR_OF_SELF)

HEROKU_SERVER_ID = SERVER_ID
PRIVATE_KEY_PATH = ABSDIR_OF_PARENT + "/key/" + SECRET_KEY_NAME

# DOMAIN
STORAGE_DOMAIN = "storage.worksmobile.com"
AUTH_DOMAIN = "auth.worksmobile.com"
DEVELOP_API_DOMAIN = "apis.worksmobile.com"

CALLBACK_ADDRESS = LOCAL_ADDRESS + "callback"
PHOTO_URL = LOCAL_ADDRESS + "static/icon.png"
BOT_NAME = "In-house FAQ Bot"

# Internal business mapping
TYPES = {
    'leave': 'HR/Leave',
    'welfare': 'Welfare/Work support',
    'security': 'Security'
}

# API ADDRESS
API_BO = {
    "headers": {
        "content-type": "application/json",
        "charset": "UTF-8"
    },

    "upload_url": "http://" + STORAGE_DOMAIN + "/openapi/message/upload.api",
    "push_url": "https://" + DEVELOP_API_DOMAIN + "/r/"
                + API_ID + "/message/v1/bot/_BOT_NO_/message/push",
    "rich_menu_url": "https://" + DEVELOP_API_DOMAIN + "/r/"
                     + API_ID + "/message/v1/bot/_BOT_NO_/richmenu",

    "home": {
        "board_title": "boards for faq",
        "board_description": "boards for faq",
        "boards_url": "https://" + DEVELOP_API_DOMAIN + "/r/"
                      + API_ID + "/home/v1/boards",

        "create_articles_url": "https://" + DEVELOP_API_DOMAIN + "/r/"
                               + API_ID + "/home/v1/articles",
    },

    "bot": "https://" + DEVELOP_API_DOMAIN + "/r/" + API_ID + "/message/v1/bot",

    "contacts_url": "https://" + DEVELOP_API_DOMAIN + "/"
                    + API_ID + "/contact/getDomainContact/v1",

    "auth_url": "https://" + AUTH_DOMAIN + "/b/"
                + API_ID + "/server/token?grant_type=urn%3Aietf%3Aparams%3Ao"
                           "auth%3Agrant-type%3Ajwt-bearer&assertion="
}

# OPEN API
OPEN_API = {
    "_info": "nwetest.com",
    "apiId": API_ID,
    "consumerKey": SERVER_CONSUMER_KEY
}

# DB CONFIG
DB_CONFIG = {
    "host": DB_HOST,
    "port": DB_PORT,
    "dbname": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "sslmode": "prefer"
}

# FILE SYSTEM
FILE_SYSTEM = {
    "image_dir": ABSDIR_OF_PARENT+"/image",
}
