import sys
reload(sys)
sys.setdefaultencoding = 'utf-8'

from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.sql import functions

from .. import Base
from app.utils.serializer import AutoSerialize


class Notification(Base, AutoSerialize):
    __tablename__ = 'notification'
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    title = Column(String)
    contents = Column(String)

    created_at = Column(DateTime(timezone=True), default=functions.now())
    updated_at = Column(DateTime(timezone=True), default=functions.now())