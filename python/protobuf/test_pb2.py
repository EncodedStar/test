# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='msgType',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\x12\x07msgType\",\n\x0cProtoTestSub\x12\r\n\x05test1\x18\x01 \x01(\x05\x12\r\n\x05test2\x18\x02 \x01(\t\"\xa6\x01\n\tProtoTest\x12\x12\n\nint32_test\x18\x01 \x01(\x05\x12\x10\n\x08str_test\x18\x02 \x01(\t\x12\x10\n\x08\x64ou_test\x18\x03 \x03(\x01\x12\'\n\x08sub_test\x18\x04 \x03(\x0b\x32\x15.msgType.ProtoTestSub\x12$\n\teunm_test\x18\x05 \x01(\x0e\x32\x11.msgType.EnumTest\x12\x12\n\nbytes_test\x18\x06 \x01(\x0c*6\n\x08\x45numTest\x12\t\n\x05TEST0\x10\x00\x12\t\n\x05TEST1\x10\x01\x12\t\n\x05TEST2\x10\x02\x12\t\n\x05TEST3\x10\x03\x62\x06proto3')
)

_ENUMTEST = _descriptor.EnumDescriptor(
  name='EnumTest',
  full_name='msgType.EnumTest',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEST0', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST3', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=238,
  serialized_end=292,
)
_sym_db.RegisterEnumDescriptor(_ENUMTEST)

EnumTest = enum_type_wrapper.EnumTypeWrapper(_ENUMTEST)
TEST0 = 0
TEST1 = 1
TEST2 = 2
TEST3 = 3



_PROTOTESTSUB = _descriptor.Descriptor(
  name='ProtoTestSub',
  full_name='msgType.ProtoTestSub',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test1', full_name='msgType.ProtoTestSub.test1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test2', full_name='msgType.ProtoTestSub.test2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=23,
  serialized_end=67,
)


_PROTOTEST = _descriptor.Descriptor(
  name='ProtoTest',
  full_name='msgType.ProtoTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int32_test', full_name='msgType.ProtoTest.int32_test', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_test', full_name='msgType.ProtoTest.str_test', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dou_test', full_name='msgType.ProtoTest.dou_test', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_test', full_name='msgType.ProtoTest.sub_test', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eunm_test', full_name='msgType.ProtoTest.eunm_test', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_test', full_name='msgType.ProtoTest.bytes_test', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=70,
  serialized_end=236,
)

_PROTOTEST.fields_by_name['sub_test'].message_type = _PROTOTESTSUB
_PROTOTEST.fields_by_name['eunm_test'].enum_type = _ENUMTEST
DESCRIPTOR.message_types_by_name['ProtoTestSub'] = _PROTOTESTSUB
DESCRIPTOR.message_types_by_name['ProtoTest'] = _PROTOTEST
DESCRIPTOR.enum_types_by_name['EnumTest'] = _ENUMTEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoTestSub = _reflection.GeneratedProtocolMessageType('ProtoTestSub', (_message.Message,), {
  'DESCRIPTOR' : _PROTOTESTSUB,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:msgType.ProtoTestSub)
  })
_sym_db.RegisterMessage(ProtoTestSub)

ProtoTest = _reflection.GeneratedProtocolMessageType('ProtoTest', (_message.Message,), {
  'DESCRIPTOR' : _PROTOTEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:msgType.ProtoTest)
  })
_sym_db.RegisterMessage(ProtoTest)


# @@protoc_insertion_point(module_scope)