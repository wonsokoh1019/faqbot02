# !/bin/env python
# -*- coding: utf-8 -*-
"""
deal user input messages
"""

__all__ = ['deal_message']

import tornado.web
import tornado.gen
from tornado.web import HTTPError
from faq_bot.model.data import make_text
from faq_bot.actions.message import echo_display
from faq_bot.externals.send_message import push_message
from faq_bot.model.cachehandle import set_user_status, get_user_status


@tornado.gen.coroutine
def deal_message(account_id, __, message):
    """
    Process messages manually entered by the user.

    :param account_id: user account id.
    :param message: user input message.
    """
    status, _, __, ___  = get_user_status(account_id)
    if status != "wait_in":
        raise HTTPError(403, "Messages not need to be processed")

    content = echo_display(message)
    set_user_status(account_id, status="done", message=message)

    yield push_message(account_id, content)