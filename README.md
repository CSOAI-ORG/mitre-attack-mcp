# MITRE ATT&CK Mapper MCP

[![PyPI](https://img.shields.io/pypi/v/mitre-attack-mcp)](https://pypi.org/project/mitre-attack-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-governance--mcp-purple)](https://meok.ai)

MITRE ATT&CK matrix lookup, tactic/technique/sub-technique mapper, and incident-to-technique correlation for cyber defenders.

## Install

```bash
pip install mitre-attack-mcp
```

## Tools

| Tool | Purpose |
|------|---------|
| `query_technique` | Query ATT&CK technique by ID (Txxxx) or name |
| `list_tactics` | All 14 enterprise tactics (TA0001-TA0040+) |
| `map_incident` | Map incident IOCs/behaviors to ATT&CK techniques |
| `group_threat_actor` | Threat actor groups (G-codes) using a technique |
| `mitigation_lookup` | Mitigations (M-codes) for a technique |

## Pairs with

- `meok-attestation-api` — POST results to https://meok-attestation-api.vercel.app/sign for cryptographically signed compliance certs
- `meok-attestation-verify` — public verification of any MEOK-signed cert
- Other MEOK governance MCPs via SOV3 `mcp_bridge_call`

## Pricing

- **Free**: 10 calls/day. No API key required.
- **Pro** £79/mo: unlimited + signed attestations. [Subscribe](https://buy.stripe.com/14A4gB3K4eUWgYR56o8k836)
- **Enterprise** £1,499/mo: white-label + on-premise + SLA. hello@meok.ai

## Status

Scaffold v1.0.0 ships the MCP framework + 5 tool stubs. v1.1.0 will add real regulation data ingestion.

If your team needs this MCP fully-loaded faster, ping hello@meok.ai for sponsored development.

## License

MIT © MEOK AI Labs

<!-- mcp-name: io.github.CSOAI-ORG/mitre-attack-mcp -->
