# !/bin/env python
# -*- coding: utf-8 -*-
"""
Handle user's transfer from query business to ask a person
"""

__all__ = ['transfer_message']

import tornado.web
import tornado.gen
import asyncio
from tornado.web import HTTPError
from faq_bot.model.data import make_text
from faq_bot.constant import TYPES
from faq_bot.externals.send_message import push_messages
from faq_bot.model.cachehandle import set_replace_user_info

@tornado.gen.coroutine
def transfer_message(account_id, callback, __):
    """
    This function prompts the user to go to ask someone.

    :param account_id: user account id.
    :param callback: Business type.
    """
    content1 = make_text("Your question will be directly delivered to "
                         "the person in charge of {type} "
                         "to answer your question directly.".format(
        type=TYPES[callback]))

    content2 = make_text("Please tell me your question.\n"
                         "Only one message can be delivered. "
                         "Please write your question at one go.")

    yield  asyncio.sleep(0.5)
    set_replace_user_info(account_id, 'wait_in', 'doing', TYPES[callback])

    yield push_messages(account_id, [content1, content2])