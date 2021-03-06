==============================
``edem.content.layout``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Base page layouts for forums.e-democracy.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Bill Bushey`_
:Contact: Bill Bushey <bill.bushey@e-democracy.org>
:Date: 2013-11-20
:Organization: `E-Democracy`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 License`_
  by `E-Democracy`_.

Introduction
============

This product provides the layouts for browser pages on forums.e-democracy.org.
It is based on `gs.content.layout`_, the product that provides layouts for
browser pages for `GroupServer`_.

Groups Listing Content Provider
===============================

The Your Groups and Suggested Groups listings in the site navigation menu are
provided by a content provider: groupserver.NavGroupsListing. This content
provider produces a simple unordered list of groups. The content provider
has two parameters that can be defined when included in a template:

* groupsTypeToDisplay - Determines which set of groups to display: 

  * groups that the user can join (joinableGroups)(default);

  * groups that the user is a member of (memberOfGroups); or  

  * suggested groups for the user to join (suggestedGroups), which is based on
    the suggestedGroups property of the site object (editable via the ZMI),
    which is a lines property containing group ids

* maxGroupsToDisplay - Defines the maximum number of groups to list. If 0
  (the default), all groups within the choosen category will be displayed.
  A negative value will cause an error.

An example of calling the content provider to display upto 6 groups that the 
user is a member of::

  <ul tal:define="groupsTypeToDisplay string:memberOfGroups;
                  maxGroupsToDisplay python:6;"
      tal:replace="structure provider:groupserver.NavGroupsListing">
  </ul>

A seperate template exists for each category of groups that can be displayed.
They can be found in browser/templates/contentProviders/.


Minimal Layout
==============

In addition to the layouts provided by gs.content.layout, this product also
provides a *Minimal* layout. Because the Full and Menu layouts of this egg use
a significant amount of dynamic content, the Minimal layout is provided for
pages on which it is better to not have dynamic content, such as Error pages.
The Minimal layout should retain much of the look of the Full layout, and might
even include menus and content stored in the ZODB, but its templates should not 
attempt to access object properties.

Resources
=========

- Code repository: https://github.com/e-democracy/edem.content.layout 
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _E-Democracy: http://e-democracy.org/
.. _Bill Bushey: http://groupserver.org/p/wbushey
.. _Creative Commons Attribution-Share Alike 3.0 License:
   http://creativecommons.org/licenses/by-sa/3.0/
.. _gs.content.layout: 
   https://source.iopen.net/groupserver/gs.content.layout/summary
