from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Correlations(Resource):
    name = "Correlations"
    available_since = "1.0"
    removed_since = None

    # Old correlation class names for 4.3 ---------------------------------------------------------

    class _InitListofCorrelations(Route):
        name = "GetCorrelations"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _NewCorrelation(Route):
        name = "New Correlation"
        httpMethod = Route.POST
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/tasks/new"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetNewJSONfile(Route):
        name = "Get new JSON file"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetJSONfile(Route):
        name = "Get JSON file"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlation/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }


    class _GetNewCSVfile(Route):
        name = "Get new CSV file"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetCSVfile(Route):
        name = "Get CSV file"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _CreateNewCorrelation(Route):
        name = "CreateNewCorrelation"
        httpMethod = Route.POST
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _RenameNewCorrelation(Route):
        name = "RenamNewCorrelation"
        httpMethod = Route.POST
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _saveCorrelationImg(Route):
        name = "saveCorrelationImg"
        httpMethod = Route.POST
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/preview"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _retrieveCorrelationsPreview(Route):
        name = "retrieveCorrelationsPreview"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/projects/{project_ID}/correlations/previews"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    # Correaltions new naming since HDP version 3.0 -----------------------------------------------

    class _GetCorrelations(Route):
        name = "GetCorrelations"
        httpMethod = Route.GET
        available_since = "2.0"
        path = "/projects/{project_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _CreateCorrelation(Route):
        name = "CreateCorrelation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _UpdateCorrelationName(Route):
        name = "UpdateCorrelationName"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetCorrelation(Route):
        name = "GetCorrelation"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetCorrelationJson(Route):
        name = "Get JSON file"
        httpMethod = Route.GET
        removed_since = "3.0"
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlation/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetCorrelationCsv(Route):
        name = "GetCorrelationCsv"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _DeleteCorrelation(Route):
        name = "DeleteCorrelation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _UpdateCorrelationPreview(Route):
        name = "UpdateCorrelationPreview"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/preview"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }
