# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common
from centreonapi.webservice import Webservice

class RTDowntime(common.CentreonObject):

    def __init__(self):
        self.webservice = Webservice.getInstance()
        self.__clapi_action = 'RTDOWNTIME'

    def add(self,host_name,time_start,time_end,fixed_time,duration,comment,apply_services):
        s, e = self.webservice.call_clapi(
                'add',
                self.__clapi_action,
                ["HOST",host_name,
                time_start,
                time_end,
                fixed_time,duration,comment,apply_services])
        return s, e

    def show_host(self,host_name):
        s, e = self.webservice.call_clapi(
                'show',
                self.__clapi_action,
                ["HOST",host_name])
        return s, e

    def show_all(self):
        s, e = self.webservice.call_clapi(
                'show',
                self.__clapi_action,
                [])
        return s, e

    def cancel(self,downtime_id):
        s, e = self.webservice.call_clapi(
                'cancel',
                self.__clapi_action,
                [downtime_id])
        return s, e
