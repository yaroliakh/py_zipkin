# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zipkin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0czipkin.proto\x12\rzipkin.proto3"\xf5\x03\n\x04Span\x12\x10\n\x08trace_id\x18\x01 \x01(\x0c\x12\x11\n\tparent_id\x18\x02 \x01(\x0c\x12\n\n\x02id\x18\x03 \x01(\x0c\x12&\n\x04kind\x18\x04 \x01(\x0e\x32\x18.zipkin.proto3.Span.Kind\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x06\x12\x10\n\x08\x64uration\x18\x07 \x01(\x04\x12/\n\x0elocal_endpoint\x18\x08 \x01(\x0b\x32\x17.zipkin.proto3.Endpoint\x12\x30\n\x0fremote_endpoint\x18\t \x01(\x0b\x32\x17.zipkin.proto3.Endpoint\x12.\n\x0b\x61nnotations\x18\n \x03(\x0b\x32\x19.zipkin.proto3.Annotation\x12+\n\x04tags\x18\x0b \x03(\x0b\x32\x1d.zipkin.proto3.Span.TagsEntry\x12\r\n\x05\x64\x65\x62ug\x18\x0c \x01(\x08\x12\x0e\n\x06shared\x18\r \x01(\x08\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"U\n\x04Kind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\n\n\x06\x43LIENT\x10\x01\x12\n\n\x06SERVER\x10\x02\x12\x0c\n\x08PRODUCER\x10\x03\x12\x0c\n\x08\x43ONSUMER\x10\x04"J\n\x08\x45ndpoint\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0c\n\x04ipv4\x18\x02 \x01(\x0c\x12\x0c\n\x04ipv6\x18\x03 \x01(\x0c\x12\x0c\n\x04port\x18\x04 \x01(\x05".\n\nAnnotation\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\t"1\n\x0bListOfSpans\x12"\n\x05spans\x18\x01 \x03(\x0b\x32\x13.zipkin.proto3.Span"\x10\n\x0eReportResponse2T\n\x0bSpanService\x12\x45\n\x06Report\x12\x1a.zipkin.proto3.ListOfSpans\x1a\x1d.zipkin.proto3.ReportResponse"\x00\x42\x12\n\x0ezipkin2.proto3P\x01\x62\x06proto3'
)


_SPAN = DESCRIPTOR.message_types_by_name["Span"]
_SPAN_TAGSENTRY = _SPAN.nested_types_by_name["TagsEntry"]
_ENDPOINT = DESCRIPTOR.message_types_by_name["Endpoint"]
_ANNOTATION = DESCRIPTOR.message_types_by_name["Annotation"]
_LISTOFSPANS = DESCRIPTOR.message_types_by_name["ListOfSpans"]
_REPORTRESPONSE = DESCRIPTOR.message_types_by_name["ReportResponse"]
_SPAN_KIND = _SPAN.enum_types_by_name["Kind"]
Span = _reflection.GeneratedProtocolMessageType(
    "Span",
    (_message.Message,),
    {
        "TagsEntry": _reflection.GeneratedProtocolMessageType(
            "TagsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SPAN_TAGSENTRY,
                "__module__": "zipkin_pb2"
                # @@protoc_insertion_point(class_scope:zipkin.proto3.Span.TagsEntry)
            },
        ),
        "DESCRIPTOR": _SPAN,
        "__module__": "zipkin_pb2"
        # @@protoc_insertion_point(class_scope:zipkin.proto3.Span)
    },
)
_sym_db.RegisterMessage(Span)
_sym_db.RegisterMessage(Span.TagsEntry)

Endpoint = _reflection.GeneratedProtocolMessageType(
    "Endpoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINT,
        "__module__": "zipkin_pb2"
        # @@protoc_insertion_point(class_scope:zipkin.proto3.Endpoint)
    },
)
_sym_db.RegisterMessage(Endpoint)

Annotation = _reflection.GeneratedProtocolMessageType(
    "Annotation",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANNOTATION,
        "__module__": "zipkin_pb2"
        # @@protoc_insertion_point(class_scope:zipkin.proto3.Annotation)
    },
)
_sym_db.RegisterMessage(Annotation)

ListOfSpans = _reflection.GeneratedProtocolMessageType(
    "ListOfSpans",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTOFSPANS,
        "__module__": "zipkin_pb2"
        # @@protoc_insertion_point(class_scope:zipkin.proto3.ListOfSpans)
    },
)
_sym_db.RegisterMessage(ListOfSpans)

ReportResponse = _reflection.GeneratedProtocolMessageType(
    "ReportResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPORTRESPONSE,
        "__module__": "zipkin_pb2"
        # @@protoc_insertion_point(class_scope:zipkin.proto3.ReportResponse)
    },
)
_sym_db.RegisterMessage(ReportResponse)

_SPANSERVICE = DESCRIPTOR.services_by_name["SpanService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016zipkin2.proto3P\001"
    _SPAN_TAGSENTRY._options = None
    _SPAN_TAGSENTRY._serialized_options = b"8\001"
    _SPAN._serialized_start = 32
    _SPAN._serialized_end = 533
    _SPAN_TAGSENTRY._serialized_start = 403
    _SPAN_TAGSENTRY._serialized_end = 446
    _SPAN_KIND._serialized_start = 448
    _SPAN_KIND._serialized_end = 533
    _ENDPOINT._serialized_start = 535
    _ENDPOINT._serialized_end = 609
    _ANNOTATION._serialized_start = 611
    _ANNOTATION._serialized_end = 657
    _LISTOFSPANS._serialized_start = 659
    _LISTOFSPANS._serialized_end = 708
    _REPORTRESPONSE._serialized_start = 710
    _REPORTRESPONSE._serialized_end = 726
    _SPANSERVICE._serialized_start = 728
    _SPANSERVICE._serialized_end = 812
# @@protoc_insertion_point(module_scope)
