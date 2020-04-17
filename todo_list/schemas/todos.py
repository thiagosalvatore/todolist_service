from marshmallow import Schema, fields
from marshmallow.validate import Length


class TODOBaseSchema(Schema):
    title = fields.String(required=True, validate=Length(max=50))
    description = fields.String(required=True, validate=Length(max=200))
    due_date = fields.DateTime(format="%Y-%m-%d %H:%M", required=True)


class TODODetailSchema(TODOBaseSchema):
    _id = fields.String(required=True)
