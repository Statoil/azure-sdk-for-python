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


class ImageDescription(Model):
    """A collection of content tags, along with a list of captions sorted by
    confidence level, and image metadata.

    :param tags: A collection of image tags.
    :type tags: list[str]
    :param captions: A list of captions, sorted by confidence level.
    :type captions:
     list[~azure.cognitiveservices.vision.computervision.models.ImageCaption]
    :param request_id: Id of the REST API request.
    :type request_id: str
    :param metadata:
    :type metadata:
     ~azure.cognitiveservices.vision.computervision.models.ImageMetadata
    """

    _attribute_map = {
        'tags': {'key': 'description.tags', 'type': '[str]'},
        'captions': {'key': 'description.captions', 'type': '[ImageCaption]'},
        'request_id': {'key': 'description.requestId', 'type': 'str'},
        'metadata': {'key': 'description.metadata', 'type': 'ImageMetadata'},
    }

    def __init__(self, *, tags=None, captions=None, request_id: str=None, metadata=None, **kwargs) -> None:
        super(ImageDescription, self).__init__(**kwargs)
        self.tags = tags
        self.captions = captions
        self.request_id = request_id
        self.metadata = metadata
