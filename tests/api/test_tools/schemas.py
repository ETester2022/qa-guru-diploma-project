schema_post_tools = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        }
    },
    "required": [
        "name"
    ]
}

schema_get_tool_name = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "toolSettings": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "enabled": {
                    "type": "boolean"
                },
                "type": {
                    "type": "string"
                },
                "dataTransfer": {
                    "type": "string"
                },
                "ioformCols": {
                    "type": "integer"
                },
                "ioformWidth": {
                    "type": "integer"
                },
                "exportCsv": {
                    "type": "boolean"
                },
                "exportJson": {
                    "type": "boolean"
                },
                "exportPdf": {
                    "type": "boolean"
                },
                "exportXlsx": {
                    "type": "boolean"
                },
                "importCsv": {
                    "type": "boolean"
                },
                "importJson": {
                    "type": "boolean"
                },
                "frozenTopEnabled": {
                    "type": "boolean"
                },
                "frozenBottomEnabled": {
                    "type": "boolean"
                },
                "frozenLeftEnabled": {
                    "type": "boolean"
                },
                "frozenRightEnabled": {
                    "type": "boolean"
                },
                "fontSize": {
                    "type": "integer"
                },
                "rowHeight": {
                    "type": "integer"
                },
                "fitToWidth": {
                    "type": "boolean"
                },
                "paginationEnabled": {
                    "type": "boolean"
                },
                "range": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "mode": {
                            "type": "string"
                        },
                        "enabled": {
                            "type": "boolean"
                        },
                        "visible": {
                            "type": "boolean"
                        },
                        "useGlobalValue": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "id",
                        "mode",
                        "enabled",
                        "visible",
                        "useGlobalValue"
                    ]
                },
                "updater": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "enabled": {
                            "type": "boolean"
                        },
                        "visible": {
                            "type": "boolean"
                        },
                        "useGlobalValue": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "id",
                        "enabled",
                        "visible",
                        "useGlobalValue"
                    ]
                },
                "label": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id"
                    ]
                },
                "permissions": {
                    "type": "object",
                    "properties": {
                        "users": {
                            "type": "array",
                            "items": {}
                        },
                        "groups": {
                            "type": "array",
                            "items": {}
                        }
                    },
                    "required": [
                        "users",
                        "groups"
                    ]
                }
            },
            "required": [
                "name",
                "enabled",
                "type",
                "dataTransfer",
                "ioformCols",
                "ioformWidth",
                "exportCsv",
                "exportJson",
                "exportPdf",
                "exportXlsx",
                "importCsv",
                "importJson",
                "frozenTopEnabled",
                "frozenBottomEnabled",
                "frozenLeftEnabled",
                "frozenRightEnabled",
                "fontSize",
                "rowHeight",
                "fitToWidth",
                "paginationEnabled",
                "range",
                "updater",
                "label",
                "permissions"
            ]
        }
    },
    "required": [
        "toolSettings"
    ]
}
