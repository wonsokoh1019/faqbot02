# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deals with user query security related problems.
"""

__all__ = ['query_security']

import tornado.gen
import tornado.web
import logging
from conf.resource import CAROUSEL, POST_BACK_URLS
from faq_bot.model.data import make_text
from faq_bot.actions.message import create_quick_replay_item, create_carousel
from faq_bot.externals.send_message import push_messages


@tornado.gen.coroutine
def query_security(account_id, __, ___):
    """
    This function deals with user query security related problems.

    :param account_id: user account id.
    """
    text = make_text("Here are FAQs about security.")

    replay = create_quick_replay_item("transfer_security",
                                      "Ask a charge")

    labels = ["more", "more", "more", "more"]

    """
    replay = create_quick_replay_item("transfer_security",
                                      "Ask a person in charge")
    labels = ["See more", "See more", "See more", "See more"]
    titles = [
        "I lost my access card.",
        "My access card has been damaged.",
        "Can visitors enter the office?",
        "I don’t remember my computer password."
    ]
    """
    titles = [
        "I lost my access card.",
        "My access card damaged.",
        "Can visitors office?",
        "I don’t remember password."
    ]
    """
    texts = [
        "Contact the Security Team. They will reissue your access card.",
        "Contact the Security Team. They will reissue your access card.",
        "Contact the Security Team "
        "in advance to allow visitors to enter the office.",
        "Contact the Security Team. "
        "They will help you change your computer password."
    ]
    """
    texts = [
        "Contact the your access card.",
        "Contact the your access card.",
        "Contact the to enter the office.",
        "Contact the your computer password."
    ]

    carousel = create_carousel(labels, POST_BACK_URLS["security"],
                    texts, CAROUSEL["security"], titles)

    carousel["quickReply"] = replay

    yield push_messages(account_id, [text, carousel])