# -*-coding:utf-8-*-
import sys

from app import create_api

from wsgiref import simple_server


api = create_api()


def manage_script(argv):
    args = argv[1:] if len(argv) > 1 else None
    if not args:
        sys.exit()
    elif args[0] == 'runserver':
        from datetime import datetime
        print '** Falcon Works {0} **'.format(str(datetime.now())[:19])
        httpd = simple_server.make_server('0.0.0.0', 8000, api)
        httpd.serve_forever()


if __name__ == "__main__":
    manage_script(sys.argv)