# PPC Weekly Audit - 2026-09-04 (Google Ads fleet)

Run: Thursday Sep 4, 2026 from the Mac through the read-only google-ads-mcp against MCC 656-695-7229. Window: last 30 days (Aug 5 to Sep 3) unless stated. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Sweep-scored every account, deep-dived the worst five, one-liners for the rest. Week-over-week score deltas are unavailable across the board because yesterday's run (Sep 3) had no Google Ads data (cloud refresh token failed).

## Attention items (read first)

1. **No accounts vanished from the MCC.** All 26 enabled, non-manager client accounts listed on Sep 4 are present. There is no prior Google list to compare against, so "vanished since last week" cannot be evaluated this run. Next week's run should compare against the 26 IDs in the sweep table below.
2. **Premium Walk-In Clinic (279-265-7852) is under the MCC.** The protocol says it denied the link in Sep 2026 and its absence is expected. It is present, enabled, spending $2,477 a month, and being edited by a third party (eddy@powercouchmedia.com edited ads on Aug 10 and Aug 18 and toggled campaign status on Aug 24 and 25; naglaa008@gmail.com changed the budget Aug 13). Update the protocol context and confirm who owns this account.
3. **Straightline Fence And Supply (550-094-8786) is not serving.** The only search campaign, "vinyl fence", is ENABLED but NOT_ELIGIBLE with reason HAS_ADS_DISAPPROVED. The LSA campaign is LIMITED with zero impressions. Zero spend in 30 days. The client is paying nothing, but also getting nothing.
4. **Statewide Home Remodeling (808-698-0148) LSA has zero impressions in 30 days** on a $68.57/day budget. Check the LSA profile for a paused status, lapsed verification, or a lost background check.
5. **Byers Fence (870-428-8862) has Recommendations Auto-Apply switched on.** Google removed six ad-group keywords on Aug 14 under "Recommendations Auto-Apply". Turn it off before applying the change list below or Google will keep editing the account.

## Fleet table (worst first)

Score is the REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). LSA-only and zero-spend accounts are not scorable on the six-category rubric and sit at the bottom with their own metrics. "Waste" is confirmed irrelevant spend from visible search terms in the last 30 days, not a projection.

| Rank | Account | ID | 30d spend | Primary conv | Score | Grade | WoW | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Byers Fence | 870-428-8862 | $406.73 | 0 | 39 | F | n/a | Max Conversions with zero counted conversions; only firing action is excluded from the conversions column | $107 confirmed, $407 unmeasured |
| 2 | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $275.98 | 4 (LSA) | 42 | F | n/a | Leftover "Orlando" search campaign spent $127 on broad retail keywords with no counted conversion; LSA itself is healthy | $43 |
| 3 | Premium Walk-In Clinic | 279-265-7852 | $2,476.92 | 35 | 46 | F | n/a | Calls-only conversion tracking, 74% broad match, five keywords at QS 1, third-party editing | $200 |
| 4 | {active} Gil, Marvin - Precision GPR LLC | 554-113-4760 | $1,935.99 | 13 | 55 | F | n/a | Seven campaigns cannibalizing the same GPR queries, QS 2 to 3 on core terms, $18.50 CPC; under active cleanup | $212 |
| 5 | Patio Style | 596-555-8707 | $2,396.96 | 133 | 59 | F | n/a | 92% of "conversions" are Get Directions clicks; Maximize Clicks with a $1.50 bid cap losing 85% of brand impressions to rank | $140 |
| 6 | Premium Medication Refills | 722-095-3380 | $1,732.56 | 9 | 60 | D | n/a | Campaign now PAUSED with ads APPROVED_LIMITED (healthcare policy); spent $1,733 for 9 leads while running | $110 (moot while paused) |
| 7 | Aqua Coat Pool Plastering | 285-714-0527 | $325.56 | 8 | 67 | D | n/a | Max Conversions on 8 conv/mo; "Pool Equipment" and "pool cleaning services" keywords are off-service; competitor names leaking | $65 |
| 8 | Rover Veterinary Care | 750-667-5721 | $2,035.35 | 28 | 67 | D | n/a | Brand campaign spent $399 on the doctor's name in broad match matching generic vet searches (now paused); both Competitors RSAs rated POOR | $77 ongoing |
| 9 | Scootz | 185-574-5478 | $1,652.26 | 48 | 68 | D | n/a | 28 keywords in one ad group; Maximize Clicks with 48 conv/mo; LSA campaign on a $0.01 budget | none confirmed |
| 10 | Florida Sealcoating | 168-852-7101 | $1,895.97 | 19 | 69 | D | n/a | Five keywords at QS 2 to 3 carrying $447; "Sealcoat Florida Inc" (a different company) in the Branded campaign; display remarketing at 0 impressions | $115 |
| 11 | The Counseling Group | 657-069-3617 | $652.58 | 6 | 73 | C | n/a | Tel-tap conversion zero for 4 months; homepage landing page dragging QS on "near me" terms (deep dive in separate report) | $67 |
| 12 | Affordable Critter Solutions | 227-108-4521 | $305.46 | 10 | 75 | C | n/a | Max Conversions on 10 conv/mo at $10/day; 11 paused campaigns cluttering the account; "nuisance wildlife removal" $58 with 0 conv | none confirmed |
| 13 | All Phase Pool Remodeling | 103-111-7688 | $915.28 | 35 | 75 | C | n/a | 56% of spend is the brand term in broad match inside non-brand ad groups; converts well but belongs in its own campaign | $42 |
| LSA | Citrus Landscape Solutions, Sanford | 661-421-1700 | $10,993.40 | 121 charged | n/a | LSA | n/a | $90.85 per charged lead; 175 leads received, 49 uncharged, 13 booked, 8 unanswered (6 messages) | n/a |
| LSA | Citrus Landscape Solutions, St. Pete | 776-474-8949 | $7,845.85 | 70 charged | n/a | LSA | n/a | $112.08 per charged lead; 107 leads, 34 uncharged, 4 booked, 5 unanswered | n/a |
| LSA | Citrus Landscape Solutions, Sarasota | 832-389-9442 | $2,681.60 | 22 charged | n/a | LSA | n/a | $121.89 per charged lead; 33 leads, 11 uncharged, 2 booked, 3 unanswered | n/a |
| LSA | Herrell Plumbing | 113-422-7395 | $2,079.60 | 30 charged | n/a | LSA | n/a | $69.32 per charged lead; 36 of 68 leads uncharged (53%), which usually means short or missed calls | n/a |
| LSA | Spectrum Electric | 624-534-6648 | $253.36 | 4 charged | n/a | LSA | n/a | $63.34 per charged lead; 9 of 13 leads uncharged (69%), 1 declined | n/a |
| LSA | Roeling Green Lawns | 168-771-6207 | $311.37 | 9 charged | n/a | LSA | n/a | LSA campaign is PAUSED; $34.60 per lead while it ran. Confirm the pause is intended | n/a |
| LSA | ABC Pressure Wash LLC (NEW) | 747-187-9947 | $0.00 | 0 | n/a | LSA | n/a | LSA live with 55 impressions and 6 clicks but no leads and no charges; smart campaign paused | n/a |
| LSA | Statewide Home Remodeling | 808-698-0148 | $0.00 | 0 | n/a | LSA | n/a | Zero impressions on an enabled LSA campaign. See attention item 4 | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0.00 | 0 | n/a | no spend | n/a | Search ads disapproved, LSA limited. See attention item 3 | n/a |
| none | Progetto Shades | 416-010-8247 | $361.65 | 1 | n/a | paused | n/a | Everything paused mid-window. PMax spent $169 for 359 clicks and 0 conversions before the pause | n/a |
| none | Jupiter Boat Supply | 216-859-2093 | $0.00 | 0 | n/a | paused | n/a | Two Shopping campaigns paused | n/a |
| none | M&S Asphalt Paving LLC | 827-724-4095 | $0.00 | 0 | n/a | paused | n/a | Three search campaigns paused | n/a |
| none | REK Marketing | 390-315-5264 | $0.00 | 0 | n/a | paused | n/a | Both campaigns paused | n/a |

Fleet totals for the 30 days: $41.5k across the 26 accounts. The three Citrus LSA accounts are $21.5k of it.

## Deep dive 1: Byers Fence (870-428-8862), score 39 F

| Category | Score |
|---|---|
| Conversion Tracking | 35 |
| Wasted Spend | 30 |
| Account Structure | 55 |
| Keywords & Targeting | 30 |
| Ads & Assets | 55 |
| Bidding & Settings | 30 |

Snapshot: one live campaign, "Leads-Search-7/24", Maximize Conversions with no target CPA, $50/day budget. 30 days: $406.73, 1,560 impressions, 46 clicks, $8.84 CPC, 2.95% CTR. Conversions column: 0. All conversions: 2. Search impression share 10%, lost to rank 89.7%, lost to budget 0.7%. The campaign spends $13.56 a day of a $50 budget.

### Findings

**Conversion tracking is misconfigured, so the bid strategy has nothing to learn from.** Three primary actions exist. "Schedule Appointment from website" and "Phone Calls" (website call) both recorded zero in 30 days. "Calls from ads" recorded 2, but its include_in_conversions_metric flag is false, so those 2 calls never reach the conversions column that Maximize Conversions optimizes on. Net effect: Google is running a conversion-based strategy on a campaign that reports zero conversions. That is why CPC is $8.84 and rank-lost share is 90%. Per house rule, the two zero actions are not declared dead. They need a manual trigger test (submit the form, tap the number on mobile) and a check that the tag is on the live site.

**Own brand and competitor names are being bought through a broad non-brand keyword.** "best residential fence company" (broad, $221.36, 27 clicks, 0 conversions) matched:

| Search term | Cost | Clicks |
|---|---|---|
| byers fence | $104.38 | 13 |
| lifetime fence and deck | $19.37 | 3 |
| lex fence | $17.42 | 1 |
| master halco apopka | $16.40 | 1 |
| aaa fence | $16.14 | 2 |
| fence outlet (3 variants) | $21.94 | 3 |
| daves fence | $5.11 | 1 |
| superior fence and rail oviedo (via "residential fence contractor") | $10.32 | 1 |

Competitor and supplier names: $106.70. The client's own brand: $104.38 at $8.03 a click through a keyword with no brand relevance. A brand campaign with exact and phrase "byers fence" would take those clicks at a fraction of the CPC.

**No negatives at campaign level, no shared negative lists.** The only negatives are ad-group level, added by the client (byersfence83@gmail.com) on Aug 12. There is no list for competitors, supplies, DIY, or jobs.

**Quality Score floor.** "vinyl fence cost" is QS 1 ($28.74, 4 clicks, 0 conversions). "cost" is a price-shopper term.

**Broad match carries 74% of measured spend** ($298 of $403 on keywords over $10). With no conversion signal, broad match has nothing to steer it.

**One RSA per ad group.** Residential Leads has one (EXCELLENT), Commercial Leads has one (GOOD). Protocol floor is two.

**Recommendations Auto-Apply is on.** Six keyword removals on Aug 14 were made by "Recommendations Auto-Apply". Google will keep changing the account until this is switched off.

**Settings that are fine:** search partners off, display off, presence-only targeting across 18 Central Florida locations.

### Prepared change list (suggestions only)

1. Turn off Recommendations Auto-Apply (Recommendations, Auto-apply, uncheck everything).
2. Fix conversions before anything else. Open "Calls from ads" and set it to be included in Conversions. Run a manual test of "Schedule Appointment from website" and "Phone Calls" and confirm the tag fires on the live site. Until at least one action is counting, the bid strategy should be Maximize Clicks with a $4.00 CPC ceiling, then move back to Maximize Conversions once 15 conversions a month are recorded.
3. Create a Brand campaign: exact and phrase "byers fence", "byers fence company", "byers fencing". Budget $5/day. Add "byers" as a phrase negative to Leads-Search-7/24.
4. Create a shared negative list "Competitors and Suppliers" and attach it: lifetime fence, lex fence, master halco, aaa fence, fence outlet, superior fence, daves fence, better fence, home depot, lowes. Phrase match.
5. Create a shared list "Wrong Intent": cost, price, prices, cheap, diy, install yourself, jobs, hiring, salary, black (matched "fence black", a product color search). Phrase match.
6. Pause "vinyl fence cost" (QS 1) and "best fence" (broad, $26.43, 0 conversions).
7. Change "best residential fence company" from broad to phrase, or replace it with phrase "residential fence company" and phrase "fence company near me".
8. Add a second RSA to each ad group.
9. Decline Google's open Search Partners and Performance Max recommendations.

## Deep dive 2: All Phase Pool Remodeling, Jacksonville (918-824-8896), score 42 F

Context applied: this is Joe's account and holds the Jacksonville LSA by design. The LSA is not the problem. It took 6 leads in 30 days, 4 charged, $149.31 spent, $37.33 per charged lead. That is the best cost per lead in the fleet.

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 40 |
| Account Structure | 50 |
| Keywords & Targeting | 30 |
| Ads & Assets | 50 |
| Bidding & Settings | 35 |

The score comes from the second campaign, "Orlando" (search, Maximize Conversions, $48.96/day). It spent $126.67 in the window on 16 clicks at $7.92 each, with 0 counted conversions and 9 all-conversions from Google-hosted local actions. It is now NOT_ELIGIBLE with reasons AD_GROUPS_PAUSED and MISSING_LEAD_FORM_EXTENSION, and it has no enabled ads. It is a leftover, not a live effort.

### Findings

- All four keywords are broad match in a single "Ad group 1": pebble tec pool finish ($36.26), pool equipment (QS 2, $31.92), pool tile (QS 3, $31.69), inground pool resurfacing contractors ($11.68). Two of the four are retail product searches, not remodeling.
- Search terms: "blue water pools" $31.55 and "pinch a penny mount dora fl" $11.73 are competitor and retailer names. $43.28 confirmed waste.
- Conversion setup: the three primary actions (Lead form submit, Calls from ads, Submit lead form) all have include_in_conversions_metric set to false. Nothing counts. Maximize Conversions had no signal.
- Change history: Joe (jtyamin5004@gmail.com) created a Business Profile location asset set on Aug 20. No campaign edits in 30 days. The ad-group pause predates the window.

### Prepared change list

1. Pause the "Orlando" campaign outright so it cannot resume serving if an ad group is re-enabled. The Orlando search effort belongs in the main account (103-111-7688), which already runs "All Phase Pool Remodeling - M".
2. If Joe wants search in this account later, rebuild from scratch: phrase and exact keywords, Jacksonville geo, a working lead form or website conversion that is included in Conversions.
3. Decline the Performance Max recommendation.
4. No LSA action needed. Two uncharged leads of six is normal.

## Deep dive 3: Premium Walk-In Clinic (279-265-7852), score 46 F

| Category | Score |
|---|---|
| Conversion Tracking | 50 |
| Wasted Spend | 35 |
| Account Structure | 60 |
| Keywords & Targeting | 25 |
| Ads & Assets | 55 |
| Bidding & Settings | 55 |

Snapshot: one campaign, "PCM_Leads_Search", Maximize Conversions with no target CPA, $50/day. 30 days: $2,476.92, 30,425 impressions, 1,388 clicks, $1.78 CPC, 4.56% CTR, 35 conversions (all from "Calls from ads"), $70.77 per call. Search impression share 19.6%, lost to budget 48.8%, lost to rank 31.6%. Primary status LIMITED. 15-mile radius, presence-only, search partners and display off. A shared negative list "PWC Global Negatives" with 264 members is attached.

Ownership note: see attention item 2. Someone at powercouchmedia.com is actively editing this account. Coordinate before applying anything below.

### Findings

**Calls-only conversion tracking.** The only primary action that counts is "Calls from ads" (35). There is no website call tracking, no form tracking, no booking tracking. The 1,122 all-conversions are Google-hosted local actions (605 "other engagements", 327 directions, 98 website visits, 53 clicks to call). For a walk-in clinic, directions and clicks-to-call are real intent, but they are secondary and the bid strategy cannot see them. Maximize Conversions is optimizing 1,388 clicks a month toward 35 ad calls. Protocol calls calls-only a major finding.

**Broad match is 74% of measured spend** ($1,698 of $2,300 on keywords over $10). The broad keywords are generic: "lab work", "low cost clinic", "walk in doctor" (now paused), "doctor near me today", "clinic open now", "physical exam near me".

**Quality Score floor is the worst in the fleet.** Five keywords at QS 1: dot physical near me (phrase, two copies, $74.59 combined, 0 conversions), same day physical near me ($38.61), cheap doctor visit ($34.55), sports physical near me ($14.10). QS 2: physical exam near me ($227.52, 90 clicks, 3 conversions). QS 3: urgent care orlando ($173.05), school physical near me, walk in doctor near me (paused).

**Confirmed irrelevant search terms (30 days, visible terms only):**

| Group | Terms | Cost |
|---|---|---|
| Hospital systems, labs, competitors | adventhealth (x2), orlando health centracare, quest diagnostics, labcorp, simonmed, rayus radiology, sanitas, moreno medical, lakeview healthcare, vip clinic, walgreens, florida department of health | $103.35 |
| Street addresses | 509 cagan view rd clermont, 4426 old winter garden rd | $17.64 |
| "Free" | free school physicals, free clinics near me no insurance, free immunization clinic | $22.76 |
| Services probably not offered | uscis medical exam, asbestos physical exam, g license physical, std testing | $61.83 |
| Pediatric | walk in clinic kids near me | $23.60 |

Total: $229.18, which is 9% of spend, from the visible fraction alone.

**Zero-conversion keywords over $10:** walk in doctor $217.49 (already paused), doctor near me today $185.36, dot physical near me $74.59, walk in physical exam $48.73, annual physical no insurance $46.35, dot physical orlando $47.86 (two copies in two ad groups), doctor without insurance near me $21.91, school physical near me $16.32, sports physical near me $14.10. Live total: $455.22.

**Structure:** "dot physical" keywords exist in both "Walk-In Clinic / Same-Day Care" and "Physicals / DOT / School / Sports". "school sports physical" sits in the Walk-In group. Three ad groups with one RSA each (all GOOD).

**Budget:** losing 48.8% of impressions to budget while 9% of visible spend is confirmed waste. The budget is not the problem yet.

### Prepared change list

1. Add website conversions before touching bids: a website call action (Google forwarding number or call tracking on the site number), a form or booking action, and set both primary. Keep "Calls from ads" primary. Move "Clicks to call" and "Local actions - Directions" to secondary (they already are) but consider a data-driven review after 30 days.
2. Add to the shared negative list, phrase match: adventhealth, centracare, orlando health, quest, labcorp, simonmed, rayus, sanitas, moreno, lakeview, vip clinic, walgreens, cvs, department of health, free, uscis, immigration, asbestos, g license, std, kids, pediatric, children. Confirm with the client whether STD testing, immigration exams, and pediatric visits are offered before adding those three groups.
3. Add an address-blocking set: "rd", "road", "blvd", "ave" as phrase negatives are too broad. Instead add the two specific address strings as exact negatives and review the terms report monthly for new ones.
4. Pause the QS 1 keywords: both "dot physical near me" copies, "same day physical near me", "cheap doctor visit", "sports physical near me". Rebuild DOT and sports physicals as exact and phrase keywords in the Physicals group only, with a dedicated landing page.
5. Pause "doctor near me today" (broad, $185, 0 conversions) and "walk in physical exam" (broad, $49, 0).
6. Convert the remaining broad keywords to phrase: lab work, low cost clinic, clinic open now, walk in clinic orlando, same day doctor visit, annual physical no insurance.
7. Remove the duplicate "dot physical orlando" and "dot physical near me" from the Walk-In group.
8. Add a second RSA to each ad group.
9. Leave the budget at $50/day until the negatives and keyword changes have two weeks of data.
10. Decline Search Partners, Display Expansion, Broad Match, and Performance Max recommendations.

## Deep dive 4: Precision GPR (554-113-4760), score 55 F, condensed

Context applied: under active cleanup since Aug 2026 (bids, negatives, conversion fix). Deliberate week-over-week changes are expected. This section records what the data shows today so next week's run can measure the cleanup, and it lists only the items the cleanup may not already cover.

| Category | Score |
|---|---|
| Conversion Tracking | 60 |
| Wasted Spend | 50 |
| Account Structure | 55 |
| Keywords & Targeting | 45 |
| Ads & Assets | 70 |
| Bidding & Settings | 45 |

Snapshot: seven enabled search campaigns, all Maximize Conversions. 30 days: $1,935.99, 13 primary conversions, roughly 198 all-conversions (the Branded campaign alone shows 141.5 all-conversions from "Local actions - Other engagements" against 0 primary).

| Campaign | Spend | Clicks | CPC | Primary conv |
|---|---|---|---|---|
| **LP Search - Services | $492.06 | 62 | $7.94 | 3.5 |
| **LP Search - GPR Scanning | $444.01 | 24 | $18.50 | 1 |
| **LP Search - Utility Mapping | $389.79 | 60 | $6.50 | 2 |
| **LP Search - Concrete Scanning | $310.15 | 26 | $11.93 | 6.5 |
| **LP Branded | $123.55 | 17 | $7.27 | 0 |
| **LP DSA - All Pages | $101.67 | 37 | $2.75 | 0 |
| **LP Search - Location | $74.77 | 8 | $9.35 | 0 |

Findings the cleanup should include if it does not already:

- **Cannibalization.** The query "gpr scanning" and its variants are matched by four campaigns (GPR Scanning, Services, Location, Concrete Scanning). Concrete Scanning converts at $47.71 per conversion; GPR Scanning at $444 per conversion for the same intent. Consolidate GPR and Location into Services and Concrete Scanning, or add cross-campaign negatives so each query has one home.
- **Quality Score floor.** "Ground Penetrating Radar" exact (QS 3, $291.29, 16 clicks, 0 primary), phrase (QS 3, $139.31), "Concrete Scanning" phrase (QS 2), "Utility Survey" exact (QS 2), "Gpr Scanning Near Me" exact and phrase (QS 3).
- **Confirmed waste, $212:** "gprs" (a national competitor) in four variants $73.17; price and cost searches $36.55; "concrete rebar finder" and "rebar detector in concrete" $27.89 (equipment shoppers); Spanish query "radar de penetración terrestre gpr" $30.14; "no cuts florida" $18.14 (competitor); "dig alert" and "sunshine utility locate" $17.35 (the free 811 service); "screening eagle gpr" $9.32 (equipment brand).
- **Brand CPC.** "Precision Gpr" exact costs $7.20 a click with a 21% budget-lost share on a $10/day budget. Brand should not lose impressions to budget. Raise the brand budget to $15/day and cap the bid.
- **Ads.** Three POOR RSAs (Ground Penetrating Radar group, Concrete Scanning Services Near Me, Concrete X Ray Near Me) and two PENDING (new, fine). Otherwise two per group.
- **Conversion actions.** 24 actions including two hidden duplicates named "precisiongpr.com (web) purchase", "Contact Us" and "Contact Us (1)", and two website-call numbers (305 and 786) that recorded zero. Include a manual test of both call numbers in the cleanup.

Negatives to add (phrase, to a shared list): gprs, gprs florida, price, cost, pricing, rebar finder, rebar detector, detector, screening eagle, proceq, dig alert, sunshine 811, 811, no cuts, radar de, penetración, rental, rent, for sale, jobs.

## Deep dive 5: Patio Style (596-555-8707), score 59 F

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 55 |
| Account Structure | 85 |
| Keywords & Targeting | 60 |
| Ads & Assets | 50 |
| Bidding & Settings | 45 |

Snapshot: four search campaigns, all Maximize Clicks (Target Spend) with CPC ceilings. 30 days: $2,396.96, 15,405 impressions, 932 clicks, 133 conversions.

| Campaign | Spend | Clicks | Conv | Bid cap | Search IS | Lost to rank |
|---|---|---|---|---|---|---|
| Outdoor Furniture | $1,036.32 | 626 | 114 | $2.50 | 18.6% | 59.0% |
| Outdoor Kitchens | $607.98 | 113 | 5 | $7.00 | 43.5% | 35.7% |
| Pergolas & Louvered Roofs | $603.78 | 96 | 7 | $8.00 | 49.4% | 35.4% |
| Brand | $148.88 | 97 | 7 | $1.50 | 14.0% | 85.1% |

The structure is the cleanest in the fleet: one campaign per product line, a separate brand campaign with phrase negatives for generic terms, a 52-member shared negative list on every campaign. The problems are measurement and bidding.

### Findings

**92% of "conversions" are Get Directions clicks.** Primary and included actions in 30 days: GA4 get_directions 122, GA4 click_to_call 7, Calls from ads 3, GA4 generate_lead 1. Two YouTube engagement actions (follow-on views, channel subscriptions) are also set primary and included; they recorded zero but should not be primary on a search account. Directions are a legitimate showroom signal, but with directions counted as primary the conversions column cannot tell a lead from a map tap. Any move to Maximize Conversions would optimize toward map taps. Fix the definitions first.

**Brand is losing 85% of impressions to rank because of a $1.50 bid cap.** "patio style" exact is QS 10 and still shows only 14% of the time. This is the cheapest fix in the fleet: raise the brand cap.

**Maximize Clicks on 133 conversions a month is backwards.** Once directions are moved to secondary and there are 30 days of clean data, the Furniture campaign will have enough calls, forms, and directions to run Maximize Conversions or a target CPA. Today the strategy is buying clicks with no regard to which ones matter.

**Zero-conversion keywords over $10:** outdoor grill island (QS 3, $240.16, 36 clicks), insulated patio cover ($199.06, 34 clicks), outdoor kitchens for sale ($75.07), louvered pergola ($67.55), outdoor kitchen orlando phrase ($54.13), outdoor kitchen contractor orlando ($16.93). Total $652.90. "outdoor grill island" and "insulated patio cover" alone are $439 with nothing to show, and their search terms explain why.

**Confirmed irrelevant search terms, $140:**

| Group | Terms | Cost |
|---|---|---|
| Roof panel product searches | insulated aluminum patio cover, lanai roof panels, insulated aluminum roof panels, patio insulated roof panels, insulated roof panels for patio, patio cover insulated roof panels, insulated porch roof panels, insulated lanai roof panels | $67.41 |
| Retail brands and competitors | paradise grill orlando, pergolux, big green egg island, blackstone outdoor kitchen, ikea grill station, modular outdoor kitchens costco, vestivium | $58.17 |
| Photos | orlando pergolas and decks photos | $14.50 |

Confirm with the client whether they sell insulated roof panels as a product. If they only install finished covers, the whole panel cluster is waste.

**Quality Score.** QS 3 on "patio furniture store near me" ($280.08, 178 clicks, 33 conversions), "outdoor grill island", "outdoor fire pit", "outdoor dining set". QS 4 on the top keyword "outdoor patio furniture" ($469.63). Low QS on the two biggest keywords means the $2.50 cap buys worse positions than it should.

**Ads.** 11 of 12 ad groups have a single RSA. Only "Patio Furniture" has two.

**Recent changes:** Tom added campaign and ad group assets on Aug 26. No keyword or bid changes in 30 days.

### Prepared change list

1. Conversion definitions: set "www.patiostyle.com - GA4 (web) get_directions", "YouTube follow-on views", and "YouTube channel subscriptions" to secondary. Keep click_to_call, generate_lead, and Calls from ads primary. Add a form or quote-request action if the site has one for kitchens and pergolas.
2. Raise the Brand campaign CPC ceiling from $1.50 to $4.00 and watch impression share for a week. Target is 80%+.
3. After 30 days of clean conversion data, move Outdoor Furniture to Maximize Conversions. Leave Kitchens and Pergolas on Maximize Clicks until each has 15 real conversions a month.
4. Pause "outdoor grill island" and "insulated patio cover" pending the client's answer on panels and grill islands. If they do sell grill islands, rebuild the keyword as exact "outdoor kitchen island orlando" with a product landing page.
5. Add to Master Negatives, phrase: roof panels, panels, aluminum roof, pergolux, paradise grill, big green egg, blackstone, ikea, costco, vestivium, photos, pictures, ideas, diy, plans.
6. Add a second RSA to the 11 single-ad groups. Start with Patio Covers & Cabanas, Outdoor Kitchens, and Built-in Grills, which carry the spend.
7. Landing pages: check that "patio furniture store near me" and "outdoor patio furniture" land on a page with store hours, address, and inventory photos above the fold. QS 3 to 4 on the two biggest keywords is mostly landing page experience.
8. Decline Google's Search Partners, Display Expansion, Maximize Conversions (for now), Target CPA, and Performance Max recommendations.

## No action needed this week (one-liners)

- **Premium Medication Refills (60 D):** campaign paused since the window, ads APPROVED_LIMITED under healthcare policy. While it ran, $1,732.56 bought 9 leads at $192.51 each and $110 went to other pharmacies' names (caremark, costco, heb, select rx, northwind, ascension, telyrx, nimble, medvantx, birdi, aetna, cost plus drugs, champva). Two clicks touched "controlled substance" queries. If it restarts, add a pharmacy-brand negative list and a "controlled" negative first, and resolve the policy limitation with Google before spending.
- **Aqua Coat (67 D):** Max Conversions on 8 conversions a month is thin. "swimming pool equipment" (broad, $44.56, 0 conversions) and "pool cleaning services" ($16.20, 0) are not plastering. Competitor names cost $46.49 (fresh finish pools, aqua pools, aqua dreams pools, pcs pools). One POOR RSA in Pool Renovations. Add competitor negatives and pause the two off-service keywords. Due for a full deep dive next week.
- **Rover Veterinary Care (67 D):** the Brand campaign's broad keywords on the doctor's name ($398.71 in 30 days, matched "dog clinic near me", "canine oncologist", "pet death doula") are already paused and removed. Good. Remaining: both Competitors RSAs are POOR, "humane pet euthanasia" (generic) lives in the Competitors campaign, and cat-care questions ("when to put down a cat", "does banfield euthanize cats") cost $45. Add "when to", "banfield", "hospice", "baton rouge", "quality of life" as phrase negatives. Due next week.
- **Scootz (68 D):** healthy CPC ($0.78) and CTR (7.2%) but 28 keywords in one ad group, brand mixed with Disney, Universal, and wheelchair terms, Maximize Clicks with 48 conversions a month, and an LSA campaign sitting on a $0.01 budget. Split into Brand, Disney, Universal, Orlando general, and Wheelchair ad groups, then move to Maximize Conversions. Set the LSA budget or pause it. Due next week.
- **Florida Sealcoating (69 D):** September ramp to $3,000 is intended, so rising spend is not a finding. Findings that are: five keywords at QS 2 to 3 carrying $447 (driveway repair near me, asphalt company orlando, paving companies near me exact and broad, asphalt paving company near me, asphalt patch repair); "sealcoat florida" and "sealcoat florida inc" ($33.27, 5 clicks, 0 conversions) look like a different company and should be exact negatives in Branded; competitor names $62 (kennedy concrete, absolute asphalt, american asphalt, martin paving, ppg traffic solutions, seal right); the FL Remarketing display campaign has an EXCELLENT ad and zero impressions on $5/day. Due next week.
- **The Counseling Group (73 C):** deep dive completed today in reports/ppc-audit-the-counseling-group-2026-09-04.md. Not due again until October.
- **Affordable Critter Solutions (75 C):** solid ads (two EXCELLENT, one GOOD, a call ad) and clean terms. "nuisance wildlife removal" ($58.42, 17 clicks, 0 conversions) is the one keyword to watch. Eleven paused campaigns should be removed for hygiene. Max Conversions on 10 conversions a month at a $10/day budget is thin but working ($30.55 per conversion).
- **All Phase Pool Remodeling (75 C):** 35 conversions at $26.15 each. The brand term "all phase pool remodeling" in broad match sits inside the Pool Renovations and Pool Resurfacing groups and takes 56% of spend ($515.59). It converts (20 conversions), so nothing is broken, but a separate Brand campaign would stop brand and non-brand data from blending. "pool repair lake mary fl" ($20.12) and "pinch a penny" ($8.17) are the only stray terms.
- **Citrus Landscape Solutions, Sanford, St. Pete, Sarasota (LSA):** $21,521 for 213 charged leads across the three, $101 per lead blended. Sarasota is the most expensive at $121.89. Sanford has 8 unanswered leads (6 messages) and St. Pete has 5; message leads that sit in NEW are still charged, so the client should answer them. Nothing to change in the campaigns themselves.
- **Herrell Plumbing (LSA):** 30 charged leads at $69.32. 36 of 68 leads (53%) were not charged, which usually means calls under the LSA duration threshold or missed calls. Worth asking the client whether calls are being answered on the first ring.
- **Spectrum Electric (LSA):** 4 charged leads at $63.34, 9 of 13 uncharged. Same answer-rate question as Herrell, on a smaller sample.
- **Roeling Green Lawns (LSA):** paused. 9 leads at $34.60 before the pause. Confirm the pause is the client's choice.
- **ABC Pressure Wash (LSA):** live, 55 impressions, 6 clicks, no leads, no charges in 30 days. Normal for a new LSA profile; revisit in two weeks.
- **Progetto Shades:** all campaigns paused mid-window. Before the pause, Performance Max spent $169.02 on 359 clicks with zero conversions and the search campaign $192.63 for one conversion. If it restarts, do not restart PMax.
- **Jupiter Boat Supply, M&S Asphalt Paving, REK Marketing:** fully paused, zero spend, nothing to do.

## Rotation

Deep-dived this run: Byers Fence, All Phase Jacksonville, Premium Walk-In Clinic, Precision GPR (condensed), Patio Style, and The Counseling Group (separate report). Due next Monday: Florida Sealcoating, Aqua Coat, Rover Veterinary Care, Scootz. The week after: Affordable Critter Solutions, All Phase Pool Remodeling, and a lead-quality review across the three Citrus LSA accounts.

## Data notes

- Search-term tables use Google's visible terms only. Google withholds low-volume terms, so confirmed waste is a floor.
- LSA lead counts come from the local_services_lead resource for Aug 5 to Sep 4, one day longer than the metrics window, so charged-lead counts can exceed the conversions column by a few.
- Quality Score is only reported on keywords with enough recent impressions. "n/a" in the source data was treated as unknown, not as low.
- The local ~/google-ads.yaml on the Mac was rejected by Google ("developer token is not valid"), so the tools/gaql.py helper could not be used. The MCP connection worked. The yaml on this machine needs the same fix as the Drive copy noted in yesterday's report.
