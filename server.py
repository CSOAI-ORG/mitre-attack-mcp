#!/usr/bin/env python3
"""
MITRE ATT&CK Mapper MCP Server
==============================
By MEOK AI Labs | https://meok.ai

MITRE ATT&CK matrix lookup, tactic/technique/sub-technique mapper, and incident-to-technique correlation for cyber defenders.

Install: pip install mitre-attack-mcp
Run:     python server.py
"""

import json
import sys
import os
from datetime import datetime, timedelta, timezone
from typing import Optional
from collections import defaultdict
from mcp.server.fastmcp import FastMCP

import os as _os

_MEOK_API_KEY = _os.environ.get("MEOK_API_KEY", "")

try:
    sys.path.insert(0, os.path.expanduser("~/clawd/meok-labs-engine/shared"))
    from auth_middleware import check_access as _shared_check_access
    _AUTH_ENGINE_AVAILABLE = True
except ImportError:
    _AUTH_ENGINE_AVAILABLE = False

    def _shared_check_access(api_key: str = ""):
        """Fallback when shared auth engine is not available."""
        if _MEOK_API_KEY and api_key and api_key == _MEOK_API_KEY:
            return True, "OK", "pro"
        if _MEOK_API_KEY and api_key and api_key != _MEOK_API_KEY:
            return False, "Invalid API key. Get one at https://meok.ai/api-keys", "free"
        return True, "OK", "free"


def check_access(api_key: str = ""):
    return _shared_check_access(api_key)


FREE_DAILY_LIMIT = 10
_usage: dict[str, list[datetime]] = defaultdict(list)
STRIPE_PRO = "https://buy.stripe.com/14A4gB3K4eUWgYR56o8k836"


def _rl(tier="free") -> Optional[str]:
    if tier in ("pro", "professional", "enterprise"):
        return None
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=1)
    _usage["anonymous"] = [t for t in _usage["anonymous"] if t > cutoff]
    if len(_usage["anonymous"]) >= FREE_DAILY_LIMIT:
        return f"Free tier limit ({FREE_DAILY_LIMIT}/day). Pro £79/mo: {STRIPE_PRO}"
    _usage["anonymous"].append(now)
    return None


mcp = FastMCP(
    "MITRE ATT&CK Mapper",
    instructions=(
        "By MEOK AI Labs — MITRE ATT&CK matrix lookup, tactic/technique/sub-technique mapper, and incident-to-technique correlation for cyber defenders. "
        "Free tier: 10/day. Pro tier (£79/mo): unlimited + signed attestations. "
        "Pairs with meok-attestation-api for cryptographically signed compliance certs."
    ),
)



@mcp.tool()
def query_technique(query: str = "", api_key: str = "") -> str:
    """Query ATT&CK technique by ID (Txxxx) or name

    Args:
        query: Optional query parameter (regulation ref, identifier, or input data).
        api_key: Optional MEOK API key for Pro+ tier features.

    Returns: JSON with structured assessment, regulation refs, and recommended actions.
    """
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return json.dumps({"error": msg, "upgrade_url": STRIPE_PRO})
    if err := _rl(tier):
        return json.dumps({"error": err, "upgrade_url": STRIPE_PRO})

    return json.dumps({
        "tool": "query_technique",
        "query": query,
        "status": "stub",
        "tool_description": "Query ATT&CK technique by ID (Txxxx) or name",
        "note": "Initial scaffold v1.0.0 — extended logic ships in v1.1 with real regulation data ingestion.",
        "regulation_refs": [],
        "next_step": "POST result to https://meok-attestation-api.vercel.app/sign for HMAC-signed compliance cert",
        "tier": tier,
        "upsell_pro": f"Pro £79/mo: signed attestations + unlimited calls: {STRIPE_PRO}" if tier == "free" else None,
    }, indent=2)


@mcp.tool()
def list_tactics(query: str = "", api_key: str = "") -> str:
    """All 14 enterprise tactics (TA0001-TA0040+)

    Args:
        query: Optional query parameter (regulation ref, identifier, or input data).
        api_key: Optional MEOK API key for Pro+ tier features.

    Returns: JSON with structured assessment, regulation refs, and recommended actions.
    """
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return json.dumps({"error": msg, "upgrade_url": STRIPE_PRO})
    if err := _rl(tier):
        return json.dumps({"error": err, "upgrade_url": STRIPE_PRO})

    return json.dumps({
        "tool": "list_tactics",
        "query": query,
        "status": "stub",
        "tool_description": "All 14 enterprise tactics (TA0001-TA0040+)",
        "note": "Initial scaffold v1.0.0 — extended logic ships in v1.1 with real regulation data ingestion.",
        "regulation_refs": [],
        "next_step": "POST result to https://meok-attestation-api.vercel.app/sign for HMAC-signed compliance cert",
        "tier": tier,
        "upsell_pro": f"Pro £79/mo: signed attestations + unlimited calls: {STRIPE_PRO}" if tier == "free" else None,
    }, indent=2)


@mcp.tool()
def map_incident(query: str = "", api_key: str = "") -> str:
    """Map incident IOCs/behaviors to ATT&CK techniques

    Args:
        query: Optional query parameter (regulation ref, identifier, or input data).
        api_key: Optional MEOK API key for Pro+ tier features.

    Returns: JSON with structured assessment, regulation refs, and recommended actions.
    """
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return json.dumps({"error": msg, "upgrade_url": STRIPE_PRO})
    if err := _rl(tier):
        return json.dumps({"error": err, "upgrade_url": STRIPE_PRO})

    return json.dumps({
        "tool": "map_incident",
        "query": query,
        "status": "stub",
        "tool_description": "Map incident IOCs/behaviors to ATT&CK techniques",
        "note": "Initial scaffold v1.0.0 — extended logic ships in v1.1 with real regulation data ingestion.",
        "regulation_refs": [],
        "next_step": "POST result to https://meok-attestation-api.vercel.app/sign for HMAC-signed compliance cert",
        "tier": tier,
        "upsell_pro": f"Pro £79/mo: signed attestations + unlimited calls: {STRIPE_PRO}" if tier == "free" else None,
    }, indent=2)


@mcp.tool()
def group_threat_actor(query: str = "", api_key: str = "") -> str:
    """Threat actor groups (G-codes) using a technique

    Args:
        query: Optional query parameter (regulation ref, identifier, or input data).
        api_key: Optional MEOK API key for Pro+ tier features.

    Returns: JSON with structured assessment, regulation refs, and recommended actions.
    """
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return json.dumps({"error": msg, "upgrade_url": STRIPE_PRO})
    if err := _rl(tier):
        return json.dumps({"error": err, "upgrade_url": STRIPE_PRO})

    return json.dumps({
        "tool": "group_threat_actor",
        "query": query,
        "status": "stub",
        "tool_description": "Threat actor groups (G-codes) using a technique",
        "note": "Initial scaffold v1.0.0 — extended logic ships in v1.1 with real regulation data ingestion.",
        "regulation_refs": [],
        "next_step": "POST result to https://meok-attestation-api.vercel.app/sign for HMAC-signed compliance cert",
        "tier": tier,
        "upsell_pro": f"Pro £79/mo: signed attestations + unlimited calls: {STRIPE_PRO}" if tier == "free" else None,
    }, indent=2)


@mcp.tool()
def mitigation_lookup(query: str = "", api_key: str = "") -> str:
    """Mitigations (M-codes) for a technique

    Args:
        query: Optional query parameter (regulation ref, identifier, or input data).
        api_key: Optional MEOK API key for Pro+ tier features.

    Returns: JSON with structured assessment, regulation refs, and recommended actions.
    """
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return json.dumps({"error": msg, "upgrade_url": STRIPE_PRO})
    if err := _rl(tier):
        return json.dumps({"error": err, "upgrade_url": STRIPE_PRO})

    return json.dumps({
        "tool": "mitigation_lookup",
        "query": query,
        "status": "stub",
        "tool_description": "Mitigations (M-codes) for a technique",
        "note": "Initial scaffold v1.0.0 — extended logic ships in v1.1 with real regulation data ingestion.",
        "regulation_refs": [],
        "next_step": "POST result to https://meok-attestation-api.vercel.app/sign for HMAC-signed compliance cert",
        "tier": tier,
        "upsell_pro": f"Pro £79/mo: signed attestations + unlimited calls: {STRIPE_PRO}" if tier == "free" else None,
    }, indent=2)



def main():
    mcp.run()


if __name__ == "__main__":
    main()
