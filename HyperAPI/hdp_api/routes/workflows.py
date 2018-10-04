from HyperAPI.hdp_api.routes import Resource, Route


class Workflows(Resource):
    name = "workflows"

    class _getWorkflows(Route):
        name = "getWorkflows"
        httpMethod = Route.GET
        path = "/workflows"

    class _getWorkflow(Route):
        name = "getWorkflow"
        httpMethod = Route.GET
        path = "/workflows/{workflow_ID}"
        _path_keys = {
            'workflow_ID': Route.VALIDATOR_OBJECTID,
        }

    class _applyWorkflow(Route):
        name = "applyWorkflow"
        httpMethod = Route.POST
        path = "/workflows/apply"

    class _getWorks(Route):
        name = "getWorks"
        httpMethod = Route.GET
        path = "/workflows/works"

    class _getWork(Route):
        name = "getWork"
        httpMethod = Route.GET
        path = "/workflows/works/{work_ID}"
        _path_keys = {
            'work_ID': Route.VALIDATOR_OBJECTID,
        }
