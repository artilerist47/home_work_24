from typing import Iterable

from marshmallow import fields, Schema, validates_schema, ValidationError

VALID_CMD_PARAMS: Iterable[str] = ("filter", "sort", "map", "unique", "limit", "regex")


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: dict[str, str], *args: any, **kwargs: any) -> dict[str, str]:
        if values["cmd"] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd" contains invalid value')
        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
