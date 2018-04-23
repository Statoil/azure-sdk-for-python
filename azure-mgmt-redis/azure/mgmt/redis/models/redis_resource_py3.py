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

from .tracked_resource import TrackedResource


class RedisResource(TrackedResource):
    """A single Redis item in List or Get Operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param redis_configuration: All Redis Settings. Few possible keys:
     rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value
     etc.
    :type redis_configuration: dict[str, str]
    :param enable_non_ssl_port: Specifies whether the non-ssl Redis server
     port (6379) is enabled.
    :type enable_non_ssl_port: bool
    :param tenant_settings: A dictionary of tenant settings
    :type tenant_settings: dict[str, str]
    :param shard_count: The number of shards to be created on a Premium
     Cluster Cache.
    :type shard_count: int
    :param minimum_tls_version: Optional: requires clients to use a specified
     TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2'). Possible
     values include: '1.0', '1.1', '1.2'
    :type minimum_tls_version: str or ~azure.mgmt.redis.models.TlsVersion
    :param sku: Required. The SKU of the Redis cache to deploy.
    :type sku: ~azure.mgmt.redis.models.Sku
    :param subnet_id: The full resource ID of a subnet in a virtual network to
     deploy the Redis cache in. Example format:
     /subscriptions/{subid}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1
    :type subnet_id: str
    :param static_ip: Static IP address. Required when deploying a Redis cache
     inside an existing Azure Virtual Network.
    :type static_ip: str
    :ivar redis_version: Redis version.
    :vartype redis_version: str
    :ivar provisioning_state: Redis instance provisioning status. Possible
     values include: 'Creating', 'Deleting', 'Disabled', 'Failed', 'Linking',
     'Provisioning', 'RecoveringScaleFailure', 'Scaling', 'Succeeded',
     'Unlinking', 'Unprovisioning', 'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.redis.models.ProvisioningState
    :ivar host_name: Redis host name.
    :vartype host_name: str
    :ivar port: Redis non-SSL port.
    :vartype port: int
    :ivar ssl_port: Redis SSL port.
    :vartype ssl_port: int
    :ivar access_keys: The keys of the Redis cache - not set if this object is
     not the response to Create or Update redis cache
    :vartype access_keys: ~azure.mgmt.redis.models.RedisAccessKeys
    :ivar linked_servers: List of the linked servers associated with the cache
    :vartype linked_servers: list[~azure.mgmt.redis.models.RedisLinkedServer]
    :param zones: A list of availability zones denoting where the resource
     needs to come from.
    :type zones: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'subnet_id': {'pattern': r'^/subscriptions/[^/]*/resourceGroups/[^/]*/providers/Microsoft.(ClassicNetwork|Network)/virtualNetworks/[^/]*/subnets/[^/]*$'},
        'static_ip': {'pattern': r'^\d+\.\d+\.\d+\.\d+$'},
        'redis_version': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'host_name': {'readonly': True},
        'port': {'readonly': True},
        'ssl_port': {'readonly': True},
        'access_keys': {'readonly': True},
        'linked_servers': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'redis_configuration': {'key': 'properties.redisConfiguration', 'type': '{str}'},
        'enable_non_ssl_port': {'key': 'properties.enableNonSslPort', 'type': 'bool'},
        'tenant_settings': {'key': 'properties.tenantSettings', 'type': '{str}'},
        'shard_count': {'key': 'properties.shardCount', 'type': 'int'},
        'minimum_tls_version': {'key': 'properties.minimumTlsVersion', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'subnet_id': {'key': 'properties.subnetId', 'type': 'str'},
        'static_ip': {'key': 'properties.staticIP', 'type': 'str'},
        'redis_version': {'key': 'properties.redisVersion', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'ssl_port': {'key': 'properties.sslPort', 'type': 'int'},
        'access_keys': {'key': 'properties.accessKeys', 'type': 'RedisAccessKeys'},
        'linked_servers': {'key': 'properties.linkedServers', 'type': '[RedisLinkedServer]'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(self, *, location: str, sku, tags=None, redis_configuration=None, enable_non_ssl_port: bool=None, tenant_settings=None, shard_count: int=None, minimum_tls_version=None, subnet_id: str=None, static_ip: str=None, zones=None, **kwargs) -> None:
        super(RedisResource, self).__init__(tags=tags, location=location, **kwargs)
        self.redis_configuration = redis_configuration
        self.enable_non_ssl_port = enable_non_ssl_port
        self.tenant_settings = tenant_settings
        self.shard_count = shard_count
        self.minimum_tls_version = minimum_tls_version
        self.sku = sku
        self.subnet_id = subnet_id
        self.static_ip = static_ip
        self.redis_version = None
        self.provisioning_state = None
        self.host_name = None
        self.port = None
        self.ssl_port = None
        self.access_keys = None
        self.linked_servers = None
        self.zones = zones