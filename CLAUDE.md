# Client-Strategy

REK Marketing client strategy documents and the weekly PPC audit routine.

## Weekly Google Ads fleet audit

The scheduled audit follows `docs/weekly-google-ads-audit-protocol.md` in full:
account discovery via the MCC, the per-account GAQL pull, the six-category
Health Score, the fleet-first report shape, the per-account context that
prevents false alarms, and the cost-discipline rules.

Data access from a cloud session: the read-only google-ads-mcp only runs on a
local Mac, so cloud runs use the google-ads Python client directly through
`tools/gaql.py`, authenticated with the `google-ads.yaml` from the owner-only
`dave-ads-setup` folder in Google Drive. Copy it to `~/google-ads.yaml` with
mode 600, delete it when the run ends, and never print any value from it.

Guardrails: query anything, mutate nothing. Skip `auction_insight_*` metrics
(Basic-access token). Segment primary conversions before calling tracking
dirty. Never declare a tag dead from zero conversions alone. Never fabricate a
number; a failed query is reported as "unavailable".

Reports go in `reports/` as `ppc-weekly-audit-YYYY-MM-DD.md`.

## Writing style

Plain sentences, no em dashes, no emojis. This applies to reports, ad copy,
and commit messages.
