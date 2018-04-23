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


class DeployServicePackageToNodeDescription(Model):
    """Defines description for downloading packages associated with a service
    manifest to image cache on a Service Fabric node.
    .

    All required parameters must be populated in order to send to Azure.

    :param service_manifest_name: Required. The name of service manifest whose
     packages need to be downloaded.
    :type service_manifest_name: str
    :param application_type_name: Required. The application type name as
     defined in the application manifest.
    :type application_type_name: str
    :param application_type_version: Required. The version of the application
     type as defined in the application manifest.
    :type application_type_version: str
    :param node_name: Required. The name of a Service Fabric node.
    :type node_name: str
    :param package_sharing_policy: List of package sharing policy information.
    :type package_sharing_policy:
     list[~azure.servicefabric.models.PackageSharingPolicyInfo]
    """

    _validation = {
        'service_manifest_name': {'required': True},
        'application_type_name': {'required': True},
        'application_type_version': {'required': True},
        'node_name': {'required': True},
    }

    _attribute_map = {
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'application_type_name': {'key': 'ApplicationTypeName', 'type': 'str'},
        'application_type_version': {'key': 'ApplicationTypeVersion', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'package_sharing_policy': {'key': 'PackageSharingPolicy', 'type': '[PackageSharingPolicyInfo]'},
    }

    def __init__(self, *, service_manifest_name: str, application_type_name: str, application_type_version: str, node_name: str, package_sharing_policy=None, **kwargs) -> None:
        super(DeployServicePackageToNodeDescription, self).__init__(**kwargs)
        self.service_manifest_name = service_manifest_name
        self.application_type_name = application_type_name
        self.application_type_version = application_type_version
        self.node_name = node_name
        self.package_sharing_policy = package_sharing_policy