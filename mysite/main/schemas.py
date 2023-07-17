import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class CrossListFilterSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="color",
                    required=False,
                    location="query",
                    schema=coreschema.String(description="color of crosses for filter"),
                )
            ]
        return self._manual_fields + api_fields