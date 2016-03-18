"""
   Active Directory manipulation class wrapper for low level c++ class.
"""

import sys

import _adclient
from _adclient import *

class ADClient:
      """
        ADClient.login can throw ADBindError on errors.
        all search functions can throw ADSearchError on errors.
        all modify functions can throw both ADSearchError and ADOperationalError on errors.
          text description will be in exception object
          numeric code can be obtained from 'get_error_num' function
      """

      AD_SCOPE_BASE = 0
      AD_SCOPE_ONELEVEL = 1
      AD_SCOPE_SUBTREE = 2

      def __init__(self):
          self.obj = _adclient.new_adclient()

      def login(self, uries, binddn, bindpw, search_base, secured = True):
          """ It binds to Active Directory uries (e.g. "ldap://example.org") 
                   as binddn (e.g. "administrator@example.org") identified by 
                   bindpw (e.g. "password"). Search Base for every ldap search 
                   would be search_base (e.g. "dc=example,dc=org").
                   It returns nothing if operation was successfull.
                uries can be single string or list of strings
          """
          if sys.version_info[0] == 3:
             string_type = str
          else:
             string_type = basestring
          if isinstance(uries, string_type):
             uries = [uries]
          _adclient.login_adclient(self.obj, uries, binddn, bindpw, search_base, secured)

      def binded_uri(self):
          return _adclient.binded_uri_adclient(self.obj)

      def searchDN(self, filter):
          """ It returns list with DNs found with 'filter'
          """
          return _adclient.searchDN_adclient(self.obj, filter)

      def search(self, ou, scope, filter, attributes):
          """ General search function.
                It returns dict with users found with 'filter' with specified 'attributes'.
          """
          return _adclient.search_adclient(self.obj, ou, scope, filter, attributes)

      def getUserGroups(self, user):
          """ It returns list with "user" groups if operation was successfull.
          """
          return _adclient.getUserGroups_adclient(self.obj, user)

      def getUsersInGroup(self, group):
          """ It returns list with members of Active Directory "group" if operation was successfull.
          """
          return _adclient.getUsersInGroup_adclient(self.obj, group)

      def getUserControls(self, user):
          """ It returns map with "user" controls ('disabled', 'locked', 'dontExpirePassword', 'mustChangePassword', 'expired').
          """
          return _adclient.getUserControls_adclient(self.obj, user)


      def groupAddUser(self, group, user):
          """  It adds "user" to Active Directory "group".
               It returns nothing if operation was successfull.
          """
          _adclient.groupAddUser_adclient(self.obj, group, user)

      def groupRemoveUser(self, group, user):
          """ It removes "user" from Active Directory "group".
              It returns nothing if operation was successfull.
          """
          _adclient.groupRemoveUser_adclient(self.obj, group, user)

      def ifDialinUser(self, user):
          """ It returns True if msNPAllowDialin user attribute set to TRUE, False - otherwise.
          """
          if (_adclient.ifDialinUser_adclient(self.obj, user) == 1):
             return True
          else:
             return False

      def getDialinUsers(self):
          """ It returns list of all users with msNPAllowDialin = TRUE.
          """
          return _adclient.getDialinUsers_adclient(self.obj)

      def getDisabledUsers(self):
          """ It returns list of all users with ADS_UF_ACCOUNTDISABLE in userAccountControl.
          """
          return _adclient.getDisabledUsers_adclient(self.obj)

      def getObjectDN(self, user):
          """ It returns user DN by short name.
          """
          return _adclient.getObjectDN_adclient(self.obj, user)

      def ifUserDisabled(self, user):
          """ It returns True if UserAccountControl flag contain ACCOUNTDISABLE property, 
                         False - otherwise.
          """
          return _adclient.ifUserDisabled_adclient(self.obj, user)

      def ifDNExists(self, dn, objectclass = '*'):
          """ It returns True of False depends on object DN existence.
              dn objectclass can be limited with corresponding argument.
          """
          return _adclient.ifDNExists_adclient(self.obj, dn, objectclass)

      def getAllOUs(self):
          """ It returns list of all organizationalUnits in search_base.
          """
          return _adclient.getAllOUs_adclient(self.obj)

      def getUsersInOU(self, OU):
          """ It returns list of all users in OU.
          """
          return _adclient.getUsersInOU_adclient(self.obj, OU)

      def getUsersInOU_SubTree(self, OU):
          """ It returns list of all users in OU and subOUs.
          """
          return _adclient.getUsersInOU_SubTree_adclient(self.obj, OU)

      def getGroups(self):
          """ It returns list of all groups in Active Directory.
          """
          return _adclient.getGroups_adclient(self.obj)

      def getUsers(self):
          """ It returns list of all users in Active Directory.
          """
          return _adclient.getUsers_adclient(self.obj)

      def getOUsInOU(self, OU):
          """ It returns list of all OUs in OU.
          """
          return _adclient.getOUsInOU_adclient(self.obj, OU)

      def getUserDisplayName(self, user):
          """ It returns string with user DisplayName property.
          """
          return _adclient.getUserDisplayName_adclient(self.obj, user)

      def getUserIpAddress(self, user):
          """ It returns string with user msRADIUSFramedIPAddress property.
          """
          return _adclient.getUserIpAddress_adclient(self.obj, user)

      def getObjectAttribute(self, object, attribute):
          """ It returns list with values of object attribute.
          """
          return _adclient.getObjectAttribute_adclient(self.obj, object, attribute)

      def getObjectAttributes(self, object):
          """ It returns map of all object attributes.
          """
          return _adclient.getObjectAttributes_adclient(self.obj, object)

      def CreateComputer(self, name, container):
          """ It creates computer with given name in given container.
          """
          _adclient.CreateComputer_adclient(self.obj, name, container)

      def CreateUser(self, cn, container, short_name):
          """ It creates user with given common name and short name in given container.
          """
          _adclient.CreateUser_adclient(self.obj, cn, container, short_name)

      def DeleteDN(self, dn):
          """ It deletes given DN.
          """
          _adclient.DeleteDN_adclient(self.obj, dn)

      def CreateOU(self, ou):
          """ It creates given OU (with subOUs if needed).
          """
          _adclient.CreateOU_adclient(self.obj, ou)

      def EnableUser(self, short_name):
          """ It enables given user.
          """
          _adclient.EnableUser_adclient(self.obj, short_name)

      def DisableUser(self, short_name):
          """ It disables given user.
          """
          _adclient.DisableUser_adclient(self.obj, short_name)

      def setUserDescription(self, dn, descr):
          _adclient.setUserDescription_adclient(self.obj, dn, descr)

      def setUserPassword(self, dn, password):
          _adclient.setUserPassword_adclient(self.obj, dn, password)

      def checkUserPassword(self, dn, password):
          """ It returns True of False depends on user credentials correctness. """
          return _adclient.checkUserPassword_adclient(self.obj, dn, password)

      def setUserDialinAllowed(self, user):
          _adclient.setUserDialinAllowed_adclient(self.obj, user)

      def setUserDialinDisabled(self, user):
          _adclient.setUserDialinDisabled_adclient(self.obj, user)

      def setUserSN_adclient(self, user, sn):
          _adclient.setUserSN_adclient(self.obj, user, sn)

      def setUserInitials(self, user, initials):
          _adclient.setUserInitials_adclient(self.obj, user, initials)

      def setUserGivenName(self, user, givenName):
          _adclient.setUserGivenName_adclient(self.obj, user, givenName)

      def setUserDisplayName(self, user, displayName):
          _adclient.setUserDisplayName_adclient(self.obj, user, displayName)

      def setUserRoomNumber(self, user, roomNum):
          _adclient.setUserRoomNumber_adclient(self.obj, user, roomNum)

      def setUserAddress(self, user, streetAddress):
          _adclient.setUserAddress_adclient(self.obj, user, streetAddress)

      def setUserInfo(self, user, info):
          _adclient.setUserInfo_adclient(self.obj, user, info)

      def setUserTitle(self, user, title):
          _adclient.setUserTitle_adclient(self.obj, user, title)

      def setUserDepartment(self, user, department):
          _adclient.setUserDepartment_adclient(self.obj, user, department)

      def setUserCompany(self, user, company):
          _adclient.setUserCompany_adclient(self.obj, user, company)

      def setUserPhone(self, user, phone):
          _adclient.setUserPhone_adclient(self.obj, user, phone)

      def setUserSN(self, user, phone):
          _adclient.setUserSN_adclient(self.obj, user, phone)

      def setUserIpAddress(self, user, ip):
          _adclient.setUserIpAddress_adclient(self.obj, user, ip)

      def setObjectAttribute(self, user, attr, ip):
          _adclient.setObjectAttribute_adclient(self.obj, user, attr, ip)

      def UnLockUser(self, user):
          """ It unlocks given user.
          """
          _adclient.UnLockUser_adclient(self.obj, user)

      def get_error_num(self):
          """ It returns int of last error occured
          """
          return _adclient.get_error_num()

      def int2ip(self, ipstr):
          return _adclient.int2ip(ipstr)
