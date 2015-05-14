# -*-coding:utf-8-*-
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

    return ''