import os
import json


def ensure_schema_structure(schema):
    if 'type' not in schema:
        schema['type'] = 'object'

    if 'pages' not in schema:
        schema['pages'] = [
            {
                'id': 'page1',
                'type': 'object',
            }
        ]

    return schema


here = os.path.split(os.path.abspath(__file__))[0]

def from_json(fname):
    return json.load(open(os.path.join(here, fname)))

OSF_META_SCHEMAS = [
    # ensure_schema_structure(from_json('osf-open-ended-1.json')),
    # ensure_schema_structure(from_json('osf-standard-1.json')),
    ensure_schema_structure(from_json('osf-standard-test.json')),
    # ensure_schema_structure(from_json('brandt-prereg-1.json')),
    ensure_schema_structure(from_json('brandt-prereg-test.json')),
    # ensure_schema_structure(from_json('brandt-postcomp-1.json')),
]
