# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T01:19:13+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Query

from models import (
    Alt,
    AnalyzeCommentRequest,
    AnalyzeCommentResponse,
    FieldXgafv,
    SuggestCommentScoreRequest,
    SuggestCommentScoreResponse,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='The Perspective Comment Analyzer API provides information about the potential impact of a comment on a conversation (e.g. it can provide a score for the "toxicity" of a comment). Users can leverage the "SuggestCommentScore" method to submit corrections to improve Perspective over time. Users can set the "doNotStore" flag to ensure that all submitted comments are automatically deleted after scores are returned.',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Perspective Comment Analyzer API',
    version='v1alpha1',
    servers=[{'url': 'https://commentanalyzer.googleapis.com/'}],
)


@app.post(
    '/v1alpha1/comments:analyze',
    description=""" Analyzes the provided text and returns scores for requested attributes. """,
    tags=['comment_evaluation'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def commentanalyzer_comments_analyze(
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: AnalyzeCommentRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1alpha1/comments:suggestscore',
    description=""" Suggest comment scores as training data. """,
    tags=['comment_evaluation'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def commentanalyzer_comments_suggestscore(
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: SuggestCommentScoreRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
