# -*- coding:utf-8 -*-
import os

from app import basedir


class StaticResource(object):
    results = {}

    def on_get(self, req, resp, path):
        static_path = os.path.join(basedir, 'static')

        static_file = os.path.join(static_path, path)
        static_file = open(static_file, 'rb')

        resp.stream = static_file
        resp.content_type = path.split('.')[-1]

        return resp