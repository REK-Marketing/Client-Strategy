# PPC Weekly Audit - 2026-09-04 (Google Ads fleet)

Run: Thursday Sep 4, 2026 from the Mac through the read-only google-ads-mcp against MCC 656-695-7229. Window: last 30 days (Aug 5 to Sep 3) unless stated. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Sweep-scored every search account, deep-dived the worst, one-liners for the rest.

Scope changes on Tom's instruction (Sep 4): Local Services Ads campaigns and LSA-only accounts are excluded from this report for now. Byers Fence is not managed by REK and is excluded. Premium Medication Refills is confirmed paused. Week-over-week score deltas are unavailable across the board because yesterday's run (Sep 3) had no Google Ads data (cloud refresh token failed).

## Attention items (read first)

1. **No accounts vanished from the MCC.** All 26 enabled, non-manager client accounts listed on Sep 4 are present. There is no prior Google list to compare against, so "vanished since last week" cannot be evaluated this run. Next week's run should compare against the 26 IDs in the sweep table below.
2. **Premium Walk-In Clinic (279-265-7852) is under the MCC.** The protocol says it denied the link in Sep 2026 and its absence is expected. It is present, enabled, spending $2,477 a month, and being edited by a third party (eddy@powercouchmedia.com edited ads on Aug 10 and Aug 18 and toggled campaign status on Aug 24 and 25; naglaa008@gmail.com changed the budget Aug 13). Update the protocol context and confirm who owns this account.
3. **Straightline Fence And Supply (550-094-8786) is not serving.** The only search campaign, "vinyl fence", is ENABLED but NOT_ELIGIBLE with reason HAS_ADS_DISAPPROVED. Zero spend in 30 days. The client is paying nothing, but also getting nothing.
4. **Byers Fence (870-428-8862) is under the MCC but REK does not manage its PPC.** It was scored and deep-dived in the first draft of this report and has been removed. For the record only: it spent $406.73 with zero counted conversions and has Recommendations Auto-Apply on. Nothing here is actionable by REK.

## Fleet table (worst first)

Score is the REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Zero-spend and fully paused accounts are not scorable on the six-category rubric and sit at the bottom. "Waste" is confirmed irrelevant spend from visible search terms in the last 30 days, not a projection.

| Rank | Account | ID | 30d spend | Primary conv | Score | Grade | WoW | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $126.67 (search) | 0 | 42 | F | n/a | Leftover "Orlando" search campaign spent $127 on broad retail keywords with no counted conversion | $43 |
| 2 | Premium Walk-In Clinic | 279-265-7852 | $2,476.92 | 35 | 46 | F | n/a | Calls-only conversion tracking, 74% broad match, five keywords at QS 1, third-party editing | $200 |
| 3 | {active} Gil, Marvin - Precision GPR LLC | 554-113-4760 | $1,935.99 | 13 | 55 | F | n/a | Seven campaigns cannibalizing the same GPR queries, QS 2 to 3 on core terms, $18.50 CPC; under active cleanup | $212 |
| 4 | Premium Medication Refills | 722-095-3380 | $1,732.56 | 9 | 60 | D | n/a | PAUSED (confirmed by Tom). Ads APPROVED_LIMITED under healthcare policy; $1,733 for 9 leads while it ran | $110 (moot) |
| 5 | Patio Style | 596-555-8707 | $2,396.96 | 133 | 65 | D | n/a | Maximize Clicks with a $1.50 brand bid cap losing 85% of brand impressions to rank; $653 on zero-conversion keywords; 11 of 12 ad groups have one RSA | $140 |
| 6 | Aqua Coat Pool Plastering | 285-714-0527 | $325.56 | 8 | 67 | D | n/a | Max Conversions on 8 conv/mo; "Pool Equipment" and "pool cleaning services" keywords are off-service; competitor names leaking | $65 |
| 7 | Rover Veterinary Care | 750-667-5721 | $2,035.35 | 28 | 67 | D | n/a | Brand campaign spent $399 on the doctor's name in broad match matching generic vet searches (now paused); both Competitors RSAs rated POOR | $77 ongoing |
| 8 | Scootz | 185-574-5478 | $1,652.26 | 48 | 68 | D | n/a | 28 keywords in one ad group; Maximize Clicks with 48 conv/mo | none confirmed |
| 9 | Florida Sealcoating | 168-852-7101 | $1,895.97 | 19 | 69 | D | n/a | Five keywords at QS 2 to 3 carrying $447; "Sealcoat Florida Inc" (a different company) in the Branded campaign; display remarketing at 0 impressions | $115 |
| 10 | The Counseling Group | 657-069-3617 | $652.58 | 6 | 73 | C | n/a | Tel-tap conversion zero in the 3 weeks since it was built Aug 12; homepage landing page dragging QS on "near me" terms (deep dive in separate report, revised Sep 4) | $71 |
| 11 | Affordable Critter Solutions | 227-108-4521 | $305.46 | 10 | 75 | C | n/a | Max Conversions on 10 conv/mo at $10/day; 11 paused campaigns cluttering the account; "nuisance wildlife removal" $58 with 0 conv | none confirmed |
| 12 | All Phase Pool Remodeling | 103-111-7688 | $915.28 | 35 | 75 | C | n/a | 56% of spend is the brand term in broad match inside non-brand ad groups; converts well but belongs in its own campaign | $42 |
| none | Straightline Fence And Supply | 550-094-8786 | $0.00 | 0 | n/a | no spend | n/a | Search ads disapproved. See attention item 3 | n/a |
| none | Progetto Shades | 416-010-8247 | $361.65 | 1 | n/a | paused | n/a | Everything paused mid-window. PMax spent $169 for 359 clicks and 0 conversions before the pause | n/a |
| none | Jupiter Boat Supply | 216-859-2093 | $0.00 | 0 | n/a | paused | n/a | Two Shopping campaigns paused | n/a |
| none | M&S Asphalt Paving LLC | 827-724-4095 | $0.00 | 0 | n/a | paused | n/a | Three search campaigns paused | n/a |
| none | REK Marketing | 390-315-5264 | $0.00 | 0 | n/a | paused | n/a | Both campaigns paused | n/a |

Excluded at Tom's request: Byers Fence (not REK-managed) and the LSA-only accounts (Citrus Landscape Solutions Sanford, St. Pete, and Sarasota, Herrell Plumbing, Spectrum Electric, Roeling Green Lawns, ABC Pressure Wash, Statewide Home Remodeling). LSA campaigns inside other accounts are also left out of the figures above.

Search spend across the 12 scored accounts for the 30 days: $16.5k.

## Deep dive 1: All Phase Pool Remodeling, Jacksonville (918-824-8896), score 42 F

Context applied: this is Joe's account and holds the Jacksonville LSA by design. The LSA is out of scope for this report. The score below is for the search side only.

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
4. Nothing else in this account is in scope this week.

## Deep dive 2: Premium Walk-In Clinic (279-265-7852), score 46 F

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

## Deep dive 3: Precision GPR (554-113-4760), score 55 F, condensed

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

### Prepared change list (requested by Tom, Sep 4)

1. Negatives, phrase match, in a new shared list attached to all seven campaigns: gprs, gprs florida, price, cost, pricing, how much, rebar finder, rebar detector, detector, screening eagle, proceq, dig alert, sunshine 811, 811, no cuts, radar de, penetración, rental, rent, for sale, jobs, salary, training, certification. Add "precision gpr" as a phrase negative to the six non-brand campaigns so brand searches only serve from Branded.
2. Consolidate. Pause the "**LP Search - Location" campaign ($74.77, 0 conversions, three POOR or AVERAGE ads) and the "**LP DSA - All Pages" campaign ($101.67, 0 conversions). Their queries are already covered by Services and Concrete Scanning. Move the two exact "Gpr Scanning Orlando" and "Gpr Scanning Tampa Bay" keywords into Services with their own ad groups if the location angle matters.
3. Give each core query one home. "Ground Penetrating Radar" exact and phrase (QS 3, $430 combined, 1 conversion) live in GPR Scanning at $18.50 a click. "Ground Scanning Services" phrase in Services converts the same intent at $7.84 a click with 2 conversions. Pause the two GPR Scanning keywords and let Services take the query, or move them into Services and cap their bid. Do not run both.
4. Cap the CPC on whatever remains in GPR Scanning at $10 through a portfolio bid strategy with a max CPC limit. $18.50 clicks with no conversions is the single biggest cost line in the account.
5. Brand: raise "**LP Branded" from $10/day to $15/day. It loses 21% of brand impressions to budget. Brand should never do that.
6. Ads: rebuild the POOR RSA in the Ground Penetrating Radar group and the two POOR RSAs in Location (moot if Location is paused). Keep the PENDING ads, they are new.
7. Conversions: remove the duplicate hidden "precisiongpr.com (web) purchase" actions and merge "Contact Us" and "Contact Us (1)". Run a manual test on both website-call numbers (305 and 786), which recorded zero. Set "precisiongpr.com (web) micro" (33 all-conversions) to secondary if it is not already, and make sure "Local actions - Other engagements" (144) stays secondary so the Branded campaign's 141.5 all-conversions never leak into the conversions column.
8. Bidding: with 13 conversions across seven campaigns, Maximize Conversions has no signal anywhere except Concrete Scanning (6.5). Put the consolidated campaigns on Maximize Clicks with a $10 cap until any one of them hits 15 conversions a month, then move that one to Maximize Conversions.
9. Decline all seven Search Partners recommendations, all Display Expansion, all Broad Match, and the Target CPA suggestion on Concrete Scanning until it has 30 days above 15 conversions.

## Deep dive 4: Patio Style (596-555-8707), score 65 D

Revised Sep 4 after Tom's note: the client's primary conversion is Get Directions to the showroom, then phone calls, then contact submissions. The first draft treated directions as a secondary signal. It is the intended primary, so the tracking finding and the first change-list item are withdrawn and the score is recomputed.

| Category | Score |
|---|---|
| Conversion Tracking | 80 |
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

**Conversion tracking matches the client's goals.** Primary and included actions in 30 days: GA4 get_directions 122, GA4 click_to_call 7, Calls from ads 3, GA4 generate_lead 1. That is the intended order of priority (directions, then calls, then contact submissions), so 133 conversions is a real number for this showroom. Two housekeeping items: the two YouTube engagement actions (follow-on views, channel subscriptions) are set primary and included, recorded zero, and should be secondary on a search account. And a second "Get directions" webpage action exists alongside the GA4 get_directions import (0 conversions in the window). If both ever fire on the same tap, directions will double count. Confirm only one is live.

**The Brand campaign's 85% rank loss is mostly phantom.** Keyword-level data (revised Sep 4): the exact keyword "patio style" has 84% impression share, 54% top-of-page and 40% absolute-top share, at $1.51 a click. "patio style longwood" is at 82% share. The loss comes from the two phrase keywords, "patio style furniture" (1,269 impressions, 12% share) and "patio style" phrase (406 impressions, 15% share), which close-variant match generic queries such as "patio furniture", "outdoor furniture", "lanai patio", "rattan furniture", "patio ideas", "big lots patio", and "city furniture". Losing those at a $1.50 cap is correct. The real brand gap is absolute-top share on the exact term, 40%, which means competitors sit above the client's own name some of the time.

**Maximize Clicks on 133 conversions a month is leaving signal on the table.** The Outdoor Furniture campaign alone recorded 114 conversions, well above the 15 a month where Maximize Conversions has enough to learn from. Today the strategy buys clicks at a $2.50 cap with no regard to which ones lead to a showroom visit or a call.

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

1. Conversion housekeeping: set "YouTube follow-on views" and "YouTube channel subscriptions" to secondary. Keep get_directions, click_to_call, generate_lead, and Calls from ads primary. Confirm the webpage "Get directions" action is not double counting the GA4 import. Add a form or quote-request action for kitchens and pergolas if the site has one.
2. Brand campaign, in this order. First pause the phrase keywords "patio style" and "patio style furniture" and keep only exact brand variants ([patio style], [patio style furniture], [patio style longwood], [patio style longwood fl], [patiostyle], [patio style fl]). Then switch the campaign from Maximize Clicks to Target Impression Share, absolute top, 90%, with a $4.00 max CPC. If staying on Maximize Clicks, raise the cap from $1.50 to $3.00. Expect the exact brand CPC to land around $2, roughly $100/mo instead of $77. Check absolute-top share after 7 days and raise the cap to $4.00 if it is still under 80%. Also confirm the campaign's phrase negatives ("patio furniture", "outdoor furniture") are live, since both still appeared as search terms in the window.
3. Move Outdoor Furniture to Maximize Conversions now. It has 114 conversions a month of signal. Leave Kitchens (5) and Pergolas (7) on Maximize Clicks until each reaches 15 conversions a month.
4. Pause "outdoor grill island" and "insulated patio cover" pending the client's answer on panels and grill islands. If they do sell grill islands, rebuild the keyword as exact "outdoor kitchen island orlando" with a product landing page.
5. Add to Master Negatives, phrase: roof panels, panels, aluminum roof, pergolux, paradise grill, big green egg, blackstone, ikea, costco, vestivium, photos, pictures, ideas, diy, plans.
6. Add a second RSA to the 11 single-ad groups. Start with Patio Covers & Cabanas, Outdoor Kitchens, and Built-in Grills, which carry the spend.
7. Landing pages: check that "patio furniture store near me" and "outdoor patio furniture" land on a page with store hours, address, and inventory photos above the fold. QS 3 to 4 on the two biggest keywords is mostly landing page experience.
8. Decline Google's Search Partners, Display Expansion, Maximize Conversions (for now), Target CPA, and Performance Max recommendations.

## Deep dive 5: All Phase Pool Remodeling (103-111-7688), score 75 C, requested by Tom

Context applied: two Ads accounts by design. This is the search home. 918-824-8896 holds the Jacksonville LSA (deep dive 1 covers its leftover search campaign).

Snapshot: one campaign, "All Phase Pool Remodeling - M", Maximize Conversions with no target, $30/day, budget-limited. 30 days: $915.28, 2,061 impressions, 155 clicks, $5.91 CPC, 7.5% CTR, 35 conversions at $26.15 each (Request quote 8, website call 5, Calls From Ads 22). Search impression share 12.8%, lost to budget 21.6%, lost to rank 65.6%. Every keyword is broad match.

### What is working

- $26.15 per conversion on a remodeling service is good. The best non-brand keyword, "pool resurfacing companies near me" (broad), produced 7 conversions on $105.85, which is $15.12 each.
- Two RSAs in every ad group, two of them EXCELLENT.
- Four primary actions, no double counting in the conversions column.

### Findings

- **Brand is inside the non-brand groups.** "all phase pool remodeling" (broad) sits in both Pool Renovations ($381.96, 56 clicks, 14 conversions) and Pool Resurfacing ($133.64, 25 clicks, 6 conversions). Together that is $515.59, 56% of spend, and 20 of the 35 conversions. Because it is broad, it also matched "all phase pool" ($15.55, 3 clicks, 0 conversions). Brand and non-brand are blended in one budget-limited campaign, so Maximize Conversions is learning mostly from brand clicks.
- **Non-brand on its own:** $399.69 for 15 conversions, $26.65 each. Healthy, but it only gets 44% of the budget.
- **Stray search terms, $42.36:** "pool repair lake mary fl" $20.12, "pinch a penny mount dora" $8.17, "pool coatings" $7.42, "white sands pool orlando" $6.65.
- **"Phone Calls 60s+"** (CLICK_TO_CALL type) is primary and recorded zero. Not declared dead; manual test.
- **"Contact Form"** recorded 4 but is excluded from the conversions column. If it is a different form from "Request quote", those are 4 uncounted leads.
- Google has 44 open keyword recommendations plus Performance Max and a budget increase.

### Prepared change list

1. Create a Brand campaign: exact and phrase "all phase pool remodeling", "all phase pool", "all phase pools", "allphase pool". $8/day. Move the two broad brand keywords out of the non-brand groups and add "all phase" as a phrase negative to the "- M" campaign.
2. Convert the non-brand broad keywords to phrase: swimming pool renovations, swimming pool renovations near me, pool coping and tile, pool coping renovation, pool renovation services. Leave "pool resurfacing companies near me" on broad since it is the best performer.
3. Negatives, phrase, campaign level or a new shared list: repair, repairs, leak, pinch a penny, leslie's, white sands, coatings, paint, cleaning, equipment, pump, filter, supply, supplies, diy, kit. Add "lake mary" only if they do not serve it.
4. Manual trigger test on "Phone Calls 60s+". Decide whether "Contact Form" should be included in Conversions; if it is a separate form from Request quote, include it.
5. Ads: Pool Resurfacing has two AVERAGE RSAs. Refresh one with resurfacing-specific headlines (pebble, plaster, resurface cost, Orlando) and the free-quote offer.
6. Budget: once brand is split out, the non-brand campaign at $30/day with 21.6% budget-lost share and a $26 CPA is a fair candidate for $40/day. Client decision.
7. Decline Performance Max and the budget recommendation as written. Review the 44 keyword suggestions only for terms containing "resurfacing", "remodel", or "renovation".

## Deep dive 6: Aqua Coat Pool Plastering (285-714-0527), score 67 D, requested by Tom

Snapshot: one campaign, "Aqua Coat Pool Plastering - M", Maximize Conversions with no target, $15/day. 30 days: $325.56, 2,330 impressions, 88 clicks, $3.70 CPC, 3.8% CTR, 8 conversions at $40.69 each (Free Estimate 2, Phone Calls 60+ 2, website call 2, Contact Form Submission 2). Search impression share 10%, lost to budget 38.2%, lost to rank 55.3%. Primary status LIMITED with reason SEARCH_VOLUME_LIMITED. Five ad groups: Pool Plastering, Pool Equipment, Pool Resurfacing, Pool Renovations, Tile. All keywords broad except one.

### Findings

- **Two ad groups are off-service.** "swimming pool equipment" (broad, $44.56, 10 clicks, 0 conversions) matched "pool equipment suppliers near me" and "inground pool handrail". "pool cleaning services" (broad, $16.20, 6 clicks, 0). That is $60.76, 19% of spend, on things a plastering company does not sell.
- **Competitor names, $46.49:** fresh finish pools $14.05, aqua pools $13.79, aqua dreams pools $9.63, pcs pools $9.02. The brand keyword "aqua coat pool plastering" is broad, which is how "aqua pools" and "aqua dreams pools" got in.
- **The cheapest converter is the smallest group.** "tile contractor tampa" (broad, $14.37, 3 clicks) produced 2 conversions at $7.19 each. Tile has room to grow.
- **Bidding is thin.** Maximize Conversions on 8 conversions a month. The CPA is acceptable, but a fifth of the clicks feeding it are off-service.
- **Budget vs volume:** Google reports both "search volume limited" and 38% of impressions lost to budget. Both can be true in a tight service radius: few searches, and the budget still cannot cover them.
- **Ads:** two per group, but Pool Renovations has one POOR. No sitelinks (Google's sitelink recommendation is the one worth taking).

### Prepared change list

1. Pause the Pool Equipment ad group and the "pool cleaning services" keyword. $60.76 a month goes back to plastering and resurfacing.
2. Negatives, phrase: equipment, supplies, supply, handrail, ladder, pump, filter, heater, cleaning, cleaner, chemicals, fresh finish, aqua pools, aqua dreams, pcs pools, pinch a penny, leslie's.
3. Change the brand keyword "aqua coat pool plastering" from broad to phrase and add exact. Broad brand is what pulls in "aqua" competitors.
4. Convert "pebble tec plaster" from broad to phrase. It matched two competitor names.
5. Grow the Tile group: add phrase "pool tile contractor", "pool tile replacement tampa", "pool tile repair tampa", and exact "pool tile contractor tampa".
6. Replace the POOR RSA in Pool Renovations. Add four sitelinks (Plastering, Resurfacing, Tile, Free Estimate).
7. Keep Maximize Conversions for now. Re-check the CPA 30 days after items 1 to 4. If it is still under $50 and budget-lost share is still above 30%, raise the budget from $15/day to $20/day.
8. Decline Search Partners, Display Expansion, Broad Match, and the dynamic image extension. Take the sitelink recommendation.

## No action needed this week (one-liners)

- **Premium Medication Refills (60 D):** paused, confirmed by Tom on Sep 4. Ads are APPROVED_LIMITED under healthcare policy. While it ran, $1,732.56 bought 9 leads at $192.51 each and $110 went to other pharmacies' names (caremark, costco, heb, select rx, northwind, ascension, telyrx, nimble, medvantx, birdi, aetna, cost plus drugs, champva). Two clicks touched "controlled substance" queries. If it restarts, add a pharmacy-brand negative list and a "controlled" negative first, and resolve the policy limitation with Google before spending.
- **Aqua Coat (67 D):** see deep dive 6 above, added at Tom's request.
- **Rover Veterinary Care (67 D):** the Brand campaign's broad keywords on the doctor's name ($398.71 in 30 days, matched "dog clinic near me", "canine oncologist", "pet death doula") are already paused and removed. Good. Remaining: both Competitors RSAs are POOR, "humane pet euthanasia" (generic) lives in the Competitors campaign, and cat-care questions ("when to put down a cat", "does banfield euthanize cats") cost $45. Add "when to", "banfield", "hospice", "baton rouge", "quality of life" as phrase negatives. Due next week.
- **Scootz (68 D):** healthy CPC ($0.78) and CTR (7.2%) but 28 keywords in one ad group, brand mixed with Disney, Universal, and wheelchair terms, and Maximize Clicks with 48 conversions a month. Split into Brand, Disney, Universal, Orlando general, and Wheelchair ad groups, then move to Maximize Conversions. Due next week.
- **Florida Sealcoating (69 D):** September ramp to $3,000 is intended, so rising spend is not a finding. Findings that are: five keywords at QS 2 to 3 carrying $447 (driveway repair near me, asphalt company orlando, paving companies near me exact and broad, asphalt paving company near me, asphalt patch repair); "sealcoat florida" and "sealcoat florida inc" ($33.27, 5 clicks, 0 conversions) look like a different company and should be exact negatives in Branded; competitor names $62 (kennedy concrete, absolute asphalt, american asphalt, martin paving, ppg traffic solutions, seal right); the FL Remarketing display campaign has an EXCELLENT ad and zero impressions on $5/day. Due next week.
- **The Counseling Group (73 C):** deep dive completed today in reports/ppc-audit-the-counseling-group-2026-09-04.md. Not due again until October.
- **Affordable Critter Solutions (75 C):** solid ads (two EXCELLENT, one GOOD, a call ad) and clean terms. "nuisance wildlife removal" ($58.42, 17 clicks, 0 conversions) is the one keyword to watch. Eleven paused campaigns should be removed for hygiene. Max Conversions on 10 conversions a month at a $10/day budget is thin but working ($30.55 per conversion).
- **All Phase Pool Remodeling (75 C):** see deep dive 5 above, added at Tom's request.
- **Progetto Shades:** all campaigns paused mid-window. Before the pause, Performance Max spent $169.02 on 359 clicks with zero conversions and the search campaign $192.63 for one conversion. If it restarts, do not restart PMax.
- **Jupiter Boat Supply, M&S Asphalt Paving, REK Marketing:** fully paused, zero spend, nothing to do.

## Rotation

Deep-dived this run: All Phase Jacksonville, Premium Walk-In Clinic, Precision GPR, Patio Style, and The Counseling Group (separate report). Both Patio Style and The Counseling Group were revised the same day after Tom supplied context the API does not carry (see the Known account context section of the protocol). Also covered at Tom's request: All Phase Pool Remodeling and Aqua Coat. Due next Monday: Florida Sealcoating, Rover Veterinary Care, Scootz. The week after: Affordable Critter Solutions.

## Data notes

- Search-term tables use Google's visible terms only. Google withholds low-volume terms, so confirmed waste is a floor.
- Quality Score is only reported on keywords with enough recent impressions. "n/a" in the source data was treated as unknown, not as low.
- The local ~/google-ads.yaml on the Mac was rejected by Google ("developer token is not valid"), so the tools/gaql.py helper could not be used. The MCP connection worked. The yaml on this machine needs the same fix as the Drive copy noted in yesterday's report.
