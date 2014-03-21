# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
import AccessControl
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from gs.viewlet.contentprovider import SiteContentProvider
from Products.GSGroup.interfaces import IGSGroupInfo

from logging import getLogger
log = getLogger('edem.groups.contentprovider')


class NavGroupsListingContentProvider(SiteContentProvider):

    def __init__(self, context, request, view):
        super(NavGroupsListingContentProvider,
              self). __init__(context, request, view)
        self.pageTemplateFileName = "browser/templates/contentProviders/"
        self.groupsInfo = createObject('groupserver.GroupsInfo', context)
        self.updated = False

    def update(self):
        if self.maxGroupsToDisplay < 0:
            raise ValueError('maxGroupsToDisplay must be 0 or greater')
        self.pageTemplateFileName += self.groupsTypeToDisplay + '.pt'
        self.pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        self.updated = True

    def render(self):
        if not self.updated:
            raise UpdateNotCalled
        return self.pageTemplate(view=self)

    @Lazy
    def joinable_groups(self):
        u = self.loggedInUser.user
        joinableGroups = self.groupsInfo.get_joinable_groups_for_user(u)
        if self.maxGroupsToDisplay:
            joinableGroups = joinableGroups[:self.maxGroupsToDisplay]
        groups = map(IGSGroupInfo, joinableGroups)
        return groups

    @Lazy
    def member_groups(self):
        user = AccessControl.getSecurityManager().getUser()
        memberGroups = self.groupsInfo.get_member_groups_for_user(user, user)
        if self.maxGroupsToDisplay:
            memberGroups = memberGroups[:self.maxGroupsToDisplay]
        groups = map(IGSGroupInfo, memberGroups)
        return groups

    @Lazy
    def suggested_groups(self):
        siteInfo = createObject('groupserver.SiteInfo', self.context)
        groupNames = siteInfo.get_property('suggestedGroups', [])
        suggestedGroups = []
        if self.maxGroupsToDisplay:
            groupNames = groupNames[:self.maxGroupsToDisplay]
        for groupName in groupNames:
            suggestedGroups.append(
                createObject('groupserver.GroupInfo', self.context, groupName))
        return suggestedGroups
