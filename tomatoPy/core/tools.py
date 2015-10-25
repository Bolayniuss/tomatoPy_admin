# -*- coding: utf-8 -*-
# tomatoPy_admin

__author__ = 'Michael Bolay'

import random


def random_hash_string(length):
    return "%32x" % random.getrandbits(length)