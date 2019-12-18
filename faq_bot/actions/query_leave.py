# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deal with issues related to leave query
"""

__all__ = ['query_leave']

import tornado.gen
import tornado.web
import logging
from conf.resource import CAROUSEL, POST_BACK_URLS
from faq_bot.model.data import make_text
from faq_bot.actions.message import create_quick_replay_item, create_carousel
from faq_bot.externals.send_message import push_messages


@tornado.gen.coroutine
def query_leave(account_id, __, ___):
    """
    This function deals with the problems related to leave query.

    :param account_id: user account id.
    """
    text = make_text("Here are FAQs about HR and leave.")

    replay = create_quick_replay_item("transfer_leave",
                                      "Ask a charge")

    labels = ["more", "more", "more", "more"]

    """
    replay = create_quick_replay_item("transfer_leave",
                                      "Ask a person in charge")
    labels = ["See more", "See more", "See more", "See more"]
    titles = [
        "I would like to know the types of leave.",
        "I would like to know how many days of leave I have.",
        "I would like to request a leave.",
        "I would like to cancel my leave request."
    ]
    """
    titles = [
        "I would  of leave.",
        "I would leave I have.",
        "I would a leave.",
        "I would leave request."
    ]
    """
    texts = [
        "Leave including annual leave, paid leave, etc. "
        "is granted according to the Labor Standards Act.",
        "You can check the remaining days of your leave via "
        "the in-house browser.",
        "You can request a leave via the in-house browser.",
        "You can cancel your leave request via the in-house browser."
    ]
    """
    texts = [
        "Leave including to the Labor Standards Act.",
        "You can check the remain browser.",
        "You can request a leave via the in-house browser.",
        "You can cancel your leave in-house browser."
    ]

    carousel = create_carousel(labels, POST_BACK_URLS["leave"],
                    texts, CAROUSEL["leave"], titles)

    carousel["quickReply"] = replay

    yield push_messages(account_id, [text, carousel])

