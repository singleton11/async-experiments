from marshmallow_sqlalchemy import ModelSchema

from .models import Project


class ProjectSchema(ModelSchema):
    """Serializer for ``Project`` model"""

    class Meta:
        model = Project
