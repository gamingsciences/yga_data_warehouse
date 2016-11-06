# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:27:59 2016

@author: Lathropk
"""

import simplejson as json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
