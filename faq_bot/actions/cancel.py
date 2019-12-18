# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deal cancel ask a person
"""

__all__ = ['cancel']

import tornado.web
import tornado.gen
from faq_bot.model.data import make_text
from faq_bot.externals.send_message import push_message
from faq_bot.model.cachehandle import get_user_status, clean_user_status


@tornado.gen.coroutine
def cancel(account_id, __, ___):
    """
    This function handles user cancellation inquiry.

    :param account_id: user account id.
    """
    status, _, __, ___ = get_user_status(account_id)
    if status != "done":
        # todo add error prompt
        raise HTTPError(500, "user status error. status error")

    content = make_text("You have canceled your question. "
                        "Please re-select the task from the menu below.")
    clean_user_status(account_id)
    yield push_message(account_id, content)