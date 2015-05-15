# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

import falcon


def create_api():
    api = falcon.API()
    add_routes(api)

    return api


def add_routes(api):
    from resource.version_check import VersionCheckResource
    version_check = VersionCheckResource()
    api.add_route('/version/{os_name}', version_check)

    from resource.privacy import PrivacyResource
    privacy = PrivacyResource()
    api.add_route('/privacy', privacy)

    from resource import StaticResource
    static = StaticResource()
    api.add_route('/static/{path}', static)

    return ''