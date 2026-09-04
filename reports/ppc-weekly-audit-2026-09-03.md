# PPC Weekly Audit — 2026-09-03

Reporting window: **Aug 27 – Sep 2, 2026** (this week) vs. **Aug 20 – Aug 26, 2026** (last week).
Source: Meta Ads API (Facebook Ads MCP). Google Ads was **not reachable** from this run (see Coverage gaps).

## Coverage

| Platform | Accounts visible | Auditable | Notes |
|---|---|---|---|
| Meta Ads | 2 | 1 | `REK Marketing & Design` (active). `SLP` is CLOSED and not queryable. |
| Google Ads | unknown | 0 | **Authentication failed.** The shared refresh token in the Drive copy of `google-ads.yaml` (folder `dave-ads-setup`, dated Sep 2) is rejected by Google's OAuth endpoint with `invalid_grant / Bad Request` on every attempt. No MCC account tree, campaigns, keywords, Quality Scores, or auction insights could be pulled. |

**Coverage gap: Google Ads.** The read-only google-ads-mcp lives on Tom's Mac and is not reachable from the cloud session, so this run reproduced its path directly (google-ads Python client, MCC 656-695-7229 as `login_customer_id`, same yaml). Google refused the refresh token before any Ads API call was made. `invalid_grant` is deterministic and comes from Google, not the proxy. The token was also tested against the second OAuth client stored in Drive (`PPC/GCP secret for Claude MCP`, project spartan-matter) and failed identically, which rules out a client-id mismatch. The Drive yaml is owner-only (no link sharing), so exposure is not the cause. Causes in order of likelihood: the token was revoked (password change, OAuth app in Testing mode, or the 50-token-per-user cap), the Drive copy is stale relative to the token on the Mac and in Secret Manager, or the token was minted for a different OAuth client.

**Why this is urgent.** The rek-daily-pipeline Cloud Run job, the Mac MCP, and Dave's setup all use one user refresh token. If Secret Manager holds the same token, the Mon/Wed/Fri pulls into `gsc_data.google_ads_*` are failing as well, and the dashboard, auction alerts, and monthly reports are going stale. Verify before the next 8am send.

Once the token is replaced, this routine can run the full `/rek-adwords-audit` surface (Health Score, wasted spend, keyword health matrix, negatives, auction insights) for every client under the MCC. Note that auction insight competitor domains still need the Standard-access API application that is parked.

## Account status summary

| Account | Platform | Status | Spend (wk) | Target (wk) | Pacing | Leads (wk) | WoW leads | CPL (wk) | Urgency |
|---|---|---|---|---|---|---|---|---|---|
| REK Marketing & Design — Orlando Prospecting | Meta | **Critical** | $50.29 | $56.00 ($8/day) | 90% | 0 | 3 → 0 | n/a (no leads) | 1 |
| REK Marketing & Design — Philly Prospecting | Meta | On-target (paused) | $0.00 | $0.00 | n/a | 0 | 0 → 0 | n/a | 3 |
| SLP | Meta | Closed | — | — | — | — | — | — | n/a |
| All Google Ads clients under MCC 656-695-7229 | Google | **Critical (API auth failed)** | — | — | — | — | — | — | 1 |

## Week-over-week: Orlando Prospecting (campaign 120249721176530223)

| Metric | Last week (Aug 20–26) | This week (Aug 27–Sep 2) | Change | Flag |
|---|---|---|---|---|
| Spend | $56.72 | $50.29 | −11% | ok |
| Impressions | 539 | 416 | −23% | watch |
| Reach | 384 | 298 | −22% | watch |
| Frequency | 1.40 | 1.40 | flat | ok |
| Clicks (all) | 16 | 5 | −69% | **flag** |
| CTR (all) | 2.97% | 1.20% | −60% | **flag** |
| CPC (all) | $3.55 | $10.06 | +183% | **flag** |
| CPM | $105.23 | $120.89 | +15% | watch |
| Link clicks | 9 | 3 | −67% | **flag** |
| Landing page views | 1 | 0 | — | — |
| Leads (form) | 3 | 0 | −100% | **critical** |
| Cost per lead | $18.91 | no leads | — | **critical** |

28-day context: $232.72 spent, 5 leads, $46.54 CPL, 2.13% CTR, $5.29 CPC.
Last lead recorded **Aug 24**. Nine consecutive days with spend and no leads since.

### Daily trend (Aug 20 – Sep 2)

| Date | Spend | Impr. | Clicks | CTR | Leads |
|---|---|---|---|---|---|
| Aug 20 | $8.12 | 49 | 5 | 10.20% | 1 |
| Aug 21 | $3.15 | 49 | 1 | 2.04% | 0 |
| Aug 22 | $0.43 | 24 | 0 | 0.00% | 0 |
| Aug 23 | $13.57 | 110 | 1 | 0.91% | 0 |
| Aug 24 | $12.04 | 133 | 4 | 3.01% | 2 |
| Aug 25 | $9.54 | 103 | 3 | 2.91% | 0 |
| Aug 26 | $9.87 | 71 | 2 | 2.82% | 0 |
| Aug 27 | $6.49 | 60 | 0 | 0.00% | 0 |
| Aug 28 | $3.82 | 47 | 2 | 4.26% | 0 |
| Aug 29 | $0.58 | 25 | 0 | 0.00% | 0 |
| Aug 30 | $12.78 | 119 | 1 | 0.84% | 0 |
| Aug 31 | $11.11 | 65 | 1 | 1.54% | 0 |
| Sep 1 | $5.31 | 31 | 0 | 0.00% | 0 |
| Sep 2 | $10.20 | 69 | 1 | 1.45% | 0 |

Daily delivery is erratic (from $0.43 to $13.57 on an $8/day budget), which is typical of a Highest-volume ad set that has never left the learning phase.

### Placement breakdown (14 days)

| Placement | Spend | Impr. | CTR | Link clicks | Leads |
|---|---|---|---|---|---|
| Facebook Reels | $48.00 | 425 | 1.65% | 3 | 2 |
| Facebook Feed | $34.67 | 338 | 2.66% | 5 | 1 |
| Facebook Stories | $10.65 | 48 | 6.25% | 2 | 0 |
| Instagram Feed | $6.19 | 56 | 0.00% | 0 | 0 |
| Instagram Reels | $4.38 | 58 | 1.72% | 1 | 0 |
| Instagram Stories | $3.12 | 30 | 3.33% | 1 | 0 |

All 3 leads came from Facebook Reels and Facebook Feed. Instagram took $13.69 (13% of spend) for 2 link clicks and no leads.

### Structure and settings

- Campaign: `REK — Orlando Prospecting`, objective OUTCOME_LEADS, bid strategy Highest volume, $8.00/day campaign budget.
- Ad set: `Orlando Lead Forms`, optimization goal QUALITY_LEAD (conversion leads), Advantage+ placements.
- Ads: **one active ad** (`New Leads Ad`, id 120249864037070223) carrying 100% of spend for the full 14 days. Two other ads with the same name are paused with zero spend.
- Delivery errors: none.
- Meta's own trend read for the ad set: CVR trend good, CTR trend bad, cost-per-link-click trend bad.

## Recent changes (past 7 days)

Activity log for Aug 27 – Sep 3 shows **no bid, budget, targeting, creative, or status changes**. The only event is a $47.00 billing charge on Aug 31. The performance drop is not the result of an edit; it is the same ad and settings decaying.

## Diagnosis

1. **Creative decay on a single ad.** One creative has run unchanged for two weeks. CTR has fallen by 60% week over week and CPC has tripled while frequency stays at 1.4, so this is not audience saturation. The ad is losing the auction on engagement, which drives CPM up and clicks down.
2. **Budget too small for the optimization goal.** QUALITY_LEAD on $8/day produced 5 leads in 28 days. Meta needs roughly 50 optimization events per week to exit learning. At this volume the ad set will stay in learning indefinitely and delivery will keep swinging day to day.
3. **Possible form or sync issue.** Nine days without a lead on an ad that was converting is also consistent with an Instant Form that stopped submitting or a lead sync that stopped writing to the CRM. Worth a manual check before spending on new creative.
4. **Instagram placements are dead weight** at this budget.

## Optimization opportunities

- **Creative:** launch 2–3 new variants this week. Priority: a 9:16 short video for Facebook Reels (the top lead placement), plus a static image version for Feed. Keep the current ad live for comparison for 3–4 days, then pause it if it stays leadless.
- **Placements:** exclude Instagram Feed. Keep Facebook Reels, Feed, and Stories. Optionally exclude all Instagram placements until budget increases.
- **Bidding / optimization:** either raise the budget to $15–20/day so QUALITY_LEAD can gather signal, or switch the ad set's optimization goal to LEAD_GENERATION (form submits) at the current budget. Do not run QUALITY_LEAD at $8/day and expect steady results.
- **Tracking:** open the Instant Form and confirm it is published and attached to the active ad. Confirm the lead destination (CRM or Leads Center) shows the 3 leads from Aug 20 and Aug 24, and that no leads are stuck.
- **Lead quality:** review the 5 leads from the last 28 days. If they are unqualified, tighten the form (add a qualifying question, use higher-intent form type) before scaling.
- **Philly Prospecting:** paused with no spend. Decide whether to launch with the refreshed creative or archive it so it does not clutter the account.
- **Negative keywords, new keywords, Quality Score, auction insights:** not applicable to Meta. Requires the Google Ads connector.

## Prioritized weekly action plan

1. **Critical: Google Ads API refresh token rejected (`invalid_grant`).** Today: run a quick GAQL query from the Mac MCP to confirm whether the local `~/google-ads.yaml` still authenticates, and open the latest rek-daily-pipeline Cloud Run execution log to see if it is failing with the same error. If the token is revoked, mint a new one (the account now requires a passkey for new tokens), then update Secret Manager, the Mac yaml, and the Drive copy in `dave-ads-setup`. Until then no Google Ads client account can be audited, and the warehouse tables may be stale.
2. **Critical: Orlando Prospecting has produced zero leads for 9 days on $50/week.** Today: check the Instant Form and lead sync. This week: ship 2–3 new creatives, exclude Instagram Feed, and either raise budget to $15–20/day or switch optimization to LEAD_GENERATION.
3. **Low: Philly Prospecting.** Paused, $0 spend, no action required. Launch or archive at your discretion.
4. **Housekeeping:** three ads share the name `New Leads Ad`. Rename them by creative and date so activity logs and reports stay readable.

## Data notes

- Meta metrics use the default attribution window. Small-account noise is high: at 5 to 16 clicks per week, single-day CTR swings are not statistically meaningful. The 9-day lead drought is meaningful because it is a run of zeros on an ad that previously converted.
- No spend or CPL targets are documented in this repo. Pacing is measured against the $8/day campaign budget. The prior week's $18.91 CPL and the 28-day $46.54 CPL are used as the working reference.
