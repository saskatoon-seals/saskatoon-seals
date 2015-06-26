import datetime
from google.appengine.ext import ndb
import hashlib


class PlayerModel(ndb.Model):
    email = ndb.StringProperty()
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    birth_country = ndb.StringProperty()
    birth_city = ndb.StringProperty()
    importance = ndb.IntegerProperty(default=0)
    bio = ndb.BlobKeyProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def build_key(cls, first_name=None, last_name=None, email=None):
        if email:
            key = email
        elif first_name and last_name:
            key = first_name + '-' + last_name
        else:
            raise ValueError
        return ndb.Key(cls, hashlib.md5(key).hexdigest())

    @classmethod
    def create(cls, **kwargs):
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        email = kwargs.get('email')
        key = cls.build_key(first_name, last_name, email)
        entity = cls(key=key, **kwargs)
        return entity.put()

    @classmethod
    def get_all_players(cls):
        return cls.query().order(cls.importance, cls.first_name).fetch()

    @classmethod
    def delete_all_players(cls):
        ndb.delete_multi(cls.query().fetch(keys_only=True))

    def to_dict(self, to_json_str=False):
        return self._to_dict(self, to_json_str=to_json_str)

    @classmethod
    def _to_dict(cls, player, to_json_str=False):
        DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
        base_d = {}
        for key, value in player._values.iteritems():
            if value is not None and to_json_str:
                if type(value.b_val) is datetime.datetime:
                    base_d[key] = value.b_val.strftime(DATETIME_FORMAT)
                else:
                    base_d[key] = value.b_val
        return base_d