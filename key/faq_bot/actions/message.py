# !/bin/env python
# -*- coding: utf-8 -*-
"""
common message
"""

__all__ = ['create_quick_replay_item', 'create_carousel',
           'create_quick_replay', 'echo_display']

from faq_bot.model.data import make_postback_action, make_quick_reply_item, \
    make_url_action, make_carousel_column, make_carousel, make_quick_reply, \
    make_text


def invalid_message():
    return make_text("I’m sorry. I couldn't understand the words. \n\n"
                     "Please select the function you want "
                     "from Bot Menu at the bottom of the chat window.")


def create_board_failed():
    return make_text("Failed to create bulletin board. \n\n"
                     "Ask the FAQ Bot manager to check if the bulletin board "
                     "creation item has been set incorrectly or "
                     "if the bulletin board title or description "
                     "has exceeded the character limit.")

def create_articles_failed():
    return make_text("Failed to complete posting. \n\n"
                     "Ask the FAQ Bot manager to check if the bulletin board "
                     "number does not exist or if other "
                     "items are set up incorrectly.")

def storage_lack():
    return make_text("Failed to complete posting. \n\n"
                     "Ask the in-house manager if the public capacity is "
                     "not enough or if the capacity available for "
                     "domain use has been exceeded.")

def create_quick_replay():
    """
    Building a quick reply floating window for messages.

        reference
        - `Common Message Property <https://developers.worksmobile.com/jp/document/100500807?lang=en>`_

    Check also: faq_bot/model/data.py
    :return: quick replay item
    """

    action0 = make_postback_action("enquire_leave", "HR/Leave", "HR/Leave")

    item0 = make_quick_reply_item(action0)

    action1 = make_postback_action("enquire_welfare", "Welfare/Work support",
                                   "Welfare/Work support")
    item1 = make_quick_reply_item(action1)

    action2 = make_postback_action("enquire_security", "Security", "Security")
    item2 = make_quick_reply_item(action2)

    return make_quick_reply([item0, item1, item2])


def echo_display(message):
    """
    Generate messages that require user confirmation.

        reference
        - `Common Message Property <https://developers.worksmobile.com/jp/document/100500807?lang=en>`_

    Check also: faq_bot/model/data.py
    :param message: User input message.
    :return: Message to prompt users.
    """
    text = "Do you want to send the following as your question? \n\n" \
           "===\n{message}\n===".format(message=message)
    content = make_text(text)

    action0 = make_postback_action("send", label="Send", display_text="Send")
    item0 = make_quick_reply_item(action0)

    action1 = make_postback_action("modify", label="Modify",
                                   display_text="Modify")
    item1 = make_quick_reply_item(action1)

    action2 = make_postback_action("cancel", label="Cancel",
                                   display_text="Cancel")
    item2 = make_quick_reply_item(action2)

    quick_reply = make_quick_reply([item0, item1, item2])

    content["quickReply"] = quick_reply

    return content


def create_quick_replay_item(callback, label, text=None):
    """
    Building a quick reply floating window for messages.
    Check also: faq_bot/model/data.py

        reference
        - `Common Message Property <https://developers.worksmobile.com/jp/document/100500807?lang=en>`_

    :param callback: callback string for the button.
    :return: quick replay item
    """

    if text is None:
        text = label

    action = make_postback_action(callback, label=label, display_text=text)

    item = make_quick_reply_item(action)
    return make_quick_reply([item])


def create_carousel(labels, urls, texts, image_urls, titles):
    """
    Building a quick reply floating window for messages.
    Check also: faq_bot/model/data.py

        reference
        - `Common Message Property <https://developers.worksmobile.com/jp/document/100500807?lang=en>`_

    :return: return carousel content
    """
    action0 = make_url_action(labels[0], urls[0])
    column0 = make_carousel_column(texts[0], [action0], title=titles[0],
                                    image_url=image_urls[0],
                                    default_action=action0)

    action1 = make_url_action(labels[1], urls[1])
    column1 = make_carousel_column(texts[1], [action1], title=titles[1],
                                    image_url=image_urls[1],
                                    default_action=action1)

    action2 = make_url_action(labels[2], urls[2])
    column2 = make_carousel_column(texts[2], [action2], title=titles[2],
                                    image_url=image_urls[2],
                                    default_action=action2)

    action3 = make_url_action(labels[3], urls[3])
    column3 = make_carousel_column(texts[3], [action3], title=titles[3],
                                    image_url=image_urls[3],
                                    default_action=action3)

    return make_carousel([column0, column1, column2, column3])