# -*- coding: utf-8; -*-
#
# (c) 2004-2007 Linbox / Free&ALter Soft, http://linbox.com
# (c) 2007-2008 Mandriva, http://www.mandriva.com
#
# $Id$
#
# This file is part of Mandriva Management Console (MMC).
#
# MMC is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# MMC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MMC; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging

import twisted.internet.reactor
import twisted.web.server
import twisted.internet.error
import twisted.web.xmlrpc
from twisted.internet import ssl

try:
    from twisted.web import http
except ImportError:
    from twisted.protocols import http

class InventoryHTTPChannel(http.HTTPChannel):
    """
    We inherit from http.HTTPChannel to log incoming connections when the
    launcher is in DEBUG mode, and to log connection errors.
    """
    
    def connectionMade(self):
        logger = logging.getLogger()
        logger.debug("Connection from %s" % (self.transport.getHost().host,))
        http.HTTPChannel.connectionMade(self)

    def connectionLost(self, reason):
        if not reason.check(twisted.internet.error.ConnectionDone):
            logger = logging.getLogger()
            logger.error(reason)
        http.HTTPChannel.connectionLost(self, reason)        

class InventorySite(twisted.web.server.Site):
    protocol = InventoryHTTPChannel

