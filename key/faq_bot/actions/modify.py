# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deal with users' modification of questions
"""

__all__ = ['modify']

import tornado.web
import tornado.gen
import asyncio
from faq_bot.model.data import make_text
from faq_bot.externals.send_message import push_message
from faq_bot.model.cachehandle import set_user_status, get_user_status


@tornado.gen.coroutine
def modify(account_id, __, ___):
    """
    This function handles the user's modification of the question

    :param account_id: user account id.
    """
    status, _, __, ____ = get_user_status(account_id)
    if status != "done":
        raise HTTPError(500, "user status error. status error")

    content = make_text("I’ll help you modify your question. "
                        "Please write your question again.")

    yield asyncio.sleep(0.5)

    set_user_status(account_id, status='wait_in')

    yield push_message(account_id, content)