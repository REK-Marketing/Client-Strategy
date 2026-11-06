# PPC Weekly Audit - 2026-11-06 (Google Ads fleet)

Run: Friday Nov 6, 2026, scheduled cloud session through tools/gaql.py (Google Ads API v25) against MCC 656-695-7229. Windows: 30 days Oct 7 to Nov 5; this week Oct 30 to Nov 5; last week Oct 23 to Oct 29. Score deltas are against the Sep 14 report, which was the last run; no audit ran in the seven weeks between. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Patio Style (19-point drop), Progetto Shades (worst REK-managed score), American Impact (new, largest account under the MCC, scope undecided), Precision GPR (measuring the cleanup), All Phase Pool Remodeling (10-point drop). One-liners for the rest.

The google-ads.yaml in the Drive folder dave-ads-setup (Sep 8 version) authenticated on the first try. It was copied with mode 600, used only by the client library, and deleted before this report was committed.

## Attention items (read first)

1. **Nothing vanished from the MCC.** All 26 accounts from Sep 14 are still linked. Six accounts are new since Sep 14: American Impact (974-265-3397), Quality Paralegal Services (447-153-2607), Color Masters (426-092-9847), Color Masters LSA (163-445-9282), ProShield (771-172-8482) and All Phase Pool Remodeling (Orlando LSA) (355-287-7099).
2. **American Impact (974-265-3397) is the largest account in the fleet and nobody at REK is editing it.** $26,663 in 30 days on search and Performance Max, 111 conversions at $240. This week $6,009 for 8 conversions at $751. The editors are contact@57clicks.com and the client's own Gmail, and they are working against each other: 57clicks paused the two main campaigns on Nov 5 and the client re-enabled them within a day. 56 keywords at Quality Score 1 to 3 carry $11,723, 69 percent of search spend. Scored 44 F, provisional, and deep-dived because the numbers are large. Tom decides whether REK manages, audits, or is only linked.
3. **Patio Style (596-555-8707) dropped 19 points because Get Directions is no longer a primary conversion.** Both directions actions (the GA4 import and the Sep 11 GTM action) are now secondary and excluded, so counted conversions fell from 166 in the Sep 14 window to 14 in this one. The taps still happen: 41 GA4 directions and 35 GTM directions in 30 days. The protocol says directions counted as primary is the client's intent. Conversion-action edits are not in change history, so who demoted them is unavailable. See deep dive 1.
4. **Progetto Shades (416-010-8247) spent $2,711 in 30 days for 2 conversions, $1,356 each, and $833 this week for none.** Tom moved all six campaigns to Maximize Clicks with bid ceilings in late October and raised budgets. The search terms are on topic (shutters, blinds, drapery) and the ads are approved, so this is a landing page and tracking problem, not a targeting problem: landing page experience is BELOW_AVERAGE on 36 of the 37 keywords at Quality Score 1 to 3. See deep dive 2.
5. **Four accounts had a conversion dip this week that is worth one more week of watching, not action yet:** Scootz 8 to 2 (Tom reworked the brand ad group Nov 3), Florida Sealcoating 9 to 2 on flat spend, Rover 6.8 to 5.2, Aqua Coat 4 to 2. All four are on next Monday's rotation.
6. **Straightline Fence And Supply (550-094-8786) is now LSA-only.** The disapproved vinyl fence search campaign was removed and the Local Services campaign spent $2,693 in 30 days. Out of scope from here; the Sep 14 attention item is closed.
7. **The Counseling Group tel-tap action works.** Website Phone Click recorded 5 taps since Oct 13. Worklist item 10 is closed. The 5 taps sit in the all-conversions column only, so the include-in-Conversions setting was switched during the window; confirm it is on.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 32 client accounts, 1 manager | 14 | 6 new since Sep 14, 0 vanished. Scored: 12 REK-managed search accounts plus 2 provisional (Filutowski, American Impact). Excluded: Byers Fence x2, Herrell Plumbing, 9 LSA-only accounts (Straightline joins them), ProShield (client-edited, LSA plus a paused Performance Max). Not scorable: Color Masters (paused Oct 22), Jupiter Boat Supply (paused), All Phase Jacksonville (no search spend), REK Marketing (internal, started Oct 23). |

Search and Performance Max spend in the 30-day window: $19,535 across the twelve REK-managed scored accounts, $42,643 at the two provisional accounts (Filutowski $15,980, American Impact $26,663), $1,387 at the paused or internal accounts. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is the zero-conversion part of visibly irrelevant search terms in 30 days (competitor names, retailers, suppliers, informational and out-of-service queries), a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $15,980 | 168 | $95 | 43 | F | +1 | Critical (scope) | Still one broad keyword, "lasik treatment cost", at $10,437; Performance Max paused and Branded cut, so conversions halved and CPA doubled; 18 UA goals and YouTube views still primary; Enhanced Conversions still on | $3,152 |
| 2 | American Impact | 974-265-3397 | $26,663 | 111 | $240 | 44 | F | new | Critical (scope) | Manual CPC search campaign at $57 a click and $557 per conversion; 69% of spend on QS 1 to 3 keywords; two editors undoing each other's pauses; lead form action demoted to secondary | $2,514 |
| 3 | Patio Style | 596-555-8707 | $2,152 | 14 | $154 | 47 | F | -19 | Critical | Directions no longer primary (166 to 14 conversions); Pergolas and Kitchens on Manual CPC with $952 on 23 zero-conversion keywords; 11 of 12 ad groups still one RSA | $145 |
| 4 | Progetto Shades | 416-010-8247 | $2,711 | 2 | $1,356 | 49 | F | new | Critical | $1,043 and $833 in the last two weeks for 2 and 0 conversions; landing page BELOW_AVERAGE almost everywhere; website call action primary but not included | $51 |
| 5 | Rover Veterinary Care | 750-667-5721 | $2,480 | 19 | $131 | 59 | F | -2 | Needs attention | "mobile dog put down service" $226 at $45 a click and "dog put to sleep" $200 with 0 conversions; Competitors RSAs still POOR; two call actions at zero for 30 days | $412 |
| 6 | Precision GPR | 554-113-4760 | $3,154 | 21 | $150 | 59 | F | +9 | Needs attention | CPA $150, within Tom's rule; budgets trimmed to $84/day on Nov 6; "gprs" still not a negative ($145 on six variants); brand keyword broad and matching engineers and boring contractors | $298 |
| 7 | Scootz | 185-574-5478 | $1,464 | 25 | $59 | 60 | D | +2 | Needs attention | Ad-group split landed Nov 3; still Maximize Clicks with 25 conversions; 6 of 7 groups one RSA; form_submit still secondary; 2 conversions this week after 8 | $83 |
| 8 | Quality Paralegal Services | 447-153-2607 | $1,459 | 51 | $29 | 61 | D | new | On target | Converts at $29 on a $27 target; hygiene findings only: 13 QS 1 to 3 keywords, one RSA per group (one POOR), one ad disapproved, Immigration campaign $110 for 0 | $233 |
| 9 | All Phase Pool Remodeling | 103-111-7688 | $871 | 13 | $67 | 62 | D | -10 | Needs attention | Conversions 30 to 13, CPA $26 to $67; brand still a broad keyword inside non-brand groups ($410 of $871); "swimming pool renovations" broad $204 for 0; master list still only on the paused campaign | $81 |
| 10 | Florida Sealcoating | 168-852-7101 | $3,175 | 25 | $127 | 66 | D | +3 | Needs attention | Budgets cut to $88/day on Oct 23 and 30 (below the $3,000 plan); Branded $568 for 2 conversions; competitor negatives from Sep still missing; 2 conversions this week | $182 |
| 11 | M&S Asphalt Paving | 827-724-4095 | $655 | 4 | $164 | 66 | D | new | Needs attention | Reactivated Oct 15 by Tom; Orlando Metro campaign has not served; 7 of 8 groups one RSA; two call actions categorized as lead forms | none confirmed |
| 12 | Aqua Coat Pool Plastering | 285-714-0527 | $463 | 13 | $36 | 67 | D | +3 | On target | 248-member master list still attached only to the paused campaign; Pool Equipment group got a new keyword and RSA on Oct 28 instead of a pause; equipment and retailer terms $122 | $122 |
| 13 | The Counseling Group | 657-069-3617 | $648 | 3 | $216 | 68 | D | +2 | On target | Small numbers, on plan at $26.50/day; tel-tap works; "therapist near me" exact QS 2 with landing page BELOW_AVERAGE; ECT, TMS-style and competitor-name queries $70 | $70 |
| 14 | Affordable Critter Solutions | 227-108-4521 | $303 | 16 | $19 | 76 | C | 0 | On target | Clean; best week of the window (6 conversions on $69) after Dave's Oct 29 keyword and RSA additions | $26 |
| none | Color Masters | 426-092-9847 | $738 | 1 | n/a | n/a | paused | new | Paused | Tom paused all three REK search campaigns Oct 12 to 22 after $738 for 1 conversion. No change list until it restarts | n/a |
| none | REK Marketing | 390-315-5264 | $649 | 1 | n/a | n/a | internal | n/a | Internal | Tom's own GBP Verification, San Diego and Philadelphia search campaigns, live since Oct 23 | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | no search spend | n/a | Paused (search) | The "Orlando" campaign is still ENABLED and NOT_ELIGIBLE, nothing spent. Worklist item 6 still open | n/a |
| none | Jupiter Boat Supply | 216-859-2093 | $0 | 0 | n/a | n/a | paused | n/a | Paused | Fully paused | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | LSA only | was no spend | Out of scope | Search campaign removed; LSA $2,693 in 30 days | n/a |

Excluded, for the record only: Byers Fence (870-428-8862) $1,664 for 8 conversions; Herrell Plumbing (113-422-7395) $2,149 search and pay-per-lead Performance Max for 191 conversions at $11 plus $2,292 LSA; ProShield (771-172-8482) client-edited, $322 on a now-paused Performance Max plus LSA. Citrus Landscape Solutions Sanford and St. Pete now carry "Pay-per-lead-PMax" campaigns outside their LSA ($513 for 4 and $49 for 1 since Oct 30); they are Performance Max, not LSA, so Tom should say whether they stay out of scope.

## Week over week (Oct 30 to Nov 5 against Oct 23 to Oct 29, search and Performance Max only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| American Impact | $4,002 to $6,009 (+50%) | 327 to 290 | 3.4% to 3.2% | $12.24 to $20.72 | 15 to 8 | $267 to $751 | Off target; budgets swung twice this week |
| Filutowski Eye Institute | $3,167 to $3,131 (-1%) | 189 to 219 | 5.8% to 5.4% | $16.76 to $14.30 | 25 to 28 | $127 to $112 | Flat |
| Progetto Shades | $1,043 to $833 (-20%) | 202 to 177 | 6.0% to 5.3% | $5.16 to $4.71 | 2 to 0 | $521 to none | Off target |
| Precision GPR | $752 to $826 (+10%) | 53 to 63 | 5.1% to 5.1% | $14.18 to $13.11 | 5 to 5 | $150 to $165 | Steady |
| Florida Sealcoating | $637 to $629 (-1%) | 71 to 98 | 6.4% to 7.2% | $8.98 to $6.41 | 9 to 2 | $71 to $314 | Watch; Residential 0 conversions on $176 |
| Patio Style | $456 to $623 (+37%) | 207 to 184 | 7.6% to 7.4% | $2.21 to $3.39 | 2 to 6 | $228 to $104 | Kitchens and Pergolas budgets raised Oct 27 and 28 |
| Rover Veterinary Care | $640 to $579 (-10%) | 50 to 46 | 15.0% to 12.3% | $12.80 to $12.58 | 6.8 to 5.2 | $95 to $110 | Watch |
| Scootz | $327 to $350 (+7%) | 367 to 397 | 7.1% to 7.1% | $0.89 to $0.88 | 8 to 2 | $41 to $175 | Watch; brand group reworked Nov 3 |
| Quality Paralegal Services | $317 to $342 (+8%) | 97 to 105 | 5.1% to 5.5% | $3.27 to $3.26 | 7 to 8 | $45 to $43 | Flat |
| All Phase Pool Remodeling | $170 to $194 (+14%) | 15 to 24 | 3.0% to 5.8% | $11.33 to $8.10 | 1 to 3 | $170 to $65 | Recovered from a bad week |
| The Counseling Group | $164 to $173 (+5%) | 39 to 41 | 6.7% to 4.0% | $4.19 to $4.21 | 0 to 1 | none to $173 | Small numbers |
| M&S Asphalt Paving | $194 to $159 (-18%) | 19 to 13 | 9.2% to 8.6% | $10.19 to $12.23 | 1 to 1 | $194 to $159 | Small numbers |
| Aqua Coat | $95 to $110 (+16%) | 18 to 22 | 5.3% to 5.5% | $5.28 to $5.00 | 4 to 2 | $24 to $55 | Watch |
| Affordable Critter Solutions | $68 to $69 (+1%) | 18 to 15 | 9.0% to 8.0% | $3.79 to $4.58 | 1 to 6 | $68 to $11 | Best week in the window |
| REK Marketing | $173 to $476 | 17 to 46 | 5.0% to 3.1% | $10.18 to $10.35 | 0 to 1 | | Internal, launched Oct 23 |

Fleet, the twelve REK-managed accounts: $4,863 to $4,887 spend, 46.8 to 41.2 conversions.

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: Affordable Critter 71 percent, Patio Style Outdoor Furniture 67 percent, Precision GPR DSA 64 percent, Scootz 61 percent, Progetto Shutters 57 percent, Counseling Group 49 percent. Largest CPC increases: American Impact ($12.24 to $20.72, search campaign alone $57 to $87 a click on its two biggest keywords), Patio Style ($2.21 to $3.39, from the Manual CPC bids set Nov 2), M&S Asphalt ($10.19 to $12.23). Rover holds 80 percent absolute top on In-Home Pet Euthanasia at $21 a click with 0.4 percent lost to budget; it is buying the top of page, not being outbid.

## Changes made in the past week (Oct 30 to Nov 6) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Precision GPR | Nov 6 | sheokand003@gmail.com (Dave) | Daily budgets trimmed: Utility Mapping $15 to $12, Services $18 to $13, Location $18 to $13, GPR Scanning $15 to $10, Branded $10 to $8. Seven campaigns now total $84/day | Lands on the $2,500 a month line. Too new to measure. |
| Progetto Shades | Oct 30, Nov 5 | tom@rekmarketing.com | Shades & Blinds budget $40 to $50; a promotion asset added to all six campaigns Nov 5. Earlier: bid ceilings set on Oct 20, 22, 23 and 26; Shutters $22 to $30 on Oct 20 | $833 this week, 0 conversions. The ceilings cut CPC from $5.16 to $4.71 but conversions did not follow. |
| Scootz | Nov 3 | tom@rekmarketing.com | "Ad group 1" renamed "Brand - Legacy", 29 keyword status flips, the group paused then re-enabled | 2 conversions this week after 8. Clicks rose to 397 at $0.88. Too early to call. |
| Patio Style | Nov 1 and 2 | paidads@rekmarketing.com | Outdoor Kitchens moved from Maximize Clicks to Manual CPC; ad-group bid $5 to $10; keyword bids on "New Outdoor Kitchens 14 Oct" set to $17.26; Built-in Grills and Outdoor Kitchens groups toggled. Oct 28: Outdoor Kitchens budget $5 to $20. Oct 27: Pergolas $10 to $25. Oct 30: one brand negative | Spend +37 percent. Outdoor Kitchens 2 conversions on $116 this week with 88 percent lost to budget; Pergolas $123 for 0 with 73 percent lost to budget. Overall CPC $2.21 to $3.39. |
| Florida Sealcoating | Oct 30 | sheokand003@gmail.com | Commercial budget $45 to $38; remarketing frequency cap and device modifier; new RSA in Residential Asphalt Patching; new display ad. Oct 23: Residential $40 to $30, Branded $20 to $15 | Spend flat, conversions 9 to 2. Daily budgets now $88, about $2,650 a month against the $3,000 plan. |
| Aqua Coat | Oct 28 to Nov 4 | sheokand003@gmail.com | Lead form asset, image assets, a new keyword and RSA in the Pool Equipment group | 2 conversions this week after 4. Worklist item 7 asked for Pool Equipment to be paused; it was expanded. |
| Affordable Critter Solutions | Oct 29, Nov 6 | sheokand003@gmail.com | Keywords "noise in the attic" and "bat removal orlando" added, new RSA in Attic group, two sitelinks removed, AI Max setting changed; image assets Nov 6 | 6 conversions on $69 this week, best of the window. |
| Rover Veterinary Care | Oct 29 | sheokand003@gmail.com | RSA edited in Pet Cremation | Cremation 2 conversions this week; no other effect visible. |
| American Impact | Nov 3, 5, 6 | contact@57clicks.com and americanimpactandenergy@gmail.com | 57clicks: 12 negatives added, Campaign 1 budget $832 to $406, Performance Max $200 to $470, Campaign 1 and Performance Max paused Nov 5, eight assets. Client: both campaigns re-enabled Nov 5, Bathroom Remodel re-enabled Nov 6, nine assets | $6,009 this week for 8 conversions. Two parties editing in opposite directions. |
| Filutowski Eye Institute | Oct 29 | catie@accaliamarketing.com | Brand Awareness budget edited three times, now $211/day (was $430 on Sep 14). Oct 15: ad schedules on four campaigns, target CPAs changed (Eye Surgery $30 to $50, Cataracts $200 to $150, Branded $15 to $50) | 30-day conversions 354 to 168. Performance Max, which gave 63 conversions at $11 in September, is paused. |
| The Counseling Group, All Phase, Quality Paralegal, M&S Asphalt | | | No bid, keyword or budget changes this week (Counseling budget $25 to $26.50 on Oct 26 by Tom; QPS and M&S built out Oct 12 to 23 by Tom) | |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

Landed: item 10 (Counseling tel-tap works, ECT off confirmed), item 14 (YouTube actions secondary), item 17 first half (Scootz split into Brand, Disney, Universal, Orlando Generic, ECV and Wheelchair, Folding and Portable on Nov 3), item 18 (Straightline campaign removed), the second Couples RSA from item 8, and the budget half of item 5 (Precision GPR budgets, Nov 6). Not landed: items 4, 6, 7 (the opposite happened), 11, 12, 13, 15 (competitor negatives; "sealcoating florida" was added as a keyword on Oct 23, not as a negative), 16, 19, the Max Conversions half of 17, the Location, DSA and gprs halves of 5, and the pauses in item 8 ("help with depression" $67 and "stress therapy" $19 still live). Item 9 (Gottman) is unknown from the API.

## Deep dive 1: Patio Style (596-555-8707), score 47 F, down 19

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 45 |
| Account Structure | 65 |
| Keywords & Targeting | 45 |
| Ads & Assets | 40 |
| Bidding & Settings | 55 |

| Campaign | Bidding | Budget/day | Spend | Clicks | CPC | Conv | CPA | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|
| Outdoor Furniture | Maximize Clicks | $30 | $887 | 619 | $1.43 | 6.0 | $148 | 23.2% | 64.4% |
| Outdoor Kitchens | Manual CPC (since Nov 1) | $20 | $531 | 127 | $4.18 | 2.0 | $265 | 32.7% | 44.7% |
| Pergolas & Louvered Roofs | Manual CPC | $25 | $503 | 45 | $11.18 | 1.0 | $503 | 66.2% | 21.4% |
| Brand | Maximize Conversions | $10 | $230 | 75 | $3.07 | 5.0 | $46 | 67.4% | 22.8% |

### Findings

**The conversion drop is a settings change, not a performance change.** Counted conversions: Calls from ads 7, Website Call Conversions 2, Thank you page 5. Not counted: GA4 get_directions 41 taps (now secondary, excluded), Get directions (GTM) 35 taps (secondary, excluded), GA4 generate_lead 5, GA4 click_to_call 4, Store visits 10. The Sep 14 worklist (item 14) asked for a check that the GTM action and the GA4 import do not double count. The result was that both were demoted. If the client's primary is still Get Directions, one of the two (the GTM action, which is the cleaner source) should be primary and included and the other secondary. As it stands, Maximize Conversions on Brand is optimizing to 14 conversions a month instead of 50 plus.

**Pergolas and Kitchens spend without converting.** 23 zero-conversion keywords cost $952: "pergola contractor" $225 at $17.31 a click, "outdoor kitchen company" $143, "outdoor kitchen design" $105, "patio cover orlando" $47 (QS 3), "pergola installation" $46, "outdoor pergola" exact $43. The one Pergolas conversion in 30 days cost $503. "New Pergolas 07 Oct" has a single RSA rated POOR. Ten keywords sit at QS 1 to 3 with landing page BELOW_AVERAGE on eight of them, including "built in outdoor kitchen" at QS 1 and "outdoor grill island" at QS 3 (worklist item 4 asked for it to be paused pending the client's answer on grill islands).

**Structure and ads.** 11 of 12 live ad groups still have one RSA (unchanged since Sep 4). Outdoor Furniture is still on Maximize Clicks with 6 counted conversions (worklist item 13); with directions restored it would have the volume for Maximize Conversions.

**Waste, visible floor $145:** "pergola assembly service" $25, "handyman to install pergola" $13, "pergola carport attached to house" $12, "show me a pergola" $12, "outdoor kitchen ideas" $15, "outdoor kitchen garage design pictures" $10, plus 120 small "ideas" and "pictures" queries. "azenco" and "mirador" remain products the store carries; "mirador" is already a negative in Master Negatives, which contradicts the Sep 14 note that it should be kept. Confirm with the client.

### Prepared change list (suggestions only)

1. Conversion actions: set "Get directions (GTM) 11 Sep" back to primary and included; leave the GA4 get_directions import secondary. Confirm the GA4 and GTM counts do not both fire on one tap (41 and 35 in the same window suggest they overlap but are not identical). Confirm Store visits stays secondary.
2. Pergolas: pause "pergola contractor" and "pergola installation" (installer intent at $11 to $17 a click, 0 conversions); keep "louvered pergola", "azenco pergola" and "patio cover" with a $6 CPC cap. Rewrite the POOR RSA in "New Pergolas 07 Oct".
3. Kitchens: pause "outdoor kitchen design", "built in outdoor kitchen" (QS 1) and "outdoor grill island" (QS 3, worklist item 4). Keep "outdoor kitchen contractors" (2 conversions on $38). Cap the $17.26 keyword bids set Nov 2 at $8.
4. New phrase negatives, deduped (not present anywhere live): assembly, handyman, carport, pictures, "show me". Already present: ideas (42 variants), panels, mirador.
5. Second RSA in Patio Furniture - Local, Patio Covers & Cabanas, Louvered Pergolas and New Outdoor Kitchens first; the rest over the month.
6. Once directions are primary again for two weeks, move Outdoor Furniture to Maximize Conversions (worklist item 13).

## Deep dive 2: Progetto Shades (416-010-8247), score 49 F, new

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 30 |
| Account Structure | 70 |
| Keywords & Targeting | 35 |
| Ads & Assets | 55 |
| Bidding & Settings | 50 |

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|
| Shades & Blinds | $50 | $1,111 | 295 | $3.77 | 1.0 | 29.2% | 56.0% |
| Shutters | $30 | $671 | 109 | $6.16 | 0.0 | 26.5% | 43.5% |
| Motorized & Smart | $16 | $425 | 67 | $6.34 | 0.0 | 21.8% | 54.0% |
| Drapery & Curtains | $12 | $308 | 58 | $5.32 | 1.0 | 11.6% | 67.9% |
| Exterior & Patio | $7 | $192 | 61 | $3.14 | 0.0 | 22.1% | 60.9% |
| Brand | $5 | $4 | 3 | $1.34 | 0.0 | 5.6% | 16.7% |

Weekly: $107, $437, $292, $1,043, $833. Conversions: 0, 0, 0, 2, 0. All five service campaigns are on Maximize Clicks with bid ceilings since Oct 20 to 26.

### Findings

**Traffic is on topic and nothing converts.** 2,773 visible search terms, all but two with zero conversions. The top ones are "plantation shutters", "shutters", "blackout curtains", "window shutters", "drapes", "somfy motorized shades", "hunter douglas shades", "norman blinds": exactly what the campaigns target. Irrelevant terms are only $51 (Smart Wings, The Blind and Shutter Pros, Macy's, "pictures of"). The 333-member global negative list is doing its job. Waste is not the problem.

**Landing pages are.** 37 keywords at QS 1 to 3 carry $765. Landing page experience is BELOW_AVERAGE on 36 of them and expected CTR is BELOW_AVERAGE on all 37. Examples: "window shutters" exact QS 3 $120, "shutters for windows" QS 1 $117, "blackout curtains" QS 2 $67, "hunter douglas" QS 3 $61, "smart shades" QS 3 $56, "outdoor patio shades" QS 2 $56, "somfy shades" QS 1 $38. $1,173 of spend has no Quality Score at all (new keywords from the Oct 15 to 21 builds).

**Tracking has gaps.** Counted: Calls from ads 1, Contact 1. "Call ((858) 338-1678)" is primary but not included in Conversions and recorded 1. "Lead form website" (GA4) and "Financing inquiry" are secondary with nothing in 30 days. "Clicks to call" from the Business Profile recorded 1. The Local actions show 19 engagements, 11 directions and 5 website visits in 30 days, so the ads do produce store-intent actions that the account does not count. Enhanced Conversions is on; fine, not healthcare.

**Ads.** Three of nine live groups have one RSA (Brand, Exterior, Designer Brands). Every RSA in the five service campaigns is AVERAGE.

### Prepared change list

1. Before any more budget: a manual trigger test of Contact, the (858) website call and the GA4 lead form on the live landing pages, and confirm which pages the Shutters, Shades & Blinds and Motorized keywords land on. Set the (858) call action to included. Until that is done, hold the five service budgets at $115/day total rather than raising further.
2. Landing pages: the Shutters and Motorized campaigns need pages that match the query (plantation shutters, motorized shades) rather than a general window-treatments page. This is the only lever that moves 36 BELOW_AVERAGE landing page scores.
3. Pause the two keywords buying brand traffic for other makers unless Progetto sells them: "hunter douglas" phrase ($61, QS 3) and "somfy shades" exact ($38, QS 1). Keep "hunter douglas blinds" (QS 7) if the store carries the line.
4. New negatives, deduped: smart wings, smartwings, "blind and shutter pros", macy, pottery barn, "pictures of", matter, blinds.com. Already present: ikea, amazon, wayfair, 3 day blinds, budget blinds, diy, "how to", reviews, jobs.
5. Second RSA in Brand, Exterior and Designer Brands; rewrite one AVERAGE RSA per service group with the query in the headline.
6. Bidding stays Maximize Clicks until the account has 15 counted conversions in 30 days; then Maximize Conversions on the first campaign to get there.

## Deep dive 3: American Impact (974-265-3397), score 44 F, provisional

Scope note: new under the MCC since Sep 14. No REK edits in 30 days. Editors: contact@57clicks.com (66 events) and americanimpactandenergy@gmail.com (21 events). The list below is prepared so Tom can decide; coordinate with 57clicks before anything is applied.

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 25 |
| Account Structure | 55 |
| Keywords & Targeting | 30 |
| Ads & Assets | 70 |
| Bidding & Settings | 40 |

Snapshot, 30 days: three enabled campaigns plus a Local Services campaign ($688, 8 leads, out of scope). Search and Performance Max $26,663, 111 conversions at $240.

| Campaign | Status | Bidding | Budget/day | Spend | Clicks | CPC | Conv | CPA | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|---|
| Campaign 1 (Impact Windows search) | enabled | Manual CPC | $406 | $12,246 | 213 | $57.49 | 22.0 | $557 | 30.7% | 28.2% |
| Leads-Performance Max-1 | enabled | Max Conversions | $470 | $9,275 | 1,664 | $5.57 | 81.0 | $115 | 20.3% | 57.6% |
| AIE Search Kitchen Remodel | paused Oct 27 | Max Conversions | $275 | $2,861 | 112 | $25.54 | 6.0 | $477 | 38.4% | 28.3% |
| AIE Search Home Renovation | paused Oct 12 | Max Conversions | $156 | $1,000 | 41 | $24.39 | 1.0 | $1,000 | 44.7% | 25.3% |
| AIE Search Bathroom Remodel | re-enabled Nov 6 | Max Conversions | $155 | $967 | 32 | $30.21 | 1.0 | $967 | 25.0% | 44.0% |
| RMK Display Remarketing | paused Oct 27 | Max Conversions | $20 | $315 | 391 | $0.81 | 0.0 | n/a | | |

### Findings

**The search campaign is a Manual CPC campaign spending $400 to $1,000 a day at $57 a click.** "window replacement company" phrase: $6,008, 99 clicks, $60.69 a click, 14.7 conversions, QS 3. "window replacement near me" phrase: $2,544, $87.71 a click, 3.3 conversions, QS 3. "window replacement company orlando" $1,266 for 0. "impact window replacement" $492 for 0. 56 keywords at QS 1 to 3 carry $11,723, which is 69 percent of search spend; expected CTR is BELOW_AVERAGE on every one. The campaign's budget was changed on Oct 12, 19, 27 (three times) and Nov 5, from $172 to $832 and back to $406. In the week of Nov 2 it spent $3,998 in four days.

**Performance Max is carrying the account.** 81 of 111 conversions at $115. Its budget went $470 to $199 (Oct 19), to $300, $200 and $199 (Oct 27), and back to $470 (Nov 5).

**Waste, visible floor $2,514** on 162 terms naming competitors, retailers, suppliers and non-services with zero conversions: "windowwall orlando" $301, "commercial windows and doors near me" $219, "lowes window replacement" $214, "$99 window replacement special" $144, "aluminum windows near me" $138, "goodman windows" $128, "american made windows melbourne" $115, "w robbins" $106, "first choice windows ocala" $105, "national bath program" $102, "polk county windows and doors" $99, "cq insulation" $59, "mr granite graceville" $56, "vinyl windows for screen porch" $55, "cabinet paint shops" $53, "glass block installers" $50. Another $2,852 went to the same kind of term with 12 conversions at $238, led by "window suppliers near me" $468, "window fabricators near me" $477, "window supply near me" $311, "mi windows series 3540" $368 and "stone spirit orlando" $306; supplier intent that converts occasionally at four times the Performance Max CPA. Google withholds the low-volume remainder, so these are floors.

**Conversion tracking.** "Submit lead form" (41 submissions in 30 days) is now secondary and excluded, yet its 41 still sit in the Conversions column, so it was demoted during the window. "Calls from ads (60s)" 66, LSA phone and message leads 8, and "YouTube follow-on views" and "YouTube channel subscriptions" are all primary and included. "Local actions - Directions" (136) and "Local actions - Other engagements" (204) are primary. The 111 counted conversions mix website forms, 60-second calls and LSA leads. Enhanced Conversions for leads is on; this is a home-improvement client, so that is fine.

**Negatives are fragmented.** Five shared lists (a 102-member "negative", and four October lists with Spanish names scoped by campaign: Remodel+Roof 281 members, Ventanas 53, competidores 2026-10-27, reparacion PMax) plus 42 campaign negatives on Campaign 1. "lowes", "lowe's" and "home depot" exist only on the Remodel+Roof list, which by its own name is not attached to the windows campaign or Performance Max, so Lowe's queries still cost $407 on Campaign 1. 57clicks did add windowwall, mi windows, first choice, abc impact, armorvue and polk county on Oct 27 and Nov 3 to 5, so the top competitor leaks are already closed going forward.

**Ads.** Three RSAs in every live group; two POOR (Bathroom Remodeling Contractors, Walk-In Shower). The windows groups are GOOD and EXCELLENT.

### Prepared change list (only if Tom confirms REK is engaged)

1. Campaign 1 off Manual CPC. Maximize Conversions with a $300 target CPA, or at minimum a $35 CPC ceiling; nothing in this campaign has earned $57 to $88 a click. Move half the $406 to Performance Max, which is 57 percent rank-lost at a $115 CPA.
2. Pause "window replacement company orlando" ($1,266, 0), "impact window replacement" ($492, 0), "impact resistant windows" exact and phrase ($450, 0, QS 2), "impact window contractor" ($137, 0), "replacement windows orlando" ($113, 0). Replace with exact "impact windows orlando", "impact window installation", "hurricane windows orlando" ("hurricane windows" matched $213 on its own).
3. Attach a retailer and supplier list to Campaign 1 and Performance Max, phrase match. New, not present anywhere live: goodman, cws, reece, tafco, window shoppe, "w robbins", "cq insulation", "stone spirit", "granite fabricator", "cabinet paint", "national bath", "love your bath", "$99", aluminum, vinyl, "glass block", "glass company", "screen porch". Present on the wrong list only (Remodel+Roof, not on windows or PMax): lowes, lowe's, home depot. Already live on Campaign 1 or PMax: windowwall, first choice, abc impact, armorvue, armour view, mi windows, polk county, mr granite, elite granite, "window glass replacement", commercial, supplier, supply, fabricator, jobs, diy.
4. Restore "Submit lead form" to primary and included (41 a month is the account's form volume), set the two YouTube actions secondary, and pick one call action (the 60-second one) as primary.
5. Agree with 57clicks and the client on one owner for pause and budget changes. Two parties flipped campaign status on Nov 5 and 6.

## Deep dive 4: Precision GPR (554-113-4760), score 59 F, up 9

Context applied: active cleanup since Aug 2026; budget line $2,500 a month, judged on cost per conversion. This window: $3,154 for 21 conversions at $150. Weekly: $716, $704, $752, $826 with 3, 6, 5, 5 conversions. September was $117 and October $138, so CPA is drifting up while spend holds; by Tom's rule that is a yellow, not a red. Dave trimmed the seven budgets to $84 a day on Nov 6.

| Category | Score |
|---|---|
| Conversion Tracking | 60 |
| Wasted Spend | 50 |
| Account Structure | 55 |
| Keywords & Targeting | 50 |
| Ads & Assets | 85 |
| Bidding & Settings | 55 |

| Campaign | Budget/day (Nov 6) | Spend | Clicks | CPC | Conv | CPA |
|---|---|---|---|---|---|---|
| LP Search - Location | $13 | $576 | 23 | $25.05 | 3.0 | $192 |
| LP Search - Concrete Scanning | $18 | $551 | 27 | $20.40 | 3.5 | $157 |
| LP Search - Services | $13 | $533 | 30 | $17.78 | 3.0 | $178 |
| LP Search - GPR Scanning | $10 | $529 | 35 | $15.11 | 2.0 | $264 |
| LP Search - Utility Mapping | $12 | $454 | 41 | $11.08 | 2.5 | $182 |
| LP DSA - All Pages | $10 | $298 | 45 | $6.62 | 5.5 | $54 |
| LP Branded | $8 | $212 | 24 | $8.85 | 1.5 | $142 |

### What moved since Sep 14

- CPA $268 to $150 and conversions 9 to 21. The cleanup is working in aggregate.
- The DSA campaign is now the cheapest source (5.5 conversions at $54). The Sep 4 advice to pause it is withdrawn; keep it and raise it before any keyword campaign.
- Conversion tracking: "Michael Phone Number (305)" now records (9 in 30 days), lp_contact_form 8, Calls from ads 2, Smart campaign calls 2. The (305) 490-0593 and (786) 508-9082 website call actions are still at zero for 30 days; with the Michael line working these two are duplicates to pause, not tags to test. The three "Contact Us" GA4 actions still coexist, all secondary.
- Still open: Location campaign duplicates GPR Scanning ("gpr scan", "gpr scanning", "gprs scanning" cost $93 in Location against exact "Gpr Scanning Near Me" at QS 3 and $28 a click). "gprs" is still not a negative: "gprs orlando" $40 plus $23, "gprs scanning" $27, "gprs" $26, "gprs locating" $17, "gprsinc com" $12; but "gprs orlando" and "gprs tampa" also produced 2.5 conversions in Concrete Scanning and Services, so block the bare term and the company name, not the city variants. The 811 negative does not catch "mygeorgia811" $20, "who to call before digging in florida" $13, "call before digging florida" $11 or "sunshine locate" $14.
- New: Dave added "precision gpr" as a BROAD keyword in Branded on Oct 23. It matched "beryl project engineering" $14, "directional boring company" $12, "structural engineer" $9, "underground utility locating services near me" $15 and "gprsinc com" $12. Change it to phrase.
- Ground Penetrating Radar exact and phrase ($183, 0 conversions, QS 3) and "ground penetrating radar surveys" ($164, 0) are still the biggest zero lines; "Gpr Scanning" phrase in the same campaign converts ($116, 1).

### Prepared change list

1. Negatives, deduped against LP NKWs (227 members, on all seven live campaigns). New: gprs (exact), gprsinc, "call before", "before digging", sunshine, "dig alert", price, pricing, "how much", beryl, "structural engineer", "directional boring", geoslice, "s&n", "for sale", georgia, topographical, "engineering companies". Already present: 811, "ditch witch", rental, "low cost".
2. "precision gpr" broad to phrase in Branded.
3. Pause "Ground Penetrating Radar" exact and phrase and "ground penetrating radar surveys" in GPR Scanning; keep "Gpr Scanning" phrase and "ground penetrating radar service near me".
4. Pause the (305) 490-0593 and (786) 508-9082 website call actions; merge the three Contact Us GA4 actions into one.
5. Leave the Nov 6 budgets for two weeks, then shift $5 a day from Location to DSA if Location's CPA is still above $180.

## Deep dive 5: All Phase Pool Remodeling (103-111-7688), score 62 D, down 10

30 days: $871, 13 conversions at $67 (Sep 14: $779, 30 at $26). Calls From Ads 11, website call 2. "Request quote", "Phone Calls 60s+" and "Contact Form" (primary, not included) recorded nothing counted. Brand terms ("all phase pool remodeling", "all phase pools", "all phase pool") produced 9 of the 13 conversions and cost $410, still as a BROAD keyword inside the non-brand "Pool Renovations" group, so the non-brand keywords delivered 4 conversions for $461. "swimming pool renovations" broad spent $204 for 0, "swimming pool renovations near me" $37 for 0. The 379-member master negative list is still attached only to the paused campaign; the live campaign runs on 91 campaign negatives. Budget-lost impression share is 57 percent at $30 a day. Dave added one keyword and edited one RSA on Oct 22; nothing else changed.

Why the score dropped: conversions fell by more than half while spend rose, the brand split (worklist item 12) did not happen, and the brand keyword is now a larger share of a smaller total.

Prepared change list: (1) brand into its own campaign with exact and phrase "all phase pool remodeling", "all phase pools", "all phase pool"; $8 a day; (2) attach the master negative list to the live campaign; (3) pause "swimming pool renovations" broad, keep "pool resurfacing companies near me" (4 conversions on $150); (4) new negatives, deduped: "red rhino" (currently only excluded per-term), "aqua pool", tempool, "american pool", "cody pools", "keystone tile", leslie, "lake mary", cleaners, coatings, "deck resurfacing"; already on the unattached master list, so they land with item 2: "pinch a penny", jacksonville, "pool builders"; (5) manual test of Request quote and Phone Calls 60s+, which have been at zero since at least Sep 4.

## Filutowski Eye Institute (192-870-7876), score 43 F, provisional, no new deep dive

Scope is still undecided since Sep 14; no REK edits in 30 days (catie@accaliamarketing.com made all 29 changes). The account changed shape: Performance Max (63 conversions at $11 in September) is paused, Brand Awareness budget is $211 a day instead of $430, and the four lead-gen campaigns got ad schedules and new target CPAs on Oct 15. Result: $15,980 for 168 conversions at $95 (Sep 14: $17,496 for 354 at $49). The catch-all "lasik treatment cost" broad keyword still took $10,437 (65 percent) for 54 conversions at $194, while Branded ($21 CPA) loses 82 percent of its impressions to budget and Eye Surgery ($49 CPA) loses 77 percent. Visible waste on competitor, retailer, insurer and optometry terms: $3,152 with zero conversions across 680 terms ("eye doctors that take florida blue" $205, "mid florida eye center mount dora" $173, "florida eye clinic altamonte" $133 plus $96 plus $95, "tomoka eye associates" $111, "the lasik vision institute" $96, "samantha xavier md" $90). Every live ad group still has one RSA; Branded's is POOR. 18 Universal Analytics goals and YouTube follow-on views remain primary and included. Enhanced Conversions for leads is still on at a medical practice. The Sep 14 change list stands as written; dedupe this run: walmart, lenscrafters, america's best, costco, stanton, visionworks, my eye doctor, target optical, pearle and eyeglass now exist on the "Search Terms" list, which is attached to the live campaigns; everything else on the Sep 14 list is still absent. A Drive sheet "FEI New Website URL Changes (for Google Ads)" owned by Tom (Oct 19) suggests REK is involved in the website; Tom should say whether that extends to the Ads account.

## No action needed this week (one-liners)

- **Rover Veterinary Care (59 F):** 19 conversions at $131 (Sep 14: 19 at $103). Click to call 10, Book appointment 7, form 2. "Calls from ads" and "Event|Contact|Calls From Website" are still zero for 30 days; the other call action works, so pause the duplicates rather than test them. Waste $412: "lap of love" variants $157 outside the Competitors campaign where it is a bid keyword (the Competitors exact keyword itself cost $256 for 1.5), "dog dementia when to put down" $74, "heaven at home pet hospice reviews" $55, "when to put your dog down quiz" $26, "euthanize dog" $27. New phrase negatives, deduped: "heaven at home", quiz, dementia, "when to put", "should i", "euthanized"; put "lap of love", lapoflove and "laps of love" on the Euthanasia and Cremation campaigns only. "peggy adams" exists on a list that is not attached to any live campaign. Pause "mobile dog put down service" ($226 at $45 a click, 0) and "dog put to sleep" ($200, 0). The two Competitors RSAs are still POOR (worklist item 16). On rotation next Monday.
- **Scootz (60 D):** 25 conversions at $59, Booqable purchases 17 and calls 8. The six-way split landed Nov 3 (worklist item 17); each new group has one RSA and the Brand group's is POOR. Still Maximize Clicks with 40 percent lost to budget; with 25 counted conversions Maximize Conversions is now defensible. form_submit remains secondary and silent. Waste $83: scooterbug $17 (only "scooterbug orlando photos" exact exists; add phrase scooterbug and "scooter bug"), "buena vista scooter" $10, "gateway scooter" $3, ucf $9, "knee scooter" $3. This week 2 conversions after 8; re-check next Monday before judging the Nov 3 change.
- **Quality Paralegal Services (61 D, new):** Tom built it Oct 12 to 23. 51 conversions at $29 on a $27 target CPA; calls 36, website calls 3, forms 6. Findings are hygiene: "family law attorney near me" broad is QS 1 but produced 8 conversions on $310, so it stays; 13 QS 1 to 3 keywords; every ad group has one RSA (one POOR); the main campaign reports HAS_ADS_DISAPPROVED; "QPS Immigration Document Prep" $110 for 0 on Maximize Clicks; a non-lawyer practice buying "best lawyers in orlando" $28 and "custody lawyers" $15 for 0. New negatives, deduped: emancipation, "process server", hotline, department, departamento (notary and notario converted once each, leave them). Already present: "clerk of courts", "phone number", número, free, gratis, salary, "how to become".
- **Florida Sealcoating (66 D):** 25 conversions at $127 on $3,175 (Sep 14: 21 at $78 on $1,647; the ramp to $3,000 a month happened). Dave cut the three search budgets to $83 a day on Oct 23 and 30, which is about $2,650 a month, below the approved plan; confirm that is intended. Branded cost $568 for 2 conversions: "florida sealcoating" exact $126 and "florida sealcoating llc" phrase $86 with 0, which for a brand term means a landing or tracking problem on those clicks. Competitor and supplier negatives from Sep 4 are still missing: new, deduped: "seal master" (two words; "sealmaster" one word exists), "tru mark", appell, "g force", "road paving", "hot asphalt", "sealers for", "asphalt driveway" (DIY intent). "asphalt paving company near me" phrase $280 for 0 at $35 a click is the keyword to cap. 2 conversions this week after 9; on rotation next Monday.
- **M&S Asphalt Paving (66 D, new this window):** Tom reactivated it Oct 15. $655 for 4 conversions at $164; Paving - Volusia carries all of it. Paving - Orlando Metro ($14 a day) has not served. 7 of 8 groups have one RSA. The "Call ((386) 215-7466)" and "Calls from ads" actions are categorized SUBMIT_LEAD_FORM; harmless but wrong. Nothing to change until it has 30 more days.
- **Aqua Coat (67 D):** 13 conversions at $36. The 248-member master list is still attached only to the paused campaign (third report in a row). Pool Equipment group got a new keyword and RSA on Oct 28, the opposite of worklist item 7; "swimming pool equipment" broad did bring 2 conversions on $125, so the group is defensible if the retailer terms are blocked. New negatives, deduped: "pool painter", "fresh finish", aquastrong, "pool rails", sekas, hayward, handrail, "blue science", "aqua pools", "pcs pools", equipment (if the group is paused), "aqua dreams", "masters pool". On the unattached master list already, so they land when it is attached: leslie, "pinch a penny", pump, heater, "repair kit", supplies. Target CPA from Sep 9 is gone; the campaign shows plain Maximize Conversions. On rotation next Monday.
- **The Counseling Group (68 D):** $648 in 30 days at $26.50 a day since Oct 26 (Tom), on plan. 3 counted conversions plus 5 tel taps that the Conversions column does not show. "therapist near me" exact ($43, 0) and "therapist orlando" exact ($16, 0) are QS 2 with landing page BELOW_AVERAGE; the Winter Park landing page (worklist item 11) is still the biggest lever. "help with depression" $67 and "stress therapy" $19 are still enabled (item 8). Depression group has a POOR RSA. New phrase negatives, deduped: ect, tmz, lavender, "deep breathing", homework, hotline, "er for", emergency, "orlando thrive", "restored purpose", "la amistad", livethelife, vernacchia, kissimmee, "post partum" (two words), medicine. Already present: tms, gorman, postpartum, medication, psychiatrist, antidepressant, supplements. Enhanced Conversions confirmed off (field absent).
- **Affordable Critter Solutions (76 C):** 16 conversions at $19, three RSAs in Attic, two in Wildlife Removal. Waste $26 ("dr critter", "critter control" name searches). The 11 paused campaigns remain (item 19). $10 a day with 31 percent lost to budget at a $19 CPA; the $15 ask stands.
- **Color Masters:** Tom's three REK search campaigns ran Oct 7 to 22 ($738, 1 conversion, Residential Painting at $10 a click with 45 percent rank-lost) and are paused. The removed Smart campaigns were the client's. No change list until it restarts.
- **REK Marketing:** internal. GBP Verification search $326 for 1 "Free Read Requested", San Diego and Philadelphia $162 each for 0; one RSA per group, one PENDING and one POOR. Not scored.
- **All Phase Jacksonville:** search side spent nothing; the "Orlando" campaign is still ENABLED and NOT_ELIGIBLE (item 6). LSA out of scope.
- **Jupiter Boat Supply:** paused, zero spend.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: American Impact (deep dive 3 item 3), Filutowski (Sep 14 list minus the ten now present), Patio Style (assembly, handyman, carport, pictures, "show me"), Progetto (smart wings, smartwings, "blind and shutter pros", macy, pottery barn, "pictures of", matter, blinds.com), Precision GPR (deep dive 4 item 1), All Phase (deep dive 5 item 4), Rover, Scootz, Florida Sealcoating, Aqua Coat, Counseling Group and Quality Paralegal (one-liners above).

Dropped as already present: American Impact windowwall, first choice, abc impact, armorvue, mi windows, polk county, mr granite, elite granite; Filutowski walmart, lenscrafters, america's best, costco, stanton, visionworks, my eye doctor, target optical, pearle, eyeglass; Precision GPR 811, ditch witch, rental; Counseling tms, gorman, postpartum, medication, psychiatrist, antidepressant, supplements; Progetto ikea, amazon, wayfair, 3 day blinds, budget blinds, diy, how to, reviews, jobs; Patio ideas, panels, mirador; Quality Paralegal clerk of courts, phone number, free, gratis, salary. Present only on a list that is not attached to a live campaign (lands when the list is attached): Aqua Coat leslie, pinch a penny, pump, heater, repair kit, supplies; All Phase pinch a penny, jacksonville, pool builders; Rover peggy adams.

Blocking-risk check: "commercial" is live as a phrase negative on American Impact's Remodel+Roof list; fine for remodel, but keep it off the windows campaign ("commercial windows" is a real service). "equipment" at Aqua Coat would block "pool equipment installation", which converted twice; add it only if the group is paused. "emergency" at the Counseling Group blocks "emergency couples therapy", which the practice does not offer, so it is safe.

New keywords to add: Patio Style exact "outdoor kitchen contractors orlando" (the converting kitchen term) and "patio furniture longwood" (converted twice through phrase); Precision GPR exact "gpr services near me" ($72, 1 conversion, currently matched by the QS 3 exact) and "underground utility near me"; Florida Sealcoating exact "asphalt companies in orlando fl" (2 conversions on $94) and "seal coating driveway"; Rover exact "at home pet euthanasia services near me" (2 conversions across two campaigns; give it one home); American Impact exact "hurricane windows orlando" and "impact windows orlando" (deep dive 3 item 2); Aqua Coat phrase "pool repair tampa" (1 conversion on $22).

Bid and budget adjustments: American Impact Campaign 1 off Manual CPC, $300 target CPA or $35 ceiling, and $200 a day to Performance Max; Patio Style cap the $17.26 kitchen bids at $8 and pause the pergola installer keywords; Progetto hold at $115 a day until tracking is verified; Precision GPR leave the Nov 6 budgets two weeks; Florida Sealcoating confirm the $88 a day cut against the $3,000 plan; Scootz Maximize Conversions once the Nov 3 change has a second week; Affordable Critter $10 to $15 a day (client decision).

Competitive read (rank-lost share as the proxy): Rover and Filutowski Branded are not being outbid (rank loss under 10 percent); their problems are conversion and budget. Affordable Critter, Patio Furniture, Scootz, Progetto and the Precision GPR DSA lose 57 to 71 percent to rank on tight budgets and Quality Score, which is a budget and relevance story. American Impact loses 28 percent to rank despite $57 clicks because its Quality Scores are 1 to 3; paying more will not fix that, better ads and pages will.

## Prioritized weekly action plan

1. **Critical, Tom: decide American Impact's scope.** If REK is engaged, deep dive 3 items 1 to 5. The Manual CPC search campaign alone spent $12,246 for 22 conversions; Performance Max in the same account does $115. If REK is only linked, say so and the routine will report it as excluded.
2. **Critical, REK (paidads): Patio Style directions.** Restore "Get directions (GTM) 11 Sep" to primary and included, confirm it does not double count the GA4 import, and leave the GA4 import secondary. Then the Pergolas and Kitchens pauses in deep dive 1.
3. **Critical, Tom: Progetto Shades tracking and landing pages.** Manual test of Contact, the (858) call action and the GA4 lead form; set the (858) action to included; hold budgets at $115 a day until then. Then the shutter and motorized landing pages.
4. **High, REK: Precision GPR.** The deduped negative list (gprs exact, gprsinc, the four 811 phrasings, sunshine, price and cost terms, the engineering and boring terms), brand keyword to phrase, pause the two dead call actions.
5. **High, REK: All Phase Pool Remodeling.** Brand campaign split, attach the master list, pause "swimming pool renovations" broad.
6. **High, REK: Rover.** Pause "mobile dog put down service" and "dog put to sleep", add the dementia, quiz and heaven-at-home negatives, scope the lap-of-love negatives to the two non-competitor campaigns, rebuild the two POOR Competitors RSAs (seven weeks open).
7. **Medium, REK: Florida Sealcoating.** Confirm the $88 a day budget is the intended level against the $3,000 plan; add the competitor and supplier negatives (nine weeks open); look at why exact brand clicks do not convert.
8. **Medium, REK: Aqua Coat.** Attach the master list to the live campaign (three reports), then the retailer and equipment negatives.
9. **Medium, REK: Scootz.** Second RSAs in the five new single-ad groups, replace the POOR Brand RSA; Maximize Conversions after next Monday's read.
10. **Medium, REK: The Counseling Group.** Confirm the tel-tap action is included in Conversions, pause "help with depression" and "stress therapy", the Depression POOR RSA, the medical-treatment negatives. Landing page remains the big lever.
11. **Low: Quality Paralegal** second RSAs and the disapproved ad, **Filutowski** scope decision (Sep 14 item 2 still open), **Affordable Critter** paused-campaign cleanup and the $15 ask, **All Phase Jacksonville** pause the Orlando campaign, **Citrus** confirm the new pay-per-lead Performance Max campaigns stay out of scope, **M&S** second RSAs after 30 more days.

## Rotation

Deep-dived this run: Patio Style, Progetto Shades, American Impact (provisional), Precision GPR, All Phase Pool Remodeling. Everything else is overdue because no run happened between Sep 14 and Nov 6. Due next Monday: Rover Veterinary Care, Florida Sealcoating and Scootz (all three with a conversion dip this week), plus Aqua Coat to measure the master-list attachment if it lands. The week after: The Counseling Group, Affordable Critter Solutions, Quality Paralegal Services, M&S Asphalt Paving.

## Data notes

- Account discovery returned 32 client accounts; Sep 14 had 26. All 26 are still present. Compare next week against this run's list.
- The google-ads client in this session supports API v23 to v26 only; v25 was used because v26 drops customer.conversion_tracking_setting.enhanced_conversions_for_leads_enabled, which the protocol requires for the healthcare check. campaign.start_date and the recommendation impact fields are not selectable in v25; Google's recommendations were pulled by type only. tools/gaql.py was not changed; the version came from the GOOGLE_ADS_API_VERSION environment variable it already honors.
- Search-term tables use Google's visible terms only. Waste figures are the zero-conversion part of pattern-matched competitor, retailer, supplier, informational and out-of-service terms, so they are floors; the Sep 14 Filutowski figure used a narrower hand-picked list, which is why the two are not directly comparable.
- Where an action's Conversions count and all-conversions count disagree for the same window (Counseling tel tap 0 against 5, American Impact Submit lead form 41 against 41 while marked secondary, Patio Style directions 0 against 41), the include-in-Conversions setting changed during the window. Conversion-action edits do not appear in change history, so who changed them and when is unavailable.
- Week-over-week uses daily rows summed into Oct 30 to Nov 5 and Oct 23 to Oct 29. The per-campaign weekly rows from the API use Monday-start weeks and are quoted only where labeled as such.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown, not low.
- Change history was pulled from Oct 8 (the API allows 30 days). The Progetto, Quality Paralegal, M&S and Color Masters builds in mid-October are visible; anything earlier is not.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
