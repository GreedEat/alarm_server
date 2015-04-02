# -*-coding:utf-8-*-
from app import create_api, Base, engine

from wsgiref import simple_server


api = create_api()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()