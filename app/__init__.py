# -*-coding:utf-8-*-
import falcon

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://subway:asdqwe123@127.0.0.1/subway',
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         expire_on_commit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def create_api():
    api = falcon.API()
    add_routes(api)

    return api


def add_routes(api):
    from resource.version_check import VersionCheckResource
    version_check = VersionCheckResource()
    api.add_route('/version/{os_name}', version_check)

    from resource.notification import (NotificationsResource,
                                       NotificationResource)
    notifications = NotificationsResource()
    notification = NotificationResource()
    api.add_route('/notifications', notifications)
    api.add_route('/notification/{id}', notification)

    return ''