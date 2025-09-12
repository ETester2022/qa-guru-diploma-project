schema_get_app_settings = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "commonSettings": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "instanceLabel": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": ["string", "null"]
                        },
                        "ru": {
                            "type": ["string", "null"]
                        },
                        "en": {
                            "type": ["string", "null"]
                        },
                        "kk": {
                            "type": ["string", "null"]
                        },
                        "de": {
                            "type": ["string", "null"]
                        }
                    },
                    "required": [
                        "id"
                    ]
                },
                "instanceLabelEnabled": {
                    "type": "boolean"
                },
                "logoImage": {
                    "type": ["string", "null"]
                },
                "logoEnabled": {
                    "type": "boolean"
                },
                "logoMesoneEnabled": {
                    "type": "boolean"
                },
                "footer": {
                    "type": "boolean"
                },
                "colorScheme": {
                    "type": "string"
                },
                "style": {
                    "type": "string"
                },
                "selectedLocalesEnabled": {
                    "type": "boolean"
                },
                "selectedLocales": {
                    "type": "array",
                    "items": [
                        {
                            "type": "string"
                        }
                    ]
                },
                "defaultLocale": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "instanceLabel",
                "instanceLabelEnabled",
                "logoImage",
                "logoEnabled",
                "logoMesoneEnabled",
                "footer",
                "colorScheme",
                "style",
                "selectedLocalesEnabled",
                "selectedLocales",
                "defaultLocale"
            ]
        },
        "timeFunctions": {
            "type": "object",
            "properties": {
                "range": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "mode": {
                            "type": "string"
                        },
                        "defaultRangeLeft": {
                            "type": "string"
                        },
                        "defaultRangeRight": {
                            "type": "string"
                        },
                        "selectedPresets": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "defaultPreset": {
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
                        "defaultRangeLeft",
                        "defaultRangeRight",
                        "selectedPresets",
                        "defaultPreset",
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
                        "defaultValue": {
                            "type": ["string", "null"]
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
                }
            },
            "required": [
                "range",
                "updater"
            ]
        }
    },
    "required": [
        "commonSettings",
        "timeFunctions"
    ]
}
