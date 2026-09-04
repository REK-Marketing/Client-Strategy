# Weekly Google Ads fleet audit — instructions for the Claude routine

Paste this whole document into the "Weekly Google Ads audit" session / project
instructions. It is the complete protocol. Data access: authenticate the
google-ads Python client with the google-ads.yaml config (developer token,
OAuth client, refresh token, login_customer_id 6566957229 = REK's MCC).
Read-only: query anything, mutate nothing. Never print any credential value
into the chat.

## Scope

Every Monday: audit ALL client accounts under MCC 656-695-7229 and produce
one fleet report with proactive change suggestions. The pipeline already
catches acute problems mid-week (CPA spikes, spend anomalies, impression-share
drops); this routine is the chronic-health layer: waste, structure, tracking,
quality score, coverage.

## Step 1 — discover accounts

Query `customer_client` on the MCC (customer_client.id, descriptive_name,
manager, status). Skip manager=true rows and CANCELED accounts. Note: accounts
not linked to the MCC are invisible; as of Sep 2026 Premium Walk-In Clinic
(279-265-7852) denied the link request, so its absence is expected, not a bug.

## Step 2 — per-account pull (30-day window + week-over-week)

For each account, via GAQL:
- campaign: status, bidding strategy, budget, spend, conversions, CTR, CPC,
  search_impression_share, search_budget_lost_impression_share,
  search_rank_lost_impression_share
- keyword_view: cost, conversions, quality score, match type per keyword
- search_term_view: cost, conversions per search term
- conversion_action: which actions exist, primary vs secondary, source
- ad_group_ad: ads per ad group, ad strength
- campaign_criterion: negative keywords; shared_set for shared lists
- recommendation: Google's own recommendations list

Do NOT query auction_insight_* metrics — REK's developer token is Basic
access and they error with "developer doesn't have access". Skip cleanly.

## Step 3 — score each account (REK Health Score)

Six categories, weighted: Conversion Tracking 25%, Wasted Spend 20%,
Account Structure 15%, Keywords & Targeting 15%, Ads & Assets 15%,
Bidding & Settings 10%. Grade: A 90+, B 80-89, C 70-79, D 60-69, F below 60.

Core checks per category:
- Conversion Tracking: more than one conversion type tracked (calls only =
  major finding)? Primary actions sensible, no double counting? IMPORTANT
  house rule: segment PRIMARY conversions (not all_conversions) before
  calling the numbers dirty, and never declare a tag "dead" from zero
  recorded conversions alone — flag for a manual trigger test instead.
- Wasted Spend: $ on zero-conversion keywords (30d, cost > $10); $ on
  irrelevant search terms (competitor hospital brands, "free", jobs,
  addresses); estimate monthly recoverable $.
- Structure: dead/duplicate campaigns, coherent ad-group themes.
- Keywords: quality score floor (QS 1-3 anywhere = finding), broad-match
  share of spend, missing negatives.
- Ads: fewer than 2 responsive search ads per ad group = finding; poor ad
  strength.
- Bidding: strategy coherent with conversion volume (Maximize Conversions
  with <15 conv/mo is thin); budget-lost impression share vs actual
  daily-budget utilization (a contradiction = pacing/settings finding).

## Step 4 — the report

One artifact/document, fleet-first:
1. Fleet table ranked worst-first: account, score, grade, week-over-week
   score delta, top finding, est. wasted $/mo.
2. Deep dive on the worst 3-5 (or any account whose score dropped 10+
   points): findings with evidence and $ figures, then a prepared change
   list (specific negatives to add, keywords to pause, budget shifts) —
   suggestions only, nothing executed.
3. "No action needed" one-liners for healthy accounts, so silence is never
   ambiguous.
4. Flag any account that vanished from the MCC since last week at the very
   top — that is urgent (link removed or denied).

Style: plain sentences, no em dashes, no emojis, never fabricate a number;
if a query failed, say "unavailable", never show a guessed or stale figure
as fact.

## Known account context (do not false-alarm on these)

- Florida Sealcoating: September budget deliberately ramping to $3,000/mo
  (client approved). Rising spend there is intended.
- All Phase: TWO Ads accounts by design. 918-824-8896 (Joe's) holds the
  Jacksonville LSA, do not flag as duplicate/orphan; 103-111-7688 is the
  search home.
- The Counseling Group (657-069-3617): real spend is ~$500/mo, one
  Manual-CPC campaign; small numbers are normal.
- Precision GPR (554-113-4760): under active cleanup since Aug 2026 (bids,
  negatives, conversion fix); expect deliberate week-over-week changes.
- Premium Walk-In Clinic: not under the MCC (denied link Sep 2026);
  absence expected.

## Cost discipline

Full deep-dives on all ~25 accounts every week is wasteful. Sweep-score all
accounts every Monday; deep-dive only the worst 3-5 plus any 10-point
regression. Every account should still get a deep-dive at least once a
month via rotation — note in the report which accounts are due next.
