# PPC Weekly Audit - 2026-11-23 (Google Ads fleet)

Run: Monday Nov 23, 2026, scheduled cloud session through tools/gaql.py (API v24) against MCC 656-695-7229. Windows: 30 days Oct 24 to Nov 22; this week Nov 16 to Nov 22; last week Nov 9 to Nov 15. Score deltas are against the Nov 16 report. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: American Impact (measuring the Nov 19 and 20 changes), Patio Style (two new campaigns and a budget ceiling that doubled), Quality Paralegal Services, M&S Asphalt Paving and Rover Reno PPC (rotation, first deep dive for each). Short status blocks for Progetto Shades, Filutowski Eye Institute and Precision GPR, which were deep-dived last week and where little or nothing changed. One-liners for the rest.

The google-ads.yaml from the Drive folder dave-ads-setup (Sep 8 version) was copied with mode 600, used only by the client library, and deleted before this report was written. No value from it appears anywhere in the session output.

## Attention items (read first)

1. **American Impact (974-265-3397): the search fix landed, but the Performance Max budget went the wrong way.** Tom switched the search campaign to Maximize Clicks with a $60 CPC ceiling on Nov 19 and Dave added 65 negatives on Nov 20. Search CPC fell from $54.76 (30-day average) to $29.21 this week and the account went from 4 conversions on $6,877 last week to 12 on $4,081 ($340 each). However, 11 of the 12 conversions came from Performance Max ($1,452, $132 each), and Tom cut the PMax budget from $300 to $100 a day on Nov 19. The search campaign spent $2,629 this week for 1 conversion, $1,466 of it on one phrase keyword, "window replacement company", with zero conversions. Deep dive 1.
2. **Rover Veterinary Care (750-667-5721) is in its second week with no enabled campaigns and zero spend.** No change events since Dave's Nov 15 pause. Whether the pause was the client's request is still unconfirmed. In the 30 days before the pause the account did 17 conversions on $2,252.
3. **Patio Style (596-555-8707): Dave built two dealer-brand search campaigns (Napoleon, Twin Eagles and Delta Heat) on Nov 17 and 18.** Six enabled campaigns now carry $151 a day of budget, about $4,600 a month, against actual spend of $1,950 to $2,560 a month since August. Ad-group bids on the new campaigns were raised from $4 to $10 on Nov 19 and keyword bids to $12 and $15 on Nov 23; the first four clicks cost $9.92 each with no conversion. The Pergolas ad-group bid was raised to $10 (the Nov 16 list asked for a $6 cap). Both Get Directions actions are still secondary, third week running. Deep dive 2.
4. **Progetto Shades (416-010-8247) recorded its first primary conversions since Oct 27: two Contact submissions, Nov 17 and Nov 19, on $874 of spend.** Nothing from the Nov 16 list has been applied and there are no change events since Nov 10. 43 keywords at Quality Score 1 to 3 still carry $2,056 of the $3,755 spent in 30 days.
5. **Precision GPR (554-113-4760): revise last week's "gprs" recommendation.** The competitor-name queries converted three times this window ("gprs orlando" 2 conversions on $71, "gprs tampa" 1 on $72), at roughly $48 each against a $204 account average. Treat GPRS as a deliberate conquest term with one home (the GPR Scanning campaign) rather than a negative. This week: $557 for 2 conversions. November to date is $1,742 for 8 ($218) against October's $3,163 for 24 ($132): spend is down and CPA is up, which under the Nov 4 rule is needs attention, not critical.
6. **Rover Reno PPC (961-477-3743): the four live campaigns have no call assets, and the account has no "Calls from ads" conversion action.** The only call assets in the account sit on the two paused campaigns. "Calls from Smart Campaign Ads" produced 9 of the account's 21 conversions in 30 days and has recorded nothing since the week of Nov 2, when Leads-Search-1 was paused. Phone calls from the ads themselves are not being measured. This week: 2 conversions on $245 after 8 on $243. Deep dive 5.
7. **Filutowski Eye Institute (192-870-7876): no changes by anyone since Oct 29, and the best week since the site launch (29 conversions on $2,181, $75 each).** A conversion action named "Cataract In-Office Appointment Scheduled" recorded its first 2 conversions this week; its creation date is unavailable in the API. The Contact form is still primary, Enhanced Conversions is still ON, and the live Cataracts ad still points at the old /cataract-surgery/ URL. Scope decision still open.
8. **Account discovery: 34 client accounts, the same 34 as Nov 16.** Nothing vanished, nothing new. Premium Walk-In Clinic and Premium Medication Refills remain unlinked as expected.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 34 client accounts, 1 manager | 14 scored, 1 paused | Same set as Nov 16. Excluded: Byers Fence x2 (not REK-managed), Herrell Plumbing (per protocol, but see Data notes), ProShield (client-run), 9 LSA-only accounts. Not scorable: Color Masters, Jupiter Boat Supply, All Phase Jacksonville (no search spend). REK Marketing's own account is listed but not scored. |

Search, Performance Max and Display spend in the 30-day window: $43,458 for 245 primary conversions across the 14 REK-managed scored accounts (Rover Veterinary Care included for the days before its pause), plus $10,526 at Filutowski Eye Institute and $1,657 in REK Marketing's own account. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Nov 16. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical (F), Needs attention (D), On target (C or better).

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $10,526 | 113 | $93 | 46 | F | +1 | Critical (scope) | "lasik treatment cost" broad is $5,659 of $10,526 and still matches clinic and doctor names ($1,296 visible); Contact form still primary; Enhanced Conversions ON in a healthcare account | $1,296 |
| 2 | Progetto Shades | 416-010-8247 | $3,755 | 3 | $1,252 | 51 | F | 0 | Critical | 43 keywords at QS 1 to 3 carry 55 percent of spend; two conversions this week after four weeks of none; nothing from Nov 16 applied | $154 |
| 3 | American Impact | 974-265-3397 | $22,343 | 37 | $604 | 52 | F | +1 | Critical | Search to Maximize Clicks with a $60 ceiling landed, CPC $55 to $29; PMax (11 of 12 conversions this week) cut to $100 a day; "window replacement company" $1,466 this week for 0 | $2,207 |
| 4 | Patio Style | 596-555-8707 | $2,599 | 13 | $200 | 54 | F | -2 | Critical | Two new dealer campaigns, budget ceiling now $151 a day; dealer bids $10 to $15 before a first conversion; directions still secondary; 11 of 12 ad groups one RSA | $205 |
| 5 | Precision GPR | 554-113-4760 | $2,650 | 13 | $204 | 56 | F | 0 | Needs attention | Spend down, CPA up ($132 October to $218 November); Location still live at $23.51 a click; "gpr scanning" matches five campaigns; GPRS conquest converting | $194 |
| 6 | M&S Asphalt Paving | 827-724-4095 | $990 | 5 | $198 | 58 | F | -2 | Needs attention | Zero change events in 30 days; Orlando Metro $223 for 0; "asphalt paving" phrase $278 for 0.5; 7 of 8 ad groups one RSA | $144 |
| 7 | Quality Paralegal Services | 447-153-2607 | $1,338 | 37 | $36 | 62 | D | -1 | Needs attention | 74 percent broad; Spanish lawyer queries not blocked ($153); all five ad groups one RSA, one POOR; conversion count halved from September to October without a spend change | $153 |
| 8 | Rover Reno PPC | 961-477-3743 | $906 | 21 | $43 | 62 | D | -2 | Needs attention | No call assets on the four live campaigns and no call conversion action; 83 to 90 percent lost to budget at $35 a day; all seven ad groups one RSA | $58 |
| 9 | All Phase Pool Remodeling | 103-111-7688 | $842 | 13 | $65 | 65 | D | 0 | Needs attention | Unchanged since Nov 10; brand still inside non-brand groups ($300 of $842); 100 percent broad; master list attached to the paused campaign only | $58 |
| 10 | Aqua Coat Pool Plastering | 285-714-0527 | $437 | 15 | $29 | 65 | D | 0 | Needs attention | 248-member master list still attached only to the paused campaign (tenth week); 4 conversions at $22 this week | $80 |
| 11 | Florida Sealcoating | 168-852-7101 | $2,530 | 21 | $120 | 67 | D | -1 | Needs attention | Dave added a Pothole Repair group and moved budget today; brand keywords $217 for 0 primary on Maximize Conversions; competitor negatives still missing (stripe it rite, dmi, all asphalt services) | $319 |
| 12 | Scootz | 185-574-5478 | $1,911 | 32 | $60 | 68 | D | +2 | Needs attention | Tom set a $75 target CPA on Nov 20 (worklist 17 done); CPC $1.01 to $1.53 in the first three days; 6 of 7 groups one RSA; form_submit still dark | $13 |
| 13 | The Counseling Group | 657-069-3617 | $601 | 2 | $301 | 69 | D | +1 | Needs attention | 2 primary in 30 days on plan ($26.50 a day); "counseling winter park" phrase $205 for 0 primary is a third of spend; one POOR RSA (Depression) | $18 |
| 14 | Affordable Critter Solutions | 227-108-4521 | $304 | 16 | $19 | 76 | C | +1 | On target | 16 conversions at $19; clean terms; four never-firing actions still primary | $17 |
| paused | Rover Veterinary Care | 750-667-5721 | $2,252 (to Nov 14) | 17 | $132 | was 49 | F | not rescored | Paused | All campaigns paused by Dave on Nov 15; zero spend this week; pause unconfirmed | $142 (pre-pause) |
| own | REK Marketing | 390-315-5264 | $1,657 | 1 | n/a | n/a | internal | n/a | Internal | GBP Verification paused around Nov 11; Philadelphia and San Diego lead campaigns $270 this week for 0 conversions, $1,111 in 30 days for 0 | n/a |
| none | Color Masters | 426-092-9847 | $0 | 0 | n/a | n/a | paused | n/a | Paused | No change since Tom paused it Oct 22 | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 | 0 | n/a | n/a | no search spend | n/a | Paused (search) | "Orlando" campaign still ENABLED at $49 a day and NOT_ELIGIBLE (ad groups paused); spends nothing (worklist 6 open) | n/a |
| none | Jupiter Boat Supply | 216-859-2093 | $0 | 0 | n/a | n/a | paused | n/a | Paused | Nothing to do | n/a |

## Week over week (Nov 16 to 22 against Nov 9 to 15, search, PMax and display only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| American Impact | $6,877 to $4,081 (-41%) | 1,558 to 669 | 2.2% to 3.0% | $4.41 to $6.10 | 4 to 12 | $1,719 to $340 | Search $2,629 for 1; PMax $1,452 for 11 after its budget was cut to $100 |
| Filutowski Eye Institute | $2,185 to $2,181 (0%) | 150 to 137 | 7% to 5% | $14.56 to $15.92 | 22 to 29 | $99 to $75 | Best week since the site launch; no changes made |
| Progetto Shades | $801 to $874 (+9%) | 189 to 210 | 4% to 4% | $4.24 to $4.16 | 0 to 2 | none to $437 | First conversions since Oct 27 (Shutters 1, Exterior 1) |
| Florida Sealcoating | $723 to $618 (-15%) | 108 to 97 | 6% to 6% | $6.69 to $6.37 | 7 to 5 | $103 to $124 | Residential 3.5 to 2; Dave's Nov 23 changes not yet measurable |
| Patio Style | $651 to $593 (-9%) | 184 to 162 | 8% to 7% | $3.54 to $3.66 | 2 to 2 | $325 to $297 | all_conversions 165 to 81; directions (secondary) 10 to 7 |
| Scootz | $593 to $505 (-15%) | 585 to 330 | 7% to 8% | $1.01 to $1.53 | 12 to 8 | $49 to $63 | Target CPA $75 set Nov 20; clicks fell, CPC rose, three days of data |
| Precision GPR | $456 to $557 (+22%) | 31 to 33 | 6% to 7% | $14.69 to $16.87 | 0 to 2 | none to $278 | GPR Scanning 1, Services 1; DSA spent nothing this week |
| Quality Paralegal Services | $306 to $344 (+12%) | 96 to 98 | 6% to 6% | $3.19 to $3.51 | 14 to 9 | $22 to $38 | Immigration campaign 1 to 0; small numbers |
| M&S Asphalt Paving | $276 to $274 (-1%) | 24 to 22 | 6% to 7% | $11.51 to $12.44 | 0 to 1 | none to $274 | One call from ads |
| Rover Reno PPC | $243 to $245 (+1%) | 149 to 94 | 11% to 17% | $1.63 to $2.61 | 8 to 2 | $30 to $123 | Tom paused an In-Home Euthanasia ad group Nov 21 and re-enabled it Nov 23 |
| All Phase Pool Remodeling | $197 to $236 (+20%) | 37 to 31 | 3% to 7% | $5.33 to $7.61 | 4 to 4 | $49 to $59 | Flat |
| The Counseling Group | $118 to $141 (+19%) | 28 to 32 | 5% to 5% | $4.23 to $4.40 | 0 to 1 | none to $141 | Form lead Nov 19; small numbers |
| Aqua Coat | $127 to $89 (-30%) | 19 to 15 | 3% to 3% | $6.69 to $5.96 | 2 to 4 | $64 to $22 | Good week |
| Affordable Critter Solutions | $84 to $69 (-18%) | 23 to 15 | 8% to 7% | $3.66 to $4.58 | 4 to 5 | $21 to $14 | Good week |
| Rover Veterinary Care | $751 to $0 | 59 to 0 | | | 4 to 0 | | Paused |
| REK Marketing (own) | $512 to $270 (-47%) | 60 to 25 | 6% to 3% | $8.53 to $10.81 | 0 to 0 | none | Internal |
| Fleet, 14 REK-managed | $12,203 to $8,627 (-29%) | | | | 61 to 57 | $200 to $151 | The drop is American Impact (-$2,796) and Rover Vet (-$751) |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share (30 days) is the proxy. Highest rank loss: Quality Paralegal campaign 1 at 70 percent, Patio Style Outdoor Furniture 67 percent, Progetto Exterior 64 percent and Shades & Blinds 59 percent, Affordable Critter 59 percent, M&S Sealcoating 57 percent and Orlando Metro 55 percent, Aqua Coat 54 percent. Highest budget loss: Filutowski 80 to 90 percent on all five campaigns, Rover Reno 83 to 90 percent, Patio Style Outdoor Kitchens 58 percent, The Counseling Group 50 percent, American Impact search 46 percent, All Phase 44 percent. Highest CPCs on REK-managed accounts: American Impact search $29.21 this week (from $54.76), Precision GPR Concrete Scanning $24.66 and Location $23.51, Florida Sealcoating Residential $23.85, Patio Style Pergolas $13.48.

## Changes made in the past week (Nov 16 to Nov 23) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| American Impact | Nov 19 | Tom | Search campaign to Maximize Clicks with a $60 CPC ceiling; PMax budget $300 to $100 a day | Search CPC $54.76 to $29.21, 90 clicks for 1 conversion ($2,629); PMax 11 conversions on $1,452 and now LIMITED by budget |
| American Impact | Nov 20 and 22 | Dave (paidads) | 65 exact-match negatives from search terms (21 on search, 44 on PMax); four RSA edits (headlines, descriptions, tracking template); one more PMax negative and asset automation opted out on Nov 22 | Too early; this week's terms still include livingston, pease, windows liquidators, lipton and monray (all matched before Nov 20) |
| Patio Style | Nov 17 to 23 | Dave (paidads) | Two new manual-CPC campaigns (Napoleon, Twin Eagles and Delta Heat) with 13 and 8 phrase keywords, a 128-member shared negative list, sitelinks; budgets set $30 and $36; ad-group bids $4 then $10; 18 Napoleon and 4 Twin Eagles keywords added Nov 23 with $12.12 and $15.13 bids; Pergolas: "pergola contractor" paused, three ad groups paused, exact negatives [pergola] and [pergolas], ad-group bid $10, "pergola installation" and "custom pergola services" converted to exact (Nov 23); Outdoor Kitchens: "outdoor kitchen company" and "outdoor kitchen design" removed (Nov 18) | Dealer campaigns $40 for 4 clicks, 0 conversions; Pergolas $212 to $129, still 0 conversions; Outdoor Kitchens $140 to $139, 0 conversions |
| Scootz | Nov 20 | Tom | Target CPA $75 on the Maximize Conversions campaign; two campaign criteria edited | Clicks 585 to 330, CPC $1.01 to $1.53, conversions 12 to 8. Three days of data, judge next week |
| Florida Sealcoating | Nov 23 | Dave (sheokand003) | New "Pothole Repair" ad group in Commercial with 22 phrase and exact keywords and one RSA; one sitelink and three callouts; Commercial budget $38 to $28, Residential $30 to $40; one keyword paused | Not measurable yet |
| Rover Reno PPC | Nov 21 and 23 | Tom | One In-Home Euthanasia ad group paused, then re-enabled 38 hours later (ad group name unavailable in the event) | In-Home Euthanasia 5 to 2 conversions; cannot be separated from the small numbers |
| Quality Paralegal | Nov 19 | Tom | Keyword "demanda por manutencion" phrase added to the Spanish campaign | No spend recorded yet |
| REK Marketing (own) | Nov 17 | Tom | Four ad edits, one campaign setting | Internal |
| Filutowski, Progetto, Precision GPR, Rover Vet, All Phase, Aqua Coat, Affordable Critter, M&S, The Counseling Group | | | No changes this week | M&S has had no change event at all since at least Oct 25 |

### Nov 16 action plan reconciliation

1. Rover Vet pause confirmation: open, no change events.
2. American Impact: landed in part. The click ceiling is $60, not $25 to $30; the negatives are exact match rather than phrase; the PMax budget was cut instead of raised.
3. Progetto manual form and call test: no API evidence either way, but the Contact action fired twice this week so the website Contact tag works. Landing page and ad rewrite: not started.
4. Filutowski scope: open.
5. Patio Style: directions not restored to primary; pergola bids raised rather than capped; two zero-conversion kitchen keywords removed (done); kitchen product negatives not added.
6. Precision GPR: "gprs scanning" keyword still live (and this report now says keep it, see attention item 5); Location still live.
7. Aqua Coat master list: still unattached.
8. Scootz to Maximize Conversions: done Nov 20. Second RSAs: not done.
9. Florida Sealcoating Branded to Target Impression Share: not done. Competitor negatives: garcia civil is now excluded; stripe it rite is not. All Phase brand split and "pinch a penny" phrase: not done.
10. Low items: M&S untouched; Quality Paralegal one keyword; Rover Reno budget unchanged; All Phase Jacksonville "Orlando" still enabled; REK Marketing GBP Verification paused around Nov 11, the two lead campaigns still spend with no conversions; Counseling Group name negatives not added.

## Deep dive 1: American Impact (974-265-3397), score 52 F, up 1

| Category | Score |
|---|---|
| Conversion Tracking | 60 |
| Wasted Spend | 35 |
| Account Structure | 55 |
| Keywords & Targeting | 45 |
| Ads & Assets | 65 |
| Bidding & Settings | 55 |

Snapshot, 30 days outside LSA: $22,343, 2,869 clicks, 37 primary conversions, $604 each. Monthly: September $2,228 for 9, October $26,058 for 117 ($223), November to date $17,980 for 21 ($856). This week $4,081 for 12 ($340). The LSA campaign (out of scope) spent $418 for 4.

| Campaign | Status | Bidding | Budget/day | 30d cost | Clicks | CPC | Conv | CPA | This week |
|---|---|---|---|---|---|---|---|---|---|
| Search, Impact Windows, Orlando | Enabled, LEARNING | Maximize Clicks, $60 ceiling (Nov 19) | $300 | $13,307 | 243 | $54.76 | 13 | $1,024 | $2,629, 90 clicks, 1 conv |
| Leads-Performance Max-1 | Enabled, LIMITED by budget | Maximize Conversions | $100 (was $300) | $7,208 | 2,533 | $2.85 | 24 | $300 | $1,452, 579 clicks, 11 conv |
| AIE Search Bathroom Remodel | Paused Nov 10 | Maximize Conversions | $155 | $807 | 16 | $50.43 | 0 | none | $0 |
| AIE Search Home Renovation | Paused Nov 10 | Maximize Conversions | $156 | $641 | 16 | $40.05 | 0 | none | $0 |
| AIE Search Kitchen Remodel | Paused | Maximize Conversions | $275 | $349 | 17 | $20.55 | 0 | none | $0 |
| RMK Display Remarketing | Paused | Maximize Conversions | $20 | $31 | 44 | $0.71 | 0 | none | $0 |

### Findings

**The click ceiling works, the keyword underneath it does not.** Search CPC is $29.21 this week against $54.76 for the 30 days. But "window replacement company" phrase (Window Replacement ad group, Quality Score 3, below-average expected CTR and ad relevance) took $1,466 of the week's $2,629 with zero conversions. The same text also exists, paused, in the Impact Windows ad group where it spent $4,047 for 6.7 conversions in 30 days. The live copy has $1,991 for 1 conversion in 30 days. "window replacement near me" phrase (QS 3) took $487 this week for 1.

**The budget moved against the evidence.** PMax produced 24 of 37 conversions in 30 days ($300 each) and 11 of 12 this week ($132 each). Its budget went from $300 to $100 a day on Nov 19 and it is now LIMITED by budget. Search produced 13 conversions on $13,307 and keeps $300 a day. The Nov 16 list asked for $100 a day to move from search to PMax.

**The new negatives are exact match.** 45 of the 65 Dave added on Nov 20 are brand or retailer names (windowwall, lowes, ply gem, polk county windows, jeld wen, andersen, pgt, pease, livingston, cws, prestige, window world, alside, armorvue, home depot, trulite, mr glass, solartite, aldora, rollshield) as exact-match negatives. An exact negative blocks only that query; "livingston windows" is blocked, "livingston windows reviews" is not. Dedupe against the search campaign's 302 live negatives: livingston and pease are now standalone exact negatives; "cost" and "reviews" exist only inside longer phrases; weathertite is a phrase negative in the shared competitor list and did not match this week. New this week and not covered: storm windows ($23 and $21), jalousie ($27), vinyl replacement windows ($35), windows liquidators ($21), monray ($21), lipton ($23), "window replacement kissimmee" ($103 for 1 click, 0 conversions), Spanish "ventanas de impacto" ($21).

**Confirmed waste, 30 days: $2,207.** Competitor, retailer and supplier queries (weathertite $504, windowwall $262, commercial windows $219, powerhrg $172, lowes $192, goodman $128, ply gem $122, polk county $99, everlasting bath $89, one and done $84, bathremodel tech $59, long home $43, livingston $35, cws $34, prestige $28, pease $23, lipton $23, windows liquidators $21) plus cost and how-much queries ($70). Most of it predates Nov 9. Visible terms cover 44 percent of keyword spend, so this is a floor.

**Conversions.** "Submit lead form" fell from 13 last week to 1 this week, and the GA4 generate_lead action (secondary) fell from 12 to 1, so the two agree and the drop is real, not a tag. "Calls from ads (60s)" rose from 2 to 11. A page-view action (secondary) began firing Nov 16 and recorded 266 this week; keep it secondary. "GET MY FREE QUOTE (Button Click)" recorded 21 this week, secondary. "Clicks to call" is primary but excluded from Conversions. Enhanced Conversions for leads is ON; not healthcare, acceptable.

**Keywords and ads.** 95 percent of keyword spend is phrase match. 60 keywords at QS 1 to 3 carry $7,788 in 30 days, led by the two "window replacement" phrases above. 38 zero-conversion keywords over $10 total $5,339 (the paused remodel campaigns included). The Window Replacement ad group still has one RSA; the other two groups have two each (4 EXCELLENT, 3 GOOD after Dave's edits).

### Prepared change list (suggestions only)

1. Put the PMax budget back to $300 a day, or at least $200. It made 11 of 12 conversions this week at $132.
2. Lower the search ceiling from $60 to $30. The average is already $29; the ceiling only bites on the expensive clicks.
3. Pause "window replacement company" phrase in Window Replacement ($1,466 this week, 0 conversions, QS 3). If the intent is wanted, use exact "impact window replacement company" and "impact window company orlando".
4. Convert the brand-name negatives from exact to phrase (livingston, pease, jeld wen, andersen, pgt, alside, armorvue, window world, lowes, home depot, windows liquidators, monray, lipton). Add phrase: storm windows, jalousie, vinyl windows (confirm the client does not sell vinyl), photos, "window costs", "windows reviews" (not the bare word "reviews", which would block brand-plus-reviews searches).
5. Second RSA in Window Replacement.
6. Reconcile the form drop (13 to 1) against the CRM before judging the Maximize Clicks switch on form volume.

## Deep dive 2: Patio Style (596-555-8707), score 54 F, down 2

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 55 |
| Account Structure | 60 |
| Keywords & Targeting | 60 |
| Ads & Assets | 55 |
| Bidding & Settings | 55 |

Snapshot, 30 days: $2,599, 795 clicks, 13 primary conversions ($200), 482 all-conversions. Monthly: August $2,557 for 122, September $1,951 for 90, October $2,075 for 14, November to date $2,057 for 9. The August and September counts include Get Directions as primary; October onward does not.

| Campaign | Bidding | Budget/day | 30d cost | Clicks | CPC | Primary conv | All conv | This week |
|---|---|---|---|---|---|---|---|---|
| Outdoor Furniture | Maximize Clicks | $30 | $903 | 599 | $1.51 | 4 | 396 | $199, 1 conv |
| Pergolas & Louvered Roofs | Manual CPC | $25 | $768 | 57 | $13.48 | 0 | 39 | $129, 0 conv |
| Outdoor Kitchens | Manual CPC | $20 | $612 | 85 | $7.21 | 2 | 19 | $139, 0 conv |
| Brand | Maximize Conversions | $10 | $275 | 50 | $5.50 | 7 | 26 | $86, 1 conv |
| Napolean Search 18 Nov | Manual CPC | $30 | $30 | 3 | $9.92 | 0 | 2 | new |
| Twin-Eagles & Delta Heat Search 18 Nov | Manual CPC | $36 | $10 | 1 | $10.00 | 0 | 0 | new |

### Findings

**Budget ceiling doubled.** Six enabled campaigns total $151 a day, about $4,600 a month. Actual spend has been $1,950 to $2,560 a month since August. The two dealer campaigns are narrow (4 clicks in five days), so delivery may stay low, but the ceiling is set and the Napoleon budget went $74 to $10 to $30 inside one hour on Nov 18. Confirm with Tom and the client that the dealer test has a budget of its own.

**Dealer bids before data.** Napoleon and Twin Eagles ad-group bids went from $4 to $10 on Nov 19; on Nov 23 two Napoleon keywords got $12.12 and $15.13 bids. The four clicks so far cost $9.89 to $9.93 each ("napoleon grills", "napoleon modular outdoor kitchen", "napoleon prestige connected"). The new shared list (128 negatives) already covers parts and review. The ad groups were created as "Ad group 1" and renamed; the campaign names carry the date.

**Directions are still secondary.** Both "Get directions (GTM) 11 Sep" (7 this week) and the GA4 get_directions import (6 this week) are secondary, as on Nov 16. Primary conversions are 13 in 30 days, so Brand (Maximize Conversions) learns from 7. The protocol says directions are the client's primary goal. This is the third report asking Tom to confirm the intended set.

**Pergolas, partly landed.** "pergola contractor" ($461 for 0 primary in 30 days) is paused, three ad groups are paused, and [pergola] and [pergolas] are exact negatives. Still live: "outdoor pergola" exact $62 for 0, "patio cover orlando" phrase QS 3 $53 for 0, "louvered pergola near me" $31 for 0, "adjustable louvered pergola" $22 for 0. The ad-group bid was raised to $10 on Nov 20 and "pergola installation" was re-created as exact at $9; the Nov 16 list asked for a $6 cap. This week: $129, 12 clicks, 0 conversions. Assembly and handyman queries ($38) are still not negatives.

**Outdoor Kitchens.** $139 this week for 0 conversions. "built in outdoor kitchen" phrase, QS 1, is still live ($109 in 30 days, $58 this week). The two Nov 16 zero-conversion keywords were removed on Nov 18 (done). Product-shopping queries still leak: 304 stainless cabinets $33, modular outdoor kitchens $20, modular cabinets $11, complete packages $11, casual kitchens $11, thor $11. Dedupe: only "ideas" exists; cabinets, modular, packages, stainless, thor are new.

**Outdoor Furniture is the account on the client's real goal.** 396 all-conversions on $903, $1.51 a click. "outdoor patio furniture" 133 all-conversions, "patio furniture store near me" 187.

**Ads.** 11 of 12 live ad groups have one RSA (unchanged since Sep 4); New Pergolas is POOR.

### Prepared change list

1. Tom: confirm the primary conversion set. If directions are primary, restore the GA4 import to primary and included.
2. Dealer campaigns: cap ad-group and keyword bids at $6 and set a combined $20 a day until the first conversion; rename the campaigns and ad groups.
3. Pergolas: ad-group bid back to $6; phrase negatives assembly, handyman, "for sale"; pause "patio cover orlando" (QS 3, $53 for 0).
4. Outdoor Kitchens: phrase negatives cabinets, modular, packages, stainless, thor, pods, backsplash; pause "built in outdoor kitchen" (QS 1).
5. Second RSA in Patio Furniture, Patio Furniture - Local, New Outdoor Kitchens, Fire Pits, Brand; rewrite New Pergolas (POOR).

## Deep dive 3: Quality Paralegal Services (447-153-2607), score 62 D, down 1

Category scores: Conversion Tracking 70, Wasted Spend 70, Account Structure 55, Keywords & Targeting 50, Ads & Assets 50, Bidding & Settings 70.

Snapshot: Orlando paralegal and immigration document preparation, REK-managed. 30 days: $1,338, 410 clicks, $3.26 CPC, 37 primary conversions ($36), 204 all-conversions. Monthly: August $1,244 for 94 ($13), September $1,413 for 98 ($14), October $1,458 for 49 ($30), November to date $1,002 for 32 ($31). This week $344 for 9 ($38) after $306 for 14 ($22).

| Campaign | Bidding | Budget/day | 30d cost | Clicks | Conv | CPA | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|
| Looking for an experienced yet affordable Paralegal? | Maximize Conversions, tCPA $27 | $28 | $719 | 179 | 20 | $36 | 24% | 70% |
| Experienced yet affordable Paralegal / Paralegal con 25 años | Maximize Conversions | $17 | $464 | 139 | 16 | $29 | 53% | 37% |
| QPS Immigration Document Prep | Maximize Clicks | $5 | $155 | 92 | 1 | $155 | 34% | 63% |

### Findings

- **The conversion count halved between September and October on flat spend** (98 to 49, $14 to $30). Calls from ads were steady at 7 to 11 a week through the whole period, so a different primary action stopped counting around Oct 1. "Clicks to call" (Google-hosted, 75 in 13 weeks) is primary but excluded from Conversions today; if it was included in September, that explains the step. Conversion action edits are not in change history, so this is unavailable from the API. Read the September CPA of $14 with that in mind.
- **74 percent of spend is broad match**, and the top keyword, "family law attorney near me" broad, is Quality Score 1 (below average on CTR, relevance and landing page) yet produced 9 conversions on $267. Lawyer-intent terms convert for a non-lawyer firm, which is a compliance exposure: one paused ad is disapproved for UNCLEAR_RELEVANCE and GOVERNMENT_DOCUMENTS_AND_OFFICIAL_SERVICES, and three Smart-campaign ads are APPROVED_LIMITED with a stale disapproval.
- **Spanish lawyer queries are not blocked, $153 in 30 days.** "abogados de familia" $21, "abogados de divorcio en español cerca de mi" $13, "abogado de familia en español cerca de mi" $11, "abogado para divorcio" $11 and a dozen variants, one conversion among them. Dedupe: "abogado" and "abogados" exist only inside longer negatives (such as "abogado gratis"); neither is a standalone negative in either campaign. Standalone-token flag: the Spanish campaign converted on "paralegal en español" and "abogados de familia en español cerca de mi", so a bare "abogado" negative there would also block Spanish speakers who use "abogado" for any legal help. Put the standalone phrase negatives in the English campaign; in the Spanish campaign add only the divorce and child-support lawyer variants as exact.
- **The two English-language campaigns overlap.** "paralegal", "paralegal in orlando", "divorce attorney orlando" and "abogados de familia" each matched both. Campaign 1 loses 70 percent of impressions to rank at a $27 target CPA.
- **Immigration campaign.** Maximize Clicks at $5 a day: $155 for 1 conversion; "renovar green card" phrase $45 on 27 clicks for 0; "citizenship and naturalization services" $18 for 0; "green card renewal help" $12 for 0.
- **Ads.** All five live ad groups have one RSA: 4 AVERAGE, 1 POOR (Spanish campaign, "Ad group 1"). Campaign names are ad headlines.

### Prepared change list

1. English campaign 1: phrase negatives abogado, abogados. Spanish campaign: exact negatives for "abogado de divorcio", "abogados de divorcio", "abogado para divorcio", "abogados para divorcios", "abogados de child support".
2. Second RSA in all five ad groups; rewrite the POOR Spanish RSA; rename campaigns and "Ad group 1".
3. Give the two English campaigns distinct roles (paralegal and document terms in one, family-law terms in the other) so they stop matching the same queries.
4. Immigration: pause "renovar green card" phrase ($45 for 0) or move the campaign to $10 a day with Maximize Conversions once it has 15 conversions; at $5 a day it cannot learn.
5. Find out which action stopped counting on Oct 1 before quoting a CPA trend to the client.

## Deep dive 4: M&S Asphalt Paving (827-724-4095), score 58 F, down 2

Category scores: Conversion Tracking 60, Wasted Spend 55, Account Structure 55, Keywords & Targeting 65, Ads & Assets 50, Bidding & Settings 60.

Snapshot: Volusia County paving, three manual-CPC campaigns. 30 days: $990, 85 clicks, $11.65 CPC, 5 primary conversions ($198). Monthly: September $328 for 5 ($66), October $597 for 5 ($119), November to date $771 for 4 ($193). Spend is up and CPA is up, month on month. This week $274 for 1. There is no change event in this account since at least Oct 25.

| Campaign | Budget/day | 30d cost | Clicks | CPC | Conv | CPA | IS | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|
| Paving - Volusia | $31 | $750 | 62 | $12.09 | 5 | $150 | 50% | 3% | 46% |
| Paving - Orlando Metro | $14 | $223 | 20 | $11.14 | 0 | none | 36% | 9% | 55% |
| Sealcoating & Repairs - Volusia | $10 | $18 | 3 | $5.97 | 0 | none | 31% | 12% | 57% |

### Findings

- **Orlando Metro has $223 in 30 days for zero conversions**, on top of $216 for zero in the Nov 16 window. "driveway paving" phrase $155 on 14 clicks, "driveway paving companies" $44, exact "driveway paving" and "driveway paving near me" $12 each. The same keyword texts in Volusia convert ("driveway paving companies" $355 for 3.5 at $101). The Nov 16 report called the duplication a structure fault; the campaigns are geo-split, so duplicate texts are by design. The fault is that Orlando does not convert.
- **"asphalt paving" phrase in Volusia: $278 for 0.5 conversions ($556).** Second-largest keyword in the account.
- **Confirmed waste, $144.** Informational: minimum temperature $13, how thick $13, does asphalt need to be sealed $12, pavement driveway cost $13, replacing driveway cost $10. Competitors: james asphalt $13, allstate paving $13, asphalt paving llc $11. Off-service: belgium blocks $12, tile for driveways $10, driveway painting $10, pervious driveway $10, quikrete $6. Dedupe against the 168 live negatives: allstate, how thick, temperature, tile and quikrete are already present (the clicks predate them or matched around them); "belgium" exists only inside a longer phrase and "belgium blocks driveway" got through. New: belgium, painting, pervious, sealed, james asphalt, asphalt paving llc, "driveway cost".
- **Sealcoating & Repairs is dormant**: $18 and 3 clicks in 30 days at $10 a day, 57 percent lost to rank.
- **Conversion actions**: "Calls from ads" (the original) has never recorded; "Calls from ads (1)" has 2 in 13 weeks; "Call ((386) 215-7466)" is typed as a lead form. Counts are usable, categories are wrong.
- **Ads**: 7 of 8 live ad groups have one RSA (5 GOOD, 3 AVERAGE, 1 EXCELLENT).
- **Bidding**: manual CPC around $12, 46 to 57 percent lost to rank, budget is not the constraint anywhere. 20 keywords at QS 1 to 3 carry only $7 because they barely serve.

### Prepared change list

1. Orlando Metro: pause it, or cut to $5 a day, until Volusia is saturated or the client confirms they want Orlando work. $439 for zero across two windows.
2. "asphalt paving" phrase: cap the bid at $8 or replace with exact "asphalt paving company" and "asphalt paving contractor".
3. Negatives, phrase, to Master Negatives: belgium, painting, pervious, sealed, "driveway cost", james asphalt, asphalt paving llc.
4. Second RSA in the seven single-ad groups.
5. Fold Sealcoating & Repairs into Volusia paving as an ad group, or raise its bids; at 3 clicks a month it is not a campaign.
6. Fix the conversion categories (the 386 call action is not a lead form) and remove the never-firing "Calls from ads".

## Deep dive 5: Rover Reno PPC (961-477-3743), score 62 D, down 2

Category scores: Conversion Tracking 65, Wasted Spend 65, Account Structure 60, Keywords & Targeting 60, Ads & Assets 55, Bidding & Settings 60.

Snapshot: Reno NV sister account to Rover Vet. 30 days: $906, 358 clicks, $2.53 CPC, 21 primary conversions ($43). Monthly: August $760 for 26, September $638 for 20, October $475 for 13, November to date $732 for 15 ($49). This week $245 for 2 ($123) after $243 for 8 ($30).

| Campaign | Status | Budget/day | 30d cost | Clicks | CPC | Conv | CPA | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| Leads-Search-1 | Paused Nov 9 | $25 | $425 | 117 | $3.64 | 11 | $39 | 49% |
| Reno In-Home Euthanasia | Enabled | $19 | $270 | 141 | $1.92 | 7 | $39 | 90% |
| Reno Pet Cremation | Enabled | $9 | $121 | 62 | $1.96 | 1.7 | $73 | 88% |
| Reno Competitor Conquest | Enabled | $5 | $72 | 33 | $2.18 | 1.3 | $54 | 88% |
| Reno Brand | Enabled | $2 | $17 | 5 | $3.36 | 0 | none | 83% |

### Findings

- **Calls from the ads are not measured.** A campaign_asset query shows call assets only on the two paused campaigns (Rover Veterinary Care and Leads-Search-1), none on the four live ones, and no ad-group call assets anywhere. The account has no AD_CALL ("Calls from ads") conversion action. The primary actions are Book appointment (9 in 30 days), the website call action (3) and "Calls from Smart Campaign Ads" (9), and the last one has recorded nothing since the week of Nov 2, the week Leads-Search-1 was paused. Since Nov 9 the new campaigns show no phone number in the ad and count no call from an ad. For a euthanasia and cremation service, where most leads are phone calls, this is the biggest gap in the account.
- **The budget is the lever.** $35 a day across four campaigns, 83 to 90 percent of impressions lost to budget, 1 to 5 percent lost to rank. At $43 a conversion the account is buying every click it can afford and stopping early. Unchanged from Nov 16; client decision.
- **Competitor names leak into the service campaigns.** "laps of love" (plural) matched four campaigns for $24 with 0 conversions; "lap of love reno" $20; "forever companion reno" $20. Dedupe: lap of love, forever companion, hearts companion, vca, peaceful paws and codapet are already campaign-level negatives on In-Home Euthanasia and Pet Cremation (as exact or phrase, which is why the plural got through). New: laps of love, lapoflove, mount rose (exists only inside a longer phrase), vetco. Keep the competitor keywords in Competitor Conquest: "banfield reno", "blue pearl pet hospital", "humane society clinic" and "pinion animal hospital" each converted once.
- **The best keyword is in the paused campaign.** "dog euthanasia near me" broad in Leads-Search-1 did 9.5 conversions on $316 ($33). Its exact-match successor in In-Home Euthanasia has 1 on $23. 51 percent of live spend is broad; 15 keywords at QS 1 to 3 carry $45.
- **Ads.** All seven live ad groups have one RSA; Competitors is POOR; the Brand RSA is APPROVED_LIMITED for a phone number in ad text, which is the symptom of the missing call asset.
- **Bidding.** Four Maximize Conversions campaigns with 0 to 7 conversions each in 30 days.
- This week's drop (8 to 2) coincides with Tom pausing an In-Home Euthanasia ad group on Nov 21 and re-enabling it on Nov 23. With these numbers it is noise until next week.

### Prepared change list

1. Add a call asset with call reporting to the four live campaigns and create a "Calls from ads" (60 seconds) primary action. Remove the phone number from the Brand RSA text once the asset exists.
2. Budget: $35 to $60 a day (client), or at minimum move Brand's $2 and Competitor Conquest's $5 into In-Home Euthanasia.
3. Add "dog euthanasia near me" phrase to In-Home Euthanasia.
4. Negatives on In-Home Euthanasia and Pet Cremation, phrase: laps of love, lapoflove, mount rose, vetco.
5. Second RSA in all seven groups; rebuild the POOR Competitors RSA.
6. Consolidate In-Home Euthanasia and Pet Cremation under one Maximize Conversions campaign (8.7 conversions a month combined) or move both to Maximize Clicks until either reaches 15 a month.

## Status blocks: deep-dived Nov 16, little or nothing changed

**Progetto Shades (51 F, unchanged).** 30 days: $3,755, 834 clicks, 3 primary conversions, 42 all-conversions (13 directions). The two Contact submissions this week (Shutters, Exterior & Patio) are the first primary conversions since Oct 27 and show the website Contact tag fires. Everything else stands: six Maximize Clicks campaigns at $120 a day; 43 keywords at QS 1 to 3 carrying $2,056 (55 percent) with landing page Below Average on all of them ("window coverings" phrase QS 3 $775 for 1, "shutter store" $502 for 0, "shutters for windows" QS 2 $248 for 0, "blackout curtains" exact QS 2 $166 for 0); 42 zero-conversion keywords over $10 totalling $2,839; the lead-form actions secondary and dark. No change events since Nov 10. Dedupe of the Nov 16 negatives: how much, where to buy, for sale, reddit, somfy, hunter douglas, norman, styles, living room, bedroom are all still absent. New leaks this week: "how much are window shutters" $12, "shutter styles" $13, "black out curtains for bedroom" $8. The Nov 16 change list stands in full; the landing pages are the first item.

**Filutowski Eye Institute (46 F, up 1).** 30 days: $10,526, 694 clicks, 113 primary conversions ($93). Monthly: September $20,785 for 329, October $18,438 for 204, November to date $7,379 for 90 ($82). This week 29 conversions on $2,181. No editor since catie@accaliamarketing.com on Oct 29. "lasik treatment cost" broad: $5,659 of $10,526 (54 percent), 31.5 conversions at $180, Quality Score 6, 10 percent impression share with 90 percent lost to budget at $211 a day. Clinic, doctor and optical queries through it: florida eye clinic altamonte $145, tomoka eye (four variants) $251, mid florida eye center $72, dr thomas $71, eye specialist haines city $68, advanced eye care sanford $64, dr coan $94, premier eye care ormond $58, my eye dr $49, innovation eye care $48, eye exam nearby $72 and more, $1,296 visible with zero conversions. Dedupe against the 76 negatives that apply to live campaigns: optometrist and eyeglass exist; none of the clinic names do. Branded converts at $29 and loses 88 percent of impressions to a $50 budget. All five live ad groups have one RSA. 11 paused ads remain disapproved for DESTINATION_NOT_WORKING on the old cataract URL; the live Cataracts RSA still uses filutowskieye.com/cataract-surgery/. New this week: "Cataract In-Office Appointment Scheduled" (primary, included) recorded 2; creation date unavailable. The Nov 16 change list stands, and item 1 (Contact form to secondary, confirm the consultation thank-you event) is now two weeks old.

**Precision GPR (56 F, unchanged).** 30 days: $2,650, 188 clicks, $14.09 CPC, 13 primary conversions ($204). This week $557 for 2. No change events since Nov 15. Open from Nov 16: Location still live ($447 for 1 at $23.51 a click, the highest CPC in the account); "gpr scanning" matched five campaigns ($81); DSA, the cheapest source at $39 a conversion, spent nothing this week ($12 last week) on a $10 budget, reason unavailable; the 305 and 786 website call actions have still never recorded. Revised: "gprs" converted three times (attention item 5), so keep "gprs scanning" as a keyword in GPR Scanning only and add "gprs" as a negative to the other six campaigns rather than to the shared list. Dedupe of the other Nov 16 negatives: 811 and ditch witch exist; rebar ($33 this week, "rebar finder"), georgia, mygeorgia811, beryl, 1 800 dig, price, directional boring, gepard, structural engineer, underground contractors are all still absent. Confirmed waste this window: $194 (gprs excluded).

## No action needed this week, or one-liners

- **All Phase Pool Remodeling (65 D, unchanged):** 13 conversions at $65, 4 this week at $59. Nothing changed since Dave's Nov 10 phrase-match work. Brand is still $300 of $842 inside non-brand groups; 100 percent broad; the 379-member master list is attached only to the paused campaign; "Phone Calls 60s+" has never recorded. Leaks: pinch a penny (three variants, $36; only the exact negative exists), atlas pools $8, pool pump repair $14. Worklist item 12 stands.
- **Aqua Coat (65 D, unchanged):** 15 conversions at $29; 4 this week at $22. The 248-member master list is still attached only to the paused campaign, tenth week. Leaks the list would have blocked: pool heater $16 and hayward $7 (heater exists only inside a longer phrase), fresh finish $15, pool rails $12, leslies $9, sekas $8, red rhino $6. Pool Equipment group live: "swimming pool equipment" $103 for 1.
- **Scootz (68 D, up 2):** target CPA $75 set Nov 20 with 32 conversions in 30 days behind it. First three days: clicks down 44 percent, CPC up 51 percent, 8 conversions at $63. Judge next week. 6 of 7 groups still one RSA. form_submit still dark; GA4 purchase (28) tracks Booqable Purchases (29), no double count. Negatives still to add: how do you, buena vista; scooterbug exists inside a longer phrase.
- **Florida Sealcoating (67 D, down 1):** 21 conversions at $120; 5 this week at $124. Dave today (Nov 23) added a Pothole Repair ad group with 22 keywords and moved $10 a day from Commercial to Residential; measure next week. Brand keywords ("florida sealcoating" phrase and exact, "florida sealcoating llc", QS 10) cost $217 for 0 primary on Maximize Conversions at $10 to $14 a click; Branded to Target Impression Share with a $4 cap is still the recommendation. Negatives: garcia civil now excluded; new or still missing: stripe it rite $17, all asphalt services inc $45, dmi paving $39, road paving company $53 (only if the client does no road work), 1 800 asphalt $15, advanced asphalt $11, appell, g force, collegiate, pensacola, hot asphalt patch $21. Blacktop and seal master exist. "Call (1-8-333-PAVEIT)" has never recorded. 12 keyword texts live in more than one ad group.
- **The Counseling Group (69 D, up 1):** 2 primary conversions in 30 days on $601, one form lead this week; tel-tap recorded 3 all-conversions. Budget $26.50 a day since Oct 26, 50 percent lost to budget: on plan. "counseling winter park" phrase is $205 of $601 for 0 primary (the exact version converted once at $14); "therapist orlando" exact QS 2 $31 for 0; "help with depression" still live at $35 for 0. Depression RSA is POOR. New exact negatives: john gallagher therapist ($10), ect therapy ($8). Enhanced Conversions confirmed OFF. Small numbers remain normal here.
- **Affordable Critter Solutions (76 C, up 1):** 16 conversions at $19, 5 this week at $14, clean terms, two EXCELLENT and GOOD ads. "animal in attic" phrase $18 for 0 is the only keyword to watch. Four never-firing actions (two Contact Us, two Smart campaign) are still primary; the 11 paused campaigns and the $10-to-$15 budget ask (worklist 19) are unchanged.
- **REK Marketing (own account):** GBP Verification paused around Nov 11. Philadelphia and San Diego lead campaigns: $1,111 in 30 days and $244 this week for 0 conversions, 45 to 53 percent lost to budget, manual CPC at $11. Internal; the same review the client accounts get.
- **Rover Veterinary Care:** paused since Nov 15, zero spend, no change events. See attention item 2. The Nov 16 re-enable order stands (Pet Cremation and Brand first, call test before Euthanasia with a $15 cap).
- **Color Masters, Jupiter Boat Supply:** paused, nothing to do.
- **All Phase Jacksonville:** the "Orlando" campaign is still ENABLED at $49 a day, NOT_ELIGIBLE (ad groups paused, no lead form), spending nothing. Pause it (worklist 6).
- **Straightline Fence:** LSA only, $2,590 for 23 leads in 30 days. Out of scope.
- **Herrell Plumbing:** excluded per protocol, but Tom is clearly working it (74 negatives Nov 9, budgets and ads Oct 28 to Nov 6). This week the Pay-per-lead PMax spent $847 for 10 leads and the search campaign $224 for 3. The protocol entry needs Tom's word.
- **Byers Fence:** client-run (byersfence83@gmail.com added 16 negatives Nov 16). $1,542 for 11 in 30 days. Excluded.
- **ProShield:** client-run LSA, no search spend, no REK edits. Excluded.

Out of scope, for the record only (LSA and Pay-per-lead PMax, 30 days): American Impact LSA $4,666 for 30; Citrus Landscape Sanford LSA $3,715 plus PMax $5,224 for 47; Citrus St. Pete LSA $2,236 plus PMax $2,810 for 24; Straightline LSA $2,590; Byers Fence LSA $1,745 for 14; Herrell LSA (paused) $802; American Impact LSA campaign in the main account $418; All Phase Orlando LSA $378 for 6; Roeling $258 for 6; ABC Pressure Wash, Spectrum Electric, Statewide Home Remodeling, Color Masters LSA, Citrus Sarasota $0.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: American Impact (storm windows, jalousie, vinyl windows pending confirmation, photos, window costs, windows reviews, plus the brand names converted from exact to phrase), Patio Style (cabinets, modular, packages, stainless, thor, pods, backsplash in Outdoor Kitchens; assembly, handyman, for sale in Pergolas), Quality Paralegal (abogado and abogados as phrase in the English campaign only; divorce and child-support lawyer variants as exact in the Spanish campaign), M&S (belgium, painting, pervious, sealed, driveway cost, james asphalt, asphalt paving llc), Rover Reno (laps of love, lapoflove, mount rose, vetco on the two service campaigns), Precision GPR (gprs on every campaign except GPR Scanning; rebar, georgia, mygeorgia811, beryl, 1 800 dig, price, directional boring, gepard, structural engineer, underground contractors), Progetto (how much, where to buy, for sale, reddit, somfy, hunter douglas, norman pending client confirmation, styles, living room, bedroom), Filutowski (the clinic and doctor names in the status block, eye exam, america best, vsp), Florida Sealcoating (stripe it rite, all asphalt services, dmi paving, 1 800 asphalt, advanced asphalt, appell, g force, collegiate, pensacola, hot asphalt patch; road only if the client does no road work), All Phase (pinch a penny as phrase, atlas pools, pump), Aqua Coat (fresh finish, pool rails, sekas, red rhino, plus attaching the master list), Counseling Group (john gallagher therapist, ect therapy), Scootz (how do you, buena vista). Standalone tokens to avoid: "reviews" at American Impact, "abogado" in Quality Paralegal's Spanish campaign, "road" at Florida Sealcoating, "pergola" anywhere outside the Pergolas campaign's own exact negatives.

New keywords to add: American Impact exact "impact window replacement company" and "impact window company orlando" in place of the generic phrase; Rover Reno phrase "dog euthanasia near me" in In-Home Euthanasia; M&S exact "asphalt paving company" and "asphalt paving contractor"; Quality Paralegal exact "paralegal en español" (converted twice at $1.77); Scootz exact "scooter rental in orlando for disney" (2 conversions on $7); Patio Style exact "patio furniture store orlando" (carried from Nov 16).

Bid and budget adjustments: American Impact PMax back to $300 a day and the search ceiling $60 to $30; Patio Style dealer bids to $6 and a $20 combined daily budget, Pergolas ad-group bid $10 to $6; M&S Orlando Metro paused or $5 a day, "asphalt paving" capped at $8; Rover Reno $35 to $60 a day (client) or the Brand and Conquest budgets into In-Home Euthanasia; Precision GPR pause Location and move its $13 to DSA and Utility Mapping; Florida Sealcoating Branded to Target Impression Share with a $4 cap; Quality Paralegal Immigration to $10 a day or pause its zero-conversion phrase; Affordable Critter $10 to $15 a day (client, carried).

Competitive read (rank-lost share as the proxy): American Impact search now loses 46 percent to budget and 22 percent to rank at a $29 CPC, so the ceiling is holding rank at a sane price; the problem has moved from the auction to the keyword. Filutowski and Rover Reno lose 80 to 90 percent to budget and almost nothing to rank: they win the auctions they enter and stop early. Quality Paralegal campaign 1 (70 percent rank loss at a $27 target CPA), Patio Style Outdoor Furniture (67 percent at a Maximize Clicks ceiling) and Progetto (52 to 64 percent on $4 ceilings) are Quality Score and bid-ceiling stories. Precision GPR Concrete Scanning ($24.66) and Location ($23.51) and Florida Sealcoating Residential ($23.85) are the three places a competitor is pushing CPC up on REK-managed accounts.

## Prioritized weekly action plan

1. **Critical, Tom today: American Impact PMax budget.** Put it back to $300 (or $200) a day; it made 11 of 12 conversions this week at $132. Then lower the search ceiling to $30 and pause "window replacement company" phrase ($1,466 this week for 0).
2. **Critical, Tom: Rover Veterinary Care.** Second week dark. Confirm the pause with Dave and the client, or re-enable Pet Cremation and Brand.
3. **Critical, Tom and Dave: Patio Style.** Confirm the dealer-campaign budget and the $151 a day ceiling with the client; cap dealer and pergola bids at $6; and decide the directions-as-primary question, third ask.
4. **Critical, REK: Progetto landing pages and ads.** The tag works (two conversions this week). Nothing else from Nov 16 has started, and 55 percent of spend sits on QS 1 to 3 keywords with Below Average landing pages.
5. **High, Tom: Rover Reno call tracking.** Call asset plus a "Calls from ads" action on the four live campaigns; phone leads have been uncounted since Nov 9.
6. **High, Tom: Filutowski.** Scope decision, and regardless, tell Accalia the Contact form must be secondary and Enhanced Conversions off. Two weeks open.
7. **High, Dave: Precision GPR.** Pause Location; give "gpr scanning" and "gprs scanning" one home in GPR Scanning with negatives elsewhere; the ten missing negatives.
8. **Medium, Dave: M&S.** Pause or cut Orlando Metro ($439 for 0 across two windows); the seven negatives; second RSAs. First touch in over 30 days.
9. **Medium, Tom: Quality Paralegal.** Spanish lawyer negatives in the English campaign; second RSAs; find out what stopped counting on Oct 1.
10. **Medium, Dave: Aqua Coat.** Attach the master list to the live campaign. Ten weeks open; five minutes of work.
11. **Low:** Florida Sealcoating Branded to Target Impression Share and the competitor negatives; All Phase brand split and "pinch a penny" phrase; Scootz second RSAs; All Phase Jacksonville pause the Orlando campaign; REK Marketing's own zero-conversion lead campaigns; Counseling Group two name negatives.

## Rotation

Deep-dived this run: American Impact, Patio Style, Quality Paralegal Services, M&S Asphalt Paving, Rover Reno PPC. Due next Monday: Aqua Coat and Affordable Critter Solutions (carried twice, must land), Scootz (to measure the target CPA), All Phase Pool Remodeling, Progetto Shades (full re-dive if nothing lands this week). The week after: The Counseling Group, Florida Sealcoating (to measure the Pothole Repair group), Filutowski Eye Institute, Precision GPR.

## Data notes

- Account discovery returned 34 client accounts, the same set as Nov 16. The next run should compare against this list.
- API v24 through google-ads 35.1.0, installed in an isolated virtualenv because the container's system Python has a mismatched cryptography build. All 24 queries succeeded for every account; no figure in this report is marked unavailable for a query failure. One additional campaign_asset query was run on Rover Reno to check call assets.
- Unavailable by design of the API: conversion action creation dates and edits (Filutowski's new cataract appointment action, Quality Paralegal's October counting change, Patio Style's directions demotion); the name of the Rover Reno ad group Tom paused on Nov 21; the keyword texts behind Patio Style's Nov 18 bid updates (the events carry criterion ids with empty text).
- Change history was pulled from Oct 25 (the API allows 30 days). Nov 23 events up to the run time are included: Dave's Florida Sealcoating and Patio Style work this morning, and Tom's Rover Reno re-enable.
- Protocol context that needs updating: American Impact (the Nov 19 bidding change and the Nov 20 negatives, Dave now editing alongside Tom); Patio Style dealer campaigns; Precision GPR GPRS conquest intent (ask Dave whether the Nov 15 keyword was deliberate conquest); Rover Vet pause (still); Herrell Plumbing (Tom editing, excluded per protocol); Scootz target CPA; Quality Paralegal conversion set change around Oct 1.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor. Visible terms covered 44 percent of keyword spend at American Impact, 70 percent at Filutowski, 58 percent at Progetto, 28 percent at M&S, 29 percent at The Counseling Group.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
