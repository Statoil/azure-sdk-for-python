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

from .entity_health_state_chunk import EntityHealthStateChunk


class DeployedServicePackageHealthStateChunk(EntityHealthStateChunk):
    """Represents the health state chunk of a deployed service package, which
    contains the service manifest name and the service package aggregated
    health state.
    .

    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param service_manifest_name: The name of the service manifest.
    :type service_manifest_name: str
    :param service_package_activation_id: The ActivationId of a deployed
     service package. If ServicePackageActivationMode specified at the time of
     creating the service
     is 'SharedProcess' (or if it is not specified, in which case it defaults
     to 'SharedProcess'), then value of ServicePackageActivationId
     is always an empty string.
    :type service_package_activation_id: str
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
    }

    def __init__(self, *, health_state=None, service_manifest_name: str=None, service_package_activation_id: str=None, **kwargs) -> None:
        super(DeployedServicePackageHealthStateChunk, self).__init__(health_state=health_state, **kwargs)
        self.service_manifest_name = service_manifest_name
        self.service_package_activation_id = service_package_activation_id