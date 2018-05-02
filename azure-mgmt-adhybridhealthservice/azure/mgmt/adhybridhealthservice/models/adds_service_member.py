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

from msrest.serialization import Model


class AddsServiceMember(Model):
    """The server details for ADDS service.

    :param domain_name: The domain name.
    :type domain_name: str
    :param site_name: The site name.
    :type site_name: str
    :param adds_roles: The list of ADDS roles.
    :type adds_roles: list[str]
    :param gc_reachable: Indicates if the global catalog for this domain is
     reachable or not.
    :type gc_reachable: bool
    :param pdc_reachable: Indicates if the primary domain controller is
     reachable or not.
    :type pdc_reachable: bool
    :param sysvol_state: Indicates if the SYSVOL state is healthy or not.
    :type sysvol_state: bool
    :param dc_types: The list of domain controller types.
    :type dc_types: list[str]
    """

    _attribute_map = {
        'domain_name': {'key': 'domainName', 'type': 'str'},
        'site_name': {'key': 'siteName', 'type': 'str'},
        'adds_roles': {'key': 'addsRoles', 'type': '[str]'},
        'gc_reachable': {'key': 'gcReachable', 'type': 'bool'},
        'pdc_reachable': {'key': 'pdcReachable', 'type': 'bool'},
        'sysvol_state': {'key': 'sysvolState', 'type': 'bool'},
        'dc_types': {'key': 'dcTypes', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(AddsServiceMember, self).__init__(**kwargs)
        self.domain_name = kwargs.get('domain_name', None)
        self.site_name = kwargs.get('site_name', None)
        self.adds_roles = kwargs.get('adds_roles', None)
        self.gc_reachable = kwargs.get('gc_reachable', None)
        self.pdc_reachable = kwargs.get('pdc_reachable', None)
        self.sysvol_state = kwargs.get('sysvol_state', None)
        self.dc_types = kwargs.get('dc_types', None)