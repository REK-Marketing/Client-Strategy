# PPC Weekly Audit - 2026-09-07

Run: Monday Sep 7, 2026, scheduled cloud session. Reporting window: Aug 31 to Sep 6, 2026 (this week) against Aug 24 to Aug 30, 2026 (last week).

Protocol: docs/weekly-google-ads-audit-protocol.md. Nothing in any account was changed.

## Attention items (read first)

1. **The Google Ads fleet audit did not run. The refresh token is still dead.** The google-ads.yaml in the owner-only Drive folder dave-ads-setup (file modified Sep 2 at 13:53 UTC, unchanged since the Sep 3 failure) was copied to the cloud session with mode 600 and tested twice through the google-ads Python client via tools/gaql.py. Google's OAuth endpoint rejected it both times with invalid_grant / Bad Request before any Ads API call was made. The egress proxy reached Google (the error body is Google's, not a proxy 403), and the client library loaded cleanly in a fresh venv, so this is the credential, not the environment. The file was deleted from the session at the end of the run.
2. **Every Google Ads figure in this report is unavailable.** No account discovery, no campaign, keyword, search-term, conversion, quality score, or change-history data for any of the 26 accounts under MCC 656-695-7229. Week-over-week deltas against the Sep 4 report could not be computed. The "vanished from the MCC" check could not be performed; next successful run must compare against the 26 IDs in the Sep 4 fleet table.
3. **The Sep 4 report ran from the Mac MCP, not this token.** The Sep 4 data notes say the Mac's local yaml was rejected with "developer token is not valid" and the MCP connection worked instead. So there are at least two broken copies of the credential (Drive and Mac yaml) and one working path (the Mac MCP). Whatever the MCP is authenticating with is the token that should be copied into Drive.
4. **Meta: both REK campaigns are now paused.** Tom paused REK Orlando Prospecting (campaign, ad set, and ad) on Sep 4 at 9:29 AM. Philly Prospecting was already paused. Meta spend for the week stopped at $37.30. Nothing on Meta is serving.

## Coverage

| Platform | Accounts visible | Auditable | Notes |
|---|---|---|---|
| Google Ads | unavailable | 0 | Authentication failed (invalid_grant). See attention item 1. |
| Meta Ads | 2 | 1 | REK Marketing & Design (active, both campaigns paused). SLP is CLOSED and not queryable. |

## Account status summary

| Account | Platform | Status | Spend (wk) | Budget (wk) | Leads (wk) | WoW leads | Urgency |
|---|---|---|---|---|---|---|---|
| All 26 client accounts under MCC 656-695-7229 | Google | Critical (API auth failed, no data) | unavailable | unavailable | unavailable | unavailable | 1 |
| REK Marketing & Design, Orlando Prospecting | Meta | Paused Sep 4 (was Critical on Sep 3) | $37.30 | $56.00 ($8/day, 4 days served) | 0 | 2 to 0 | 2 |
| REK Marketing & Design, Philly Prospecting | Meta | Paused, no spend | $0.00 | $0.00 | 0 | 0 to 0 | 3 |
| SLP | Meta | Closed | n/a | n/a | n/a | n/a | n/a |

On-target, needs attention, critical: no Google Ads account can be classified this week. The Sep 4 fleet table stands as the most recent classification. Its top three (All Phase Jacksonville 42 F, Premium Walk-In Clinic 46 F, Precision GPR 55 F) and its prepared change lists remain the open work.

## Google Ads: what was attempted

| Step | Result |
|---|---|
| Locate credential | Found google-ads.yaml in Drive folder dave-ads-setup, 355 bytes, modified 2026-09-02 13:53 UTC, owner-only |
| Install client | google-ads Python package installed in a fresh venv, imports clean |
| Auth test 1 | customer_client discovery on the MCC: invalid_grant / Bad Request |
| Auth test 2 | customer LIMIT 1 on the MCC after a pause: invalid_grant / Bad Request |
| Proxy check | Proxy status healthy, no relay failures recorded, Google reached |
| Cleanup | ~/google-ads.yaml deleted, no values printed |

The setup note in the same Drive folder (SETUP-DAVE.md) still says the yaml "already contains a working refresh token" and that Premium Walk-In Clinic is unlinked. Both statements are out of date: the token fails, and the Sep 4 run found Premium Walk-In Clinic linked and spending.

### Fix, in order

1. On the Mac, run one GAQL query through the working google-ads-mcp to confirm it still authenticates today. If it does, locate the yaml or token store the MCP actually reads and compare its refresh_token to the Drive copy. They will differ.
2. If the MCP also fails, mint a new refresh token with the OAuth client already in the yaml (the account requires a passkey for new tokens, per the Sep 3 report). Causes ranked on Sep 3 still apply: revoked token, OAuth app in Testing mode (7-day expiry), or the 50-token-per-user cap.
3. Update all copies: Secret Manager for the rek-daily-pipeline Cloud Run job, the Mac yaml, and the Drive copy in dave-ads-setup. Update SETUP-DAVE.md so Dave does not copy a dead file.
4. Check the last three rek-daily-pipeline executions. If they carry the same token, the Mon/Wed/Fri pulls into gsc_data.google_ads_* have been failing since at least Sep 3 and the dashboard and alerts are stale.
5. Re-run this routine. It will produce the full fleet table with week-over-week deltas against Sep 4.

### Rotation, carried forward

Deep dives due from the Sep 4 rotation were Florida Sealcoating, Rover Veterinary Care, and Scootz. None could be done. They stay due for the next successful run, with Affordable Critter Solutions the week after.

## Meta: REK Marketing & Design (1504808084730595)

### Week-over-week: Orlando Prospecting (campaign 120249721176530223)

| Metric | Last week (Aug 24 to Aug 30) | This week (Aug 31 to Sep 6) | Change | Note |
|---|---|---|---|---|
| Spend | $55.12 | $37.30 | -32% | paused Sep 4, 9:29 AM |
| Impressions | 558 | 244 | -56% | 4 days served vs 7 |
| Reach | 389 | 168 | -57% | |
| Frequency | 1.43 | 1.45 | flat | |
| Clicks (all) | 12 | 5 | -58% | |
| CTR (all) | 2.15% | 2.05% | -5% | flat |
| CPC (all) | $4.59 | $7.46 | +63% | flag |
| CPM | $98.78 | $152.87 | +55% | flag |
| Link clicks | 6 | 4 | -33% | |
| Leads (form) | 2 | 0 | -100% | 0 leads since Aug 24 |
| Cost per lead | $27.56 | no leads | | |

Meta reports the two leads for Aug 24 to Aug 30 in the campaign's default attribution window. The Sep 3 report, which used Aug 27 to Sep 2, showed the last lead on Aug 24 and none after. Both windows agree: no lead in 13 days of serving before the pause.

Philly Prospecting: paused, $0.00 both weeks, no change.

### Recent changes (Aug 31 to Sep 6)

- Aug 31, 9:05 AM: Meta billed the account $47.00.
- Sep 4, 9:29 AM: Tom Klingebiel set REK Orlando Prospecting (campaign), Orlando Lead Forms (ad set), and New Leads Ad (ad) to Inactive through Power Editor. The ad had last exited learning on Aug 16.
- Sep 4, 3:44 PM and 3:49 PM: Meta auto-created 13 custom audiences named asa_auto_custom_audience. These are system-generated (actor Meta, not a user) and are the Advantage+ audience seeds Meta builds when a campaign is edited. They are not a user change and need no action, but they will clutter the Audiences list.

No bid, budget, targeting, or creative changes were made. The pause carried out the Sep 3 action plan's "pause it if it stays leadless" step. The creative refresh, placement exclusion, and budget or optimization change from that plan have not happened yet.

### Impact of the pause

Before the pause the campaign was on the trajectory the Sep 3 report described: CPM up 55% and CPC up 63% week over week on the same single creative, with no leads. Pausing stopped roughly $8/day of spend that was producing nothing. The account is now idle. The Sep 3 diagnosis (creative decay, budget too small for QUALITY_LEAD optimization, possible Instant Form or lead sync issue, Instagram placements dead weight) still stands and is what a relaunch needs to address.

## Optimization opportunities

Google Ads: unavailable this week. The Sep 4 prepared change lists for All Phase Jacksonville, Premium Walk-In Clinic, Precision GPR, Patio Style, All Phase Pool Remodeling, and Aqua Coat remain the current recommendations. No new negatives, keywords, bid adjustments, or competitive insights can be proposed without data.

Meta, for the Orlando relaunch when Tom is ready:

- Confirm the Instant Form is published and attached, and that the Aug 20 and Aug 24 leads reached the CRM. Do this before spending on new creative.
- Launch with 2 to 3 new creatives: a 9:16 video for Facebook Reels (the top lead placement on Sep 3 data) and a static image for Feed.
- Exclude Instagram Feed. Keep Facebook Reels, Feed, and Stories.
- Either raise the budget to $15 to $20/day so QUALITY_LEAD has signal, or switch the ad set to LEAD_GENERATION at $8/day. Do not relaunch QUALITY_LEAD at $8/day unchanged.
- Rename the three ads sharing the name New Leads Ad by creative and date.
- Delete or ignore the 13 asa_auto_custom_audience entries; they will be recreated on the next edit anyway.

## Prioritized weekly action plan

1. **Critical: replace the Google Ads refresh token.** Today: confirm whether the Mac MCP still authenticates, copy its working credential into Drive and Secret Manager, or mint a new token if it also fails. Check the rek-daily-pipeline logs for the same invalid_grant error. Until this is done the weekly fleet audit, the daily pipeline, and Dave's setup are all blind. Two consecutive scheduled runs (Sep 3 and Sep 7) have now failed on this.
2. **High: re-run the fleet audit once the token works.** Deep dives due: Florida Sealcoating, Rover Veterinary Care, Scootz. Compare the account list against the 26 IDs from Sep 4.
3. **Medium: decide the Orlando Prospecting relaunch.** The pause on Sep 4 was the right call. Relaunch only with the form check, new creative, placement exclusion, and budget or optimization change above.
4. **Low: Philly Prospecting.** Paused, no spend. Launch alongside Orlando with the refreshed creative or archive it.
5. **Housekeeping: update SETUP-DAVE.md in Drive** once the token is fixed, and correct its Premium Walk-In Clinic note (the account is linked and spending as of Sep 4).

## Data notes

- Meta metrics use the default attribution window. At 5 to 12 clicks a week, single-week CTR and CPC swings are noisy. The lead drought is the meaningful signal.
- Meta week boundaries in this report are Monday to Sunday (Aug 24 to Aug 30 and Aug 31 to Sep 6), which differs from the Sep 3 report's Thursday to Wednesday windows. Do not compare the two reports' weekly figures directly.
- No Google Ads number in this report was estimated or carried forward as current data. Where Sep 4 figures are referenced they are labeled as Sep 4 figures.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
