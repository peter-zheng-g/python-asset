# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset_v1p5beta1/proto/assets.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.orgpolicy.v1 import (
    orgpolicy_pb2 as google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2,
)
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.identity.accesscontextmanager.v1 import (
    access_level_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2,
)
from google.identity.accesscontextmanager.v1 import (
    access_policy_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2,
)
from google.identity.accesscontextmanager.v1 import (
    service_perimeter_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2,
)
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/asset_v1p5beta1/proto/assets.proto",
    package="google.cloud.asset.v1p5beta1",
    syntax="proto3",
    serialized_options=b"\n com.google.cloud.asset.v1p5beta1B\nAssetProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p5beta1;asset\370\001\001\252\002\034Google.Cloud.Asset.V1p5Beta1\312\002\034Google\\Cloud\\Asset\\V1p5beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/google/cloud/asset_v1p5beta1/proto/assets.proto\x12\x1cgoogle.cloud.asset.v1p5beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/orgpolicy/v1/orgpolicy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a:google/identity/accesscontextmanager/v1/access_level.proto\x1a;google/identity/accesscontextmanager/v1/access_policy.proto\x1a?google/identity/accesscontextmanager/v1/service_perimeter.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x90\x04\n\x05\x41sset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x38\n\x08resource\x18\x03 \x01(\x0b\x32&.google.cloud.asset.v1p5beta1.Resource\x12)\n\niam_policy\x18\x04 \x01(\x0b\x32\x15.google.iam.v1.Policy\x12\x35\n\norg_policy\x18\x06 \x03(\x0b\x32!.google.cloud.orgpolicy.v1.Policy\x12N\n\raccess_policy\x18\x07 \x01(\x0b\x32\x35.google.identity.accesscontextmanager.v1.AccessPolicyH\x00\x12L\n\x0c\x61\x63\x63\x65ss_level\x18\x08 \x01(\x0b\x32\x34.google.identity.accesscontextmanager.v1.AccessLevelH\x00\x12V\n\x11service_perimeter\x18\t \x01(\x0b\x32\x39.google.identity.accesscontextmanager.v1.ServicePerimeterH\x00\x12\x11\n\tancestors\x18\n \x03(\t:\'\xea\x41$\n\x1f\x63loudasset.googleapis.com/Asset\x12\x01*B\x17\n\x15\x61\x63\x63\x65ss_context_policy"\xa0\x01\n\x08Resource\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1e\n\x16\x64iscovery_document_uri\x18\x02 \x01(\t\x12\x16\n\x0e\x64iscovery_name\x18\x03 \x01(\t\x12\x14\n\x0cresource_url\x18\x04 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12%\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\xb4\x01\n com.google.cloud.asset.v1p5beta1B\nAssetProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p5beta1;asset\xf8\x01\x01\xaa\x02\x1cGoogle.Cloud.Asset.V1p5Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p5beta1b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2.DESCRIPTOR,
        google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,
        google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2.DESCRIPTOR,
        google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2.DESCRIPTOR,
        google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_ASSET = _descriptor.Descriptor(
    name="Asset",
    full_name="google.cloud.asset.v1p5beta1.Asset",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.asset.v1p5beta1.Asset.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="asset_type",
            full_name="google.cloud.asset.v1p5beta1.Asset.asset_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resource",
            full_name="google.cloud.asset.v1p5beta1.Asset.resource",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="iam_policy",
            full_name="google.cloud.asset.v1p5beta1.Asset.iam_policy",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="org_policy",
            full_name="google.cloud.asset.v1p5beta1.Asset.org_policy",
            index=4,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="access_policy",
            full_name="google.cloud.asset.v1p5beta1.Asset.access_policy",
            index=5,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="access_level",
            full_name="google.cloud.asset.v1p5beta1.Asset.access_level",
            index=6,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="service_perimeter",
            full_name="google.cloud.asset.v1p5beta1.Asset.service_perimeter",
            index=7,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ancestors",
            full_name="google.cloud.asset.v1p5beta1.Asset.ancestors",
            index=8,
            number=10,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\352A$\n\037cloudasset.googleapis.com/Asset\022\001*",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="access_context_policy",
            full_name="google.cloud.asset.v1p5beta1.Asset.access_context_policy",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=486,
    serialized_end=1014,
)


_RESOURCE = _descriptor.Descriptor(
    name="Resource",
    full_name="google.cloud.asset.v1p5beta1.Resource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="version",
            full_name="google.cloud.asset.v1p5beta1.Resource.version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="discovery_document_uri",
            full_name="google.cloud.asset.v1p5beta1.Resource.discovery_document_uri",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="discovery_name",
            full_name="google.cloud.asset.v1p5beta1.Resource.discovery_name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resource_url",
            full_name="google.cloud.asset.v1p5beta1.Resource.resource_url",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.asset.v1p5beta1.Resource.parent",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="google.cloud.asset.v1p5beta1.Resource.data",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1017,
    serialized_end=1177,
)

_ASSET.fields_by_name["resource"].message_type = _RESOURCE
_ASSET.fields_by_name[
    "iam_policy"
].message_type = (
    google_dot_iam_dot_v1_dot_policy__pb2.google_dot_iam_dot_v1_dot_policy__pb2._POLICY
)
_ASSET.fields_by_name[
    "org_policy"
].message_type = google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2._POLICY
_ASSET.fields_by_name[
    "access_policy"
].message_type = (
    google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2._ACCESSPOLICY
)
_ASSET.fields_by_name[
    "access_level"
].message_type = (
    google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2._ACCESSLEVEL
)
_ASSET.fields_by_name[
    "service_perimeter"
].message_type = (
    google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2._SERVICEPERIMETER
)
_ASSET.oneofs_by_name["access_context_policy"].fields.append(
    _ASSET.fields_by_name["access_policy"]
)
_ASSET.fields_by_name["access_policy"].containing_oneof = _ASSET.oneofs_by_name[
    "access_context_policy"
]
_ASSET.oneofs_by_name["access_context_policy"].fields.append(
    _ASSET.fields_by_name["access_level"]
)
_ASSET.fields_by_name["access_level"].containing_oneof = _ASSET.oneofs_by_name[
    "access_context_policy"
]
_ASSET.oneofs_by_name["access_context_policy"].fields.append(
    _ASSET.fields_by_name["service_perimeter"]
)
_ASSET.fields_by_name["service_perimeter"].containing_oneof = _ASSET.oneofs_by_name[
    "access_context_policy"
]
_RESOURCE.fields_by_name[
    "data"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name["Asset"] = _ASSET
DESCRIPTOR.message_types_by_name["Resource"] = _RESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType(
    "Asset",
    (_message.Message,),
    {
        "DESCRIPTOR": _ASSET,
        "__module__": "google.cloud.asset_v1p5beta1.proto.assets_pb2",
        "__doc__": """Cloud asset. This includes all Google Cloud Platform resources, Cloud
  IAM policies, and other non-GCP assets.
  
  Attributes:
      name:

          The full name of the asset. For example:
          ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
          See https://cloud.google.com/apis/design/resource_names#full_resource_name
          for more information.
      asset_type:
          Type of the asset. Example: “compute.googleapis.com/Disk”.
      resource:
          Representation of the resource.
      iam_policy:
          Representation of the actual Cloud IAM policy set on a cloud
          resource. For each resource, there must be at most one Cloud
          IAM policy set on it.
      org_policy:
          Representation of the Cloud Organization Policy set on an
          asset. For each asset, there could be multiple Organization
          policies with different constraints.
      access_context_policy:
          Representation of the Cloud Organization access policy.
      ancestors:
          Asset’s ancestry path in Cloud Resource Manager (CRM)
          hierarchy, represented as a list of relative resource names.
          Ancestry path starts with the closest CRM ancestor and ends at
          root. If the asset is a CRM project/folder/organization, this
          starts from the asset itself.  Example: [“projects/123456789”,
          “folders/5432”, “organizations/1234”]
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p5beta1.Asset)
    },
)
_sym_db.RegisterMessage(Asset)

Resource = _reflection.GeneratedProtocolMessageType(
    "Resource",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCE,
        "__module__": "google.cloud.asset_v1p5beta1.proto.assets_pb2",
        "__doc__": """Representation of a cloud resource.
  
  Attributes:
      version:
          The API version. Example: “v1”.
      discovery_document_uri:
          The URL of the discovery document containing the resource’s
          JSON schema. For example: ``"https://www.googleapis.com/discov
          ery/v1/apis/compute/v1/rest"``. It will be left unspecified
          for resources without a discovery-based API, such as Cloud
          Bigtable.
      discovery_name:
          The JSON schema name listed in the discovery document.
          Example: “Project”. It will be left unspecified for resources
          (such as Cloud Bigtable) without a discovery-based API.
      resource_url:
          The REST URL for accessing the resource. An HTTP GET operation
          using this URL returns the resource itself. Example:
          ``https://cloudresourcemanager.googleapis.com/v1/projects/my-
          project-123``. It will be left unspecified for resources
          without a REST API.
      parent:
          The full name of the immediate parent of this resource. See
          `Resource Names <https://cloud.google.com/apis/design/resource
          _names#full_resource_name>`__ for more information.  For GCP
          assets, it is the parent resource defined in the `Cloud IAM
          policy hierarchy <https://cloud.google.com/iam/docs/overview#p
          olicy_hierarchy>`__. For example: ``"//cloudresourcemanager.go
          ogleapis.com/projects/my_project_123"``.  For third-party
          assets, it is up to the users to define.
      data:
          The content of the resource, in which some sensitive fields
          are scrubbed away and may not be present.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p5beta1.Resource)
    },
)
_sym_db.RegisterMessage(Resource)


DESCRIPTOR._options = None
_ASSET._options = None
# @@protoc_insertion_point(module_scope)