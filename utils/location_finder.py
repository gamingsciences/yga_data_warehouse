# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 10:54:32 2016

@author: Lathropk
"""

from conformed_dimensions.models import LocationDimension

def get_location(rec):
    # get the location object form the conformed_dim Location model
        try:
            casino_str = str.strip(rec['CasinoCode'])
        except:
            casino_str = ''
        try:
            area_str = str.strip(rec['Area'])
        except:
            area_str = ''
        try:
            section_str = str.strip(rec['Section'])
        except:
            section_str = ''
        try:
            position_str = str.strip(rec['Loc'])
        except:
            position_str = ''
        
        if casino_str == '10':
            casino_name = 'YC'
        else:
            casino_name = 'Buckys'
            
        location, created = LocationDimension.objects.get_or_create(casino=casino_name,
                                                                    area=area_str,
                                                                    section=section_str,
                                                                    position=position_str)
        return location
