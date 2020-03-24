# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common
from centreonapi.webservice import Webservice


class Realtime(common.CentreonObject):

    def __init__(self):
        self.webservice = Webservice.getInstance()

    def getServices(self, action, values=None):
        """
            Get some services info
            More info about values here:
            https://documentation.centreon.com/docs/centreon/en/latest/api/api_rest/index.html#service-status
        """
        self.realtime_services = self.webservice.centreon_realtime(
            action,
             'services',
            values)
        return self.realtime_services

    def getHosts(self, action, values=None):
        """
            Get some hosts info
            More info about values here:
            https://documentation.centreon.com/docs/centreon/en/latest/api/api_rest/index.html#host-status
        """
        self.realtime_hosts = self.webservice.centreon_realtime(
            action,
             'hosts',
            values)
        return self.realtime_hosts