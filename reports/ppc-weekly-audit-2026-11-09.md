# PPC Weekly Audit - 2026-11-09 (Google Ads fleet)

Run: Monday Nov 9, 2026, scheduled cloud session through tools/gaql.py (Google Ads API v26) against MCC 656-695-7229. Windows: 30 days Oct 10 to Nov 8; this week Nov 2 to Nov 8; last week Oct 26 to Nov 1; prior month Sep 10 to Oct 9. Score deltas are against the Sep 14 report, the last run with Google Ads data (the Sep 21 to Nov 2 Mondays have no report in this repo). Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Progetto Shades (worst REK-managed score), Patio Style (14-point drop), All Phase Pool Remodeling (13-point drop), Precision GPR (spend up and CPA up, the protocol's own trigger), American Impact (new, largest spender under the MCC, provisional). One-liners for the rest.

Credential: the google-ads.yaml in the Drive folder dave-ads-setup (unchanged since Sep 8) authenticated on the first try, was copied with mode 600, read only by the client library, and deleted before this report was written. The installed google-ads client (35.0.0) no longer ships API v22, so the run used v26; tools/gaql.py now defaults to v26.

## Attention items (read first)

1. **No account vanished from the MCC.** All 26 accounts from the Sep 14 list are still linked. Premium Walk-In Clinic and Premium Medication Refills remain absent, as expected. Seven accounts are new under the MCC since Sep 14: American Impact (974-265-3397), Quality Paralegal Services (447-153-2607), Rover Reno PPC (961-477-3743), Color Masters (426-092-9847), Color Masters LSA (163-445-9282), ProShield (771-172-8482), All Phase Pool Remodeling Orlando LSA (355-287-7099).
2. **American Impact (974-265-3397) spent $24,543 in 30 days, and the client raised the main search campaign budget to $1,200 a day on Nov 8.** No REK user appears in its change history; the editors are contact@57clicks.com (66 changes) and americanimpactandenergy@gmail.com (23). This week: $7,029 for 5 primary conversions ($1,406 each), search CPC $121. The "Search | Impact Windows | Orlando For Web" campaign averaged $627 per conversion over 30 days and is still in bidding-strategy learning. At $1,200 a day it could spend $36,000 next month. Tom needs to say whether REK manages, audits, or is only linked. Scored below as 47 F, provisional.
3. **Progetto Shades (416-010-8247) spent $1,689 in the last 14 days with zero primary conversions, and $2,927 in 30 days for 2.** The website lead form action ("Lead form website") is secondary and last recorded on Oct 3; "Web form (start)" fired twice since Oct 24 with no completion recorded. Tracking first, then bids. Deep dive 1.
4. **Patio Style (596-555-8707) primary conversions fell from 108 in August and 90 in September to 14 in October and 5 so far in November, with spend flat.** Both directions actions (the GA4 get_directions import and "Get directions (GTM) 11 Sep") are now secondary and excluded. Directions kept firing (77 Google-hosted, 39 GA4, 33 GTM in 30 days), so this is a configuration change, not a demand drop. The protocol records Get Directions as the client's primary conversion. Confirm with Paid Ads whether the demotion was deliberate. Deep dive 2.
5. **Precision GPR (554-113-4760): spend up and CPA up in the same window, which is the protocol's trigger.** Sep 10 to Oct 9: $2,602, 30 conversions, $87. Oct 10 to Nov 8: $3,049, 19 conversions, $160. Dave cut six budgets on Nov 6 (now $84 a day, in line with the $82 target) and this week came in at $702 for 6 conversions ($117). Deep dive 4.
6. **Scootz form tracking is now 12 weeks dark.** The GA4 form_submit action last recorded on Aug 16 and is still secondary and excluded. Tom restructured the campaign on Nov 3 (themed ad groups, 29 legacy keywords paused) and the client raised the budget from $50 to $75 a day on Nov 8. The restructure is being measured on purchases and calls only.
7. **Pay-per-lead Performance Max campaigns started serving Nov 7 in three LSA-only accounts.** Citrus Landscape Solutions Sanford ($357 a day budget, $1,106 spent in two days, 9 conversions), Citrus St. Pete ($214 a day, $376, 4 conversions) and Herrell Plumbing ($79 a day, $259, 3 conversions). Robbie set the Citrus budgets on Oct 28; Tom set Herrell's on Nov 2. These accounts are out of scope by Tom's Sep 4 rule, so this is for the record, but the Citrus Sanford budget is the largest daily budget in the fleet after American Impact.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 33 client accounts, 1 manager | 15 | 7 new since Sep 14, 0 vanished. Excluded: Byers Fence x2, Herrell Plumbing, 10 LSA-only accounts. Not scorable: Color Masters (paused Oct 22), ProShield (client-run, paused), Straightline Fence (LSA only now), All Phase Jacksonville (no search spend), Jupiter Boat Supply (paused), REK Marketing (own account, noted separately). |

Search, Performance Max and display spend in the 30-day window: $20,241 across the 13 REK-managed scored accounts (Precision GPR $3,049, Progetto Shades $2,927, Florida Sealcoating $2,870, Rover Veterinary Care $2,612, Patio Style $2,234, Scootz $1,505, Quality Paralegal $1,397, All Phase $827, M&S Asphalt $756, Rover Reno $719, The Counseling Group $595, Aqua Coat $456, Affordable Critter $294). Plus $14,184 at Filutowski Eye Institute and $24,543 at American Impact, both linked and not REK-edited. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor; the components are listed in each deep dive or one-liner. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $14,184 | 157 | $90 | 43 | F | +1 | Critical (scope) | Broad "lasik treatment cost" still $9,092 for 45 conversions ($202) matching other clinics; Branded converts at $21 and loses 84% to budget | $596 (top 8 terms only) |
| 2 | Progetto Shades | 416-010-8247 | $2,927 | 2 | $1,463 | 45 | F | new score | Critical | Zero conversions in 14 days on $1,689; website lead form action secondary and silent since Oct 3; 37 keywords at QS 1 to 3 carrying $800 | $75 |
| 3 | American Impact | 974-265-3397 | $24,543 | 82 | $299 | 47 | F | new | Critical (scope) | Client set the search budget to $1,200/day on Nov 8; this week $1,406 per conversion; 40 keywords at QS 1 to 3 carrying $10,876 | $2,129 |
| 4 | Patio Style | 596-555-8707 | $2,234 | 12 | $186 | 52 | F | -14 | Critical | Both directions actions demoted to secondary; primary conversions 90 to 14 month over month; 11 of 12 ad groups one RSA | $88 |
| 5 | Precision GPR | 554-113-4760 | $3,049 | 19 | $160 | 53 | F | +3 | Critical | Spend up 17% and CPA up 84% versus the prior 30 days; GPR Scanning $481 for 1 conversion; no new negatives since August | $177 |
| 6 | Rover Veterinary Care | 750-667-5721 | $2,612 | 20 | $131 | 57 | F | -4 | Needs attention | In-Home Pet Euthanasia at $23 a click, $1,081 for 4.2 conversions; master negative list not attached to the two biggest campaigns; Competitors RSAs still POOR | $223 |
| 7 | All Phase Pool Remodeling | 103-111-7688 | $827 | 13 | $64 | 59 | F | -13 | Needs attention | Every primary conversion in 30 days came from a brand search term; non-brand spent about $460 for 0; CPA $26 in Aug-Sep, $64 now | $92 |
| 8 | Scootz | 185-574-5478 | $1,505 | 22 | $68 | 59 | F | +1 | Needs attention | Form action dark 12 weeks; restructure landed Nov 3; new Brand group RSA is POOR; budget to $75/day Nov 8 | none confirmed |
| 9 | Florida Sealcoating | 168-852-7101 | $2,870 | 21 | $137 | 61 | D | -2 | Needs attention | Sep 4 competitor negatives still missing after 9 weeks; this week 2 conversions on $540; 1-8-333-PAVEIT action zero in 90 days | $147 |
| 10 | Quality Paralegal Services | 447-153-2607 | $1,397 | 42 | $33 | 65 | D | new | Needs attention | CPA $13 in Aug, $18 in Sep, $33 now as the Smart campaign was paused; QS 1 on "family law attorney near me" ($278); attorney and abogado queries on a paralegal account | $43 |
| 11 | Aqua Coat Pool Plastering | 285-714-0527 | $456 | 14 | $33 | 66 | D | +2 | Needs attention | 248-member master list still attached only to the paused campaign; Pool Equipment group still live matching supplier queries | $100 |
| 12 | M&S Asphalt Paving | 827-724-4095 | $756 | 6 | $126 | 66 | D | reactivated | Needs attention | Orlando Metro served 2 days and Sealcoating 5 days in 30; one RSA in 7 of 8 groups; CPA $56 in Sep, $126 now | $98 |
| 13 | The Counseling Group | 657-069-3617 | $595 | 1 | $595 | 67 | D | +1 | Needs attention | Tel-tap action now records (5 in Oct) but shows 0 in the Conversions column; 1 form lead in 30 days; QS 2 on "therapist near me" | $58 |
| 14 | Rover Reno PPC | 961-477-3743 | $719 | 18 | $40 | 69 | D | new | On target | CPA equals the $40 target; 47% lost to budget at $25/day; one RSA, AVERAGE | $127 (competitor hospital names, some convert) |
| 15 | Affordable Critter Solutions | 227-108-4521 | $294 | 14 | $21 | 78 | C | +2 | On target | Clean; $10/day still loses 18 to 42% of impressions to budget | none confirmed |
| none | Color Masters | 426-092-9847 | $667 | 0 | n/a | n/a | paused | n/a | Paused | REK-built painting campaigns; $1,019 in October for 3 conversions; Tom paused all three Oct 12 to 22 | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | n/a | was Critical | LSA only | The search campaign no longer exists; the LSA spent $2,423 for 19 leads. The COMPROMISED_SITE item is closed by removal | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 | 0 | n/a | n/a | no spend | n/a | Paused (search) | "Orlando" campaign still ENABLED and NOT_ELIGIBLE, nothing leaking | n/a |
| none | ProShield | 771-172-8482 | $304 | 1 | n/a | n/a | not REK | new | Client-run | One PMax campaign, paused Nov 2 by info@proshieldgd.com; no REK edits | n/a |
| none | Jupiter Boat Supply | 216-859-2093 | $0 | 0 | n/a | n/a | paused | n/a | Paused | No change | n/a |
| none | REK Marketing (own account) | 390-315-5264 | $895 | 1 | n/a | n/a | internal | n/a | Internal | Tom re-enabled Philadelphia and San Diego lead campaigns Oct 29; $654 this week, 1 conversion. Not a client account | n/a |

Excluded from scoring per protocol: Byers Fence ($1,529 in 30 days, client-run), Byers Fence (LSA), Herrell Plumbing (LSA plus client Smart campaigns; see attention item 7 for the new search and PMax campaigns Tom enabled Nov 2), Citrus Landscape Solutions x3, Spectrum Electric, Roeling Green Lawns, ABC Pressure Wash, Statewide Home Remodeling, Color Masters LSA, All Phase Orlando LSA.

## Week over week (Nov 2 to 8 against Oct 26 to Nov 1, search, PMax and display only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| American Impact | $3,882 to $7,029 (+81%) | 224 to 359 | 2.8% to 3.6% | $17.33 to $19.58 | 14 to 5 | $277 to $1,406 | Off target. Search CPC $59 to $121; PMax $863 to $2,519 for 1 conversion |
| Filutowski Eye Institute | $3,071 to $2,974 (-3%) | 175 to 217 | 5.3% to 5.6% | $17.55 to $13.71 | 22 to 36 | $140 to $83 | Improving after the Oct 29 budget cut on Brand Awareness ($455 to $211/day) |
| Progetto Shades | $837 to $852 (+2%) | 177 to 186 | 5.7% to 5.5% | $4.73 to $4.58 | 0 to 0 | n/a | Off target, two weeks without a conversion |
| Precision GPR | $917 to $702 (-23%) | 68 to 53 | 6.1% to 4.5% | $13.48 to $13.25 | 5 to 6 | $183 to $117 | Budget cuts Nov 6; this week on plan |
| Patio Style | $502 to $683 (+36%) | 186 to 186 | 6.9% to 7.7% | $2.70 to $3.67 | 4 to 5 | $126 to $137 | Outdoor Kitchens moved to Manual CPC Nov 1: CPC $3.48 to $11.54, 88% lost to budget |
| Rover Veterinary Care | $683 to $654 (-4%) | 47 to 49 | 13.4% to 12.0% | $14.54 to $13.36 | 7 to 5 | $98 to $131 | In-Home Pet Euthanasia CPC $25 to $32 |
| Florida Sealcoating | $641 to $540 (-16%) | 75 to 106 | 5.5% to 7.6% | $8.55 to $5.10 | 7 to 2 | $92 to $270 | Off target this week; Residential 3 to 0 conversions |
| Scootz | $319 to $389 (+22%) | 378 to 424 | 7.0% to 6.7% | $0.84 to $0.92 | 5 to 3 | $64 to $130 | First week after the Nov 3 restructure; too early |
| Quality Paralegal | $316 to $352 (+11%) | 93 to 115 | 5.3% to 5.4% | $3.39 to $3.06 | 5 to 9 | $63 to $39 | Recovering; campaign 1 lost 82% of impressions to rank |
| All Phase Pool Remodeling | $168 to $221 (+32%) | 15 to 30 | 3.4% to 5.2% | $11.18 to $7.36 | 1 to 4 | $168 to $55 | Better week, brand-driven |
| M&S Asphalt Paving | $183 to $221 (+21%) | 18 to 18 | 9.1% to 9.3% | $10.19 to $12.26 | 1 to 3 | $183 to $74 | Volusia converting; Orlando Metro served 2 days |
| Rover Reno PPC | $151 to $217 (+44%) | 52 to 54 | 10.8% to 10.1% | $2.91 to $4.02 | 5 to 4 | $30 to $54 | Flat, within target |
| The Counseling Group | $155 to $188 (+21%) | 37 to 44 | 5.4% to 4.6% | $4.18 to $4.26 | 0 to 1 | n/a to $188 | Small numbers, normal |
| Aqua Coat | $119 to $91 (-24%) | 26 to 14 | 5.4% to 5.2% | $4.58 to $6.50 | 4 to 4 | $30 to $23 | Flat |
| Affordable Critter Solutions | $63 to $70 (+10%) | 13 to 18 | 8.5% to 7.0% | $4.85 to $3.86 | 2 to 4 | $32 to $17 | Flat |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: Quality Paralegal campaign 1 at 82 percent, Progetto Exterior & Patio 72 percent, Affordable Critter 69 percent, Patio Style Outdoor Furniture 64 percent, Precision GPR DSA 58 percent, Progetto Shades & Blinds 55 percent, Aqua Coat 51 percent. Where Quality Score is 1 to 3 (Progetto, Quality Paralegal, American Impact) the rank loss is a quality problem, not an auction problem. Rover In-Home Pet Euthanasia holds 82 percent absolute top at $23 to $32 a click, which is the opposite problem: paying for position it does not need.

## Changes made in the past week (Nov 2 to Nov 9) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Scootz | Nov 3 | Tom | Restructure: 29 keyword status changes, 4 ad group updates. Live groups are now Brand (1 keyword), Brand - Legacy (3), Disney (7), Universal (1), ECV and Wheelchair (5), Orlando Generic (12), Folding and Portable (1) | Legacy group still carried $1,197 of the $1,505 in 30 days. This week 3 conversions on $389. The new Brand RSA is POOR. Measure again Nov 16 |
| Scootz | Nov 8 | justin.mccarthy088@gmail.com (client) | Budget $50 to $75 a day | None yet. Client-initiated 50 percent raise on a Target Spend campaign with a dark form action |
| Precision GPR | Nov 6 | Dave (sheokand003) | Six budget cuts: Location $18 to $13, Services $18 to $13, GPR Scanning $15 to $12 to $10, Utility Mapping $15 to $12, Branded $10 to $8 (Tom had cut GPR Scanning $20 to $15 on Oct 21) | Daily budgets now total $84, matching Tom's $82 target. This week $702 for 6 conversions at $117 |
| Patio Style | Nov 1 | Paid Ads (paidads@) | Outdoor Kitchens from Target Spend ($7 ceiling) to Manual CPC with enhanced CPC | CPC $3.48 to $11.54, impressions 522 to 114, 88 percent lost to budget, 2 conversions on $196 |
| Patio Style | Nov 2 and 5 | Paid Ads | 5 keyword status changes, 2 ad group changes, 3 assets | Too early |
| Progetto Shades | Nov 5 | Tom | 6 campaign assets, 1 asset update (after Oct 30 Shades & Blinds budget $40 to $50 and Oct 26 CPC ceilings $12 to $10, $12 to $9, $18 to $12) | Zero conversions this week on $852 |
| Quality Paralegal | Nov 2 | Tom | 6 campaign negatives | 9 conversions this week at $39, up from 5 at $63 |
| Rover Veterinary Care | Nov 9 | Dave | One ad update (today) | Not measurable |
| American Impact | Nov 3 to 8 | 57clicks and client | 12 campaign negatives (57clicks); client re-enabled PMax, Search, Bathroom and Home Renovation Nov 5 to 7; client set Search budget $406 to $1,200 a day Nov 8 | See attention item 2 |
| Herrell Plumbing | Nov 2 and 6 | Tom | Search campaign enabled with $33 a day, PMax budget $78.57 a day, content network off Nov 6 | $238 search and $259 PMax this week, 4 conversions. Account is marked LSA-only in the protocol; context needs updating |
| Citrus Sanford and St. Pete | Oct 28 (serving from Nov 7) | Robbie | Pay-per-lead PMax budgets $357 and $214 a day | $1,106 and $376 in two days, 13 conversions. Out of scope, for the record |
| REK Marketing | Oct 29 to Nov 6 | Tom | Philadelphia and San Diego lead campaigns re-enabled; 500 edits in 30 days | $654 this week, 1 conversion (GBP Free Read) |
| Straightline Fence | Nov 2 and 3 | Robbie | LSA paused and re-enabled, budget $85.71 to $71.43, 12 criteria | Out of scope |
| Florida Sealcoating, Rover, Aqua Coat, All Phase, Counseling Group, Affordable Critter, Rover Reno, M&S | | | No bid, keyword, budget or negative changes Nov 2 to 8 (Dave added assets to several on Nov 4 to 6) | |

### Sep 14 action plan reconciliation

Landed: Scootz restructure (item 4, second half, done Nov 3 without the form fix first); Counseling Group medication negatives (antidepressant and supplements are phrase negatives now); Precision GPR GPR Scanning budget cut (item 5, partly); Patio Style second RSA in Patio Furniture (one group of the three asked). Not landed: Scootz form test and restore (item 4, first half), Precision GPR negatives list (item 5), Rover manual conversion test and negatives and POOR RSAs (item 6), Florida Sealcoating competitor negatives and Branded match types (item 7), Aqua Coat master list attachment (item 8), Counseling Group tel-tap test (item 9, though the action now records), Patio Style directions double-count check (item 10, now moot since both are secondary), All Phase brand split (item 11), Affordable Critter budget ask (item 11), Progetto bidding during learning (item 11, Tom moved everything to Target Spend with ceilings Oct 20 to 26, which is the suggested direction). Filutowski scope (item 2) and Straightline (item 3) are still open as decisions.

## Deep dive 1: Progetto Shades (416-010-8247), score 45 F

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 30 |
| Account Structure | 70 |
| Keywords & Targeting | 35 |
| Ads & Assets | 55 |
| Bidding & Settings | 50 |

Snapshot, 30 days: six search campaigns, all Target Spend with CPC ceilings since Oct 20 to 26. $2,927, 641 clicks, $4.57 CPC, 5.7 percent CTR, 2 primary conversions, 42 all-conversions (local actions). Prior 30 days: $1,680 for 9 conversions at $187.

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | Search IS | Lost to rank |
|---|---|---|---|---|---|---|---|
| Shades & Blinds | $50 | $1,200 | 321 | $3.74 | 1 | 15.0% | 56.9% |
| Shutters | $30 | $729 | 121 | $6.02 | 0 | 29.3% | 43.4% |
| Motorized & Smart | $16 | $436 | 69 | $6.32 | 0 | 24.4% | 53.9% |
| Drapery & Curtains | $12 | $355 | 64 | $5.55 | 1 | 21.0% | 62.1% |
| Exterior & Patio | $7 | $201 | 62 | $3.24 | 0 | 17.5% | 61.7% |
| Brand | $5 | $6 | 4 | $1.51 | 0 | 85.7% | 14.3% |

### Findings

**The form is probably not being counted.** Primary and included actions: "Calls from ads" (1 in 30 days) and "Contact" (1, last Oct 24). "Lead form website" is secondary and excluded and last recorded Oct 3. "Web form (start)" recorded on Oct 24 and Nov 7 with no completion anywhere. "Call ((858) 338-1678)" is marked primary but excluded from Conversions and fired once on Oct 27. Six GA4 actions are hidden. Not declared dead: a manual submit on progettoshades.com, then check which tag fires and whether the Ads import still points at a live GA4 event. Until that is done, zero-conversion keyword figures below are unreliable for pausing decisions.

**Quality Score floor is the worst in the fleet.** 37 of 85 keywords with impressions are QS 1 to 3 and carried $800: "shutters for windows" phrase QS 1 ($151), "window shutters" exact QS 3 ($101), "blackout curtains" exact QS 2 ($83), "smart shades" exact QS 3 ($61), "hunter douglas" phrase QS 3 ($53), "outdoor patio shades" QS 2 ($47), "somfy shades" exact QS 1 ($38). All show BELOW_AVERAGE expected CTR and most show BELOW_AVERAGE landing page experience. All nine ad groups run AVERAGE or GOOD RSAs; four groups have one RSA. Rank loss of 43 to 72 percent is this, not the auction.

**Spend concentration without a conversion.** 41 keywords over $10 with zero conversions, $2,208: "shutter store" phrase $327, "smart home shades" $202, "shutters for windows" $151, "window shutters" $101, "window drapery" exact $90, "hunter douglas blinds" $86, "blackout curtains" $83, "window shade store" $82, "best motorized shades" $75, "patio sun shade" $72. "window coverings" phrase produced the one search conversion on $460.

**Waste floor, $75:** "shutters san diego" $13.01 and "window shutters san diego" $12.68 (wrong market; the Shutters group has a "plantation shutters san diego" keyword, confirm the service area), "the blind and shutter pros" $11.10, "how much are window shutter blinds" $11.04, "smart wings blinds" $11.02, "matter smart roller shade motor" $8.14, "normanusa" $8.14. Dedupe against the 333-member iLP Global Negatives list: diy, how to, amazon, ikea, home depot, lowes, target, walmart, wayfair, bed bath, blinds to go, budget blinds, 3 day blinds, curtains (exact), fabric and exterior shutters are already present. New: how much, blinds.com, smart wings, blind and shutter pros, matter, san diego (if not served), drapes (if drapery is not sold as ready-made), living room, bedroom, hurricane. Norman, Hunter Douglas and Somfy are bid on deliberately in the Designer Brands and Motorized groups, so they are not proposed.

**Bidding.** Tom moved all six campaigns from Target Impression Share to Target Spend with CPC ceilings between Oct 20 and 26 ($10 Shades & Blinds, $12 Shutters, $9 Motorized), then raised Shades & Blinds to $50 a day on Oct 30. That is the direction the Sep 14 note suggested. With no reliable conversion signal there is nothing to optimize toward, so the ceilings are doing the work.

### Prepared change list

1. Manual form submit and call test today. If the form fires in GA4 but not in Ads, re-import or recreate the action and set it primary and included. If it does not fire in GA4, the site tag is the problem.
2. Until the form is confirmed, cut Shutters to $15 a day and Motorized & Smart to $8 a day, and pause "shutter store", "smart home shades", "window shade store" and "best motorized shades" (together $686, 0 conversions, 1 all-conversion). Keep Shades & Blinds, which holds the only converting keyword.
3. Rewrite the Plantation Shutters, Drapery and Motorized RSAs with the keyword in headline 1 and a city or showroom headline, to move expected CTR and ad relevance off BELOW_AVERAGE. Add a second RSA to Exterior, Designer Brands, Brand and Plantation Shutters.
4. Negatives (phrase) to iLP Global Negatives: how much, blinds.com, smart wings, blind and shutter pros, matter, living room, bedroom, hurricane. Exact: shutters san diego and window shutters san diego if San Diego is outside the service area.

## Deep dive 2: Patio Style (596-555-8707), score 52 F, down 14

Context applied: the client's primary conversion is Get Directions, then calls, then contact forms. The protocol says not to flag directions being primary. This dive flags the opposite: directions are no longer primary.

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 55 |
| Account Structure | 70 |
| Keywords & Targeting | 55 |
| Ads & Assets | 45 |
| Bidding & Settings | 55 |

| Campaign | Bidding | Budget/day | Spend | Clicks | CPC | Primary conv | All conv | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| Outdoor Furniture | Target Spend | $30 | $902 | 631 | $1.43 | 4 | 440 | 24.3% |
| Outdoor Kitchens | Manual CPC (since Nov 1) | $20 | $550 | 119 | $4.63 | 2 | 23 | 35.7% |
| Pergolas & Louvered Roofs | Manual CPC | $25 | $535 | 46 | $11.64 | 1 | 13 | 61.5% |
| Brand | Maximize Conversions | $10 | $247 | 75 | $3.29 | 5 | 57 | 66.9% |

### Findings

**Primary conversions collapsed because the definition changed, not demand.** Primary conversions by month: August 108, September 90, October 14, November 5 so far. Directions by month, all-conversions: Google-hosted "Local actions - Directions" 63, 90, 77, 20; GA4 get_directions import 101, 102, 41, 7; "Get directions (GTM) 11 Sep" 38, 37, 6. The GA4 import and the GTM action are both secondary and excluded today; on Sep 14 the GTM action was primary and included. Conversion action edits do not appear in change history, so the date cannot be fixed from the API; the monthly numbers put it in October. Today's primary set is Calls from ads (5 in 30 days), "Website Call Conversions 11 Sep" (3) and "Thank you page 11 Sep" (4). If this was done to stop the GA4 and GTM actions double counting one tap, the fix is to keep one of them primary, not neither. The Brand campaign runs Maximize Conversions on 5 conversions in 30 days, so the demotion also starved its bidding signal.

**Outdoor Kitchens Manual CPC switch, Nov 1.** CPC went from $3.48 to $11.54 in a week, impressions fell 522 to 114, and the campaign now loses 88 percent of impressions to budget at $20 a day. Two conversions on $196 this week, after none the week before, so it is not clearly worse, but the budget was also moved $14 to $5 to $20 between Oct 27 and 28. One week of each setting is not enough to judge; the whipsaw is.

**Pergolas at $11.64 a click.** $535 for 1 primary conversion and 13 all-conversions. "pergola contractor" phrase $277 for 0, "patio cover orlando" QS 3 $64 for 0. The one RSA in New Pergolas 07 Oct is POOR.

**Keywords and ads.** 26 zero-conversion keywords over $10, $1,220, but with directions excluded most carry all-conversions ("outdoor kitchen company" 5, "outdoor kitchen design" 3, "patio furniture orlando" exact 22), so do not pause on this month's column. QS 1 to 3 on 8 keywords: "built in outdoor kitchen" QS 1, "retractable pergola" QS 1, "outdoor dining set" QS 2, "patio cover orlando" QS 3, "outdoor fire pit" QS 3. 11 of 12 ad groups still have one RSA (Patio Furniture has two, both EXCELLENT); Premium Brands is AVERAGE and New Pergolas is POOR.

**Waste floor, $88:** "pergola assembly service" $25.14, "handyman to install pergola" $12.97, "outdoor kitchen ideas" $14.93, "outdoor kitchen garage design pictures" $9.99, "pergola carport attached to house" $12.42, "show me a pergola" $12.09. Dedupe: panels, roof panels and mirador are in the 57-member Master Negatives; "ideas" and "design" exist only as exact negatives on Brand and Pergolas. New: assembly, handyman, pictures, carport, big green egg, tru island, vestivium, hampton bay, polywood. Keep azenco (a carried brand, and an ad group).

### Prepared change list

1. Ask Paid Ads which directions action should be primary. Recommendation: "Get directions (GTM) 11 Sep" primary and included (it is the site-side tap), GA4 get_directions secondary, Google-hosted Local actions left as they are. This restores the client's primary conversion to the Conversions column and to Brand's bidding.
2. Outdoor Kitchens: pick one setting and hold it two weeks. If Manual CPC stays, set max CPC at $5 on the New Outdoor Kitchens 14 Oct group; otherwise return to Target Spend with the $7 ceiling.
3. Pergolas: cap "pergola contractor" at $6 or pause it; rewrite the POOR New Pergolas RSA; add phrase negatives assembly, handyman, carport, pictures to Master Negatives.
4. Second RSAs in Outdoor Kitchens, New Pergolas and Premium Brands first (the three single-RSA groups with the most spend).
5. Negatives (phrase) to Master Negatives: assembly, handyman, pictures, carport, big green egg, tru island, vestivium, hampton bay, polywood.

## Deep dive 3: All Phase Pool Remodeling (103-111-7688), score 59 F, down 13

Context applied: two accounts by design; 918-824-8896 holds the Jacksonville LSA and is not a duplicate.

| Category | Score |
|---|---|
| Conversion Tracking | 70 |
| Wasted Spend | 50 |
| Account Structure | 50 |
| Keywords & Targeting | 50 |
| Ads & Assets | 70 |
| Bidding & Settings | 55 |

Snapshot: one search campaign, Maximize Conversions, $30 a day. 30 days: $827, 112 clicks, $7.38 CPC, 13 primary conversions at $64 (Calls From Ads 10, Call 888 2, Request quote 1). The Aug 11 to Sep 9 window was $845 for 32 conversions at $26. Impression share 11.3 percent, 55 percent lost to budget, 33 percent lost to rank.

### Findings

- **All 13 primary conversions came from brand searches.** The converting search terms are "all phase pool remodeling" in two ad groups (4 and 4 conversions, $330 together) and "all phase pool" (1). The brand keyword "all phase pool remodeling" broad sits in Pool Resurfacing ($216) and Pool Renovations ($148) and is 44 percent of spend. Non-brand keywords spent about $460 for zero primary conversions: "swimming pool renovations" broad $191 (25 all-conversions, 0 primary), "pool resurfacing companies near me" $153 (4 conversions, all brand queries matched through it), "swimming pool renovations near me" $40, "pool tile replacement" $22, "pool tile installation" $15. This is the Sep 4 brand-split item, still open, and the reason the CPA more than doubled.
- **100 percent broad match** across 25 keywords with impressions.
- **"Phone Calls 60s+" is still zero in 90 days** while "Calls From Ads" recorded 10. Both are primary and included; they are two call actions on the same calls. Test, then make one of them secondary.
- **The 379-member All Phase Master Negatives list is attached only to the paused campaign.** The live campaign runs on 91 campaign negatives. Same pattern as Aqua Coat.
- **Waste floor, $92:** "red rhino jacksonville" $28.52 (Dave added it as an exact negative Oct 22, after the click), "pinch a penny orlando" $15.67, "pinch a penny sanford" $4.90, "pool pump repair near me open now" $13.73, "aqua pool us llc" $10.54, "tempool inc jacksonville fl" $5.36, "general contractors in orlando florida" $4.62, "american pools & spas" $3.90, "keystone tile orlando" $2.69, "aqua pools" $2.12. Dedupe against the 91 live negatives: none of leslie, pinch a penny, pump repair, tempool, aqua pool, general contractor, above ground, fiberglass, cody, american pool, keystone, jacksonville exist on the live campaign.

### Prepared change list

1. Brand split: new ad group or campaign "Brand" with [all phase pool remodeling], [all phase pool], "all phase pools" exact and phrase; add phrase negative "all phase" to the three service groups. Then the service groups show their real CPA.
2. Attach All Phase Master Negatives to the live campaign; drop the duplicates from the 91 campaign negatives afterwards.
3. Phrase negatives: pinch a penny, leslie, pump repair, tempool, aqua pool, general contractor, above ground, fiberglass, cody pools, american pool, keystone, jacksonville, open now.
4. Convert "swimming pool renovations" and "swimming pool renovations near me" to phrase; $231 for 0 primary conversions on broad.
5. Test "Phone Calls 60s+" and "Calls From Ads" on one call; set the one that does not fire to secondary.

## Deep dive 4: Precision GPR (554-113-4760), score 53 F, up 3

Context applied: cleanup since Aug 2026; $2,500 monthly budget is flexible; judge on cost per conversion; flag only when spend and CPA rise together. They did: Sep 10 to Oct 9 $2,602 at $87; Oct 10 to Nov 8 $3,049 at $160. October alone was $3,163 at $138, as recorded in the protocol. This week after Dave's budget cuts: $702 for 6 at $117.

| Category | Score |
|---|---|
| Conversion Tracking | 50 |
| Wasted Spend | 45 |
| Account Structure | 50 |
| Keywords & Targeting | 45 |
| Ads & Assets | 85 |
| Bidding & Settings | 45 |

| Campaign | Budget/day (after Nov 6) | Spend | Clicks | CPC | Primary conv | CPA | This week |
|---|---|---|---|---|---|---|---|
| LP Search - Location | $13 | $591 | 24 | $24.63 | 3.0 | $197 | $121, 1 conv |
| LP Search - Services | $13 | $527 | 29 | $18.18 | 3.0 | $176 | $131, 0 conv |
| LP Search - Concrete Scanning | $18 | $498 | 24 | $20.76 | 2.5 | $199 | $96, 0 conv |
| LP Search - GPR Scanning | $10 | $481 | 31 | $15.53 | 1.0 | $481 | $93, 0 conv |
| LP Search - Utility Mapping | $12 | $434 | 38 | $11.43 | 2.5 | $174 | $112, 1 conv |
| LP DSA - All Pages | $10 | $284 | 44 | $6.46 | 5.5 | $52 | $68, 3 conv |
| LP Branded | $8 | $233 | 27 | $8.63 | 1.5 | $155 | $80, 1 conv |

### Findings

- **The DSA is now the best campaign, which reverses the Sep 4 advice to pause it.** $284 for 5.5 conversions at $52 and 25 all-conversions, with 30 percent lost to budget at $10 a day. GPR Scanning is the worst: $481 for 1 conversion, "ground penetrating radar surveys" phrase $184 for 0, "Ground Penetrating Radar" exact and phrase $182 for 0 at QS 3.
- **Conversion actions unchanged since September.** "Calls From Website (305)" and "(786)" are still primary and still zero in 90 days; "Michael Phone Number (305)" recorded 9 and lp_contact_form 6; "Contact Us", "Contact Us (1)" and "Contact us" still coexist as secondary. The manual test from Sep 4 is still due.
- **No negatives added since August.** Visible this window: "gpr scanning price" $23.14 and "ground penetrating radar price" $11.52 (price is not a negative; only "low cost" is), "mygeorgia811" $20.46, "sunshine locate" $14.04 and "sunshine811" $7.52 (811 is a broad negative and did not catch either), "call before digging florida" $10.68, "beryl project engineering" $14.34, "structural engineer" $14.58 across two rows, "gprsinc com" $11.95, "directional boring company" $11.86, "ditch witch cable locator" $11.01 (ditch witch exists only as exact), "gpr locator" $19.33, "topographical survey near me" $6.48. Waste floor $177 (sum of the lines above).
- **Do not add "gprs" as a blanket negative after all.** The Sep 4 list proposed it. This window "gprs orlando" converted 1.5 times on $36 and "gprs tampa" once on $37 in the Concrete Scanning and Services campaigns. Searchers using the competitor's name are converting. Block only the navigational variants: gprsinc, gprs inc, gprs phone number, gprs solutions, gprs company.
- **Structure.** Seven campaigns on Maximize Conversions with 1 to 5.5 conversions each. Location and Services overlap with the four service campaigns on the same queries ("gpr scanning" matched three campaigns).
- **Bidding and budget.** After Nov 6 the daily budgets total $84, which is Tom's $82 target. Branded loses 59 percent to budget at $8 a day.

### Prepared change list

1. Negatives, phrase, to LP NKWs: price, pricing, how much, georgia, sunshine, call before digging, engineer, engineering, boring, topographical, survey near me, locator (phrase, the exact variants exist). Exact: gprsinc com, gprs inc, gprs phone number, gprs solutions, gprs company, beryl project engineering, keller. Already present and skipped: low cost, 811, ditch witch (exact), equipment, rental, rentals, underground utility locator.
2. Move budget, not total: GPR Scanning $10 to $6, DSA $10 to $14. Same $84 total.
3. Manual test on the two website call actions and the three Contact Us actions; set the ones that do not fire to secondary, delete the duplicates.
4. Fold Location into the four service campaigns (its ad groups are "Gpr Scanning Orlando", "Gpr Scanning Tampa Bay", "Concrete X Ray Tampa Bay") so Maximize Conversions sees 5 to 8 conversions per campaign instead of 1 to 3.

## Deep dive 5: American Impact (974-265-3397), score 47 F, provisional

Scope note: new to the MCC since Sep 14. No REK user in 30 days of change history; the editors are contact@57clicks.com and americanimpactandenergy@gmail.com. Scored because of the size; nothing should be touched until Tom says whether REK is engaged.

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 30 |
| Account Structure | 55 |
| Keywords & Targeting | 30 |
| Ads & Assets | 70 |
| Bidding & Settings | 35 |

| Campaign | Status | Budget/day | Spend 30d | Clicks | CPC | Primary conv | CPA | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| Search / Impact Windows / Orlando For Web | enabled, learning | $1,200 (since Nov 8) | $11,283 | 189 | $59.70 | 18 | $627 | 30.0% |
| Leads-Performance Max-1 | enabled | $470 | $9,052 | 1,532 | $5.91 | 61 | $148 | 22.9% |
| AIE / Search / Kitchen Remodel | paused Oct 27 | $275 | $2,405 | 97 | $24.80 | 3 | $802 | |
| AIE / Search / Bathroom Remodel | re-enabled Nov 6 | $155 | $1,075 | 28 | $38.41 | 0 | n/a | |
| AIE / Search / Home Renovation | re-enabled Nov 7 | $156 | $480 | 22 | $21.80 | 0 | n/a | |
| RMK Display Remarketing | paused Oct 27 | $20 | $247 | 328 | $0.75 | 0 | n/a | |

Spend by window: Aug 11 to Sep 9 $3,218; Sep 10 to Oct 9 $10,049; Oct 10 to Nov 8 $24,543; October alone $26,058 for 117 conversions at $223. This week $7,029 for 5 conversions.

### Findings

- **Budget whipsaw.** The search campaign budget went $325 to $406 (Oct 12), $406 to $172 (Oct 19), $172 to $430 to $537 to $832 (Oct 27), $832 to $406 (Nov 5, 57clicks), then $406 to $1,200 (Nov 8, client). 57clicks paused Search, PMax and the LSA on Nov 5; the client re-enabled them within hours. Two hands on the account pulling in opposite directions.
- **Quality Score.** 40 keywords at QS 1 to 3 carried $10,876: "window replacement company" phrase QS 3 $5,443 for 11.7 conversions ($467), "window replacement near me" QS 3 $2,544 for 3.3 ($763), "countertop installation" QS 1 $931 for 1, "bathroom renovation" QS 3 $460 for 0. Expected CTR and landing page are BELOW_AVERAGE on all of them.
- **Waste floor, $2,129, from visible terms:** competitor and retailer names (windowwall orlando $300.81, lowes window replacement $213.66 plus $24.67, goodman windows $127.67, first choice windows ocala $105.09, armorvue $80.32 across two rows, abc impact windows $45.88, national bath program $102.37, everlasting bath $89.44, one and done bath $84.26, long home bathroom $42.71, love your bath $39.31, bathremodel tech reviews $58.66, bcs stone $57.12, mr granite graceville $55.88, elite granite melbourne $38.96, duncan stone tavares $34.24), service mismatch (commercial windows and doors $219.41, window glass replacement three rows $167.93, glass block installers $49.85), and offer-shopping ("$99 window replacement special" $143.91, free bathroom remodel $38.77, senior bathroom assistance program $7.92). 57clicks added a 21-member competitor list on Oct 27 (ADS-037), so part of this predates it.
- **Conversion tracking.** 14 primary actions including "YouTube follow-on views" and "YouTube channel subscriptions", two "Calls from ads" variants (60s version primary with 55, plain version secondary with 3), and "Submit lead form" (24 in 30 days) set secondary while the 60-second call action is the only website-side primary. The PMax campaign's 61 conversions are therefore mostly calls.
- **Ads.** Three RSAs per ad group, GOOD to EXCELLENT in the windows groups, POOR in three remodel groups.

### Prepared change list (only if Tom confirms REK is engaged)

1. Decide one owner for budgets. Hold the search campaign at $400 a day until it leaves learning; $1,200 a day at a $627 CPA is $36,000 a month for about 57 conversions.
2. Promote "Submit lead form" to primary; demote the two YouTube actions.
3. Negatives (phrase) across Search and PMax: lowes, home depot, windowwall, goodman, first choice, armorvue, abc impact, national bath, everlasting, one and done, long home, love your bath, bath fitter, re-bath, bcs stone, mr granite, elite granite, duncan stone, commercial, glass replacement, glass block, $99, free, assistance program, reviews. Dedupe against the five live shared lists: unavailable this run (the lists total 460 members; a per-term check was not done for an account REK does not edit).
4. Rewrite the three POOR remodel RSAs and split "window replacement company" and "window replacement near me" into their own ad group with a windows landing page, which is the QS 3 problem.

## No action needed this week, or holding, one-liners

- **Rover Veterinary Care (57 F, down 4):** $2,612 for 20 conversions at $131. In-Home Pet Euthanasia spent $1,081 at $23 a click for 4.2 conversions while holding 82 percent absolute top; "dog put to sleep" phrase $200 for 0, "mobile dog put down service" $349 for 1, "dog dementia when to put down" one click $73.74. The 332-member Account Negatives Master list is attached to Brand and Competitors only, not to In-Home Pet Euthanasia or Pet Cremation Services, which is why "peggy adams cremation" ($8.48), "cheap dog cremation" and "affordable dog cremation" ($18.32) got through despite peggy adams, cheap and affordable being on the list. Dave added six phrase keywords Oct 23, two of them question intent ("when is it time to euthanize a cat", "put dog down at home"), plus one exact negative for a Spanish cremation-cost query. Competitors RSAs still POOR, nine weeks after the first note. Waste floor $223: dementia $73.74, quiz $25.88, heaven at home hospice reviews $54.98, euthanize dog $27.08, euthanized dogs $14.88, peggy adams cremation $8.48, cheap and affordable cremation $18.32. Dedupe: new are when to, signs, quality of life, should i, paws to health, dementia, quiz, hospice, heaven at home, vca; present are banfield, peggy adams, cheap, affordable, memorial (exact only). Action: attach the master list to the two service campaigns, add the question-intent phrase negatives, cap In-Home at a $12 CPC or set a $150 target CPA, pause "dog put to sleep", rebuild the two POOR RSAs. Add exact "at home pet euthanasia services near me" (2 conversions across campaigns).
- **Scootz (59 F, up 1):** see attention item 6. The restructure is in; Brand - Legacy still has 3 enabled keywords and carried 80 percent of 30-day spend. Weekly clicks halved from the week of Oct 5 while spend held, so CPC went $0.71 to $1.22 over the month; cause not visible in change history (Tom's Oct 22 campaign update has no changed_fields recorded). The new Brand RSA is POOR; "scootz orlando" phrase converted 6 times on $62. Hold bids until Nov 16; do the form test first.
- **Florida Sealcoating (61 D, down 2):** daily budgets now $88 (Commercial $38, Residential $30, Branded $15, Remarketing $5) after Dave's Oct 23 and 30 cuts, which is $2,680 a month, under the $3,000 plan; not an overspend, and worth confirming with the client. 21 conversions at $137 in 30 days, 2 this week. The Sep 4 competitor and supplier negatives are still not in the 252-member master list or the 296 campaign negatives: ppg, absolute, gem seal, seal right, martin, kennedy, american asphalt, millings, cold mix, who sells are all still new, and this window adds seal master ($46 across four rows), tru mark $26.26, p&p striping $9.88, appell $7.30, g force $5.33, sealers $11.49, asphalt repair cost $11.80, hot asphalt patch $20.71, concrete crack repair $7.89. Waste floor $147. Branded still matches generic ("sealcoating orlando fl" $29.17) and the exact "florida sealcoating" keyword spent $121 for 0 primary. "Call (1-8-333-PAVEIT)" is zero in 90 days; test it. Add phrase "asphalt companies in orlando fl" (2 conversions, $94) and exact "seal coating driveway". The FL Remarketing ad is APPROVED_LIMITED for ALCOHOL_INFORMATION, which looks like a mis-review of an image asset; appeal it.
- **Quality Paralegal Services (65 D, new):** Tom-built since Oct 12, 207 edits. $1,397 for 42 conversions at $33, this week 9 at $39. Conversions were 92 and 80 in the two prior months at $13 and $18 when the Smart campaign was live (80,000 impressions a month, now 10,000). Campaign 1 reports HAS_ADS_DISAPPROVED but no enabled ad is disapproved, so the flag is on a paused or removed ad; detail unavailable. QS 1 on "family law attorney near me" broad ($278, 6 conversions), "divorce lawyers near me" and "paralegal help"; 75 percent of spend on broad. Watch item: "abogados", "attorney" and "lawyer" queries ($60 or so visible) on a non-lawyer document preparer; Florida regulates how paralegal services may advertise, so the ad copy should say non-attorney plainly. Waste floor $43: legal consultation free $11.07, emancipation at 17 $4.78, departamento de la familia $5.91, green card renewal fee $4.20, migraconnect $3.46, family court florida $3.95, free notary orlando $3.37, oficina de child support $3.29, acta de divorcio por internet $3.25. Add exact "divorce paralegal", "cheap divorce", "apostille orlando", "notario publico cerca de mi" (all converted). Two of five ad groups have one RSA plus one non-RSA ad; the Spanish RSA is POOR.
- **Aqua Coat (66 D, up 2):** 14 conversions at $33, flat. The 248-member Master Negative Lisst is still attached only to the paused campaign (worklist item 8, nine weeks). Dave swapped 22 keywords in and 17 out on Oct 22. Pool Equipment group still live: "swimming pool equipment" $97 for 1, supplier queries aquastrong, hayward, leslies, pinch a penny, pool rails. Waste floor $100 (fresh finish $15.47, aquastrong $12.09, pool rails $11.50, leslies $8.63, sekas $7.76, hayward $11.37, pinch a penny $14.42, handrail $8.10, blue science $5.43, diy $1.71, masters pool resurfacing $1.28, supplies $1.76). All of these are new to the live campaign's 89 negatives.
- **M&S Asphalt Paving (66 D, reactivated Sep 14):** Tom's account. $756 for 6 conversions at $126 (Sep window $56). Paving - Volusia carries it ($691, 6 conversions); Paving - Orlando Metro served 2 days and Sealcoating & Repairs 5 days in 30, both losing 68 to 71 percent to rank at Manual CPC. Seven of eight groups have one RSA. Waste floor $98: buds asphalt milling $24.80, all asphalt services $10.46, ecogrid $9.97, tile for driveways $9.86, driveway painting $9.83, ways to pave $9.77, pavement driveway cost $12.54, quikrete $5.99, chip seal $4.98. Phrase negatives: milling, painting, tile, ecogrid, quikrete, chip seal, ways to, cost (the "driveway cost" exact exists; use phrase).
- **The Counseling Group (67 D, up 1):** budget $26.50 a day since Oct 26, $595 in 30 days on 20 serving days, on plan. One form lead in 30 days; the tel-tap action recorded 5 in October and 1 in November in all-conversions but 0 in Conversions, which is what happens when an action is switched to primary after the conversions occurred, so the column will fill from the switch date forward; no tag problem indicated. Enhanced Conversions could not be checked through the API this run (the account-level field was removed in v26); confirm it is still off in the UI. Medication negatives landed. New small leaks, $58: ect therapy $7.93, deep breathing $7.60, four competitor names $18.77 (orlando thrive, restored purpose, la amistad, livethelife), can i go to the er $3.94, lavender $3.84, three DIY depression queries $11.91, post partum (two words) $3.99. Add phrase: ect, lavender, er, emergency, post partum, orlando thrive, restored purpose, la amistad, livethelife; "ways to", "things to help" to the DIY list. QS 2 on exact "therapist near me" and "therapist orlando" with BELOW_AVERAGE expected CTR; the Therapist Near Me group's three RSAs are all AVERAGE.
- **Rover Reno PPC (69 D, new):** one campaign, Maximize Conversions with a $40 target, $719 for 18 at $40, 47 percent lost to budget at $25 a day. One AVERAGE RSA. Broad "dog euthanasia near me" matched local hospital names; some converted (spca, blue pearl, banfield, pinion) so Tom may be keeping them on purpose. Non-converting hospital names $127. Mountain view, vca, blue pearl, klaich, vetco exist as exact negatives with "reno" in them and the queries came through without it; use phrase. Budget $25 to $35 is the one bid change worth making.
- **Affordable Critter Solutions (78 C, up 2):** 14 conversions at $21, two EXCELLENT RSAs, clean terms. "wildlife animal control" broad $19 for 0 is the only watch. $10 a day loses 18 to 42 percent to budget week to week; the $15 ask stands.
- **Filutowski Eye Institute (43 F, up 1):** Accalia cut the Brand Awareness budget from $455 to $211 a day on Oct 29 and set target CPAs Oct 15; this week improved to $83 per conversion. The broad "lasik treatment cost" keyword still spent $9,092 for 45 conversions and matched "cornea specialist" $214.67, "florida eye clinic altamonte" $312.18 across two rows, "mid florida eye center" $173.48, "tomoka eye" $110.65. Branded converts at $21 and loses 84 percent to budget at $50 a day. The 18 hidden Universal Analytics goals are still set primary. Branded RSA is POOR; one RSA per group. Scope decision still open.
- **Straightline Fence:** the search campaign is gone from the account; only the LSA remains (Robbie). The Sep 14 COMPROMISED_SITE item closes as removed, not resolved. Out of scope from here.
- **Color Masters:** Tom's painting campaigns spent $1,019 in October for 3 conversions at $340 and were paused Oct 12 to 22. The 92-member REK Painting Negatives list is ready for a relaunch. Report as paused.
- **All Phase Jacksonville:** "Orlando" campaign ENABLED but NOT_ELIGIBLE (ad groups paused, missing lead form). Pause it when convenient.
- **ProShield:** client-run PMax, $304 for 1 conversion, paused Nov 2 by the client. No REK edits. Needs a scope note.
- **Jupiter Boat Supply:** paused, nothing to do.
- **REK Marketing (own account):** Philadelphia and San Diego lead campaigns live again since Oct 29 at $25 a day each, $654 this week, 1 conversion (GBP Free Read). Not scored.

Out of scope, for the record only: Citrus Landscape Solutions LSA spend $7,497 Sanford, $4,328 St. Pete, $804 Sarasota in 30 days plus the new Pay-per-lead PMax campaigns in attention item 7; Herrell Plumbing LSA $2,121 and client Smart campaigns $1,683 (both paused by Oct 30), with Tom's new search and PMax campaigns live since Nov 2; Byers Fence (LSA) $1,940; Straightline LSA $2,423; All Phase Orlando LSA $517; Roeling Green Lawns $176; ABC Pressure Wash, Spectrum Electric, Statewide Home Remodeling $0.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Progetto (deep dive 1 item 4), Patio Style (deep dive 2 item 5), All Phase (deep dive 3 item 3), Precision GPR (deep dive 4 item 1, and do not add plain "gprs"), American Impact (deep dive 5 item 3, if engaged), Rover (when to, signs, quality of life, should i, paws to health, dementia, quiz, hospice, heaven at home, vca; plus attach the master list), Florida Sealcoating (ppg, absolute, gem seal, seal right, martin, kennedy, american asphalt, millings, cold mix, who sells, seal master, tru mark, p&p, appell, g force, sealers, repair cost, hot patch, concrete), Aqua Coat (fresh finish, aquastrong, rails, leslie, sekas, hayward, pinch a penny, handrail, blue science, supplies, pump, heater, diy; plus attach the master list), Counseling Group (ect, lavender, er, emergency, post partum, orlando thrive, restored purpose, la amistad, livethelife, ways to, things to help), Quality Paralegal (free consultation, emancipation, departamento, oficina, renewal fee, family court, por internet), M&S (milling, painting, tile, ecogrid, quikrete, chip seal, ways to, cost phrase), Rover Reno (phrase versions of mountain view, vca, blue pearl, klaich, vetco, mount rose, monte vista, battle born).

New keywords to add: Florida Sealcoating phrase "asphalt companies in orlando fl" (2 conversions, $94) and exact "seal coating driveway" (1, $40); Rover exact "at home pet euthanasia services near me" (2 conversions in two campaigns); Quality Paralegal exact "divorce paralegal", "cheap divorce", "apostille orlando", "notario publico cerca de mi"; Aqua Coat exact "pool repair tampa" (1, $22); Scootz keep "scootz orlando" phrase in the new Brand group (6 conversions, $62); Precision GPR exact "gpr services near me" (1, $72) already covered by "Gpr Scanning Near Me", no add.

Bid and budget adjustments: Progetto Shutters $30 to $15 and Motorized $16 to $8 until tracking is confirmed; Patio Style Outdoor Kitchens hold one setting, Pergolas cap $6; Precision GPR GPR Scanning $10 to $6 and DSA $10 to $14; Rover In-Home Pet Euthanasia $12 CPC cap or $150 target CPA; Rover Reno $25 to $35; Affordable Critter $10 to $15 (client decision); American Impact search $1,200 to $400 a day (if engaged); All Phase non-brand to phrase match after the brand split.

Competitive read (rank-lost share as the proxy): Quality Paralegal campaign 1 lost 82 percent to rank this week at QS 1 to 5, a quality story; Progetto 43 to 72 percent at QS 1 to 3, quality; Affordable Critter 69 percent and Aqua Coat 51 percent on $10 and $15 budgets, a budget story; Patio Style Outdoor Furniture 64 percent at a $1.43 CPC by design; Rover In-Home 82 percent absolute top, overbidding; Filutowski 84 to 90 percent lost to budget everywhere, a budget allocation story (Branded starved, Brand Awareness fed).

## Prioritized weekly action plan

1. **Critical, Tom today: American Impact scope and the $1,200 a day budget.** Decide whether REK is engaged. If yes, deep dive 5 items 1 and 2 first. If no, say so and the routine reports it as excluded. Either way the client should know what $1,200 a day buys at a $627 CPA.
2. **Critical, Tom today: Progetto Shades form test.** Deep dive 1 item 1, then the budget cuts in item 2 until the form is confirmed. $1,689 in two weeks with nothing to show is the most urgent REK-managed problem.
3. **Critical, Paid Ads this week: Patio Style directions.** Confirm which directions action should be primary and restore it (deep dive 2 item 1). Then hold Outdoor Kitchens on one bidding setting for two weeks.
4. **Critical, Dave: Precision GPR negatives and the DSA budget swap.** Deep dive 4 items 1 and 2. The budget cuts landed; the negatives have waited since August. Keep "gprs" bidding, block only the navigational variants.
5. **High, Dave: Rover.** Attach the master list to In-Home Pet Euthanasia and Pet Cremation Services, add the question-intent negatives, cap In-Home bids, pause "dog put to sleep", rebuild the two POOR Competitors RSAs (nine weeks open).
6. **High, Dave: All Phase brand split and master list attachment.** Deep dive 3 items 1 to 3. Every conversion this month was brand.
7. **High, Tom: Scootz form test** before judging the restructure or the client's budget raise. Rebuild the POOR Brand RSA.
8. **High, Dave: Florida Sealcoating** competitor and supplier negatives (nine weeks), Branded to exact and phrase with generic negatives, PAVEIT call test, confirm the $2,680 a month pace with the client.
9. **Medium, Tom: Quality Paralegal** attorney and abogado query review for compliance, second RSAs, convert "family law attorney near me" to phrase.
10. **Medium, Dave: Aqua Coat** attach the master list, pause Pool Equipment or add the supplier negatives.
11. **Medium, Tom: M&S** second RSAs, fix Orlando Metro and Sealcoating serving (bids or budgets), the nine negatives.
12. **Low: Counseling Group** eleven small negatives and the Therapist Near Me RSAs; **Rover Reno** budget $25 to $35 and phrase competitor negatives; **Affordable Critter** budget ask; **All Phase Jacksonville** pause the Orlando campaign; **Filutowski** scope decision still open.

## Proposed protocol context updates (for Tom to confirm, not applied)

- American Impact (974-265-3397): linked since October; edited by 57clicks and the client; scope undecided.
- Quality Paralegal Services (447-153-2607): REK-managed search since Oct 12 (Tom). Non-lawyer document preparer; watch attorney-intent queries and ad copy.
- Rover Reno PPC (961-477-3743): REK-managed search, Reno NV market for Rover Veterinary Care; one campaign, $40 target CPA.
- M&S Asphalt Paving (827-724-4095): reactivated Sep 14, 2026 (Tom); three Manual CPC campaigns.
- Color Masters (426-092-9847): REK-built, paused Oct 22, 2026; Color Masters LSA (163-445-9282) is LSA-only.
- ProShield (771-172-8482): linked, client-run, not REK-managed.
- Herrell Plumbing: Tom enabled "Herrell Plumbing - Search" and a Pay-per-lead PMax on Nov 2, 2026. If these are REK-run, the LSA-only note is out of date.
- Straightline Fence: search campaign removed; LSA only. Remove from the search fleet.
- Citrus Landscape Solutions Sanford and St. Pete: Pay-per-lead PMax campaigns live since Nov 7 with $357 and $214 a day budgets (Robbie). Out of scope unless Tom says otherwise.
- REK Marketing (390-315-5264): REK's own account; exclude from client scoring.
- Patio Style: record which directions action is the intended primary once Paid Ads answers.

## Rotation

Deep-dived this run: Progetto Shades, Patio Style, All Phase Pool Remodeling, Precision GPR, American Impact. Due Nov 16: Rover Veterinary Care (carried), Scootz (post-restructure measurement), Florida Sealcoating (carried). Nov 23: Quality Paralegal, Rover Reno, M&S Asphalt (first full dives for the new and reactivated accounts). Nov 30: The Counseling Group, Aqua Coat, Affordable Critter.

## Data notes

- Account discovery returned 33 client accounts against 26 on Sep 14; the seven additions are listed in attention item 1. No removals. Compare next week against this run's list.
- The google-ads Python client installed this run (35.0.0) ships API versions v23 to v26 only; v22 raised "service does not exist". The run used v26 and tools/gaql.py now defaults to it. Two v26 field changes: campaign.start_date and end_date are gone from the campaign resource query, and customer.conversion_tracking_setting.enhanced_conversions_for_leads_enabled no longer exists, so the Enhanced Conversions check for healthcare accounts relied on the per-action settings and should be confirmed in the UI.
- The recommendation impact fields are no longer selectable in v26; recommendation counts are available (for example Filutowski 103, Florida Sealcoating 94, Progetto 82) but types came back empty and were not used.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor, and every floor lists its components.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history covers Oct 11 to Nov 9 (30-day API limit). Conversion action edits are not included, which is why the Patio Style demotion and the Counseling Group tel-tap promotion cannot be dated from the API.
- Score deltas span eight weeks (Sep 14 to Nov 9) because the Sep 21 to Nov 2 runs left no reports in this repo.
- Deep dive 5 (American Impact) negative dedupe was not performed against the account's five shared lists; stated as unavailable rather than guessed.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
