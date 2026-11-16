# PPC Weekly Audit - 2026-11-16 (Google Ads fleet)

Run: Monday Nov 16, 2026, scheduled cloud session through tools/gaql.py (API v24, the installed client no longer ships v22) against MCC 656-695-7229. Windows: 30 days Oct 17 to Nov 15; this week Nov 9 to Nov 15; last week Nov 2 to Nov 8. Score deltas are against the Sep 14 report, the last run; there was no run in between, so "delta" covers nine weeks. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: American Impact (new, largest spend), Progetto Shades (worst CPA), Patio Style (10-point drop), Rover Veterinary Care (12-point drop, paused), Precision GPR (measuring the cleanup), Filutowski Eye Institute (scope still open). One-liners for the rest.

The google-ads.yaml from the Drive folder dave-ads-setup (Sep 8 version) was copied with mode 600, used only by the client library, and deleted before this report was written. No value from it appears anywhere in the session output.

## Attention items (read first)

1. **Rover Veterinary Care (750-667-5721) has no enabled campaigns. Dave paused all four live search campaigns at 00:35 on Nov 15** (In-Home Pet Euthanasia, Pet Cremation Services, Competitors, Brand Campaign). The account spent $2,795 for 20 primary conversions in the 30 days before that and $751 for 4 conversions last week. Nothing in the API says why. If this was the client's request, record it in the protocol context; if not, the account has been dark since Saturday.
2. **American Impact (974-265-3397) is new under the MCC and is now the largest account in the fleet: $22,997 in 30 days outside LSA for 44 primary conversions, $523 each.** Tom took over editing on Nov 9 from 57clicks (contact@57clicks.com) and the client, and has already cut the search budget from $1,200 to $300 a day and paused three remodel campaigns. The search campaign still pays $64.74 a click on average and this week spent $3,814 for 2 conversions. Deep dive 1 has the change list.
3. **Progetto Shades (416-010-8247) has recorded zero primary conversions since Oct 27 on $2,400 of spend.** 30 days: $3,304, 2 conversions. All six campaigns are on Maximize Clicks, 41 keywords sit at Quality Score 1 to 3 and carry $1,704 (52 percent of spend), with landing page experience Below Average on every one of them. The lead-form actions are secondary and one of them ("Lead form website") last fired Oct 3. Not declared dead: a manual form and call test is the first step. Deep dive 2.
4. **Patio Style (596-555-8707) no longer counts Get Directions as a conversion.** Both directions actions (the GA4 import and the Sep 11 GTM action) are now secondary. The protocol says directions as primary is the client's intent. Primary conversions fell from 166 (Sep 14 window) to 12, which is a configuration change, not a performance collapse, but the account now optimizes on 12 conversions a month and the pergola campaign has spent $664 for zero. Deep dive 3.
5. **Filutowski Eye Institute (192-870-7876): still no REK user in change history (only catie@accaliamarketing.com, three budget cuts on Oct 29), but REK built the new website that launched in late October** (Tom's sheet "FEI New Website URL Changes (for Google Ads)", Oct 19). The sheet says the Contact form must not be counted as a conversion and the old thank-you URLs stop firing at launch. In Google Ads, "Contact Page Form Submit (1)" is still primary and the Cataracts campaign still sends traffic to /cataract-surgery/, which now redirects. Enhanced Conversions for leads is ON in a healthcare account. Scope decision still needed; deep dive 6.
6. **Precision GPR: Dave added "gprs scanning" as a keyword on Nov 15.** GPRS is Ground Penetrating Radar Systems Inc., the national competitor whose name has leaked through search terms since August ("gprs orlando", "gprs tampa", "gprsinc com", $140 this window). The Sep 4 list asked for "gprs" as a negative. This week the account spent $456 for zero primary conversions.
7. **Eight accounts are new under the MCC since Sep 14 and none vanished.** Premium Medication Refills and Premium Walk-In Clinic remain unlinked as expected. New: American Impact, American Impact Windows & Doors LSA, Color Masters, Color Masters LSA, ProShield, Quality Paralegal Services, Rover Reno PPC, All Phase Pool Remodeling (Orlando LSA). Scope and context for each is in the Coverage section; the protocol's Known account context needs entries for them (see Data notes).

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 34 client accounts, 1 manager | 15 | 8 new since Sep 14, 0 vanished. Excluded: Byers Fence x2 (not REK-managed), Herrell Plumbing (LSA plus client Smart campaigns per protocol, but see Data notes), ProShield (client-run search and LSA, San Diego garage doors, no REK edits), 9 LSA-only accounts. Not scorable: 5 paused or zero-search accounts. REK Marketing's own account is listed but not scored. |

Search, Performance Max and Display spend in the 30-day window: $44,095 across the 14 REK-managed scored accounts, plus $11,696 at Filutowski Eye Institute and $1,407 in REK Marketing's own account. Local Services campaigns are excluded from every figure in this report. The three Citrus Landscape Solutions accounts now also run Google "Pay-per-lead" Performance Max campaigns ($3,164 Sanford, $1,579 St. Pete in 30 days, Robbie edited budgets Oct 28); they stay out of scope with the LSA work until Tom says otherwise.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical (F), Needs attention (D), On target (C or better).

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $11,696 | 122 | $96 | 45 | F | +3 | Critical (scope) | "lasik treatment cost" broad still 59 percent of spend ($6,891, $191 CPA) matching other clinics; Contact form counted as a conversion against REK's own site spec; Enhanced Conversions ON in a healthcare account | $1,208 |
| 2 | Rover Veterinary Care | 750-667-5721 | $2,795 | 20 | $140 | 49 | F | -12 | Critical (paused) | All four live campaigns paused by Dave on Nov 15; no enabled campaigns remain; euthanasia campaign was paying $26.50 a click at a $299 CPA | $172 |
| 3 | American Impact | 974-265-3397 | $22,997 | 44 | $523 | 51 | F | new | Critical | Search campaign $12,560 at $64.74 CPC for 15 conversions; competitor and retail brand queries cost $2,234; 9 conversions in the last two weeks on $13,900 | $2,234 |
| 4 | Progetto Shades | 416-010-8247 | $3,304 | 2 | $1,652 | 51 | F | relaunch | Critical | Zero primary conversions since Oct 27; 41 keywords at QS 1 to 3 carrying $1,704; every campaign on Maximize Clicks | $65 |
| 5 | Patio Style | 596-555-8707 | $2,411 | 12 | $201 | 56 | F | -10 | Needs attention | Directions no longer primary (config change); Pergolas $664 for 0 conversions at $13.28 CPC; 11 of 12 ad groups still one RSA | $104 |
| 6 | Precision GPR | 554-113-4760 | $2,801 | 18 | $156 | 56 | F | +6 | Needs attention | Competitor "gprs scanning" added as a keyword Nov 15; zero conversions this week; Location and DSA campaigns still live (Sep 4 list) | $268 |
| 7 | M&S Asphalt Paving | 827-724-4095 | $920 | 6 | $153 | 60 | D | reactivated | Needs attention | Three campaigns live since September (was reported paused); "driveway paving" phrase duplicated in two campaigns, $216 for 0 conversions; 7 of 8 ad groups one RSA | $118 |
| 8 | Quality Paralegal Services | 447-153-2607 | $1,350 | 41 | $33 | 63 | D | new | Needs attention | Healthy numbers; 76 percent broad match, top keyword "family law attorney near me" at QS 1; all five ad groups one RSA, one POOR | $54 |
| 9 | Rover Reno PPC | 961-477-3743 | $857 | 23 | $37 | 64 | D | new | Needs attention | Tom rebuilt it Nov 6 to 12; four new Maximize Conversions campaigns losing 90 percent of impressions to budget at $35 a day; all seven ad groups one RSA | $7 |
| 10 | All Phase Pool Remodeling | 103-111-7688 | $824 | 14 | $59 | 65 | D | -7 | Needs attention | Brand still inside non-brand groups ($305 of $824); 100 percent of spend on broad match; "Phone Calls 60s+" still zero since it was built | $79 |
| 11 | Aqua Coat Pool Plastering | 285-714-0527 | $435 | 13 | $33 | 65 | D | +1 | Needs attention | 248-member master negative list still attached only to the paused campaign; Pool Equipment group live, "swimming pool equipment" $117 for 1 conversion | $105 |
| 12 | Scootz | 185-574-5478 | $1,753 | 26 | $67 | 66 | D | +8 | Needs attention | Restructured into seven themed groups Nov 3 (worklist 17 done); 26 conversions now support Maximize Conversions; 6 of 7 groups one RSA; form_submit still dark | $21 |
| 13 | Florida Sealcoating | 168-852-7101 | $2,748 | 25 | $110 | 68 | D | +5 | Needs attention | Brand keywords pay $10.40 a click at QS 10 on Maximize Conversions; competitor negatives from Sep still missing (garcia, stripe it rite); "asphalt patch repair" QS 3 $98 for 0 | $132 |
| 14 | The Counseling Group | 657-069-3617 | $597 | 1 | $597 | 68 | D | +2 | Needs attention | 1 primary conversion in 30 days; tel-tap action now records (resolved); "counseling winter park" $204 for 0 primary; ads moved to the Winter Park page Oct 20 (worklist 11 done) | $34 |
| 15 | Affordable Critter Solutions | 227-108-4521 | $303 | 12 | $25 | 75 | C | -1 | On target | Clean; 11 paused campaigns still present; $10 a day losing 29 percent to budget at a $25 CPA | none confirmed |
| own | REK Marketing | 390-315-5264 | $1,407 | 1 | n/a | n/a | internal | n/a | Internal | Three manual-CPC lead campaigns (GBP Verification, San Diego, Philadelphia) losing 50 to 78 percent to budget; $1,173 on zero-conversion keywords | n/a |
| none | Color Masters | 426-092-9847 | $0 this week | 0 | n/a | n/a | paused | n/a | Paused | REK-built painting account; Tom paused Residential and Commercial on Oct 22 after $1,602 and 3 conversions since September | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | LSA only | was no spend | Out of scope | The disapproved search campaign is gone; the account is LSA only now ($2,439, 21 leads at $116 in 30 days). Worklist item 18 closed | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | no search spend | n/a | Paused (search) | The leftover "Orlando" campaign is still ENABLED at $49 a day and still spends nothing (worklist item 6 open) | n/a |
| none | Jupiter Boat Supply | 216-859-2093 | $0 | 0 | n/a | n/a | paused | n/a | Paused | Two Shopping campaigns paused, no changes | n/a |

## Week over week (Nov 9 to 15 against Nov 2 to 8, search, PMax and display only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| American Impact | $7,023 to $6,877 (-2%) | 354 to 1,561 | 3.6% to 2.2% | $19.84 to $4.41 | 5 to 4 | $1,405 to $1,719 | PMax clicks 308 to 1,477 after Tom's Nov 9 settings; search $3,998 to $3,814 for 4 then 2 conversions |
| Filutowski Eye Institute | $2,974 to $2,185 (-27%) | 217 to 150 | 5.6% to 7.2% | $13.71 to $14.56 | 37 to 21 | $80 to $104 | Budgets cut Oct 29; Eye Surgery and LASIK lead-gen 0 conversions this week |
| Progetto Shades | $852 to $801 (-6%) | 186 to 189 | 5.5% to 4.3% | $4.58 to $4.24 | 0 to 0 | none | Third week at zero |
| Precision GPR | $702 to $456 (-35%) | 53 to 31 | 4.5% to 6.2% | $13.25 to $14.69 | 6 to 0 | $117 to none | Budgets cut Nov 6; spend down and CPA up, which is the flag condition |
| Florida Sealcoating | $540 to $723 (+34%) | 105 to 109 | 7.6% to 6.3% | $5.14 to $6.64 | 2 to 7 | $270 to $103 | Dave's Nov 10 and 14 keyword work; good week |
| Patio Style | $683 to $651 (-5%) | 186 to 184 | 7.7% to 7.9% | $3.67 to $3.54 | 5 to 2 | $137 to $325 | Outdoor Kitchens 2 to 0; all_conversions 104 to 98 (directions steady) |
| Rover Veterinary Care | $654 to $751 (+15%) | 49 to 59 | 12.0% to 14.7% | $13.36 to $12.73 | 5 to 4 | $131 to $188 | Paused Nov 15 |
| Scootz | $389 to $594 (+53%) | 424 to 586 | 6.7% to 7.1% | $0.92 to $1.01 | 4 to 10 | $97 to $59 | Client raised budget $50 to $75 on Nov 8; best week since August |
| Quality Paralegal Services | $352 to $306 (-13%) | 115 to 96 | 5.4% to 5.7% | $3.06 to $3.19 | 9 to 14 | $39 to $22 | On plan |
| M&S Asphalt Paving | $221 to $276 (+25%) | 18 to 24 | 9.3% to 6.3% | $12.26 to $11.51 | 3 to 0 | $74 to none | Small numbers |
| Rover Reno PPC | $217 to $243 (+12%) | 54 to 149 | 10.1% to 11.0% | $4.02 to $1.63 | 4 to 8 | $54 to $30 | Rebuild working; CPC down 60% |
| All Phase Pool Remodeling | $222 to $197 (-11%) | 31 to 37 | 5.4% to 3.5% | $7.16 to $5.33 | 4 to 4 | $55 to $49 | Flat after Nov 10 phrase-match change |
| The Counseling Group | $188 to $118 (-37%) | 44 to 28 | 4.6% to 4.7% | $4.26 to $4.23 | 1 to 0 | $188 to none | Small numbers; $26.50 a day since Oct 26 |
| Aqua Coat | $91 to $127 (+40%) | 14 to 19 | 5.2% to 3.5% | $6.50 to $6.69 | 5 to 2 | $18 to $64 | Small numbers |
| Affordable Critter Solutions | $69 to $84 (+22%) | 18 to 23 | 7.0% to 7.8% | $3.86 to $3.66 | 4 to 4 | $17 to $21 | Flat |
| REK Marketing (own) | $654 to $512 (-22%) | 66 to 60 | 3.5% to 5.6% | $9.91 to $8.53 | 1 to 0 | $654 to none | Internal |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share (30 days, impression-weighted) is the proxy. Highest rank loss: Quality Paralegal 64 percent, Affordable Critter 60 percent, Patio Style 58 percent, Progetto 56 percent, American Impact 55 percent, Aqua Coat 55 percent. Highest budget loss: Filutowski 87 percent, Rover Reno 77 percent, REK Marketing 70 percent, The Counseling Group 53 percent, All Phase 42 percent, Precision GPR 41 percent. Highest CPCs: American Impact search $64.74, Rover Vet euthanasia $26.50, Filutowski LASIK $23 to $25, Florida Sealcoating Residential $23.44, Precision GPR Location $24.22.

## Changes made in the past week (Nov 9 to Nov 16) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Rover Veterinary Care | Nov 15 00:35 | Dave (sheokand003@gmail.com) | Paused all four live campaigns | Account dark. Attention item 1 |
| American Impact | Nov 9 to 13 | Tom | Search budget $1,200 to $800 to $600 to $300 a day; LSA budget $1,377 to $143; paused Bathroom Remodel and Home Renovation (Nov 10); AI Max and asset automation off; network and enhanced CPC settings; ad schedule rebuilt (Nov 12); two LSA service criteria removed (Nov 13) | Spend $7,023 to $6,877; PMax clicks 308 to 1,477 at $1.44 a click; conversions 5 to 4. Too early. Home Renovation still spent $621 this week before the pause landed |
| Scootz | Nov 8 and 9 | Client (justin.mccarthy088@gmail.com), Tom | Budget $50 to $75; four negatives (how much, can you rent, power chair, knee scooter) | Conversions 4 to 10, CPA $97 to $59 |
| Rover Reno PPC | Nov 9 and 12 | Tom | Paused Leads-Search-1; budgets $5 to $9 and $13 to $19; geo targeting to presence on four campaigns; AI Max off; four negatives removed | Conversions 4 to 8, CPA $54 to $30, CPC $4.02 to $1.63 |
| Florida Sealcoating | Nov 10 and 14 | Dave | Six sealcoating keywords broad to phrase; "paving contractors in my area" and "asphalt repair" added; "tru mark inc" negative; device bid modifier removed; four ad edits; one keyword re-enabled | Conversions 2 to 7, CPA $270 to $103 |
| All Phase Pool Remodeling | Nov 10 | Dave | Nine tile and resurfacing keywords recreated as phrase match, one paused, one ad edit | CPC $7.16 to $5.33, conversions flat at 4 |
| Precision GPR | Nov 6 and 15 | Dave | Budgets cut on six campaigns (now $84 a day total); keywords "concrete x ray" and "gprs scanning" added; three ad edits | Spend $702 to $456, conversions 6 to 0. See attention item 6 |
| Patio Style | Nov 13 | paidads@rekmarketing.com | 14 negatives on Outdoor Kitchens ("ideas", "how much", "newage reviews") | Outdoor Kitchens $196 to $140, conversions 2 to 0; one week is too little |
| Quality Paralegal | Nov 12 and 13 | Tom | 11 campaign negatives, two campaign setting edits | Conversions 9 to 14 |
| Affordable Critter | Nov 15 | Dave | "racoons in my attic" phrase added, four keywords paused, one ad edit | Not measurable yet |
| Aqua Coat | Nov 15 | Dave | Three keywords paused | Not measurable yet |
| Progetto Shades | Nov 10 | Tom | Five ad status edits | No change in results |
| Filutowski, The Counseling Group, M&S Asphalt, Byers Fence | | | No bid, keyword, budget or negative changes this week | |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

Landed since Sep 14: item 11 (Counseling Group ads moved to /therapist-winter-park.html on Oct 20) and item 10 in effect (the tel-tap action records: 6 in 90 days); item 17 first half (Scootz split into Brand, Disney, Universal, Orlando Generic, ECV and Wheelchair, Folding and Portable on Nov 3); item 4 negatives half ("panels" and "roof panels" are in Patio Style's Master Negatives); item 15 partly ("tru mark inc" Nov 10, "sealcoat florida" phrase). Item 18 is closed because the Straightline search campaign no longer exists. Item 14 resolved differently: both directions actions are secondary now, which needs Tom's confirmation (attention item 4). Not landed: 5 (Precision GPR: Location and DSA still live, "gprs" now bid on instead of excluded), 6 (All Phase Jacksonville "Orlando" campaign still enabled), 7 (Aqua Coat master list still unattached, Pool Equipment still live), 8 (Counseling greenlit set: "help with depression" still live at $43), 12 (All Phase brand split), 13 (Patio Style Outdoor Furniture still Maximize Clicks, 11 single-RSA groups), 17 second half (Scootz to Maximize Conversions), 19 (Affordable Critter paused campaigns).

## Deep dive 1: American Impact (974-265-3397), score 51 F, new

| Category | Score |
|---|---|
| Conversion Tracking | 60 |
| Wasted Spend | 30 |
| Account Structure | 55 |
| Keywords & Targeting | 45 |
| Ads & Assets | 65 |
| Bidding & Settings | 50 |

Snapshot: Orlando impact windows and doors. 30 days outside LSA: $22,997, 2,838 clicks, 44 primary conversions, $523 per conversion. Monthly: September $2,228 for 9, October $26,058 for 117, November to date $13,900 for 9. Editors in the window: contact@57clicks.com (Oct 19 to Nov 5), the client (Nov 5 to 8), Tom (Nov 9 onward). Enhanced Conversions for leads is ON; not healthcare, acceptable.

| Campaign | Status | Bidding | Budget/day | 30d cost | Clicks | CPC | Conv | CPA |
|---|---|---|---|---|---|---|---|---|
| Search, Impact Windows, Orlando | Enabled | Maximize Conversions | $300 (was $1,200) | $12,560 | 194 | $64.74 | 15 | $837 |
| Leads-Performance Max-1 | Enabled | Maximize Conversions | $300 | $7,698 | 2,406 | $3.20 | 28 | $275 |
| AIE Search Kitchen Remodel | Paused | Maximize Conversions | $275 | $1,174 | 54 | $21.73 | 1 | $1,174 |
| AIE Search Bathroom Remodel | Paused Nov 10 | Maximize Conversions | $155 | $807 | 16 | $50.43 | 0 | none |
| AIE Search Home Renovation | Paused Nov 10 | Maximize Conversions | $156 | $641 | 16 | $40.05 | 0 | none |
| RMK Display Remarketing | Paused | Maximize Conversions | $20 | $118 | 152 | $0.77 | 0 | none |

Primary conversions in 30 days by action: Calls from ads (60s) 34, Submit lead form 8, LSA phone 6, LSA message 3, First Time Phone Call 2. "Call From Website ((689) 219-5507)" has never recorded. The GA4 "generate_lead" action (secondary) recorded 19 in the same window against 8 for the primary "Submit lead form", so the primary form action may be undercounting; compare the two against the CRM before trusting the $837 search CPA.

### Findings

**The search campaign is buying single clicks at $150 to $500.** Dated search terms: "weathertite windows reviews" $504 for 2 clicks on Nov 9, "window suppliers near me" $489 for 2 on Nov 3, "window fabricators near me" $477 for 1 on Nov 4, "mi windows series 3540" $368 for 1 on Nov 5, "window supply near me" $311 on Nov 2, "windows and doors near me" $306, "windowwall orlando" $262, "windows in orlando" $260 on Nov 12. Maximize Conversions with no CPC ceiling and a $1,200 budget is what produced these; the Nov 9 budget cut to $300 limits the damage but does not change the bid logic. Note that "weathertite" is a phrase negative in the shared list "AIE | Negativas competidores" and that list is attached to this campaign, yet the term served on Nov 9. Check in the UI whether the list attachment is active.

**Confirmed waste, 30 days: $2,234.** Competitor and retailer brands: weathertite $504, windowwall $301, lowes $239, goodman $128, ply gem $122, first choice windows ocala $105, polk county windows $99; commercial "commercial windows and doors near me" $219; and $517 in the now-paused remodel campaigns (powerhrg $172, everlasting bath $89, one and done bath $84, bathremodel tech $59, bcs stone $57, mr granite $56). Dedupe against live negatives: weathertite, lowes, first choice windows, polk county window, commercial and power home remodeling already exist (windowwall and polk county are also campaign negatives). Dropped as present. New: goodman, ply gem, mi windows, powerhrg, everlasting bath, one and done, bathremodel, reviews, supply, suppliers, fabricators, condo, aluminum.

**Keywords.** 88 percent of keyword spend is phrase match. "impact window company" phrase $1,356 for 2 conversions; "replacement windows orlando" $629 for 0; "window replacement company" $525 for 1; "window replacement orlando" $260 for 0. Quality Score 1 to 3 on 16 keywords ($544), led by "impact resistant windows" exact and phrase at QS 2 ($374 for 0 primary, 13 all-conversions) and "window replacement near me" QS 3 ($142 for 0). Landing page Below Average on most of them.

**Ads.** Three live ad groups; Window Replacement has one RSA. Strengths: 2 EXCELLENT, 2 GOOD, 3 AVERAGE.

**Bidding.** Maximize Conversions on a campaign that produced 15 conversions in 30 days at $837 is the wrong tool until the cost per click is contained. PMax at $275 per conversion is the better half of the account and its 24 percent budget loss is the cheaper place for the next dollar.

### Prepared change list (suggestions only)

1. Search campaign: switch to Maximize Conversions with a target CPA of $300 (October's blended figure was $223) or, simpler, to Maximize Clicks with a $25 CPC ceiling for two weeks while the negatives settle. Either stops the $250 to $500 clicks.
2. Add the new negatives above as phrase to "AIE | Negativas competidores" (brands) and to the search campaign (supply, suppliers, fabricators, reviews, condo, aluminum). Verify the shared list is actually applied.
3. Pause "replacement windows orlando" phrase ($629, 0) and "window replacement orlando" phrase ($260, 0); keep "impact windows orlando" exact and add exact "impact windows orlando fl", "hurricane impact windows orlando", "impact windows and doors orlando" (converting queries this window: "impact windows" 7 all-conversions on $67, "hurricane windows" 2 on $136).
4. Second RSA in Window Replacement; rewrite the QS 2 impact-resistant ad group around the /impact-windows page.
5. Reconcile "Submit lead form" (8) against GA4 generate_lead (19) and the CRM, then decide which one is primary. Remove or mark secondary the never-firing "Call From Website".
6. Move $100 a day from search to PMax (PMax lost 24 percent of impressions to budget at a $275 CPA).

## Deep dive 2: Progetto Shades (416-010-8247), score 51 F, first score since the relaunch

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 55 |
| Account Structure | 75 |
| Keywords & Targeting | 30 |
| Ads & Assets | 55 |
| Bidding & Settings | 50 |

Snapshot: San Diego window coverings, relaunched by Tom on Sep 10. 30 days: $3,304, 718 clicks, $4.60 CPC, 2 primary conversions, 40 all-conversions (13 directions, 12 other local actions, 8 website visits). Monthly: September $1,143 for 7, October $2,460 for 4, November to date $1,804 for 0. Six campaigns, all Maximize Clicks with CPC ceilings Tom tuned Oct 20 to 26; Shades & Blinds budget $40 to $50 on Oct 30. Total budget $120 a day. Enhanced Conversions ON; not healthcare.

| Campaign | 30d cost | Conv | All conv | IS | Rank lost |
|---|---|---|---|---|---|
| Shades & Blinds | $1,377 | 1 | 23 | 16% | 58% |
| Shutters | $883 | 0 | 1 | 31% | 40% |
| Motorized & Smart | $459 | 0 | 3 | 24% | 52% |
| Drapery & Curtains | $372 | 1 | 8 | 23% | 55% |
| Exterior & Patio | $208 | 0 | 1 | 17% | 62% |
| Brand | $4 | 0 | 4 | 83% | 17% |

### Findings

**Conversions stopped on Oct 27.** Primary actions: "Calls from ads" (last Oct 23), "Contact" (last Oct 24), "Call ((858) 338-1678)" (last Oct 27, secondary-counted). The lead-form actions are secondary: "Lead form website" last fired Oct 3 (4 in 90 days), "Lead form - Submit" never, "Web form (start)" fired Oct 24, Nov 7 and Nov 13 with no completion recorded after it. Three form starts and zero submits in three weeks is either a broken form or a broken thank-you event. Not declared dead: submit the form and place a call from an ad click, then check GA4 and the Ads import. Until that is done, every number below is a traffic number, not a lead number.

**Quality Score is the chronic problem.** 41 live keywords at QS 1 to 3 carry $1,704, 52 percent of keyword spend. "window coverings" phrase QS 3, $646, 169 clicks, 1 conversion. "shutters for windows" QS 2 $191, "blackout curtains" exact QS 2 $135, "window shutters" exact QS 3 $119, "patio sun shade" QS 2 $99, "smart shades" QS 3 $61, "hunter douglas" QS 3 $58, "somfy shades" QS 3 $43. Landing page experience is Below Average on all of them and expected CTR Below Average on all but one. The ads are 12 AVERAGE and 4 GOOD, none EXCELLENT. This is an ad-copy and landing-page problem before it is a bidding problem.

**Spend is spread thin across generic retail intent.** "shutter store" $454 for 0 primary (1 all), "best window shades" $103, "window shade store" $101, "best motorized shades" $100, "window treatment store" $64. Rank-lost share is 40 to 62 percent everywhere on a $4 to $6 CPC ceiling, so the account is buying the cheapest positions on the broadest terms.

**Waste is small by terms, large by keyword.** Confirmed off-brand shopping: somfy $30, hunter douglas $17, norman $18 (brand-name searches the showroom may or may not carry, confirm with the client). The pattern matches on "what is" and reddit cost $0. Zero-conversion keywords above $10: 43 of them, $2,437.

### Prepared change list

1. Manual test today: contact form, lead form, and a call from a mobile ad. Confirm GA4 generate_lead or form_submit fires and the Ads import maps to it. Then set the working form action to primary and included. Nothing else in this list matters until this is done.
2. Rewrite one RSA per ad group to EXCELLENT with the keyword in two headlines, and point each campaign at the matching category page rather than a general page (the Below Average landing page score on every keyword suggests one URL for all).
3. Pause the retail-intent keywords with zero primary and zero or one all-conversion: "shutter store", "best window shades", "window shade store", "window treatment store", "best motorized shades", "shutters for windows", "blackout curtains" exact. That is $1,148 of the window's spend.
4. Add phrase negatives: reddit, what is, somfy, hunter douglas, norman (after the client confirms which brands it sells), zebra shutters, sliding shutters, curtain store.
5. Keep Maximize Clicks until two weeks after step 1 shows conversions, then move Shades & Blinds (the only campaign with volume) to Maximize Conversions.
6. Brand campaign: $5 a day and $4 spent; it is fine.

## Deep dive 3: Patio Style (596-555-8707), score 56 F, down 10

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 55 |
| Account Structure | 75 |
| Keywords & Targeting | 60 |
| Ads & Assets | 40 |
| Bidding & Settings | 45 |

Snapshot: 30 days $2,411, 837 clicks, $2.88 CPC, 12 primary conversions (5 calls from ads, 4 website call conversions, 3 thank-you page), 464 all-conversions (73 GA4 directions, 36 GTM directions, 223 other local actions, 61 website visits). Monthly: September $1,951 for 90, October $2,075 for 14, November to date $1,421 for 7.

### Findings

**Directions were demoted between Sep 14 and now.** On Sep 14 both "Get directions (GTM) 11 Sep" and the GA4 get_directions import were primary and included. Today both are secondary, along with GA4 click_to_call, which duplicates the primary "Website Call Conversions 11 Sep". The protocol says Get Directions is the client's primary goal. Either the Known account context is out of date or the demotion was unintended. Conversion action edits do not appear in change history, so the date and author are unavailable. The practical effect: Brand (Maximize Conversions) now learns from 6 conversions a month instead of about 50, and the fleet table shows a $201 CPA where the client-facing figure, with directions, is about $20.

**Pergolas & Louvered Roofs: $664 for 0 primary conversions, 3 all-conversions, $13.28 a click, manual CPC, 54 percent lost to budget.** "pergola contractor" phrase $464 (24 clicks, 0 primary, 5 all). On Nov 2 five keyword bids were set at $11.39 to $32.85 and two ad-group default bids were raised ($5 to $10 and $0.01 to $5). Those bids are what the $13 CPC comes from. Terms this window: "pergola showrooms near me" $26 (relevant, they have a showroom), "pergola assembly service" $25 and "handyman to install pergola" $13 (not relevant), "pergolas" $18 and "pergola" $13 (generic).

**Outdoor Kitchens: $576 for 2 conversions at $288.** "outdoor kitchen company" $264 for 0, "outdoor kitchen design" $107 for 0, "built in outdoor kitchen" QS 1 $62 for 0. The Nov 13 "ideas" negatives were the right call; "304 stainless steel outdoor kitchen cabinets" $33, "modular outdoor kitchen cabinets" $11, "casual kitchens outdoor cabinets" $11 and "complete outdoor kitchen packages" $11 are product-shopping queries still leaking (cabinets, modular, packages are not negatives).

**Outdoor Furniture (Maximize Clicks, $908): 4 primary, 440 all-conversions.** This is where the directions live: "outdoor furniture near me" 41 all-conversions on $40, "outdoor furniture" 34 on $19, "patio furniture orlando" 25 on $24. On the client's real goal it is the best campaign in the account.

**Ads.** 11 of 12 live ad groups have one RSA (unchanged since Sep 4); one POOR.

### Prepared change list

1. Tom to confirm the intended primary set. If directions are primary (per protocol), restore the GA4 get_directions import to primary and included and keep the GTM one secondary (that resolves the Sep 14 double-count question the other way around). Then the account can go back to Maximize Conversions where it has volume.
2. Pergolas: cap CPC at $6 (drop the $11 to $33 bids), add phrase negatives assembly, handyman, install service; keep "pergola contractor" but on exact plus phrase "pergola contractor orlando".
3. Outdoor Kitchens: add phrase negatives cabinets, modular, packages, stainless; pause "built in outdoor kitchen" (QS 1).
4. Second RSA in the top five single-ad groups (Patio Furniture, New Pergolas, New Outdoor Kitchens, Fire Pits, Brand). Worklist item 13 stands.
5. Outdoor Furniture: leave on Maximize Clicks until step 1 is settled.

## Deep dive 4: Rover Veterinary Care (750-667-5721), score 49 F, down 12, paused Nov 15

Category scores: Conversion Tracking 55, Wasted Spend 50, Account Structure 40, Keywords & Targeting 50, Ads & Assets 50, Bidding & Settings 45. Scored on the 30 days before the pause.

30 days: $2,795, 230 clicks, $12.15 CPC, 20 primary conversions (Book appointment 9, Click to call 8, Form submit 3), $140 per conversion. Monthly: September $1,403 for 18, October $2,324 for 18, November to Nov 14 $1,510 for 10. The In-Home Pet Euthanasia campaign spent $1,272 at $26.50 a click for 4.2 conversions ($299 each); Pet Cremation $856 for 8 ($107); Competitors $574 for 5.5 ($104); Brand $93 for 2.2. Dave paused all four at 00:35 on Nov 15 (Google Ads web UI). The Jupiter, Core Services, PMax and LSA campaigns were already paused, so the account now has no enabled campaign.

Open from Sep 14, still visible in the data: "Calls from ads" has recorded nothing since Aug 24 and "Event|Contact|Calls From Website" nothing since Sep 15 (both still primary); "lap of love" exact in Competitors spent $113 for 0 (intended competitor play, but zero return in two windows); informational terms "dog dementia when to put down" $74 and competitor reviews "heaven at home pet hospice reviews" $55 leaked through broad euthanasia keywords. Tom and Dave each edited an ad on Nov 9, which may be the POOR Competitors RSAs from worklist item 16; not verifiable while paused.

Prepared change list: (1) Tom confirms whether the pause was requested by the client; if not, re-enable Pet Cremation and Brand first (the two campaigns under $110 per conversion), then Competitors, and hold Euthanasia until its CPC is capped at $15. (2) Before any re-enable, run the manual call test and set the two dead call actions to secondary so Maximize Conversions trains on the five that fire. (3) Add phrase negatives dementia, reviews, hospice reviews, peggy adams; keep "lap of love" only in Competitors.

## Deep dive 5: Precision GPR (554-113-4760), score 56 F, up 6, measuring the cleanup

Category scores: Conversion Tracking 55, Wasted Spend 50, Account Structure 50, Keywords & Targeting 50, Ads & Assets 85, Bidding & Settings 40.

| Campaign | Budget/day | 30d cost | Clicks | CPC | Conv | CPA | IS | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| LP Search - Location | $13 | $557 | 23 | $24.22 | 2 | $279 | 69% | 18% |
| LP Search - Concrete Scanning | $13 | $504 | 23 | $21.89 | 2.5 | $201 | 62% | 24% |
| LP Search - Services | $13 | $455 | 24 | $18.97 | 2 | $228 | 49% | 36% |
| LP Search - GPR Scanning | $10 | $390 | 26 | $14.99 | 1 | $390 | 37% | 42% |
| LP Search - Utility Mapping | $12 | $389 | 36 | $10.82 | 2.5 | $156 | 30% | 33% |
| LP Branded | $8 | $265 | 31 | $8.56 | 1.5 | $177 | 17% | 60% |
| LP DSA - All Pages | $10 | $241 | 39 | $6.18 | 6.5 | $37 | 14% | 40% |

30 days: $2,801, 18 primary conversions, $156 each. Monthly: September $2,580 for 22 ($117), October $3,163 for 24 ($132), November to date $1,185 for 6 ($198). This week $456 for zero. Per the Nov 4 rule the flag condition is spend up and CPA up; here spend is down (Dave cut six budgets on Nov 6, the total is now $84 a day, inside the $2,500 line) and CPA is up. Report it as needs attention, not critical.

What landed: the website call actions partially work now ("Michael Phone Number (305)" 8 conversions, lp_contact_form 6, Calls from Smart Campaign Ads 3, Calls from ads 1); the three "Contact Us" duplicates are secondary; 44 RSAs are GOOD or EXCELLENT. What did not: Location and DSA are still enabled (Sep 4 item 2); DSA is now the cheapest conversion source in the account at $37, so keep it and pause Location instead ($557 for 2, the highest CPC in the account). "gpr scanning" still matches four campaigns. The three "Calls From Website" 305 and 786 actions have still never recorded. Seven campaigns on Maximize Conversions with 1 to 6.5 conversions each.

Negatives, deduped against LP NKWs (227 members) and campaign lists: "gprs" is NOT present (only "gpr" exact, which does not block "gprs orlando"); new: gprs (phrase), 1 800 dig, georgia, mygeorgia811, beryl, price, pricing, directional boring, underground contractors. Already present: 811, locates, inc, utility locator. Confirmed waste this window: $268 (gprs variants $140, 1 800 dig $18, mygeorgia811 $20, beryl $14, gprsinc $12, underground contractors $27, directional boring $12, price $12, utility locates $13).

Prepared change list: (1) Remove the "gprs scanning" keyword added Nov 15 and add "gprs" as a phrase negative to LP NKWs. (2) Pause LP Search - Location; move its $13 to DSA and Utility Mapping. (3) Give "gpr scanning" one home (GPR Scanning campaign) and add it as an exact negative in Location, Services and Concrete Scanning. (4) Switch the five remaining service campaigns to Maximize Clicks with a $12 ceiling until any one of them reaches 15 conversions a month, or consolidate them into two (Concrete and Utility) so one strategy has the volume. (5) Manual call test on the 305 and 786 website numbers, then set the dead ones secondary.

## Deep dive 6: Filutowski Eye Institute (192-870-7876), score 45 F, up 3, scope still open

Category scores: Conversion Tracking 50, Wasted Spend 35, Account Structure 55, Keywords & Targeting 45, Ads & Assets 40, Bidding & Settings 45.

30 days: $11,696, 767 clicks, $15.25 CPC, 122 primary conversions, $96 each. Monthly: September $20,785 for 329, October $18,438 for 203, November to date $5,198 for 60. The only editor in the window is catie@accaliamarketing.com, who cut the Brand Awareness budget $455 to $255 to $243 to $211 on Oct 29. Five live campaigns, all LIMITED by budget (78 to 90 percent lost): Brand Awareness LASIK $6,900 for 36 ($192), Branded $1,451 for 57 ($25), Lead Gen Cataracts $1,125 for 8 ($141), Eye Surgery $1,122 for 15 ($75), Lead Gen LASIK $1,099 for 6 ($183).

What is new since Sep 14: REK built the new website (launch about Oct 19 to 26). Tom's URL sheet instructs that /thank-you/consultation/ is the lead, the contact form is NOT a conversion, careers is not a lead, and all old thank-you URLs stop firing at launch. In Google Ads today: "Contact Page Form Submit (1)" is still primary and included (2 in 30 days, 28 in 90); "More Info Form Submit" fell from 7 to 9 a week in early October to 2, 1, 7, 1 in the four weeks since launch; "Vision In-Office Appointment Scheduled" 8 a week in September to 1, 2, 2, 6, 3. Spend fell too, so this is not proof the tags broke, but the sheet predicted exactly this kind of drop and someone needs to verify which actions now fire on the new thank-you pages. The Cataracts campaign's live RSA still uses /cataract-surgery/, which the sheet marks as a 301 to /services/cataract/; 25 paused ads in the account are disapproved for DESTINATION_NOT_WORKING, none live. Enhanced Conversions for leads is ON; the hygiene rule for healthcare clients says it stays OFF without a BAA.

Still open from Sep 14: "lasik treatment cost" broad is $6,891 of $11,696 (59 percent) and matched "mid florida eye center mount dora" $145, "florida eye clinic altamonte" $134, "tomoka eye associates" $72, "eye physicians of central florida" $65, "advanced eye care sanford" $64, "dr pal" $63 and a dozen more clinic and doctor names ($851 visible), plus general eye-exam and optometrist queries ($357). All five live ad groups have one RSA (Branded is POOR). Branded converts at $25 and loses 88 percent of impressions to a $50 budget while Brand Awareness converts at $192 on $211 a day.

Prepared change list (only if Tom confirms REK is engaged on Ads): (1) Set "Contact Page Form Submit (1)" to secondary per the site spec; confirm the consultation thank-you event is what "More Info Form Submit" and "Vision In-Office Appointment Scheduled" now fire on. (2) Turn Enhanced Conversions for leads off. (3) Update the Cataracts final URL to /services/cataract/ and the paused sitelink to the blog. (4) Brand Awareness budget $211 to $120 and Branded $50 to $120. (5) Convert "lasik treatment cost" to phrase and add the clinic names as phrase negatives to the "Search Terms" shared list (none of the 12 above is present). (6) Second RSA in every live ad group; rewrite Branded (POOR).

## No action needed this week, or one-liners

- **Quality Paralegal Services (63 D, new):** Orlando paralegal and immigration document prep, REK-managed (Tom's negatives Oct 23 to Nov 13). 41 conversions at $33, this week 14 at $22. 76 percent of spend on broad match; "family law attorney near me" is QS 1 ($281, 9 conversions) and lawyer-intent terms are off-service for a non-lawyer firm; Spanish "abogado de divorcio" variants ($60) are not blocked (only "abogado gratis" is). All five ad groups have one RSA, one POOR; one paused ETA is disapproved under GOVERNMENT_DOCUMENTS_AND_OFFICIAL_SERVICES, which is the policy to watch for this vertical. Campaign names are ad headlines and one ad group is "Ad group 1". Due for a deep dive next week.
- **M&S Asphalt Paving (60 D, reactivated):** reported paused on Sep 14; three manual-CPC campaigns have run since September ($328, $597, $497 by month). 6 conversions at $153; "driveway paving" phrase is live in both Paving campaigns ($216 for 0) and should have one home; "Call ((386) 215-7466)" is typed as a lead form; 7 of 8 ad groups have one RSA; 46 percent impression share with only 4 percent lost to budget, so the budget ($55 a day) is not the constraint. Negatives to add: allstate paving, buds asphalt, belgium block, ecogrid, tile, painting, resin bound, how thick, minimum temperature.
- **Rover Reno PPC (64 D, new):** Reno NV sister account to Rover Vet. Tom paused the old Leads-Search-1 on Nov 9 and the four new campaigns (In-Home Euthanasia, Pet Cremation, Competitor Conquest, Brand) did 8 conversions at $30 this week at $1.63 a click. They lose 87 to 90 percent of impressions to budget at $35 a day total; that is the lever. Every ad group has one RSA; the Brand RSA is APPROVED_LIMITED for a phone number in ad text. Competitor hospital names are already negatives.
- **All Phase Pool Remodeling (65 D, down 7):** 14 conversions at $59. The drop is structural, not performance: brand is still inside non-brand groups ($305 of $824), 100 percent of spend is broad, "Phone Calls 60s+" has never recorded, Contact Form recorded 0 primary in 30 days (1 all). Dave's Nov 10 phrase-match conversion cut CPC to $5.33. New leaks: "pinch a penny" phrase still missing (three variants $34; only exact "pinch a penny" and "pinch a penny pool resurfacing" exist), atlas pools $8, aqua pool $11, cody pools $4, keystone tile $3. Worklist item 12 stands.
- **Aqua Coat (65 D, up 1):** 13 conversions at $33. The 248-member master list is still attached only to the paused campaign, nine weeks after the first flag; the live campaign leaked pool heater $23, leslies $9, pinch a penny $8 and pool pump terms that the list would have blocked. Pool Equipment group still live: "swimming pool equipment" $117 for 1. New negatives: fresh finish, sekas, aqua custom, aqua wizard, masters pool, aquastrong, pool rails, handrail. Dave's Oct 22 phrase-match rebuild of the equipment keywords and Nov 15 pauses are noted.
- **Scootz (66 D, up 8):** the restructure landed Nov 3 (seven themed groups), the client raised the budget to $75 on Nov 8, and the week was 10 conversions at $59. 26 conversions in 30 days clears the Maximize Conversions bar (worklist 17 second half). Six of seven groups have one RSA, one POOR. form_submit is still secondary and silent; GA4 purchase (secondary, 21) tracks Booqable Purchases (primary, 20) closely, so purchases are not double counted. Negatives: scooter bug, ucf, how do you.
- **Florida Sealcoating (68 D, up 5):** best week in the window (7 conversions, $103). Budgets are $88 a day since Oct 23 and 30; October closed at $3,362. Brand keywords ("florida sealcoating" phrase and exact, QS 10) cost $10.40 a click on Maximize Conversions, $275 for 0 primary (36 all-conversions, so brand searchers call and get directions): put Branded on Target Impression Share with a $4 cap as was done at Patio Style. "asphalt patch repair" QS 3 $98 for 0. Competitor negatives still missing: garcia civil, stripe it rite; add road, hot asphalt patch, quikrete. "Call (1-8-333-PAVEIT)" has never recorded.
- **The Counseling Group (68 D, up 2):** 1 primary conversion in 30 days on $597 (form, Nov 2); tel-tap recorded 4 all-conversions (6 in 90 days), so worklist item 10 is resolved. Tom moved all three RSAs to /therapist-winter-park.html on Oct 20 (item 11 done), added "help in marriage" exact Oct 21, budget $26.50 Oct 26. "counseling winter park" phrase $204 for 0 primary (1 all) is a third of spend; "therapist orlando" exact QS 2. Enhanced Conversions confirmed OFF. New exact negatives: restored purpose counseling, la amistad, christine whittaker, hedy schleifer, imago; phrase: ect therapy, emergency room, post partum (postpartum exists), medicine. One RSA is POOR. Small numbers remain normal here.
- **Affordable Critter Solutions (75 C, down 1):** 12 conversions at $25, clean terms, EXCELLENT ad. Dave added "racoons in my attic" and paused four keywords on Nov 15. The 11 paused campaigns and the $10-to-$15 budget ask (worklist 19) are unchanged.
- **REK Marketing (own account):** three manual-CPC campaigns (GBP Verification, San Diego Leads, Philadelphia Leads) spent $1,407 for 1 conversion, losing 50 to 78 percent of impressions to budget; $1,173 on zero-conversion keywords. Internal, not scored; worth the same review the client accounts get.
- **Color Masters:** Tom paused the two service campaigns Oct 22 ($1,602 and 3 conversions since September). Paused, no change list.
- **All Phase Jacksonville:** the "Orlando" search campaign is still ENABLED at $49 a day and still spends nothing. Pause it when convenient (worklist 6).
- **Straightline Fence:** now LSA only; the disapproved search campaign was removed. Out of scope.
- **Jupiter Boat Supply:** paused, nothing to do.
- **Herrell Plumbing:** excluded per the Oct 15 protocol note, but Tom added 74 negatives on Nov 9 and edited budgets and ads Oct 28 to Nov 6, so the context may be stale. The search campaign spent $480 for 1 conversion in 30 days; the Pay-per-lead PMax $636 for 9.
- **Byers Fence:** excluded. For the record: the client (byersfence83@gmail.com) runs it; "vinyl fence cost" broad at QS 1 spent $970 of $1,225.
- **ProShield:** new, San Diego garage doors, client-run (info@proshieldgd.com built a search campaign Oct 22 and paused it the same day); LSA live. No REK edits. Excluded pending Tom's word.

Out of scope, for the record only: American Impact Windows & Doors LSA $6,061 in 30 days; Citrus Landscape Sanford LSA $5,795 plus Pay-per-lead PMax $3,164 (28 leads); Citrus St. Pete LSA $2,747 plus PMax $1,579; Byers Fence LSA $2,432; Straightline LSA $2,439; Herrell LSA $1,438; All Phase Orlando LSA $517; Roeling $236; Citrus Sarasota $133; ABC Pressure Wash, Spectrum Electric, Statewide Home Remodeling, Color Masters LSA $0.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: American Impact (goodman, ply gem, mi windows, powerhrg, everlasting bath, one and done, bathremodel, reviews, supply, suppliers, fabricators, condo, aluminum), Progetto (reddit, what is, somfy, hunter douglas, norman pending client confirmation, zebra shutters, sliding shutters, curtain store), Patio Style (assembly, handyman, cabinets, modular, packages, stainless), Precision GPR (gprs phrase, 1 800 dig, georgia, mygeorgia811, beryl, price, pricing, directional boring, underground contractors), Filutowski (the 12 clinic and doctor names in deep dive 6, optometrist, eye exam), Florida Sealcoating (garcia, stripe it rite, road, hot asphalt patch, quikrete), All Phase (pinch a penny phrase, atlas pools, aqua pool, cody pools, keystone tile), Aqua Coat (fresh finish, sekas, aqua custom, aqua wizard, masters pool, aquastrong, pool rails, handrail, plus attaching the master list), Counseling Group (the five names and ect, emergency room, post partum, medicine), M&S (allstate paving, buds asphalt, belgium block, ecogrid, tile, painting, how thick, minimum temperature), Quality Paralegal (abogado de divorcio, abogados de familia, emancipation, clarksville), Scootz (scooter bug, ucf, how do you), Rover Reno (a+ animal hospital). Flagged standalone tokens to avoid: "reviews" at American Impact would also block "american impact windows reviews" (brand intent), so pair it as "windows reviews" and "weathertite reviews" instead; "road" at Florida Sealcoating is safe only if the client does not do road work.

New keywords to add: American Impact exact "impact windows orlando fl", "hurricane impact windows orlando", "impact windows and doors orlando"; Florida Sealcoating exact "asphalt paving company orlando" (converted at $54) and "driveway sealcoating" phrase already converting at $37; Rover Reno exact "in home pet euthanasia reno" and "pet cremation reno"; Scootz exact "scooter rental universal orlando" and "foldable scooter rental orlando" (converting at $89 and $79 under phrase); Patio Style exact "patio furniture store orlando".

Bid and budget adjustments: American Impact search to a $300 target CPA or a $25 click ceiling, $100 a day from search to PMax; Precision GPR pause Location, Maximize Clicks with a $12 ceiling on the thin campaigns; Patio Style pergola CPC cap $6; Florida Sealcoating Branded to Target Impression Share with a $4 cap; Rover Reno $35 to $60 a day (90 percent lost to budget at $30 per conversion, client decision); Filutowski Brand Awareness $211 to $120 and Branded $50 to $120; Scootz Maximize Conversions now; Affordable Critter $10 to $15 a day (still a client decision).

Competitive read (rank-lost share as the proxy): American Impact's 55 percent rank loss at a $64 CPC says the auction is expensive and the account is also paying above it; cap bids before adding budget. Progetto, Patio Style, Quality Paralegal, Aqua Coat and Affordable Critter lose 55 to 64 percent to rank on $4 ceilings or tight budgets, a Quality Score and budget story. Filutowski and Rover Reno lose 87 to 90 percent to budget and almost nothing to rank: they are winning the auctions they enter and simply stop early. Florida Sealcoating Residential at $23.44 a click and Precision GPR Location at $24.22 are the two places a competitor is pushing CPC up on REK-managed accounts.

## Prioritized weekly action plan

1. **Critical, Tom today: Rover Veterinary Care.** Confirm the Nov 15 pause with Dave and the client. If unintended, re-enable Pet Cremation and Brand first, then run the call test before Euthanasia goes back on with a $15 cap.
2. **Critical, Tom: American Impact.** Target CPA or click ceiling on the search campaign (deep dive 1, item 1) and the brand negatives (item 2). This is the single largest recoverable figure in the fleet, about $2,200 a month at the floor and far more in overpaid clicks.
3. **Critical, REK: Progetto Shades manual form and call test**, then the landing page and ad rewrite. Nothing bought since Oct 27 can be judged until tracking is confirmed.
4. **Critical, Tom: Filutowski scope.** Decide whether REK manages the Ads account. Regardless of the answer, tell Accalia that the contact form must be secondary and that Enhanced Conversions should be off, because REK built the site and wrote the spec.
5. **High, Tom: Patio Style conversion set.** Confirm directions as primary (attention item 4), then cap the pergola bids and add the kitchen product negatives.
6. **High, Dave: Precision GPR.** Remove the "gprs scanning" keyword, add "gprs" as a negative, pause Location. Fifteen minutes.
7. **Medium, Dave: Aqua Coat.** Attach the master list to the live campaign. Nine weeks open; five minutes of work.
8. **Medium, Tom: Scootz** to Maximize Conversions, second RSAs in the six single-ad groups.
9. **Medium, Dave: Florida Sealcoating** Branded to Target Impression Share, competitor negatives, All Phase brand split and "pinch a penny" phrase.
10. **Low:** M&S "driveway paving" one home and second RSAs; Quality Paralegal second RSAs and Spanish lawyer negatives; Rover Reno budget ask; All Phase Jacksonville pause the Orlando campaign; REK Marketing's own zero-conversion keywords; Counseling Group name negatives.

## Rotation

Deep-dived this run: American Impact, Progetto Shades, Patio Style, Rover Veterinary Care, Precision GPR, Filutowski Eye Institute. Due next Monday: Quality Paralegal Services, M&S Asphalt Paving and Rover Reno PPC (new or reactivated, never deep-dived), plus Aqua Coat and Affordable Critter Solutions (carried from Sep 14). The week after: All Phase Pool Remodeling, The Counseling Group, Scootz, Florida Sealcoating.

## Data notes

- Account discovery returned 34 client accounts against 26 on Sep 14; compare next week against this run's list. The MCC link table shows 34 active and 16 inactive links; the inactive set includes both Premium accounts and nothing new that was active on Sep 14.
- The installed google-ads library (35.1.0) no longer ships API v22; this run used v24 via GOOGLE_ADS_API_VERSION. tools/gaql.py should default to v24. Three field names changed: campaign.start_date and end_date are not selectable, keyword_view does not support search_budget_lost_impression_share, and recommendation.impact sub-fields are not selectable. Five Counseling Group queries hit transient 500 errors and were re-run cleanly.
- Protocol context that needs updating from this run: Rover Vet pause (intended or not); American Impact (REK-managed since Nov 9, 57clicks and the client also have access); Quality Paralegal, Rover Reno, M&S Asphalt (active, REK-managed); Color Masters (paused Oct 22); ProShield (client-run, excluded); Straightline (LSA only now); Patio Style primary conversion set; Herrell Plumbing (Tom editing again); Citrus Landscape Pay-per-lead PMax campaigns; Filutowski site launch and the conversion spec; Filutowski and American Impact Enhanced Conversions status.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor. Visible terms covered 60 percent of keyword spend at American Impact and 33 percent at Precision GPR.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Oct 18 (the API allows 30 days). Conversion action edits are not included in change history, which is why the Patio Style demotion cannot be dated.
- The Patio Style Nov 2 keyword bid events reference criterion ids that are not in the current keyword report, so the five keywords are not named here.
- LSA cost data lags by several days in some accounts (last recorded spend dates range from Nov 4 to Nov 15); LSA figures are out of scope and shown for the record only.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
