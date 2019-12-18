# !/bin/env python
# -*- coding: utf-8 -*-


import tornado.gen
from conf.resource import CAROUSEL
from faq_bot.model.data import make_text, make_message_action, \
    make_list_template_element, make_list_template
from faq_bot.externals.send_message import push_messages


def image_introduce():
    """
    This function constructs three image carousels for self introduction.
    Check also: faq_bot/model/data.py

        reference
        - `Common Message Property <https://developers.worksmobile.com/kr/document/100500805?lang=en>`_

    :return: image carousels type message content.
    """

    action0 = make_message_action("See FAQs", "query_leave", "See FAQs")
    action1 = make_message_action("See FAQs", "query_welfare", "See FAQs")
    action2 = make_message_action("See FAQs", "query_security", "See FAQs")

    element0 = make_list_template_element("HR/Leave",
                                          "See FAQs about HR and leave.",
                                          action=action0)
    element1 = make_list_template_element("Welfare/Work support",
                                          "See FAQs about welfare "
                                          "and work support.",
                                          action=action1)
    element2 = make_list_template_element("Security", "See FAQs about security.",
                                          action=action2)

    return make_list_template([element0, element1, element2])

@tornado.gen.coroutine
def query(account_id, __, ___):
    # todo
    # 此处查询用户的咨询状态，如果用户在

    content1 = make_text("Please select an work-related item "
                         "that you would like to know.")

    content2 = image_introduce()

    yield push_messages(account_id, [content1, content2])