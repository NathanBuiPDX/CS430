# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ quote, name, type, date, source, rating ]
    where quote, name, type,  and source Python strings, rating is the integer
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['quote'], entity['name'],entity['date'].strftime("%Y-%m-%d %H:%M"), entity['type'], entity['source'], entity['rating']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-bui-nbui')

    def select(self):
        query = self.client.query(kind = 'Quote')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,quote, name, quoteType, source, rating):
        key = self.client.key('Quote')
        rev = datastore.Entity(key)
        rev.update( {
            'quote': quote,
            'name': name,
            'type' : quoteType,
            'date' : datetime.today(),
            'source' : source,
            'rating': rating
            })
        self.client.put(rev)
        return True
