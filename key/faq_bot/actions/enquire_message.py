# !/bin/env python
# -*- coding: utf-8 -*-
"""
Prompt user for enquire message
"""

__all__ = ['enquire_message']

import tornado.web
import tornado.gen
import asyncio
from faq_bot.model.data import make_text
from faq_bot.constant import TYPES
from faq_bot.model.cachehandle import set_replace_user_info
from faq_bot.externals.send_message import push_messages

@tornado.gen.coroutine
def enquire_message(account_id, callback, __):
    """
    This function prompts the user for a message.

    :param account_id: user account id.
    :param callback: Callback corresponding to business type.
    """
    content1 = make_text("You have selected {type}. "
                         "Please tell me your question.".format(
        type=TYPES[callback]))

    content2 = make_text("Only one message can be delivered. "
                         "Please write your question at one go.")

    yield asyncio.sleep(0.5)

    set_replace_user_info(account_id, 'wait_in', 'doing', TYPES[callback])

    yield push_messages(account_id, [content1, content2])

