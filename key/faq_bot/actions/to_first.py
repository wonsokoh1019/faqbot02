# !/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import logging
from faq_bot.model.data import make_text
from faq_bot.externals.send_message import push_message


@tornado.gen.coroutine
def to_first(account_id, __, ___):
    process_flag = False
    if process_flag:
        content = make_text("Cannot be selected since you are currently "
                            "in Initial Menu. \n\n"
                            "Select it if you want to find FAQ or go back to "
                            "Initial Menu while the person in charge is "
                            "checking your question.")
    else:
        content = make_text("Moved to FAQ Initial Menu.")

    yield push_message(account_id, content)