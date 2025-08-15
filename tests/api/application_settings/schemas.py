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
        "instanceLabelEnabled": {
          "type": "boolean"
        },
        "logoImage": {
          "type": "string"
        },
        "logoEnabled": {
          "type": "boolean"
        },
        "logoMesoneEnabled": {
          "type": "boolean"
        },
        "colorScheme": {
          "type": "string"
        },
        "style": {
          "type": "string"
        },
        "selectedLocales": {
          "type": "array",
          "items": [
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            }
          ]
        },
        "selectedLocalesEnabled": {
          "type": "boolean"
        },
        "defaultLocale": {
          "type": "string"
        },
        "footer": {
          "type": "boolean"
        },
        "instanceLabel": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "ru": {
              "type": "string"
            },
            "en": {
              "type": "string"
            },
            "kk": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "ru",
            "en",
            "kk"
          ]
        }
      },
      "required": [
        "id",
        "instanceLabelEnabled",
        "logoImage",
        "logoEnabled",
        "logoMesoneEnabled",
        "colorScheme",
        "style",
        "selectedLocales",
        "selectedLocalesEnabled",
        "defaultLocale",
        "footer",
        "instanceLabel"
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
            "enabled": {
              "type": "boolean"
            },
            "visible": {
              "type": "boolean"
            },
            "useGlobalValue": {
              "type": "boolean"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "id",
            "enabled",
            "visible",
            "useGlobalValue",
            "defaultValue"
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