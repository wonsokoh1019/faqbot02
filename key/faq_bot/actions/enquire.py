# !/bin/env python
# -*- coding: utf-8 -*-
"""
Handle user selection ask a person
"""

__all__ = ['enquire']

import tornado.web
import tornado.gen
from faq_bot.model.data import make_text
from faq_bot.actions.message import create_quick_replay
from faq_bot.externals.send_message import push_message


@tornado.gen.coroutine
def enquire(account_id, __, ___):
    """
    This function handles the user's selection of ask a person

    :param account_id: user account id.
    """
    content = make_text("Select a task related to your question.")

    content["quickReply"] = create_quick_replay()

    yield push_message(account_id, content)
