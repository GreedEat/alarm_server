# -*- coding:utf-8 -*-
import json
import os
basedir = os.path.abspath(os.path.dirname(__file__))

import falcon


class VersionCheckResource(object):
    results = {}

    def on_get(self, req, resp, os_name):
        if os_name not in ('Android', 'ios'):
            resp.status = falcon.HTTP_400
            return resp

        filename = '%s.txt' % os_name
        file_path = \
            os.path.join(basedir, '..', 'utils', 'versions', filename)
        version = open(file_path, 'r').read()

        self.results['version'] = version
        resp.body = json.dumps(self.results, indent=4)
        return resp