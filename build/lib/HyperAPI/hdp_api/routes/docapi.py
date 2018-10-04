from HyperAPI.hdp_api.routes import Resource, Route


class DocApi(Resource):
    name = "DocApi"

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
