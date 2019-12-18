# !/bin/env python
# -*- coding: utf-8 -*-
"""
Start using robots
"""

__all__ = ['register_rich_menun', 'start_content', 'start']

import tornado.web
import tornado.gen
import logging
from faq_bot.model.data import  make_text
from faq_bot.externals.send_message import push_messages
from faq_bot.common.global_data import get_value
from faq_bot.externals.richmenu import set_user_specific_rich_menu


@tornado.gen.coroutine
def register_rich_menun(account_id):
    """
    Set up rich menu for chat with users.
    Check also: faq_bot/model/data.py

        reference
        - `Common Message Property <https://developers.worksmobile.com/jp/document/1005040?lang=en>`_

    :param account_id: user account id
    """
    if account_id is None:
        logging.error("account_id is None.")
        return False
    rich_menu_id = get_value("rich_menu", None)
    if rich_menu_id is None:
        logging.error("get rich_menu_id failed.")
        raise Exception("get rich_menu_id failed.")

    return set_user_specific_rich_menu(rich_menu_id, account_id)


@tornado.gen.coroutine
def start_content(account_id):
    yield register_rich_menun(account_id)

    content1 = make_text("Hello. I’m FAQ Bot. "
                         "I’m here to answer your office-related questions.")

    content2 = make_text("Please select an item from the menu below.")

    return [content1, content2]


@tornado.gen.coroutine
def start(account_id, _, __):
    """
    Handle the user start using robots.
    Send the robot's self introduction information,
    and the chat room is bound with rich menu.

    :param account_id: user account id.
    """
    contents = yield start_content(account_id)

    yield push_messages(account_id, contents)
