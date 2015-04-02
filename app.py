# -*- coding:utf-8 -*-
import json
import os
basedir = os.path.abspath(os.path.dirname(__file__))

import falcon
from wsgiref import simple_server


class VersionCheckResource(object):
    results = {}

    def on_get(self, req, resp, os_name):
        if os_name in ('Android', 'ios'):
            filename = '%s.txt' % os_name
            file_path = os.path.join(basedir, filename)
            version = open(file_path, 'r').read()
        else:
            resp.status = falcon.HTTP_400
            return ''

        self.results['version'] = version
        resp.body = json.dumps(self.results)
        return ''


app = falcon.API()
version_check = VersionCheckResource()
app.add_route('/version/{os_name}', version_check)


if __name__ == "__main__":
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()