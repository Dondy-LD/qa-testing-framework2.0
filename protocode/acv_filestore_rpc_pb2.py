# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acv_filestore_rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protocode import acv_common_message_pb2 as acv__common__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='acv_filestore_rpc.proto',
  package='acv.proto.acv',
  syntax='proto3',
  serialized_options=b'\n\031com.ncs.vit.vca.proto.acvB\022ACVFileStoreProtos',
  serialized_pb=b'\n\x17\x61\x63v_filestore_rpc.proto\x12\racv.proto.acv\x1a\x18\x61\x63v_common_message.proto\"!\n\x13\x41\x64\x64\x46ileStoreRequest\x12\n\n\x02id\x18\x01 \x01(\t\"@\n\x14\x41\x64\x64\x46ileStoreResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\"$\n\x16RemoveFileStoreRequest\x12\n\n\x02id\x18\x01 \x01(\t\"C\n\x17RemoveFileStoreResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\"\x17\n\x15ListFileStoresRequest\"N\n\x16ListFileStoresResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\x12\n\n\x02id\x18\x02 \x03(\t\"8\n\x1cPutFileStoreDirectoryRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"I\n\x1dPutFileStoreDirectoryResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\"L\n\x1dPutFileStoreFileRequestHeader\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x11\n\tfile_size\x18\x03 \x01(\x04\"z\n\x17PutFileStoreFileRequest\x12>\n\x06header\x18\x01 \x01(\x0b\x32,.acv.proto.acv.PutFileStoreFileRequestHeaderH\x00\x12\x17\n\rfile_fragment\x18\x02 \x01(\x0cH\x00\x42\x06\n\x04type\"D\n\x18PutFileStoreFileResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\"6\n\x1aRemoveFileStorePathRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"G\n\x1bRemoveFileStorePathResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\"3\n\x17GetFileStoreFileRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"]\n\x1eGetFileStoreFileResponseHeader\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\x12\x11\n\tfile_size\x18\x02 \x01(\x04\"|\n\x18GetFileStoreFileResponse\x12?\n\x06header\x18\x01 \x01(\x0b\x32-.acv.proto.acv.GetFileStoreFileResponseHeaderH\x00\x12\x17\n\rfile_fragment\x18\x02 \x01(\x0cH\x00\x42\x06\n\x04type\"H\n\x19ListFileStorePathsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x11\n\trecursive\x18\x03 \x01(\x08\"v\n\x1aListFileStorePathsResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.acv.proto.acv.ACVResult\x12.\n\x04info\x18\x02 \x03(\x0b\x32 .acv.proto.acv.FileStorePathInfo2\xc3\x06\n\x0c\x41\x43VFileStore\x12W\n\x0c\x41\x64\x64\x46ileStore\x12\".acv.proto.acv.AddFileStoreRequest\x1a#.acv.proto.acv.AddFileStoreResponse\x12`\n\x0fRemoveFileStore\x12%.acv.proto.acv.RemoveFileStoreRequest\x1a&.acv.proto.acv.RemoveFileStoreResponse\x12]\n\x0eListFileStores\x12$.acv.proto.acv.ListFileStoresRequest\x1a%.acv.proto.acv.ListFileStoresResponse\x12r\n\x15PutFileStoreDirectory\x12+.acv.proto.acv.PutFileStoreDirectoryRequest\x1a,.acv.proto.acv.PutFileStoreDirectoryResponse\x12\x65\n\x10PutFileStoreFile\x12&.acv.proto.acv.PutFileStoreFileRequest\x1a\'.acv.proto.acv.PutFileStoreFileResponse(\x01\x12\x65\n\x10GetFileStoreFile\x12&.acv.proto.acv.GetFileStoreFileRequest\x1a\'.acv.proto.acv.GetFileStoreFileResponse0\x01\x12l\n\x13RemoveFileStorePath\x12).acv.proto.acv.RemoveFileStorePathRequest\x1a*.acv.proto.acv.RemoveFileStorePathResponse\x12i\n\x12ListFileStorePaths\x12(.acv.proto.acv.ListFileStorePathsRequest\x1a).acv.proto.acv.ListFileStorePathsResponseB/\n\x19\x63om.ncs.vit.vca.proto.acvB\x12\x41\x43VFileStoreProtosb\x06proto3'
  ,
  dependencies=[acv__common__message__pb2.DESCRIPTOR,])




_ADDFILESTOREREQUEST = _descriptor.Descriptor(
  name='AddFileStoreRequest',
  full_name='acv.proto.acv.AddFileStoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.AddFileStoreRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=101,
)


_ADDFILESTORERESPONSE = _descriptor.Descriptor(
  name='AddFileStoreResponse',
  full_name='acv.proto.acv.AddFileStoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.AddFileStoreResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=167,
)


_REMOVEFILESTOREREQUEST = _descriptor.Descriptor(
  name='RemoveFileStoreRequest',
  full_name='acv.proto.acv.RemoveFileStoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.RemoveFileStoreRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=205,
)


_REMOVEFILESTORERESPONSE = _descriptor.Descriptor(
  name='RemoveFileStoreResponse',
  full_name='acv.proto.acv.RemoveFileStoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.RemoveFileStoreResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=274,
)


_LISTFILESTORESREQUEST = _descriptor.Descriptor(
  name='ListFileStoresRequest',
  full_name='acv.proto.acv.ListFileStoresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=299,
)


_LISTFILESTORESRESPONSE = _descriptor.Descriptor(
  name='ListFileStoresResponse',
  full_name='acv.proto.acv.ListFileStoresResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.ListFileStoresResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.ListFileStoresResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=379,
)


_PUTFILESTOREDIRECTORYREQUEST = _descriptor.Descriptor(
  name='PutFileStoreDirectoryRequest',
  full_name='acv.proto.acv.PutFileStoreDirectoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.PutFileStoreDirectoryRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='acv.proto.acv.PutFileStoreDirectoryRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=381,
  serialized_end=437,
)


_PUTFILESTOREDIRECTORYRESPONSE = _descriptor.Descriptor(
  name='PutFileStoreDirectoryResponse',
  full_name='acv.proto.acv.PutFileStoreDirectoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.PutFileStoreDirectoryResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=512,
)


_PUTFILESTOREFILEREQUESTHEADER = _descriptor.Descriptor(
  name='PutFileStoreFileRequestHeader',
  full_name='acv.proto.acv.PutFileStoreFileRequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.PutFileStoreFileRequestHeader.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='acv.proto.acv.PutFileStoreFileRequestHeader.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='acv.proto.acv.PutFileStoreFileRequestHeader.file_size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=590,
)


_PUTFILESTOREFILEREQUEST = _descriptor.Descriptor(
  name='PutFileStoreFileRequest',
  full_name='acv.proto.acv.PutFileStoreFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='acv.proto.acv.PutFileStoreFileRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_fragment', full_name='acv.proto.acv.PutFileStoreFileRequest.file_fragment', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='acv.proto.acv.PutFileStoreFileRequest.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=592,
  serialized_end=714,
)


_PUTFILESTOREFILERESPONSE = _descriptor.Descriptor(
  name='PutFileStoreFileResponse',
  full_name='acv.proto.acv.PutFileStoreFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.PutFileStoreFileResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=784,
)


_REMOVEFILESTOREPATHREQUEST = _descriptor.Descriptor(
  name='RemoveFileStorePathRequest',
  full_name='acv.proto.acv.RemoveFileStorePathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.RemoveFileStorePathRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='acv.proto.acv.RemoveFileStorePathRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=786,
  serialized_end=840,
)


_REMOVEFILESTOREPATHRESPONSE = _descriptor.Descriptor(
  name='RemoveFileStorePathResponse',
  full_name='acv.proto.acv.RemoveFileStorePathResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.RemoveFileStorePathResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=913,
)


_GETFILESTOREFILEREQUEST = _descriptor.Descriptor(
  name='GetFileStoreFileRequest',
  full_name='acv.proto.acv.GetFileStoreFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.GetFileStoreFileRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='acv.proto.acv.GetFileStoreFileRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=966,
)


_GETFILESTOREFILERESPONSEHEADER = _descriptor.Descriptor(
  name='GetFileStoreFileResponseHeader',
  full_name='acv.proto.acv.GetFileStoreFileResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.GetFileStoreFileResponseHeader.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='acv.proto.acv.GetFileStoreFileResponseHeader.file_size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1061,
)


_GETFILESTOREFILERESPONSE = _descriptor.Descriptor(
  name='GetFileStoreFileResponse',
  full_name='acv.proto.acv.GetFileStoreFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='acv.proto.acv.GetFileStoreFileResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_fragment', full_name='acv.proto.acv.GetFileStoreFileResponse.file_fragment', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='acv.proto.acv.GetFileStoreFileResponse.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1063,
  serialized_end=1187,
)


_LISTFILESTOREPATHSREQUEST = _descriptor.Descriptor(
  name='ListFileStorePathsRequest',
  full_name='acv.proto.acv.ListFileStorePathsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='acv.proto.acv.ListFileStorePathsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='acv.proto.acv.ListFileStorePathsRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recursive', full_name='acv.proto.acv.ListFileStorePathsRequest.recursive', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1189,
  serialized_end=1261,
)


_LISTFILESTOREPATHSRESPONSE = _descriptor.Descriptor(
  name='ListFileStorePathsResponse',
  full_name='acv.proto.acv.ListFileStorePathsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='acv.proto.acv.ListFileStorePathsResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='acv.proto.acv.ListFileStorePathsResponse.info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1263,
  serialized_end=1381,
)

_ADDFILESTORERESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_REMOVEFILESTORERESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_LISTFILESTORESRESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_PUTFILESTOREDIRECTORYRESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_PUTFILESTOREFILEREQUEST.fields_by_name['header'].message_type = _PUTFILESTOREFILEREQUESTHEADER
_PUTFILESTOREFILEREQUEST.oneofs_by_name['type'].fields.append(
  _PUTFILESTOREFILEREQUEST.fields_by_name['header'])
_PUTFILESTOREFILEREQUEST.fields_by_name['header'].containing_oneof = _PUTFILESTOREFILEREQUEST.oneofs_by_name['type']
_PUTFILESTOREFILEREQUEST.oneofs_by_name['type'].fields.append(
  _PUTFILESTOREFILEREQUEST.fields_by_name['file_fragment'])
_PUTFILESTOREFILEREQUEST.fields_by_name['file_fragment'].containing_oneof = _PUTFILESTOREFILEREQUEST.oneofs_by_name['type']
_PUTFILESTOREFILERESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_REMOVEFILESTOREPATHRESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_GETFILESTOREFILERESPONSEHEADER.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_GETFILESTOREFILERESPONSE.fields_by_name['header'].message_type = _GETFILESTOREFILERESPONSEHEADER
_GETFILESTOREFILERESPONSE.oneofs_by_name['type'].fields.append(
  _GETFILESTOREFILERESPONSE.fields_by_name['header'])
_GETFILESTOREFILERESPONSE.fields_by_name['header'].containing_oneof = _GETFILESTOREFILERESPONSE.oneofs_by_name['type']
_GETFILESTOREFILERESPONSE.oneofs_by_name['type'].fields.append(
  _GETFILESTOREFILERESPONSE.fields_by_name['file_fragment'])
_GETFILESTOREFILERESPONSE.fields_by_name['file_fragment'].containing_oneof = _GETFILESTOREFILERESPONSE.oneofs_by_name['type']
_LISTFILESTOREPATHSRESPONSE.fields_by_name['result'].message_type = acv__common__message__pb2._ACVRESULT
_LISTFILESTOREPATHSRESPONSE.fields_by_name['info'].message_type = acv__common__message__pb2._FILESTOREPATHINFO
DESCRIPTOR.message_types_by_name['AddFileStoreRequest'] = _ADDFILESTOREREQUEST
DESCRIPTOR.message_types_by_name['AddFileStoreResponse'] = _ADDFILESTORERESPONSE
DESCRIPTOR.message_types_by_name['RemoveFileStoreRequest'] = _REMOVEFILESTOREREQUEST
DESCRIPTOR.message_types_by_name['RemoveFileStoreResponse'] = _REMOVEFILESTORERESPONSE
DESCRIPTOR.message_types_by_name['ListFileStoresRequest'] = _LISTFILESTORESREQUEST
DESCRIPTOR.message_types_by_name['ListFileStoresResponse'] = _LISTFILESTORESRESPONSE
DESCRIPTOR.message_types_by_name['PutFileStoreDirectoryRequest'] = _PUTFILESTOREDIRECTORYREQUEST
DESCRIPTOR.message_types_by_name['PutFileStoreDirectoryResponse'] = _PUTFILESTOREDIRECTORYRESPONSE
DESCRIPTOR.message_types_by_name['PutFileStoreFileRequestHeader'] = _PUTFILESTOREFILEREQUESTHEADER
DESCRIPTOR.message_types_by_name['PutFileStoreFileRequest'] = _PUTFILESTOREFILEREQUEST
DESCRIPTOR.message_types_by_name['PutFileStoreFileResponse'] = _PUTFILESTOREFILERESPONSE
DESCRIPTOR.message_types_by_name['RemoveFileStorePathRequest'] = _REMOVEFILESTOREPATHREQUEST
DESCRIPTOR.message_types_by_name['RemoveFileStorePathResponse'] = _REMOVEFILESTOREPATHRESPONSE
DESCRIPTOR.message_types_by_name['GetFileStoreFileRequest'] = _GETFILESTOREFILEREQUEST
DESCRIPTOR.message_types_by_name['GetFileStoreFileResponseHeader'] = _GETFILESTOREFILERESPONSEHEADER
DESCRIPTOR.message_types_by_name['GetFileStoreFileResponse'] = _GETFILESTOREFILERESPONSE
DESCRIPTOR.message_types_by_name['ListFileStorePathsRequest'] = _LISTFILESTOREPATHSREQUEST
DESCRIPTOR.message_types_by_name['ListFileStorePathsResponse'] = _LISTFILESTOREPATHSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddFileStoreRequest = _reflection.GeneratedProtocolMessageType('AddFileStoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDFILESTOREREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.AddFileStoreRequest)
  })
_sym_db.RegisterMessage(AddFileStoreRequest)

AddFileStoreResponse = _reflection.GeneratedProtocolMessageType('AddFileStoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDFILESTORERESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.AddFileStoreResponse)
  })
_sym_db.RegisterMessage(AddFileStoreResponse)

RemoveFileStoreRequest = _reflection.GeneratedProtocolMessageType('RemoveFileStoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILESTOREREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.RemoveFileStoreRequest)
  })
_sym_db.RegisterMessage(RemoveFileStoreRequest)

RemoveFileStoreResponse = _reflection.GeneratedProtocolMessageType('RemoveFileStoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILESTORERESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.RemoveFileStoreResponse)
  })
_sym_db.RegisterMessage(RemoveFileStoreResponse)

ListFileStoresRequest = _reflection.GeneratedProtocolMessageType('ListFileStoresRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESTORESREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.ListFileStoresRequest)
  })
_sym_db.RegisterMessage(ListFileStoresRequest)

ListFileStoresResponse = _reflection.GeneratedProtocolMessageType('ListFileStoresResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESTORESRESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.ListFileStoresResponse)
  })
_sym_db.RegisterMessage(ListFileStoresResponse)

PutFileStoreDirectoryRequest = _reflection.GeneratedProtocolMessageType('PutFileStoreDirectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTFILESTOREDIRECTORYREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.PutFileStoreDirectoryRequest)
  })
_sym_db.RegisterMessage(PutFileStoreDirectoryRequest)

PutFileStoreDirectoryResponse = _reflection.GeneratedProtocolMessageType('PutFileStoreDirectoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTFILESTOREDIRECTORYRESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.PutFileStoreDirectoryResponse)
  })
_sym_db.RegisterMessage(PutFileStoreDirectoryResponse)

PutFileStoreFileRequestHeader = _reflection.GeneratedProtocolMessageType('PutFileStoreFileRequestHeader', (_message.Message,), {
  'DESCRIPTOR' : _PUTFILESTOREFILEREQUESTHEADER,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.PutFileStoreFileRequestHeader)
  })
_sym_db.RegisterMessage(PutFileStoreFileRequestHeader)

PutFileStoreFileRequest = _reflection.GeneratedProtocolMessageType('PutFileStoreFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTFILESTOREFILEREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.PutFileStoreFileRequest)
  })
_sym_db.RegisterMessage(PutFileStoreFileRequest)

PutFileStoreFileResponse = _reflection.GeneratedProtocolMessageType('PutFileStoreFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTFILESTOREFILERESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.PutFileStoreFileResponse)
  })
_sym_db.RegisterMessage(PutFileStoreFileResponse)

RemoveFileStorePathRequest = _reflection.GeneratedProtocolMessageType('RemoveFileStorePathRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILESTOREPATHREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.RemoveFileStorePathRequest)
  })
_sym_db.RegisterMessage(RemoveFileStorePathRequest)

RemoveFileStorePathResponse = _reflection.GeneratedProtocolMessageType('RemoveFileStorePathResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILESTOREPATHRESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.RemoveFileStorePathResponse)
  })
_sym_db.RegisterMessage(RemoveFileStorePathResponse)

GetFileStoreFileRequest = _reflection.GeneratedProtocolMessageType('GetFileStoreFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFILESTOREFILEREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.GetFileStoreFileRequest)
  })
_sym_db.RegisterMessage(GetFileStoreFileRequest)

GetFileStoreFileResponseHeader = _reflection.GeneratedProtocolMessageType('GetFileStoreFileResponseHeader', (_message.Message,), {
  'DESCRIPTOR' : _GETFILESTOREFILERESPONSEHEADER,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.GetFileStoreFileResponseHeader)
  })
_sym_db.RegisterMessage(GetFileStoreFileResponseHeader)

GetFileStoreFileResponse = _reflection.GeneratedProtocolMessageType('GetFileStoreFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFILESTOREFILERESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.GetFileStoreFileResponse)
  })
_sym_db.RegisterMessage(GetFileStoreFileResponse)

ListFileStorePathsRequest = _reflection.GeneratedProtocolMessageType('ListFileStorePathsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESTOREPATHSREQUEST,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.ListFileStorePathsRequest)
  })
_sym_db.RegisterMessage(ListFileStorePathsRequest)

ListFileStorePathsResponse = _reflection.GeneratedProtocolMessageType('ListFileStorePathsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESTOREPATHSRESPONSE,
  '__module__' : 'acv_filestore_rpc_pb2'
  # @@protoc_insertion_point(class_scope:acv.proto.acv.ListFileStorePathsResponse)
  })
_sym_db.RegisterMessage(ListFileStorePathsResponse)


DESCRIPTOR._options = None

_ACVFILESTORE = _descriptor.ServiceDescriptor(
  name='ACVFileStore',
  full_name='acv.proto.acv.ACVFileStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1384,
  serialized_end=2219,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddFileStore',
    full_name='acv.proto.acv.ACVFileStore.AddFileStore',
    index=0,
    containing_service=None,
    input_type=_ADDFILESTOREREQUEST,
    output_type=_ADDFILESTORERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveFileStore',
    full_name='acv.proto.acv.ACVFileStore.RemoveFileStore',
    index=1,
    containing_service=None,
    input_type=_REMOVEFILESTOREREQUEST,
    output_type=_REMOVEFILESTORERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFileStores',
    full_name='acv.proto.acv.ACVFileStore.ListFileStores',
    index=2,
    containing_service=None,
    input_type=_LISTFILESTORESREQUEST,
    output_type=_LISTFILESTORESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PutFileStoreDirectory',
    full_name='acv.proto.acv.ACVFileStore.PutFileStoreDirectory',
    index=3,
    containing_service=None,
    input_type=_PUTFILESTOREDIRECTORYREQUEST,
    output_type=_PUTFILESTOREDIRECTORYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PutFileStoreFile',
    full_name='acv.proto.acv.ACVFileStore.PutFileStoreFile',
    index=4,
    containing_service=None,
    input_type=_PUTFILESTOREFILEREQUEST,
    output_type=_PUTFILESTOREFILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFileStoreFile',
    full_name='acv.proto.acv.ACVFileStore.GetFileStoreFile',
    index=5,
    containing_service=None,
    input_type=_GETFILESTOREFILEREQUEST,
    output_type=_GETFILESTOREFILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveFileStorePath',
    full_name='acv.proto.acv.ACVFileStore.RemoveFileStorePath',
    index=6,
    containing_service=None,
    input_type=_REMOVEFILESTOREPATHREQUEST,
    output_type=_REMOVEFILESTOREPATHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFileStorePaths',
    full_name='acv.proto.acv.ACVFileStore.ListFileStorePaths',
    index=7,
    containing_service=None,
    input_type=_LISTFILESTOREPATHSREQUEST,
    output_type=_LISTFILESTOREPATHSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACVFILESTORE)

DESCRIPTOR.services_by_name['ACVFileStore'] = _ACVFILESTORE

# @@protoc_insertion_point(module_scope)
