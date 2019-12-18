#!/bin/env python
# -*- coding: utf-8 -*-
"""
Process requests of users
"""

__all__ = ['CallbackHandler', 'post']

import json
import logging
import tornado.gen
import tornado.web
from faq_bot.check_and_handle_actions import CheckAndHandleActions


class CallbackHandler(tornado.web.RequestHandler):
    """
    Process business requests of users.

    tornado.web.RequestHandler base class for HTTP request handlers.

        reference
        - `Common Message Property <https://www.tornadoweb.org/en/stable/web.html>`_
    """

    @tornado.gen.coroutine
    def post(self):
        """
        Implement the handle to corresponding HTTP method.
        Check also: faq_bot/router.py
        """

        logging.info("request para path:%s", self.request.uri)
        try:
            body = json.loads(self.request.body)
        except json.JSONDecodeError:
            logging.exception('Failed parse json:%s' % self.request.body)
            raise tornado.web.HTTPError(403, "boy is not json.")

        logging.info("request para body:%s", self.request.body)
        checker = CheckAndHandleActions()
        yield checker.execute(body)

        self.finish()
