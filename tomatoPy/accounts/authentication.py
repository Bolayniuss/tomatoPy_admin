# -*- coding: utf-8 -*-
# tomatoPy_admin

__author__ = 'Michael Bolay'

from rest_framework.authentication import TokenAuthentication

from accounts.models import ClientToken


class ClientTokenAuthentication(TokenAuthentication):
    model = ClientToken