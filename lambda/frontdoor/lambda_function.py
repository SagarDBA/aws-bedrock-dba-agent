"""
AWS Bedrock DBA Agent — Front-door Lambda
=========================================
Public-facing Lambda function that bridges the HTML chat UI to the
Bedrock supervisor agent. Exposes a Lambda Function URL with CORS
configured for browser access.

Runtime: Python 3.12
VPC: NOT in VPC — needs direct access to Bedrock API
IAM: dba-agent-lambda-role (bedrock:InvokeAgent)
Timeout: 5 minutes (Bedrock agent responses can be slow)
Memory: 256 MB
"""

import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ---------------------------------------------------------------------------
# Configuration — replace with your values
# ---------------------------------------------------------------------------
AGENT_ID       = '<YOUR_BEDROCK_SUPERVISOR_AGENT_ID>'
AGENT_ALIAS_ID = '<YOUR_BEDROCK_SUPERVISOR_AGENT_ALIAS_ID>'
REGION         = 'us-east-1'

# ---------------------------------------------------------------------------
# Bedrock agent runtime client
# ---------------------------------------------------------------------------
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name=REGION)

# ---------------------------------------------------------------------------
# Handler
# ---------------------------------------------------------------------------

def lambda_handler(event, context):
    """
    <Receives POST requests from the HTML chat UI via Lambda Function URL.
    Handles OPTIONS preflight for CORS. Parses message and session_id from
    the JSON body, invokes the Bedrock supervisor agent, streams the
    completion response, and returns the assembled text.

    Request body:
    {
        "message": "show me blocking sessions in MySQL",
        "session_id": "session-abc123"
    }

    Response body:
    {
        "response": "Here are the blocking sessions...",
        "session_id": "session-abc123"
    }

    Important: CORS headers are NOT set in the Lambda response — they are
    handled entirely by the Lambda Function URL CORS configuration.
    Setting them in both places causes the 'multiple values' CORS error.
    >
    """
    # <OPTIONS preflight handling — return 200 with empty body>
    # <Parse body: message (required), session_id (default: 'default-session')>
    # <bedrock_agent_runtime.invoke_agent() with enableTrace=False>
    # <Stream completion chunks: event['chunk']['bytes'].decode('utf-8')>
    # <Return assembled response with session_id>
    # <Error handling — return 500 with error message>
    pass


def cors_response(status_code, body):
    """
    <Returns a Lambda Function URL compatible response dict.
    Only sets Content-Type header — CORS headers handled by Function URL config.>
    """
    # <Return dict with statusCode, headers (Content-Type only), body>
    pass
