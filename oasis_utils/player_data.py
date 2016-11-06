# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:58:42 2016

@author: lathropk
"""
from django.conf import settings
from sqlalchemy import MetaData, select, cast, Date


oasis_engine = settings.OASIS_ENGINE
metadata = MetaData(oasis_engine)
metadata.reflect(only=['CDS_Player', 'PlayerAddress'])
connection = oasis_engine.connect()

Player = metadata.tables['CDS_Player']
Address = metadata.tables['PlayerAddress']

def player_update(audit_date):
    #audit_date = parse(_audit_date)
    
    s = select([Player.c.Player_ID.label('player_id'),
                Player.c.Timestamp.label('player_timestamp'),
                Player.c.EntryDate.label('date_joined'),
                Player.c.LastName.label('last_name'),
                Player.c.FirstName.label('first_name'),
                Player.c.Birthday.label('birth_date'),
                Player.c.Gender.label('gender'),
                Player.c.EMail.label('email'),
                Address.c.Address1A.label('address_a'),
                Address.c.Address1B.label('address_b'),
                Address.c.City1.label('city'),
                Address.c.State1.label('state'),
                Address.c.Zip1.label('zip_code'),
                Address.c.Country1_ID.label('country'),
                Address.c.HomePhone1.label('phone'),
                Player.c.CallFlag.label('call_flag'),
                Player.c.MailFlag.label('mail_flag'),
                ])
    
    s = s.select_from(Player.join(Address, 
                          Player.c.Player_ID == Address.c.Player_ID))
    
    s = s.where(cast(Player.c.Timestamp, Date) == audit_date)
        
    rp = connection.execute(s)
    
    resultset = [dict(row) for row in rp]
    
    return resultset
    
def player_load():
    
    s = select([Player.c.Player_ID.label('player_id'),
                Player.c.EntryDate.label('date_joined'),
                Player.c.LastName.label('last_name'),
                Player.c.FirstName.label('first_name'),
                Player.c.Birthday.label('birth_date'),
                Player.c.Gender.label('gender'),
                Player.c.EMail.label('email'),
                Address.c.Address1A.label('address_a'),
                Address.c.Address1B.label('address_b'),
                Address.c.City1.label('city'),
                Address.c.State1.label('state'),
                Address.c.Zip1.label('zip_code'),
                Address.c.Country1_ID.label('country'),
                Address.c.HomePhone1.label('phone'),
                Player.c.CallFlag.label('call_flag'),
                Player.c.MailFlag.label('mail_flag'),
                ])
    
    s = s.select_from(Player.join(Address, 
                          Player.c.Player_ID == Address.c.Player_ID))
    
        
    rp = connection.execute(s)
    
    resultset = [dict(row) for row in rp]
    
    return resultset

def get_player(player_id):
    
    s = select([Player.c.Player_ID.label('player_id'),
                Player.c.Timestamp.label('player_timestamp'),
                Player.c.EntryDate.label('date_joined'),
                Player.c.LastName.label('last_name'),
                Player.c.FirstName.label('first_name'),
                Player.c.Birthday.label('birth_date'),
                Player.c.Gender.label('gender'),
                Player.c.EMail.label('email'),
                Address.c.Address1A.label('address_a'),
                Address.c.Address1B.label('address_b'),
                Address.c.City1.label('city'),
                Address.c.State1.label('state'),
                Address.c.Zip1.label('zip_code'),
                Address.c.Country1_ID.label('country'),
                Address.c.HomePhone1.label('phone'),
                Player.c.CallFlag.label('call_flag'),
                Player.c.MailFlag.label('mail_flag'),
                ])
    
    s = s.select_from(Player.join(Address, 
                          Player.c.Player_ID == Address.c.Player_ID))
    
    s = s.where(Player.c.Player_ID == player_id)
        
    rp = connection.execute(s)
    
    resultset = [dict(row) for row in rp]
    
    return resultset
