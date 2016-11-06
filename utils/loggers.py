# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 10:46:01 2016

@author: Lathropk
"""
import os
import datetime
import logging
from django.conf import settings


class ExtractLogger:
    logger = None
    def myLogger(self):
        if None == self.logger:
            self.logger=logging.getLogger('OasisExtract')
            self.logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            log_file = os.path.join(settings.PROJECT_DIR, 
                                    'logs\oasis_extract_'+ now.strftime("%Y-%m-%d") +'.log')
            handler=logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        return self.logger


class TransformLogger:
    logger = None
    def myLogger(self):
        if None == self.logger:
            self.logger=logging.getLogger('OasisTransform')
            self.logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            log_file = os.path.join(settings.PROJECT_DIR, 
                                    'logs\oasis_transform_'+ now.strftime("%Y-%m-%d") +'.log')
            handler=logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        return self.logger


class UpdateDimLogger:
    logger = None
    def myLogger(self):
        if None == self.logger:
            self.logger=logging.getLogger('ConformedDimUpdate')
            self.logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            log_file = os.path.join(settings.PROJECT_DIR, 
                                    'logs\conformed_dim_update_'+ now.strftime("%Y-%m-%d") +'.log')
            handler=logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        return self.logger


class UpdatePlayerActivityLogger:
    logger = None
    def myLogger(self):
        if None == self.logger:
            self.logger=logging.getLogger('PlayerActivityUpdate')
            self.logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            log_file = os.path.join(settings.PROJECT_DIR, 
                                    'logs\player_activity_update_'+ now.strftime("%Y-%m-%d") +'.log')
            handler=logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        return self.logger
        
class UpdateElasticLogger:
    logger = None
    def myLogger(self):
        if None == self.logger:
            self.logger=logging.getLogger('ElasticUpdate')
            self.logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            log_file = os.path.join(settings.PROJECT_DIR, 
                                    'logs\elastic_update_'+ now.strftime("%Y-%m-%d") +'.log')
            handler=logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        return self.logger
