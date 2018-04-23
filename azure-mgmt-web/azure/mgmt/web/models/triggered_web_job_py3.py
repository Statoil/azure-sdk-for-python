# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class TriggeredWebJob(ProxyOnlyResource):
    """Triggered Web Job Information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param latest_run: Latest job run information.
    :type latest_run: ~azure.mgmt.web.models.TriggeredJobRun
    :param history_url: History URL.
    :type history_url: str
    :param scheduler_logs_url: Scheduler Logs URL.
    :type scheduler_logs_url: str
    :ivar triggered_web_job_name: Job name. Used as job identifier in ARM
     resource URI.
    :vartype triggered_web_job_name: str
    :param run_command: Run command.
    :type run_command: str
    :param url: Job URL.
    :type url: str
    :param extra_info_url: Extra Info URL.
    :type extra_info_url: str
    :param job_type: Job type. Possible values include: 'Continuous',
     'Triggered'
    :type job_type: str or ~azure.mgmt.web.models.WebJobType
    :param error: Error information.
    :type error: str
    :param using_sdk: Using SDK?
    :type using_sdk: bool
    :param settings: Job settings.
    :type settings: dict[str, object]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'triggered_web_job_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'latest_run': {'key': 'properties.latestRun', 'type': 'TriggeredJobRun'},
        'history_url': {'key': 'properties.historyUrl', 'type': 'str'},
        'scheduler_logs_url': {'key': 'properties.schedulerLogsUrl', 'type': 'str'},
        'triggered_web_job_name': {'key': 'properties.name', 'type': 'str'},
        'run_command': {'key': 'properties.runCommand', 'type': 'str'},
        'url': {'key': 'properties.url', 'type': 'str'},
        'extra_info_url': {'key': 'properties.extraInfoUrl', 'type': 'str'},
        'job_type': {'key': 'properties.jobType', 'type': 'WebJobType'},
        'error': {'key': 'properties.error', 'type': 'str'},
        'using_sdk': {'key': 'properties.usingSdk', 'type': 'bool'},
        'settings': {'key': 'properties.settings', 'type': '{object}'},
    }

    def __init__(self, *, kind: str=None, latest_run=None, history_url: str=None, scheduler_logs_url: str=None, run_command: str=None, url: str=None, extra_info_url: str=None, job_type=None, error: str=None, using_sdk: bool=None, settings=None, **kwargs) -> None:
        super(TriggeredWebJob, self).__init__(kind=kind, **kwargs)
        self.latest_run = latest_run
        self.history_url = history_url
        self.scheduler_logs_url = scheduler_logs_url
        self.triggered_web_job_name = None
        self.run_command = run_command
        self.url = url
        self.extra_info_url = extra_info_url
        self.job_type = job_type
        self.error = error
        self.using_sdk = using_sdk
        self.settings = settings