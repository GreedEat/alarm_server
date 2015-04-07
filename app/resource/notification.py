# -*- coding:utf-8 -*-
import json

import falcon

from .. import db_session as db
from ..model.notification import Notification


class NotificationsResource(object):
    results = {}
    data = {}

    def on_get(self, req, resp):
        self.results['notifications'] = []
        self.data['filters'] = ['id', 'created_at']
        raw_filters = req.get_param('filters')
        if raw_filters:
            self.data['filters'] += raw_filters.split(',')

        notifications = db.query(Notification).all()
        for notification in notifications:
            self.results['notifications']\
                .append(notification.get_public(extra=self.data['filters']))
        resp.body = json.dumps(self.results, indent=4)

        return resp


class NotificationResource(object):
    results = {}

    def on_get(self, req, resp, id):
        if not id:
            resp.status = falcon.HTTP_400
            return resp

        notification = Notification.query.get(id)
        if not notification:
            resp.status = falcon.HTTP_404
            return resp

        self.results['notification'] = notification.get_public()

        resp.body = json.dumps(self.results, indent=4)

        return resp