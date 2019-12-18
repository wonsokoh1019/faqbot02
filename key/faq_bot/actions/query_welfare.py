# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deals with user query welfare related problems
"""

__all__ = ['query_welfare']

import tornado.gen
import tornado.web
import logging
from conf.resource import CAROUSEL, POST_BACK_URLS
from faq_bot.model.data import make_text
from faq_bot.actions.message import create_quick_replay_item, create_carousel
from faq_bot.externals.send_message import push_messages


@tornado.gen.coroutine
def query_welfare(account_id, __, ___):
    """
    This function deals with user query welfare related problems.

    :param account_id: user account id.
    """
    text = make_text("Here are FAQs about welfare and work support.")

    replay = create_quick_replay_item("transfer_welfare",
                                      "Ask a charge")
    labels = ["more", "more", "more", "more"]
    """
    labels = ["See more", "See more", "See more", "See more"]
    replay = create_quick_replay_item("transfer_welfare",
                                      "Ask a person in charge")
    titles = [
        "I would like to know the types of in-house welfare.",
        "What kinds of in-house clubs are there?",
        "Can I use a company car?",
        "How can I receive office supplies?"
    ]
    """

    titles = [
        "I would welfare.",
        "What clubs are there?",
        "Can I company car?",
        "How can office supplies?"
    ]

    """
    texts = [
        "In-house welfare includes the four main insurances, "
        "medical checkup, in-house clubs, etc.",
        "The company is supporting a variety of club activities "
        "such as sports, self-development, etc.",
        "Contact the Work Support Team to request a company car.",
        "Visit the Work Support Team to receive office supplies."
    ]
    """
    texts = [
        "In-house welfare in-house clubs, etc.",
        "The company is self-development, etc.",
        "Contact the to request a company car.",
        "Visit the  to receive office supplies."
    ]

    carousel = create_carousel(labels, POST_BACK_URLS["welfare"],
                    texts, CAROUSEL["welfare"], titles)

    carousel["quickReply"] = replay

    yield push_messages(account_id, [text, carousel])