from fastavro import writer, parse_schema

schema = {
        "name": "CertLog",
        "type": "record",
        "namespace": "nl.openintel.certlog",
        "fields": [
                        {
                            "name": "cert_index",
                            "type": "int"
                        },
                        {
                            "name": "cert_link",
                            "type": ["null", "string"],
                            "default": ""
                        },
                        {
                            "name": "chain",
                            "type": {
                                "type": "array",
                                "items": {
                                    "name": "chain_record",
                                    "type": "record",
                                    "fields": [
                                        {
                                            "name": "as_der",
                                            "type": ["null", "string"]
                                        },
                                        {
                                            "name": "extensions",
                                            "type": {
                                                "name": "extensions",
                                                "type": "record",
                                                "fields": [
                                                    {
                                                        "name": "authorityInfoAccess",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "authorityKeyIdentifier",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "basicConstraints",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "certificatePolicies",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "crlDistributionPoints",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "keyUsage",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "subjectKeyIdentifier",
                                                        "type": ["null", "string"]
                                                    }
                                                ]
                                            }
                                        },
                                        {
                                            "name": "fingerprint",
                                            "type": ["null", "string"]
                                        },
                                        {
                                            "name": "not_after",
                                            "type": "float"
                                        },
                                        {
                                            "name": "not_before",
                                            "type": "float"
                                        },
                                        {
                                            "name": "serial_number",
                                            "type": ["null", "string"]
                                        },
                                        {
                                            "name": "subject",
                                            "type": {
                                                "name": "subject",
                                                "type": "record",
                                                "fields": [
                                                    {
                                                        "name": "C",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "CN",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "L",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "O",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "OU",
                                                        "type": [
                                                            ["null", "string"],
                                                            "null"
                                                        ]
                                                    },
                                                    {
                                                        "name": "ST",
                                                        "type": ["null", "string"]
                                                    },
                                                    {
                                                        "name": "aggregated",
                                                        "type": ["null", "string"]
                                                    }
                                                ]
                                            }
                                        }
                                    ]
                                }
                            }
                        },
                        {
                            "name": "leaf_cert",
                            "type": {
                                "name": "leaf_cert",
                                "type": "record",
                                "fields": [
                                    {
                                        "name": "all_domains",
                                        "type": {
                                            "type": "array",
                                            "items": ["null", "string"]
                                        }
                                    },
                                    {
                                        "name": "as_der",
                                        "type": ["null", "string"]
                                    },
                                    {
                                        "name": "extensions",
                                        "type": "extensions"
                                    },
                                    {
                                        "name": "fingerprint",
                                        "type": ["null", "string"]
                                    },
                                    {
                                        "name": "not_after",
                                        "type": "float"
                                    },
                                    {
                                        "name": "not_before",
                                        "type": "float"
                                    },
                                    {
                                        "name": "serial_number",
                                        "type": ["null", "string"]
                                    },
                                    {
                                        "name": "subject",
                                        "type": "subject",
                                    }
                                ]
                            }
                        },
                        {
                            "name": "seen",
                            "type": "float"
                        },
                        {
                            "name": "source",
                            "type": {
                                "name": "source",
                                "type": "record",
                                "fields": [
                                    {
                                        "name": "name",
                                        "type": ["null", "string"]
                                    },
                                    {
                                        "name": "url",
                                        "type": ["null", "string"]
                                    }
                                ]
                            }
                        },
                        {
                            "name": "update_type",
                            "type": ["null", "string"]
                        }

        ]
}

def write_to_avro(filename, records):
    parsed_schema = parse_schema(schema)
    with open(filename, 'wb') as out:
        writer(out, parsed_schema, records, validator=True)


