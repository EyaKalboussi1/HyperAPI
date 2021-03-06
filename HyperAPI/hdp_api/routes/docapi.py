from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class DocApi(Resource):
    name = "DocApi"
    available_since = "1.0"
    removed_since = None

    class _docApi(Route):
        name = "docApi"
        httpMethod = Route.GET
        path = "/doc"

    class _docApihypercubeApi(Route):
        name = "docApihypercubeApi"
        httpMethod = Route.GET
        path = "/doc/hypercubeApi.json"

    class _docApiProcessReq(Route):
        name = "docApiProcessReq"
        httpMethod = Route.POST
        path = "/doc/processReq"
