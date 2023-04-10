#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6220053152:AAGnUqi9oQscdpEj2Wiby19lwE02kIh0nM0")
    API_ID = int(os.environ.get("API_ID", "29410389"))
    API_HASH = os.environ.get("API_HASH", "0c716764715886f6641477ffbb63e1ee")
    AUTH_USERS = "6253923773"

