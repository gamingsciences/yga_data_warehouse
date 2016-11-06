# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 15:48:10 2016

@author: Lathropk
"""
from django.conf import settings
from sqlalchemy import MetaData, select


oasis_engine = settings.OASIS_ENGINE
metadata = MetaData(oasis_engine)
metadata.reflect(only=['CDS_SlotMast',
                       ])
connection = oasis_engine.connect()

SlotMast = metadata.tables['CDS_SlotMast']



def location_info():

    s = select([SlotMast.c.LocationString.label('location'),
                SlotMast.c.CasinoCode.label('casino'),
                SlotMast.c.Area.label('area'),
                SlotMast.c.Section.label('section'),
                SlotMast.c.Loc.label('position'),
                ])
                 
    s = s.select_from(SlotMast)             
    s = s.distinct(SlotMast.c.CasinoCode, SlotMast.c.Area, SlotMast.c.Section,
                   SlotMast.c.Loc)
                     
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    
    return resultset
