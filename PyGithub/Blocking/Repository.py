# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.Attributes

import PyGithub.Blocking.Contributor
import PyGithub.Blocking.Organization
import PyGithub.Blocking.PublicKey
import PyGithub.Blocking.Team
import PyGithub.Blocking.User


class Repository(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_fork`
      * :meth:`.AuthenticatedUser.create_repo`
      * :meth:`.AuthenticatedUser.get_repo`
      * :meth:`.AuthenticatedUser.get_repos`
      * :meth:`.AuthenticatedUser.get_starred`
      * :meth:`.AuthenticatedUser.get_subscriptions`
      * :meth:`.Github.get_repo`
      * :meth:`.Github.get_repos`
      * :meth:`.Organization.create_fork`
      * :meth:`.Organization.create_repo`
      * :meth:`.Organization.get_repo`
      * :meth:`.Organization.get_repos`
      * :meth:`.Repository.get_forks`
      * :attr:`.Repository.parent`
      * :attr:`.Repository.source`
      * :meth:`.Team.get_repos`
      * :meth:`.User.get_repo`
      * :meth:`.User.get_repos`
      * :meth:`.User.get_starred`
      * :meth:`.User.get_subscriptions`
    """

    class AnonymousContributor(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Repository.get_contributors`
        """

        def _initAttributes(self, contributions=None, name=None, type=None, **kwds):
            super(Repository.AnonymousContributor, self)._initAttributes(**kwds)
            self.__contributions = self._createIntAttribute("Repository.AnonymousContributor.contributions", contributions)
            self.__name = self._createStringAttribute("Repository.AnonymousContributor.name", name)
            self.__type = self._createStringAttribute("Repository.AnonymousContributor.type", type)

        @property
        def contributions(self):
            """
            :type: :class:`int`
            """
            return self.__contributions.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def type(self):
            """
            :type: :class:`string`
            """
            return self.__type.value

    class Permissions(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Repository.permissions`
        """

        def _initAttributes(self, admin=None, pull=None, push=None, **kwds):
            super(Repository.Permissions, self)._initAttributes(**kwds)
            self.__admin = self._createBoolAttribute("Repository.Permissions.admin", admin)
            self.__pull = self._createBoolAttribute("Repository.Permissions.pull", pull)
            self.__push = self._createBoolAttribute("Repository.Permissions.push", push)

        def _updateAttributes(self, admin=None, pull=None, push=None, **kwds):
            super(Repository.Permissions, self)._updateAttributes(**kwds)
            self.__admin.update(admin)
            self.__pull.update(pull)
            self.__push.update(push)

        @property
        def admin(self):
            """
            :type: :class:`bool`
            """
            return self.__admin.value

        @property
        def pull(self):
            """
            :type: :class:`bool`
            """
            return self.__pull.value

        @property
        def push(self):
            """
            :type: :class:`bool`
            """
            return self.__push.value

    def _initAttributes(self, archive_url=PyGithub.Blocking.Attributes.Absent, assignees_url=PyGithub.Blocking.Attributes.Absent, blobs_url=PyGithub.Blocking.Attributes.Absent, branches_url=PyGithub.Blocking.Attributes.Absent, clone_url=PyGithub.Blocking.Attributes.Absent, collaborators_url=PyGithub.Blocking.Attributes.Absent, comments_url=PyGithub.Blocking.Attributes.Absent, commits_url=PyGithub.Blocking.Attributes.Absent, compare_url=PyGithub.Blocking.Attributes.Absent, contents_url=PyGithub.Blocking.Attributes.Absent, contributors_url=PyGithub.Blocking.Attributes.Absent, created_at=PyGithub.Blocking.Attributes.Absent, default_branch=PyGithub.Blocking.Attributes.Absent, description=PyGithub.Blocking.Attributes.Absent, downloads_url=PyGithub.Blocking.Attributes.Absent, events_url=PyGithub.Blocking.Attributes.Absent, fork=PyGithub.Blocking.Attributes.Absent, forks=PyGithub.Blocking.Attributes.Absent, forks_count=PyGithub.Blocking.Attributes.Absent, forks_url=PyGithub.Blocking.Attributes.Absent, full_name=PyGithub.Blocking.Attributes.Absent, git_commits_url=PyGithub.Blocking.Attributes.Absent, git_refs_url=PyGithub.Blocking.Attributes.Absent, git_tags_url=PyGithub.Blocking.Attributes.Absent, git_url=PyGithub.Blocking.Attributes.Absent, has_issues=PyGithub.Blocking.Attributes.Absent, has_wiki=PyGithub.Blocking.Attributes.Absent, homepage=PyGithub.Blocking.Attributes.Absent, hooks_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, id=PyGithub.Blocking.Attributes.Absent, issue_comment_url=PyGithub.Blocking.Attributes.Absent, issue_events_url=PyGithub.Blocking.Attributes.Absent, issues_url=PyGithub.Blocking.Attributes.Absent, keys_url=PyGithub.Blocking.Attributes.Absent, labels_url=PyGithub.Blocking.Attributes.Absent, language=PyGithub.Blocking.Attributes.Absent, languages_url=PyGithub.Blocking.Attributes.Absent, merges_url=PyGithub.Blocking.Attributes.Absent, milestones_url=PyGithub.Blocking.Attributes.Absent, mirror_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, network_count=PyGithub.Blocking.Attributes.Absent, notifications_url=PyGithub.Blocking.Attributes.Absent, open_issues=PyGithub.Blocking.Attributes.Absent, open_issues_count=PyGithub.Blocking.Attributes.Absent, owner=PyGithub.Blocking.Attributes.Absent, parent=PyGithub.Blocking.Attributes.Absent, permissions=PyGithub.Blocking.Attributes.Absent, private=PyGithub.Blocking.Attributes.Absent, pulls_url=PyGithub.Blocking.Attributes.Absent, pushed_at=PyGithub.Blocking.Attributes.Absent, releases_url=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, source=PyGithub.Blocking.Attributes.Absent, ssh_url=PyGithub.Blocking.Attributes.Absent, stargazers_count=PyGithub.Blocking.Attributes.Absent, stargazers_url=PyGithub.Blocking.Attributes.Absent, statuses_url=PyGithub.Blocking.Attributes.Absent, subscribers_count=PyGithub.Blocking.Attributes.Absent, subscribers_url=PyGithub.Blocking.Attributes.Absent, subscription_url=PyGithub.Blocking.Attributes.Absent, svn_url=PyGithub.Blocking.Attributes.Absent, tags_url=PyGithub.Blocking.Attributes.Absent, teams_url=PyGithub.Blocking.Attributes.Absent, trees_url=PyGithub.Blocking.Attributes.Absent, updated_at=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, watchers=PyGithub.Blocking.Attributes.Absent, watchers_count=PyGithub.Blocking.Attributes.Absent, has_downloads=None, master_branch=None, organization=None, **kwds):
        super(Repository, self)._initAttributes(**kwds)
        self.__archive_url = self._createStringAttribute("Repository.archive_url", archive_url)
        self.__assignees_url = self._createStringAttribute("Repository.assignees_url", assignees_url)
        self.__blobs_url = self._createStringAttribute("Repository.blobs_url", blobs_url)
        self.__branches_url = self._createStringAttribute("Repository.branches_url", branches_url)
        self.__clone_url = self._createStringAttribute("Repository.clone_url", clone_url)
        self.__collaborators_url = self._createStringAttribute("Repository.collaborators_url", collaborators_url)
        self.__comments_url = self._createStringAttribute("Repository.comments_url", comments_url)
        self.__commits_url = self._createStringAttribute("Repository.commits_url", commits_url)
        self.__compare_url = self._createStringAttribute("Repository.compare_url", compare_url)
        self.__contents_url = self._createStringAttribute("Repository.contents_url", contents_url)
        self.__contributors_url = self._createStringAttribute("Repository.contributors_url", contributors_url)
        self.__created_at = self._createDatetimeAttribute("Repository.created_at", created_at)
        self.__default_branch = self._createStringAttribute("Repository.default_branch", default_branch)
        self.__description = self._createStringAttribute("Repository.description", description)
        self.__downloads_url = self._createStringAttribute("Repository.downloads_url", downloads_url)
        self.__events_url = self._createStringAttribute("Repository.events_url", events_url)
        self.__fork = self._createBoolAttribute("Repository.fork", fork)
        self.__forks = self._createIntAttribute("Repository.forks", forks)
        self.__forks_count = self._createIntAttribute("Repository.forks_count", forks_count)
        self.__forks_url = self._createStringAttribute("Repository.forks_url", forks_url)
        self.__full_name = self._createStringAttribute("Repository.full_name", full_name)
        self.__git_commits_url = self._createStringAttribute("Repository.git_commits_url", git_commits_url)
        self.__git_refs_url = self._createStringAttribute("Repository.git_refs_url", git_refs_url)
        self.__git_tags_url = self._createStringAttribute("Repository.git_tags_url", git_tags_url)
        self.__git_url = self._createStringAttribute("Repository.git_url", git_url)
        self.__has_issues = self._createBoolAttribute("Repository.has_issues", has_issues)
        self.__has_wiki = self._createBoolAttribute("Repository.has_wiki", has_wiki)
        self.__homepage = self._createStringAttribute("Repository.homepage", homepage)
        self.__hooks_url = self._createStringAttribute("Repository.hooks_url", hooks_url)
        self.__html_url = self._createStringAttribute("Repository.html_url", html_url)
        self.__id = self._createIntAttribute("Repository.id", id)
        self.__issue_comment_url = self._createStringAttribute("Repository.issue_comment_url", issue_comment_url)
        self.__issue_events_url = self._createStringAttribute("Repository.issue_events_url", issue_events_url)
        self.__issues_url = self._createStringAttribute("Repository.issues_url", issues_url)
        self.__keys_url = self._createStringAttribute("Repository.keys_url", keys_url)
        self.__labels_url = self._createStringAttribute("Repository.labels_url", labels_url)
        self.__language = self._createStringAttribute("Repository.language", language)
        self.__languages_url = self._createStringAttribute("Repository.languages_url", languages_url)
        self.__merges_url = self._createStringAttribute("Repository.merges_url", merges_url)
        self.__milestones_url = self._createStringAttribute("Repository.milestones_url", milestones_url)
        self.__mirror_url = self._createStringAttribute("Repository.mirror_url", mirror_url)
        self.__name = self._createStringAttribute("Repository.name", name)
        self.__network_count = self._createIntAttribute("Repository.network_count", network_count)
        self.__notifications_url = self._createStringAttribute("Repository.notifications_url", notifications_url)
        self.__open_issues = self._createIntAttribute("Repository.open_issues", open_issues)
        self.__open_issues_count = self._createIntAttribute("Repository.open_issues_count", open_issues_count)
        self.__owner = self._createUnionAttribute("Repository.owner", "type", dict(User=PyGithub.Blocking.User.User, Organization=PyGithub.Blocking.Organization.Organization), owner)
        self.__parent = self._createClassAttribute("Repository.parent", Repository, parent)
        self.__permissions = self._createStructAttribute("Repository.permissions", Repository.Permissions, permissions)
        self.__private = self._createBoolAttribute("Repository.private", private)
        self.__pulls_url = self._createStringAttribute("Repository.pulls_url", pulls_url)
        self.__pushed_at = self._createDatetimeAttribute("Repository.pushed_at", pushed_at)
        self.__releases_url = self._createStringAttribute("Repository.releases_url", releases_url)
        self.__size = self._createIntAttribute("Repository.size", size)
        self.__source = self._createClassAttribute("Repository.source", Repository, source)
        self.__ssh_url = self._createStringAttribute("Repository.ssh_url", ssh_url)
        self.__stargazers_count = self._createIntAttribute("Repository.stargazers_count", stargazers_count)
        self.__stargazers_url = self._createStringAttribute("Repository.stargazers_url", stargazers_url)
        self.__statuses_url = self._createStringAttribute("Repository.statuses_url", statuses_url)
        self.__subscribers_count = self._createIntAttribute("Repository.subscribers_count", subscribers_count)
        self.__subscribers_url = self._createStringAttribute("Repository.subscribers_url", subscribers_url)
        self.__subscription_url = self._createStringAttribute("Repository.subscription_url", subscription_url)
        self.__svn_url = self._createStringAttribute("Repository.svn_url", svn_url)
        self.__tags_url = self._createStringAttribute("Repository.tags_url", tags_url)
        self.__teams_url = self._createStringAttribute("Repository.teams_url", teams_url)
        self.__trees_url = self._createStringAttribute("Repository.trees_url", trees_url)
        self.__updated_at = self._createDatetimeAttribute("Repository.updated_at", updated_at)
        self.__url = self._createStringAttribute("Repository.url", url)
        self.__watchers = self._createIntAttribute("Repository.watchers", watchers)
        self.__watchers_count = self._createIntAttribute("Repository.watchers_count", watchers_count)

    def _updateAttributes(self, eTag, archive_url=PyGithub.Blocking.Attributes.Absent, assignees_url=PyGithub.Blocking.Attributes.Absent, blobs_url=PyGithub.Blocking.Attributes.Absent, branches_url=PyGithub.Blocking.Attributes.Absent, clone_url=PyGithub.Blocking.Attributes.Absent, collaborators_url=PyGithub.Blocking.Attributes.Absent, comments_url=PyGithub.Blocking.Attributes.Absent, commits_url=PyGithub.Blocking.Attributes.Absent, compare_url=PyGithub.Blocking.Attributes.Absent, contents_url=PyGithub.Blocking.Attributes.Absent, contributors_url=PyGithub.Blocking.Attributes.Absent, created_at=PyGithub.Blocking.Attributes.Absent, default_branch=PyGithub.Blocking.Attributes.Absent, description=PyGithub.Blocking.Attributes.Absent, downloads_url=PyGithub.Blocking.Attributes.Absent, events_url=PyGithub.Blocking.Attributes.Absent, fork=PyGithub.Blocking.Attributes.Absent, forks=PyGithub.Blocking.Attributes.Absent, forks_count=PyGithub.Blocking.Attributes.Absent, forks_url=PyGithub.Blocking.Attributes.Absent, full_name=PyGithub.Blocking.Attributes.Absent, git_commits_url=PyGithub.Blocking.Attributes.Absent, git_refs_url=PyGithub.Blocking.Attributes.Absent, git_tags_url=PyGithub.Blocking.Attributes.Absent, git_url=PyGithub.Blocking.Attributes.Absent, has_issues=PyGithub.Blocking.Attributes.Absent, has_wiki=PyGithub.Blocking.Attributes.Absent, homepage=PyGithub.Blocking.Attributes.Absent, hooks_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, id=PyGithub.Blocking.Attributes.Absent, issue_comment_url=PyGithub.Blocking.Attributes.Absent, issue_events_url=PyGithub.Blocking.Attributes.Absent, issues_url=PyGithub.Blocking.Attributes.Absent, keys_url=PyGithub.Blocking.Attributes.Absent, labels_url=PyGithub.Blocking.Attributes.Absent, language=PyGithub.Blocking.Attributes.Absent, languages_url=PyGithub.Blocking.Attributes.Absent, merges_url=PyGithub.Blocking.Attributes.Absent, milestones_url=PyGithub.Blocking.Attributes.Absent, mirror_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, network_count=PyGithub.Blocking.Attributes.Absent, notifications_url=PyGithub.Blocking.Attributes.Absent, open_issues=PyGithub.Blocking.Attributes.Absent, open_issues_count=PyGithub.Blocking.Attributes.Absent, owner=PyGithub.Blocking.Attributes.Absent, parent=PyGithub.Blocking.Attributes.Absent, permissions=PyGithub.Blocking.Attributes.Absent, private=PyGithub.Blocking.Attributes.Absent, pulls_url=PyGithub.Blocking.Attributes.Absent, pushed_at=PyGithub.Blocking.Attributes.Absent, releases_url=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, source=PyGithub.Blocking.Attributes.Absent, ssh_url=PyGithub.Blocking.Attributes.Absent, stargazers_count=PyGithub.Blocking.Attributes.Absent, stargazers_url=PyGithub.Blocking.Attributes.Absent, statuses_url=PyGithub.Blocking.Attributes.Absent, subscribers_count=PyGithub.Blocking.Attributes.Absent, subscribers_url=PyGithub.Blocking.Attributes.Absent, subscription_url=PyGithub.Blocking.Attributes.Absent, svn_url=PyGithub.Blocking.Attributes.Absent, tags_url=PyGithub.Blocking.Attributes.Absent, teams_url=PyGithub.Blocking.Attributes.Absent, trees_url=PyGithub.Blocking.Attributes.Absent, updated_at=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, watchers=PyGithub.Blocking.Attributes.Absent, watchers_count=PyGithub.Blocking.Attributes.Absent, has_downloads=None, master_branch=None, organization=None, **kwds):
        super(Repository, self)._updateAttributes(eTag, **kwds)
        self.__archive_url.update(archive_url)
        self.__assignees_url.update(assignees_url)
        self.__blobs_url.update(blobs_url)
        self.__branches_url.update(branches_url)
        self.__clone_url.update(clone_url)
        self.__collaborators_url.update(collaborators_url)
        self.__comments_url.update(comments_url)
        self.__commits_url.update(commits_url)
        self.__compare_url.update(compare_url)
        self.__contents_url.update(contents_url)
        self.__contributors_url.update(contributors_url)
        self.__created_at.update(created_at)
        self.__default_branch.update(default_branch)
        self.__description.update(description)
        self.__downloads_url.update(downloads_url)
        self.__events_url.update(events_url)
        self.__fork.update(fork)
        self.__forks.update(forks)
        self.__forks_count.update(forks_count)
        self.__forks_url.update(forks_url)
        self.__full_name.update(full_name)
        self.__git_commits_url.update(git_commits_url)
        self.__git_refs_url.update(git_refs_url)
        self.__git_tags_url.update(git_tags_url)
        self.__git_url.update(git_url)
        self.__has_issues.update(has_issues)
        self.__has_wiki.update(has_wiki)
        self.__homepage.update(homepage)
        self.__hooks_url.update(hooks_url)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__issue_comment_url.update(issue_comment_url)
        self.__issue_events_url.update(issue_events_url)
        self.__issues_url.update(issues_url)
        self.__keys_url.update(keys_url)
        self.__labels_url.update(labels_url)
        self.__language.update(language)
        self.__languages_url.update(languages_url)
        self.__merges_url.update(merges_url)
        self.__milestones_url.update(milestones_url)
        self.__mirror_url.update(mirror_url)
        self.__name.update(name)
        self.__network_count.update(network_count)
        self.__notifications_url.update(notifications_url)
        self.__open_issues.update(open_issues)
        self.__open_issues_count.update(open_issues_count)
        self.__owner.update(owner)
        self.__parent.update(parent)
        self.__permissions.update(permissions)
        self.__private.update(private)
        self.__pulls_url.update(pulls_url)
        self.__pushed_at.update(pushed_at)
        self.__releases_url.update(releases_url)
        self.__size.update(size)
        self.__source.update(source)
        self.__ssh_url.update(ssh_url)
        self.__stargazers_count.update(stargazers_count)
        self.__stargazers_url.update(stargazers_url)
        self.__statuses_url.update(statuses_url)
        self.__subscribers_count.update(subscribers_count)
        self.__subscribers_url.update(subscribers_url)
        self.__subscription_url.update(subscription_url)
        self.__svn_url.update(svn_url)
        self.__tags_url.update(tags_url)
        self.__teams_url.update(teams_url)
        self.__trees_url.update(trees_url)
        self.__updated_at.update(updated_at)
        self.__url.update(url)
        self.__watchers.update(watchers)
        self.__watchers_count.update(watchers_count)

    @property
    def archive_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__archive_url.needsLazyCompletion)
        return self.__archive_url.value

    @property
    def assignees_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__assignees_url.needsLazyCompletion)
        return self.__assignees_url.value

    @property
    def blobs_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__blobs_url.needsLazyCompletion)
        return self.__blobs_url.value

    @property
    def branches_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__branches_url.needsLazyCompletion)
        return self.__branches_url.value

    @property
    def clone_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__clone_url.needsLazyCompletion)
        return self.__clone_url.value

    @property
    def collaborators_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__collaborators_url.needsLazyCompletion)
        return self.__collaborators_url.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__comments_url.needsLazyCompletion)
        return self.__comments_url.value

    @property
    def commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commits_url.needsLazyCompletion)
        return self.__commits_url.value

    @property
    def compare_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__compare_url.needsLazyCompletion)
        return self.__compare_url.value

    @property
    def contents_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__contents_url.needsLazyCompletion)
        return self.__contents_url.value

    @property
    def contributors_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__contributors_url.needsLazyCompletion)
        return self.__contributors_url.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def default_branch(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__default_branch.needsLazyCompletion)
        return self.__default_branch.value

    @property
    def description(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__description.needsLazyCompletion)
        return self.__description.value

    @property
    def downloads_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__downloads_url.needsLazyCompletion)
        return self.__downloads_url.value

    @property
    def events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__events_url.needsLazyCompletion)
        return self.__events_url.value

    @property
    def fork(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__fork.needsLazyCompletion)
        return self.__fork.value

    @property
    def forks(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__forks.needsLazyCompletion)
        return self.__forks.value

    @property
    def forks_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__forks_count.needsLazyCompletion)
        return self.__forks_count.value

    @property
    def forks_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__forks_url.needsLazyCompletion)
        return self.__forks_url.value

    @property
    def full_name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__full_name.needsLazyCompletion)
        return self.__full_name.value

    @property
    def git_commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_commits_url.needsLazyCompletion)
        return self.__git_commits_url.value

    @property
    def git_refs_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_refs_url.needsLazyCompletion)
        return self.__git_refs_url.value

    @property
    def git_tags_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_tags_url.needsLazyCompletion)
        return self.__git_tags_url.value

    @property
    def git_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_url.needsLazyCompletion)
        return self.__git_url.value

    @property
    def has_issues(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__has_issues.needsLazyCompletion)
        return self.__has_issues.value

    @property
    def has_wiki(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__has_wiki.needsLazyCompletion)
        return self.__has_wiki.value

    @property
    def homepage(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__homepage.needsLazyCompletion)
        return self.__homepage.value

    @property
    def hooks_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__hooks_url.needsLazyCompletion)
        return self.__hooks_url.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def issue_comment_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issue_comment_url.needsLazyCompletion)
        return self.__issue_comment_url.value

    @property
    def issue_events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issue_events_url.needsLazyCompletion)
        return self.__issue_events_url.value

    @property
    def issues_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issues_url.needsLazyCompletion)
        return self.__issues_url.value

    @property
    def keys_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__keys_url.needsLazyCompletion)
        return self.__keys_url.value

    @property
    def labels_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__labels_url.needsLazyCompletion)
        return self.__labels_url.value

    @property
    def language(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__language.needsLazyCompletion)
        return self.__language.value

    @property
    def languages_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__languages_url.needsLazyCompletion)
        return self.__languages_url.value

    @property
    def merges_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__merges_url.needsLazyCompletion)
        return self.__merges_url.value

    @property
    def milestones_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__milestones_url.needsLazyCompletion)
        return self.__milestones_url.value

    @property
    def mirror_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__mirror_url.needsLazyCompletion)
        return self.__mirror_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def network_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__network_count.needsLazyCompletion)
        return self.__network_count.value

    @property
    def notifications_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__notifications_url.needsLazyCompletion)
        return self.__notifications_url.value

    @property
    def open_issues(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__open_issues.needsLazyCompletion)
        return self.__open_issues.value

    @property
    def open_issues_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__open_issues_count.needsLazyCompletion)
        return self.__open_issues_count.value

    @property
    def owner(self):
        """
        :type: :class:`.User` or :class:`.Organization`
        """
        self._completeLazily(self.__owner.needsLazyCompletion)
        return self.__owner.value

    @property
    def parent(self):
        """
        :type: :class:`.Repository`
        """
        self._completeLazily(self.__parent.needsLazyCompletion)
        return self.__parent.value

    @property
    def permissions(self):
        """
        :type: :class:`.Permissions`
        """
        self._completeLazily(self.__permissions.needsLazyCompletion)
        return self.__permissions.value

    @property
    def private(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__private.needsLazyCompletion)
        return self.__private.value

    @property
    def pulls_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__pulls_url.needsLazyCompletion)
        return self.__pulls_url.value

    @property
    def pushed_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__pushed_at.needsLazyCompletion)
        return self.__pushed_at.value

    @property
    def releases_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__releases_url.needsLazyCompletion)
        return self.__releases_url.value

    @property
    def size(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__size.needsLazyCompletion)
        return self.__size.value

    @property
    def source(self):
        """
        :type: :class:`.Repository`
        """
        self._completeLazily(self.__source.needsLazyCompletion)
        return self.__source.value

    @property
    def ssh_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__ssh_url.needsLazyCompletion)
        return self.__ssh_url.value

    @property
    def stargazers_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__stargazers_count.needsLazyCompletion)
        return self.__stargazers_count.value

    @property
    def stargazers_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__stargazers_url.needsLazyCompletion)
        return self.__stargazers_url.value

    @property
    def statuses_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__statuses_url.needsLazyCompletion)
        return self.__statuses_url.value

    @property
    def subscribers_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__subscribers_count.needsLazyCompletion)
        return self.__subscribers_count.value

    @property
    def subscribers_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__subscribers_url.needsLazyCompletion)
        return self.__subscribers_url.value

    @property
    def subscription_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__subscription_url.needsLazyCompletion)
        return self.__subscription_url.value

    @property
    def svn_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__svn_url.needsLazyCompletion)
        return self.__svn_url.value

    @property
    def tags_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__tags_url.needsLazyCompletion)
        return self.__tags_url.value

    @property
    def teams_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__teams_url.needsLazyCompletion)
        return self.__teams_url.value

    @property
    def trees_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__trees_url.needsLazyCompletion)
        return self.__trees_url.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    @property
    def watchers(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__watchers.needsLazyCompletion)
        return self.__watchers.value

    @property
    def watchers_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__watchers_count.needsLazyCompletion)
        return self.__watchers_count.value

    def add_to_collaborators(self, user):
        """
        Calls the `PUT /repos/:owner/:repo/collaborators/:user <http://developer.github.com/v3/repos/collaborators#add-collaborator>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.collaborators_url, collaborator=user)
        self._triggerSideEffect("PUT", url)

    def create_key(self, title, key):
        """
        Calls the `POST /repos/:owner/:repo/keys <http://developer.github.com/v3/repos/keys#create>`__ end point.

        This is the only method calling this end point.

        :param title: mandatory :class:`string`
        :param key: mandatory :class:`string`
        :rtype: :class:`.PublicKey`
        """

        title = PyGithub.Blocking.Parameters.normalizeString(title)
        key = PyGithub.Blocking.Parameters.normalizeString(key)

        url = uritemplate.expand(self.keys_url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(title=title, key=key)
        return self._createInstance(PyGithub.Blocking.PublicKey.PublicKey, "POST", url, postArguments=postArguments)

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo <http://developer.github.com/v3/repos#delete-a-repository>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        self._triggerSideEffect("DELETE", url)

    def edit(self, name=None, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, default_branch=None):
        """
        Calls the `PATCH /repos/:owner/:repo <http://developer.github.com/v3/repos#edit>`__ end point.

        This is the only method calling this end point.

        :param name: optional :class:`string`
        :param description: optional :class:`string` or :class:`Reset`
        :param homepage: optional :class:`string` or :class:`Reset`
        :param private: optional :class:`bool`
        :param has_issues: optional :class:`bool`
        :param has_wiki: optional :class:`bool`
        :param default_branch: optional :class:`string`
        :rtype: None
        """

        if name is not None:
            name = PyGithub.Blocking.Parameters.normalizeString(name)
        if description is not None:
            description = PyGithub.Blocking.Parameters.normalizeStringReset(description)
        if homepage is not None:
            homepage = PyGithub.Blocking.Parameters.normalizeStringReset(homepage)
        if private is not None:
            private = PyGithub.Blocking.Parameters.normalizeBool(private)
        if has_issues is not None:
            has_issues = PyGithub.Blocking.Parameters.normalizeBool(has_issues)
        if has_wiki is not None:
            has_wiki = PyGithub.Blocking.Parameters.normalizeBool(has_wiki)
        if default_branch is not None:
            default_branch = PyGithub.Blocking.Parameters.normalizeString(default_branch)

        if name is None:
            name = self.name

        url = uritemplate.expand(self.url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(name=name, description=description, homepage=homepage, private=private, has_issues=has_issues, has_wiki=has_wiki, default_branch=default_branch)
        self._updateWith("PATCH", url, postArguments=postArguments)

    def get_assignees(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/assignees <http://developer.github.com/v3/issues/assignees#list-assignees>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.assignees_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)

    def get_collaborators(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/collaborators <http://developer.github.com/v3/repos/collaborators#list>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.collaborators_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)

    def get_contributors(self, anon=None, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/contributors <http://developer.github.com/v3/repos#list-contributors>`__ end point.

        This is the only method calling this end point.

        :param anon: optional :class:`bool`
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Contributor` or :class:`.AnonymousContributor`
        """

        if anon is not None:
            anon = PyGithub.Blocking.Parameters.normalizeBool(anon)
        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.contributors_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(anon=anon, per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.Attributes.Switch("type", dict(Anonymous=lambda session, attributes, eTag: PyGithub.Blocking.Repository.Repository.AnonymousContributor(session, attributes), User=PyGithub.Blocking.Contributor.Contributor)), "GET", url, urlArguments=urlArguments)

    def get_forks(self, sort=None, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#list-forks>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "newest" or "oldest" or "stargazers"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if sort is not None:
            sort = PyGithub.Blocking.Parameters.normalizeEnum(sort, "newest", "oldest", "stargazers")
        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.forks_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(sort=sort, per_page=per_page)
        return self._createPaginatedList(Repository, "GET", url, urlArguments=urlArguments)

    def get_key(self, id):
        """
        Calls the `GET /repos/:owner/:repo/keys/:id <http://developer.github.com/v3/repos/keys#get>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.PublicKey`
        """

        id = PyGithub.Blocking.Parameters.normalizeInt(id)

        url = uritemplate.expand(self.keys_url, key_id=str(id))
        return self._createInstance(PyGithub.Blocking.PublicKey.PublicKey, "GET", url)

    def get_keys(self):
        """
        Calls the `GET /repos/:owner/:repo/keys <http://developer.github.com/v3/repos/keys#list>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PublicKey`
        """

        url = uritemplate.expand(self.keys_url)
        return self._createList(PyGithub.Blocking.PublicKey.PublicKey, "GET", url)

    def get_stargazers(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/stargazers <http://developer.github.com/v3/activity/starring#list-stargazers>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.stargazers_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)

    def get_subscribers(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/subscribers <http://developer.github.com/v3/activity/watching#list-watchers>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.subscribers_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)

    def get_teams(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/teams <http://developer.github.com/v3/repos#list-teams>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Team`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.teams_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.Team.Team, "GET", url, urlArguments=urlArguments)

    def has_in_assignees(self, user):
        """
        Calls the `GET /repos/:owner/:repo/assignees/:assignee <http://developer.github.com/v3/issues/assignees#check-assignee>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: :class:`bool`
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.assignees_url, user=user)
        return self._createBool("GET", url)

    def has_in_collaborators(self, user):
        """
        Calls the `GET /repos/:owner/:repo/collaborators/:user <http://developer.github.com/v3/repos/collaborators#get>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: :class:`bool`
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.collaborators_url, collaborator=user)
        return self._createBool("GET", url)

    def remove_from_collaborators(self, user):
        """
        Calls the `DELETE /repos/:owner/:repo/collaborators/:user <http://developer.github.com/v3/repos/collaborators#remove-collaborator>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.collaborators_url, collaborator=user)
        self._triggerSideEffect("DELETE", url)