# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class PrivacyResource(object):
    results = {}

    def on_get(self, req, resp):
        filename = 'privacy.txt'
        privacy_path = os.path.join(basedir, '..', 'utils', 'privacy')

        privacy = os.path.join(privacy_path, filename)
        privacy = open(privacy, 'r').read()

        resp.body = privacy

        return resp