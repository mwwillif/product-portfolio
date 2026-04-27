import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from config import MODEL_NAME, ALLOWED_SECTIONS

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JOB_ANALYSIS_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "top_required_skills": {"type": "array", "items": {"type": "string"}},
        "screening_keywords": {"type": "array", "items": {"type": "string"}},
        "domain_signals": {"type": "array", "items": {"type": "string"}},
        "preferred_tools": {"type": "array", "items": {"type": "string"}},
        "leadership_expectations": {"type": "array", "items": {"type": "string"}},
        "functional_priorities": {"type": "array", "items": {"type": "string"}},
        "transformation_signals": {"type": "array", "items": {"type": "string"}},
        "compliance_signals": {"type": "array", "items": {"type": "string"}},
        "architecture_signals": {"type": "array", "items": {"type": "string"}},
        "consulting_signals": {"type": "array", "items": {"type": "string"}},
        "strongest_resume_themes": {"type": "array", "items": {"type": "string"}}
    },
    "required": [
        "top_required_skills",
        "screening_keywords",
        "domain_signals",
        "preferred_tools",
        "leadership_expectations",
        "functional_priorities",
        "transformation_signals",
        "compliance_signals",
        "architecture_signals",
        "consulting_signals",
        "strongest_resume_themes"
    ]
}

RESUME_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "updates": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "section_id": {
                        "type": "string",
                        "enum": ALLOWED_SECTIONS
                    },
                    "content": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["section_id", "content"]
            }
        }
    },
    "required": ["updates"]
}


def _call_json(messages, schema_name, schema):
    response = client.responses.create(
        model=MODEL_NAME,
        input=messages,
        text={
            "format": {
                "type": "json_schema",
                "name": schema_name,
                "schema": schema,
                "strict": True
            }
        }
    )
    return json.loads(response.output_text)


def get_job_analysis(messages):
    return _call_json(messages, "job_analysis", JOB_ANALYSIS_SCHEMA)


def get_resume_updates(messages):
    return _call_json(messages, "resume_updates", RESUME_SCHEMA)