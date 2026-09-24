# Design

## Purpose

Jevの判断機能を、agentから安全に呼び出せるbounded MCP primitiveとして提供する独立serviceを目指す。

## Current state

このrepositoryはscaffoldであり、現時点ではproduction MCP endpointとして利用しない。実行可能な参照実装は `mcp-toolbox/servers/jev-cloudflare` にある。

## Design principles

- **strict schema。** 入出力契約を曖昧にしない。
- **server-side credentials。** clientへprovider credentialを渡さない。
- **authenticated remote access。**
- **fail-closed。** timeout、schema違反、provider errorを暗黙成功にしない。
- **bounded execution。** input size、timeout、rate、budgetを制限する。
- **deterministic CI first。** mockで契約を常時検証し、real API smoke testは補助とする。

## Non-goals

- 汎用LLM proxyになること。
- 無制限のremote executionを許可すること。
- scaffold段階でlive endpointとして扱うこと。

## Source of truth

production baselineの実装条件はIssue #1、現行の実行可能referenceは `mcp-toolbox/servers/jev-cloudflare` とする。
