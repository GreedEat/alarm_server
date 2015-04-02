# -*- coding:utf-8 -*-
import json
import os
basedir = os.path.abspath(os.path.dirname(__file__))

import falcon


class VersionCheckResource(object):
    results = {}

    def on_get(self, req, resp, os_name):
        if os_name in ('Android', 'ios'):
            filename = '%s.txt' % os_name
            file_path = \
                os.path.join(basedir, '..', 'utils', 'versions', filename)
            version = open(file_path, 'r').read()
        else:
            resp.status = falcon.HTTP_400
            return ''

        self.results['version'] = version
        resp.body = json.dumps(self.results)
        return ''