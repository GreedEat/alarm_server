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
        version_path = os.path.join(basedir, '..', 'utils', 'versions')

        version_name = os.path.join(version_path, 'name', filename)
        version_code = os.path.join(version_path, 'code', filename)

        version_name = open(version_name, 'r').read()
        version_code = open(version_code, 'r').read()

        self.results['version'] = {
            'name': version_name,
            'code': version_code
        }
        resp.body = json.dumps(self.results, indent=4)
        return resp