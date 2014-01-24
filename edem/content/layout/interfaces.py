# coding=utf-8
from __future__ import unicode_literals
from zope.viewlet.interfaces import IViewletManager
from zope.contentprovider.interfaces import IContentProvider
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema import ASCIILine, Choice, Int


class IEDemSiteNavMMVM(IViewletManager):
    '''Viewlet Manager for E-Democracy's site navigation mega menu'''

class IGSNavGroupsListing(IContentProvider):
    '''Content Provider for a listing of groups in a nav menu'''
    groupsTypeToDisplay = Choice(
        title="Type of Groups to Display",
        description="Defines which groups to display to the user: "
                    "groups that the user can join (joinableGroups)(default), "
                    "groups that the user is a member of (memberOfGroups), or "
                    "suggested groups for the user to join (suggestedGroups).",
        vocabulary=SimpleVocabulary.fromValues([
                    'joinableGroups',
                    'memberOfGroups',
                    'suggestedGroups']),
        required=False,
        default='joinableGroups'

    )

    maxGroupsToDisplay = Int(
        title="Maximum Groups to Display",
        description="The maximum number of groups to display to the user."
                    "A value of 0 (the default) results in all groups being "
                    "displayed. Negative values will throw an error.",
        required=False,
        default=0)
