# MCP-Jev

> **Status: scaffold / not deployable.**
>
> This repository does not currently contain a production MCP implementation.
> Do not configure Codex or another MCP client to use this repository as a live endpoint yet.

The intended production baseline is tracked in [Issue #1](https://github.com/palladiumailab-collabmAILab/MCP-Jev/issues/1).

For the currently implemented Jev-on-Cloudflare MCP code in this organization, see
[`mcp-toolbox/servers/jev-cloudflare`](https://github.com/palladiumailab-collabmAILab/mcp-toolbox/tree/main/servers/jev-cloudflare).

## Intended direction

The standalone MCP-Jev repository is intended to expose bounded Jev judgment primitives with:

- strict schemas;
- server-side credentials;
- authenticated remote access;
- fail-closed error handling;
- input, timeout, rate, and budget limits;
- deterministic mocked CI plus optional real-API smoke tests.

Until Issue #1 is implemented and CI exists here, `mcp-toolbox/servers/jev-cloudflare` is the executable reference and this repository should be treated as planning/scaffolding only.
