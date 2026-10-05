# PPC Weekly Audit - 2026-10-05 (Google Ads fleet)

Run: Monday Oct 5, 2026, scheduled cloud session through tools/gaql.py (API v25) against MCC 656-695-7229. Windows: 30 days Sep 5 to Oct 4; this week Sep 28 to Oct 4; last week Sep 21 to Sep 27. Score deltas are against the Sep 28 report (reports/ppc-weekly-audit-2026-09-28.md, still on its draft PR branch along with the Sep 21 report; neither has been merged to main). Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives, per the Sep 28 rotation: Scootz, Rover Veterinary Care, Progetto Shades, All Phase Pool Remodeling, plus Patio Style because its conversion tracking regression is still open. Filutowski Eye Institute and Color Masters get extended notes. One-liners for the rest.

The credential file was copied from the Drive folder dave-ads-setup with mode 600, used only by the client library, and deleted before this report was written. No credential value appears anywhere in this file.

## Attention items (read first)

1. **Patio Style (596-555-8707) is in its third week with no counted directions conversion.** Both directions actions (the GA4 get_directions import and "Get directions (GTM) 11 Sep") are still secondary and excluded. The taps continue: 10 and 11 in all_conversions this week. Counted conversions this week: 4 (3 ad calls, 1 website call). Nobody has touched the conversion settings since the Sep 28 flag; Dave's only change in the account this week was raising a Pergolas ad group bid from $2 to $5 on Oct 1. See deep dive 1.
2. **Scootz (185-574-5478) has had no edits since Sep 2, five weeks.** GA4 form_submit is still secondary and has recorded nothing since the week of Aug 10. This week 4 conversions on $337 (2 Booqable purchases, 2 ad calls). The Sep 14 and Sep 28 change lists have not been started. See deep dive 2.
3. **Rover Veterinary Care: the 332-member "Account Negatives - Master" list is attached only to Brand and Competitors.** The two campaigns that spend the most, In-Home Pet Euthanasia ($302) and Pet Cremation Services ($522), run without it. That is why "pet angel phone number" ($38), "peggy adams cremation" and "pet cemetery near me" matched Pet Cremation this window although those tokens are in the master list. Same fault as Aqua Coat and All Phase, now in a third account. See deep dive 3.
4. **Florida Sealcoating Branded has gone two weeks with zero conversions on $423.** Branded spent $269 this week (up from $154) for 0 conversions; in 30 days $661 for 4. The phrase keyword "florida sealcoating" is paying $20.67 a click, which is not a brand price; "florida sealcoating llc" phrase spent $181 for 0. The $17 target CPA Dave removed on Sep 15 has not gone back. Daily budgets still total $125 ($3,750 a month) against the $3,000 plan. Competitor and supplier negatives are now four weeks outstanding and "m&s asphalt paving", another REK client, cost Florida Sealcoating $51 this week.
5. **Filutowski Eye Institute (192-870-7876): spend fell this week ($5,216 to $4,212) and so did conversions (72.7 to 57.3).** No one edited the account. The strict waste floor on the broad catch-all keyword is $7,786 in 30 days and $1,588 this week. The Sep 14 scope decision is still open; this is the fourth report carrying it.
6. **Color Masters (426-092-9847) has its first conversion: one lead form on Oct 4, after $780 and 79 clicks in two weeks at $9.88 a click.** Tom paused seven research-prone keywords on Sep 29 and removed the ad schedule on Oct 2, so the campaigns now run around the clock. $260 of the $300 visible search-term spend is still DIY, cost or color-idea research. See the new-account note.
7. **No account vanished from the MCC and none is new.** Discovery returned the same 30 client accounts as Sep 28. Premium Walk-In Clinic remains absent, which is expected.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 30 client accounts, 1 manager | 14 | 0 new, 0 vanished since Sep 28. Excluded: Byers Fence x2, 9 LSA-only accounts, Straightline (LSA only), the unnamed 163-445-9282 (Color Masters' LSA shell, see one-liners). Not scorable: Jupiter Boat Supply, REK Marketing (paused), All Phase Jacksonville (search not eligible). |

Search, display and Performance Max spend in the 30-day window: $16,114 across the 13 REK-managed scored accounts, plus $19,674 at Filutowski Eye Institute. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 28. Conv is counted primary conversions, 30 days. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $19,674 | 290 | $68 | 40 | F | 0 | Critical (scope) | "lasik treatment cost" broad took $13,751 and 877 of its visible terms are other practices, doctors or addresses; strict floor $7,786 | $7,786 |
| 2 | Color Masters | 426-092-9847 | $780 | 1 | $780 | 52 | F | -5 | Needs attention (new) | First conversion Oct 4; $260 of $300 visible spend is research or DIY; ad schedule removed Oct 2 | $260 |
| 3 | Scootz | 185-574-5478 | $1,519 | 29 | $52 | 55 | F | -1 | Critical | No edits in five weeks; form_submit still secondary and silent; one ad group, 32 keywords, Maximize Clicks | $25 |
| 4 | Patio Style | 596-555-8707 | $1,939 | 65 | $30 | 56 | F | -4 | Critical | Directions still secondary (third week); "patio styles" phrase still in Brand; Pergolas $474 for 0 and its bid went up Oct 1 | $97 |
| 5 | Quality Paralegal Services | 447-153-2607 | $923 search, $451 smart | 22 search, 53 smart | $42 search | 56 | F | +1 | Needs attention | 94 percent broad match on lawyer terms; a POOR RSA and an unrated single ad in two groups; search conversions 7 to 7 after Tom's Sep 23 keywords | $105 |
| 6 | Progetto Shades | 416-010-8247 | $1,385 | 9 | $154 | 57 | F | -1 | Needs attention | 29 keywords at QS 1 to 3 carrying $581; every ad group one RSA; CPA $200 to $209 | $60 |
| 7 | Precision GPR | 554-113-4760 | $2,544 | 23 | $111 | 57 | F | +3 | Needs attention | Best 30 days since the cleanup began ($164 to $111); the negative list, Location and DSA pauses still not applied; "gprs" variants $157 | $272 |
| 8 | Florida Sealcoating | 168-852-7101 | $2,914 | 25 | $117 | 59 | F | -3 | Needs attention | Branded 0 conversions for two weeks on $423 at $11.81 to $14.15 a click; competitor negatives four weeks outstanding; budgets $125 a day | $390 |
| 9 | The Counseling Group | 657-069-3617 | $501 | 3 | $167 | 63 | D | -4 | Needs attention | Zero conversions for two weeks on 57 clicks; tel-tap action zero at 54 days; "help with depression" and "stress therapy" still live | $8 since Sep 21 |
| 10 | Rover Veterinary Care | 750-667-5721 | $1,340 | 17 | $79 | 65 | D | -1 | Needs attention | Master negative list not attached to the two main campaigns; Pet Cremation $522 for 3 conversions; In-Home budget raised to $50 Oct 2 | $130 |
| 11 | All Phase Pool Remodeling | 103-111-7688 | $694 | 13 | $53 | 66 | D | -4 | Needs attention | Spend $169 to $256 after the target CPA came off; master list link still REMOVED; brand term $280 of $694 inside non-brand groups | $55 |
| 12 | M&S Asphalt Paving | 827-724-4095 | $338 | 5 | $68 | 66 | D | +2 | On target (small) | 3 conversions on $106 this week; Orlando Metro and Sealcoating campaigns now paused and Volusia budget reads $39, neither change is in change history | $51 |
| 13 | Aqua Coat Pool Plastering | 285-714-0527 | $496 | 18 | $28 | 67 | D | +1 | On target | 4 conversions at $22 this week; master list still attached only to the paused campaign; Pool Equipment group still live ($137) | $100 |
| 14 | Affordable Critter Solutions | 227-108-4521 | $290 | 12 | $24 | 75 | C | -1 | On target | Clean; the only leak is county animal-control phone-number queries ($28) | $28 |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | n/a | n/a | Out of scope | LSA only since Sep 22: $2,346 in 30 days, 18 leads at $130 | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | n/a | n/a | Paused (search) | LSA paused Sep 24; the "Orlando" search campaign is still ENABLED and NOT_ELIGIBLE (worklist item 6) | n/a |
| none | Jupiter Boat Supply, REK Marketing | | $0 | 0 | n/a | n/a | n/a | n/a | Paused | No changes | n/a |

Confirmed waste across the fleet: $9,414 a month, of which $7,786 sits in Filutowski Eye Institute. Excluding Filutowski the figure is $1,628.

No account cleared 76. The four marked On target have no blocking defect and converted on plan this week.

## Week over week (Sep 28 to Oct 4 against Sep 21 to 27, search, display and PMax only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $5,216 to $4,212 (-19%) | 509 to 422 | 6.3% to 5.7% | $10.25 to $9.98 | 72.7 to 57.3 | $72 to $73 | Brand Awareness $3,750 to $2,832 and its conversions 15.7 to 22.0; Cataracts 7 to 2 |
| Precision GPR | $622 to $571 (-8%) | 41 to 45 | 7.5% to 5.9% | $15.18 to $12.69 | 6 to 9 | $104 to $63 | Best week on record; Branded 2 conversions on $9 |
| Florida Sealcoating | $698 to $922 (+32%) | 79 to 106 | 6.1% to 5.5% | $8.83 to $8.70 | 5 to 6 | $140 to $154 | Branded $154 to $269 for 0; Commercial lost 66% of impressions to budget |
| Patio Style | $480 to $396 (-18%) | 202 to 184 | 6.1% to 6.4% | $2.38 to $2.15 | 8 to 4 | $60 to $99 | Tracking, not performance; directions taps 10 to 11 uncounted |
| Progetto Shades | $599 to $418 (-30%) | 107 to 95 | 4.1% to 4.0% | $5.60 to $4.40 | 3 to 2 | $200 to $209 | Shades & Blinds $286 to $169; CPC fell at the $7 ceilings |
| Scootz | $326 to $337 (+3%) | 540 to 483 | 7.1% to 5.9% | $0.60 to $0.70 | 7 to 4 | $47 to $84 | Booqable purchases 4 to 2 |
| Quality Paralegal (search) | $267 to $273 (+2%) | 59 to 69 | 4.2% to 6.1% | $4.52 to $3.96 | 7 to 7 | $38 to $39 | Flat; smart campaign 8 to 3 conversions as its budget went $5 to $2 to $5 |
| Color Masters | $393 to $387 (-2%) | 39 to 40 | 7.9% to 8.2% | $10.08 to $9.67 | 0 to 1 | none to $387 | First lead Oct 4 |
| Rover Veterinary Care | $231 to $241 (+4%) | 58 to 62 | 11.4% to 12.1% | $3.99 to $3.89 | 7 to 4 | $33 to $60 | In-Home 4 to 1; Pet Cremation $91 to $151 for 1 |
| All Phase Pool Remodeling | $169 to $256 (+51%) | 39 to 31 | 5.3% to 5.1% | $4.34 to $8.26 | 3 to 4 | $56 to $64 | CPC nearly doubled without the target CPA; 53% lost to budget |
| M&S Asphalt Paving | $149 to $106 (-29%) | 11 to 9 | 7.1% to 4.9% | $13.55 to $11.80 | 0 to 3 | none to $35 | Two estimate forms and a call |
| The Counseling Group | $137 to $118 (-14%) | 31 to 26 | 5.8% to 2.9% | $4.42 to $4.55 | 0 to 0 | none | Second zero week; impressions 538 to 882 |
| Aqua Coat Pool Plastering | $128 to $90 (-30%) | 20 to 16 | 2.5% to 3.2% | $6.39 to $5.61 | 3 to 4 | $43 to $22 | Budget lost share 61% to 39% |
| Affordable Critter Solutions | $60 to $63 (+6%) | 19 to 20 | 6.5% to 12.7% | $3.15 to $3.17 | 2 to 2 | $30 to $32 | Flat |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: Progetto Drapery 85 percent and Shades & Blinds 59 percent, Affordable Critter 73 percent, Patio Style Outdoor Furniture 67 percent, Precision GPR DSA 58 percent, Aqua Coat 54 percent, Scootz 55 percent. Highest budget loss this week: Filutowski Brand Awareness 80 percent (30d) and Branded 59 percent, Quality Paralegal search campaigns 52 and 74 percent, Florida Sealcoating Commercial 66 percent, Rover Competitors 56 percent (by design at $5), All Phase 53 percent, Counseling Group 45 percent, Precision GPR GPR Scanning 43 percent. Largest CPC moves: All Phase $4.34 to $8.26, Precision GPR GPR Scanning $14.92 to $20.00, Florida Sealcoating Commercial $14.01 to $22.25; Progetto Motorized $6.48 to $5.18 and Rover Cremation $3.81 to $3.87 flat.

## Changes made in the past week (Sep 29 to Oct 5) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Color Masters | Sep 29, Oct 2 | tom@rekmarketing.com | Seven keywords paused in Residential (exterior house painting, painting contractor, cabinet painting, cabinet refinishing, interior house painting and two more); all 18 ad-schedule slots removed Oct 2 | Spend flat at $387; the first lead came Oct 4 on "painters port orange". The campaigns now serve 24 hours a day. |
| Rover Veterinary Care | Oct 2, Oct 3 | tom@, sheokand003@gmail.com | In-Home Pet Euthanasia budget $30 to $50; enhanced CPC toggled on In-Home | Too early. In-Home spent $42 this week against a $50 a day budget and loses nothing to budget, so the raise will not change delivery until bids or keywords change. |
| Patio Style | Oct 1 | paidads@rekmarketing.com | Pergolas ad group bid $2 to $5 | Pergolas is $474 in 30 days for 0 primary conversions. A bid raise there before the client answers on panels adds cost without a conversion signal. |
| Aqua Coat | Sep 29 to Oct 5 | sheokand003@gmail.com | "hayward pool products" switched from phrase to broad Oct 1, one keyword paused, assets added on four days | The broad version matched "hayward pool pump tech support" for $17 on its first click. |
| Quality Paralegal Services | Oct 1 | tom@rekmarketing.com | Two ads paused in the English search campaign | Paralegals Services #2 keeps two enabled RSAs; "Affordable and experienced Paralegal" is down to one ad with no strength rating. |
| All Phase Pool Remodeling | Oct 1 | sheokand003@gmail.com | Two RSAs edited | Spend rose 51 percent for one more conversion; CPC $4.34 to $8.26 since the target CPA was removed Sep 25. |
| All Phase Orlando LSA, unnamed 163-445-9282 | Sep 28, Oct 3, Oct 5 | tom@, colormasters88@gmail.com | Orlando LSA budget set to $71.43; the unnamed account's LSA budget $12.86 to $35.71 with a schedule, Tom edited its criteria this morning | Out of scope. The unnamed account is Color Masters' Local Services shell (edited by colormasters88@gmail.com). |
| M&S Asphalt Paving | undated | not in change history | Paving - Orlando Metro and Sealcoating & Repairs - Volusia are PAUSED; Paving - Volusia budget reads $39 a day (last logged change $15 to $27 on Sep 24) | Volusia converted 3 times on $106 this week. Confirm the pauses and the $39 were intended. |
| Scootz, The Counseling Group, Florida Sealcoating, Progetto Shades, Precision GPR, Affordable Critter, Filutowski | | | No changes since the Sep 28 run | The Sep 28 action plan items for these accounts have not been applied. Scootz is at five weeks without an edit, Florida Sealcoating's negatives at four. |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

No new items landed this week. Still open: 3 (Patio Style phrase brand keywords came back Sep 16 and remain), 4, 5, 6, 7 (Pool Equipment and the master-list attachment), 8 (Depression RSA still POOR, "help with depression" and "stress therapy" still live), 10, 11, 12, 13, 16 (RSAs and negatives), 17, 19. Client answers: none recorded.

## Deep dive 1: Patio Style (596-555-8707), score 56 F, down 4

Context applied: the client's primary conversion is Get Directions to the showroom, then calls, then forms. Outdoor Furniture on Maximize Clicks at a $2.50 cap is by design.

| Category | Score |
|---|---|
| Conversion Tracking | 30 |
| Wasted Spend | 65 |
| Account Structure | 60 |
| Keywords & Targeting | 55 |
| Ads & Assets | 65 |
| Bidding & Settings | 65 |

| Campaign | Budget/day | Strategy | 30d spend | Clicks | CPC | Primary conv | All conv | This week |
|---|---|---|---|---|---|---|---|---|
| PS / Search / Outdoor Furniture | $30 | Maximize Clicks, $2.50 cap | $909 | 655 | $1.39 | 53 | 530 | $189, 2 conv |
| PS / Search / Pergolas & Louvered Roofs | $16 | Manual CPC | $474 | 64 | $7.40 | 0 | 3 | $86, 0 conv |
| PS / Search / Outdoor Kitchens | $12 | Maximize Clicks, $7 cap | $360 | 96 | $3.75 | 5 | 78 | $83, 0 conv |
| PS / Search / Brand | $6 | Target Impression Share 90%, $4 cap | $197 | 65 | $3.03 | 7 | 57 | $39, 2 conv |

The 65 primary conversions in the 30-day column include the directions counted in early September before the demotion; only 4 were counted this week.

Conversions by action by week (all_conversions, Google weeks starting Monday):

| Action | Aug 10 | Aug 17 | Aug 24 | Aug 31 | Sep 7 | Sep 14 | Sep 21 | Sep 28 |
|---|---|---|---|---|---|---|---|---|
| GA4 get_directions (import), now secondary | 14 | 42 | 38 | 43 | 28 | 16 | 15 | 10 |
| Get directions (GTM) 11 Sep, now secondary | 0 | 0 | 0 | 0 | 2 | 14 | 15 | 11 |
| Calls from ads, primary | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 3 |
| Website Call Conversions 11 Sep, primary | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 |
| Thank you page 11 Sep, primary | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| Send us a messages 11 Sep, secondary | 0 | 0 | 0 | 0 | 0 | 3 | 4 | 1 |

### Findings

- **Directions are still not counted.** Both directions actions remain primary false, included false. The showroom is still getting 10 to 15 directions taps a week from ads; Google Ads reports 4 conversions. Target Impression Share on Brand and Maximize Clicks on the others are not conversion-driven, so bidding is not hurt yet, but reporting and any future move to Maximize Conversions are.
- **Two new conversion actions created Sep 29 are miscategorised.** "Phone Call Click 29/ Sep" and "Send a messages landing page 29 Sep" are both typed GET_DIRECTIONS (as is "Send us a messages 11 Sep"). They are secondary, so nothing is counted wrongly today, but a phone click labelled as directions will confuse the next person who tries to repair this.
- **Brand drift continues.** "patio styles" phrase, added Sep 16, is $127 in 30 days for 1 conversion and this week matched "ideas for screened in patio" $8, "lanai furniture ideas" $8, "patios decorations" $8, "patio cover ideas" $6. The Sep 4 exact-only fix is undone. Brand is BIDDING_STRATEGY_LIMITED at $6 a day and lost 56 percent of impressions to budget this week.
- **Pergolas spent $474 for 0 primary conversions**, led by "insulated patio cover" ($150, 23 clicks) and "patio cover orlando" ($130, QS 3). Panel queries still arrive ($42: "aluminum patio roof panels", "insulated porch roof panels", "insulated pan roof", "snap lock insulated aluminum roof panels", "patio roof panels insulated") although "panels" and "roof panels" are phrase negatives; the matches are plural and compound forms. On Oct 1 the Patio Covers ad group bid went from $2 to $5. The client's answer on insulated panels (worklist item 4) is still outstanding, so this bid raise is in the wrong direction.
- **Ads**: 11 of 12 enabled ad groups have one RSA (Patio Furniture has two). The paused predecessors from Sep 25 are still there to re-enable.
- **Dedupe**: panels, roof panels, mirador present in Master Negatives. Absent: ideas, idea, decorations, makeover, pan roof, sink, cabinets, daytona, big green egg, tru island, vestivium, hampton bay, polywood (the store sells Polywood, keep), azenco (keep), cost, best, 2026, gas grill, 48 round.

### Prepared change list

1. Today: set the GA4 get_directions import back to primary and included. Leave the GTM action secondary so one tap counts once. Retype the two Sep 29 actions (phone click as PHONE_CALL_LEAD, message as SUBMIT_LEAD_FORM or CONTACT).
2. Brand: remove "patio styles" phrase, or add phrase negatives ideas, decorations, makeover, cover ideas to Brand. Raise Brand to $10 a day so Target Impression Share is not LIMITED.
3. Pergolas: revert the Oct 1 bid raise until the client answers on panels. Pause "insulated patio cover" and "patio cover orlando". Add phrase negatives pan roof, porch roof, cost, best, 2026 to Master Negatives.
4. Re-enable one paused RSA in each single-ad group.
5. Hold worklist item 13 (Maximize Conversions) until directions have two counted weeks.

## Deep dive 2: Scootz (185-574-5478), score 55 F, down 1

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 70 |
| Account Structure | 45 |
| Keywords & Targeting | 65 |
| Ads & Assets | 75 |
| Bidding & Settings | 50 |

Snapshot: one search campaign, Maximize Clicks, $50 a day, BUDGET_CONSTRAINED. 30 days: $1,519, 34,297 impressions, 2,364 clicks, $0.64 CPC, 6.9 percent CTR, 29 primary conversions at $52. Search impression share 27 percent, 19 percent lost to budget, 54 percent lost to rank.

Counted conversions by week (Aug 10 to Sep 28): Booqable Purchases 4, 2, 5, 4, 5, 10, 4, 2; Calls from ads 1, 2, 0, 0, 0, 2, 3, 2. GA4 form_submit: 28 in the Aug 10 week, then zero for seven weeks; it is still secondary and excluded.

### Findings

- **Nothing has changed since Sep 2.** Change history for the last 30 days is empty. The form action has not been tested or restored, the ad group has not been split, and the account runs exactly as it did on Sep 14.
- **Only purchases and ad calls count**, so 8 enabled keywords with $331 of spend show zero primary conversions while carrying 8 to 21 Google-hosted local actions each ("electric wheelchair rental disney world" $102, "scooter rental disney world area" $68, "ecv rental universal orlando" $44, "mobility scooters orlando" $34). Do not pause on this data; fix tracking first.
- **Brand lives inside the non-brand campaign**: "scootz mobility scooter rentals" exact ($30, 3 conversions), "scootz orlando" phrase ($28, 0) and the brand search terms "scootz rentals", "scootz mobility scooter", "scootz orlando" ($36 combined) are all in Ad group 1 at the non-brand $2.50 cap.
- **Search terms are clean.** Visible 30-day waste is $25: "scooterbug" (a competitor) $8 across three variants, and "how much" and "cost" price queries $17 that still match although the Sep 14 report thought price-shopping negatives existed; "how much" is not in the 10-member "negative words" list or the 34 campaign negatives. "2 person scooter rental orlando" ($6, 9 clicks) is on-service if they rent tandems.
- **Google's open recommendations** for the account: switch to Maximize Conversions, add Performance Max, search partners, display expansion, four keywords, and a budget raise. Ignore all but the bidding one, and only after tracking is repaired.

### Prepared change list

1. Manual form submit on scootzrentals.com this week; confirm the GA4 form_submit event fires and is linked, then set it primary and included.
2. Phrase negatives: scooterbug, how much, cost, price. Exact brand into its own Brand campaign on Target Impression Share.
3. The Sep 14 five-way split (Brand, Disney, Universal, Orlando, Wheelchair), then Maximize Conversions after two weeks with 15 or more counted conversions.

## Deep dive 3: Rover Veterinary Care (750-667-5721), score 65 D, down 1

| Category | Score |
|---|---|
| Conversion Tracking | 70 |
| Wasted Spend | 60 |
| Account Structure | 55 |
| Keywords & Targeting | 65 |
| Ads & Assets | 55 |
| Bidding & Settings | 75 |

| Campaign | Budget/day | Strategy | 30d spend | Clicks | CPC | Conv | CPA | This week |
|---|---|---|---|---|---|---|---|---|
| Pet Cremation Services | $30 | Manual CPC | $522 | 97 | $5.38 | 3 | $174 | $151, 1 conv |
| Competitors | $5 | Maximize Conversions | $417 | 59 | $7.07 | 5 | $83 | $38, 1 conv |
| In-Home Pet Euthanasia | $50 (was $30 until Oct 2) | Manual CPC | $302 | 52 | $5.81 | 7 | $43 | $42, 1 conv |
| Brand Campaign | $10 | Maximize Conversions | $99 | 19 | $5.22 | 2 | $50 | $11, 1 conv |

Three weeks after Dave's Sep 16 rebuild: 17 conversions on $1,340 ($79), against 17 on $1,424 ($84) in the Sep 28 window. The rebuild holds. This week dipped to 4.

### Findings

- **The master negative list is attached to the wrong campaigns.** "Account Negatives - Master" (332 members) is linked to Brand and Competitors plus the paused legacy campaigns, not to In-Home Pet Euthanasia or Pet Cremation Services. Those two run on "Rover - N" (6 members), "Rover Core Exclusions" (24) and 40 ad-group negatives. Terms that the master list already blocks got through this window in Pet Cremation: "pet angel phone number" $38, "pet angels cremation" $8, "peggy adams cremation" $4, "peggy adams euthanasia" $4, "pet cemetery near me" $16. Attaching the list is one click and fixes about $70 of this window's waste.
- **Pet Cremation Services is the weak campaign now**: $522 for 3 conversions. "pet cremation near me" phrase $91 for 0, "pet cremation services" $154 for 0.3, "dog cremation" $26 for 0, "pet cremation florida" $27 for 0. Out-of-area terms ("pet cremation fort lauderdale" $8, "pet cremation west palm beach" $16, "pet cremation cape coral" $4) and memorial-product terms ("cat urns", "cat urn", "dog memorial with ashes" $12) are the leak.
- **Competitors**: Dave paused "lap of love" exact, "lap of love near me" and "lap of love veterinary" on Sep 16, yet "lap of love" variants still cost $152 across the account because "humane pet euthanasia" phrase ($271, 4 conversions) and the In-Home keywords match them ("lapse of love" $24, "lap of love jupiter" $17 and $11, "laps of love near me" $11 and $9). At $5 a day Competitors is 56 percent budget-limited, so the lap-of-love traffic is now being bought by the service campaigns at full price.
- **Brand**: "katie matzke" phrase is still live, $72 in 30 days for 1 conversion (worklist item 16 and the Sep 14 list). "rover pet euthanasia" $17 for 1.
- **Ads**: Competitors still carries a POOR RSA next to an AVERAGE one. Cat Euthanasia and In-Home Pet Euthanasia groups still have one RSA each.
- **Budget**: Tom raised In-Home from $30 to $50 on Oct 2. The campaign spent $42 for the whole week and loses 0 percent to budget at $3.50 to $6 manual bids, so the extra budget cannot be spent without higher bids or more keywords. Enhanced CPC was toggled on Oct 3.
- **Conversions**: "Event|Contact|Calls From Website" recorded zero for two weeks while the new "Click to call (on website)" action recorded 2 and 2, which looks like a tag replacement rather than a fault. Confirm one of them is retired so the other is not double counted when both fire.

### Prepared change list

1. Attach "Account Negatives - Master" to In-Home Pet Euthanasia and Pet Cremation Services.
2. Phrase negatives to Rover Core Exclusions: when to, signs, quality of life, should i, paws to health, urns, urn, memorial, fort lauderdale, west palm, cape coral, free. Dedupe: peggy adams, banfield, taps, cemetery exist in the master list (hence item 1); none of the others exist anywhere live.
3. Decide on lap of love: either re-enable [lap of love] in Competitors at a sensible budget or add "lap of love", "laps of love", "lapse of love" as phrase negatives to In-Home and Cremation so the service campaigns stop paying competitor prices.
4. Pause "pet cremation near me" and "pet cremation services" phrase or cut their bids to $3; move "where to cremate a dog" ($12, 1 conversion) in as exact.
5. Pause "katie matzke" and "rover pet euthanasia" in Brand. Rebuild the POOR Competitors RSA; second RSA in Cat and In-Home groups.
6. Either take In-Home back to $30 or raise its bids; the $50 is idle.

## Deep dive 4: Progetto Shades (416-010-8247), score 57 F, down 1

| Category | Score |
|---|---|
| Conversion Tracking | 70 |
| Wasted Spend | 70 |
| Account Structure | 65 |
| Keywords & Targeting | 35 |
| Ads & Assets | 50 |
| Bidding & Settings | 55 |

| Campaign | Budget/day | Ceiling | 30d spend | Clicks | CPC | Conv | CPA | Search IS | Lost to rank | This week |
|---|---|---|---|---|---|---|---|---|---|---|
| Shades & Blinds | $25 | $7 | $656 | 130 | $5.05 | 4 | $164 | 16% | 66% | $169, 1 conv |
| Motorized & Smart | $10 | $7 | $252 | 44 | $5.73 | 1 | $252 | 27% | 55% | $67, 0 conv |
| Shutters | $12 | $7 | $243 | 39 | $6.23 | 2 | $122 | 36% | 62% | $95, 0 conv |
| Exterior & Patio | $7 | $4 | $177 | 50 | $3.53 | 1 | $177 | 26% | 58% | $53, 0 conv |
| Drapery & Curtains | $6 | $4 | $46 | 12 | $3.85 | 0 | n/a | 15% | 78% | $24, 0 conv |
| Brand | $5 | $2 | $11 | 6 | $1.77 | 1 | $11 | 60% | 33% | $11, 1 conv |

30 days: $1,385, 281 clicks, 9 conversions (Contact form 8, Calls from ads 1) at $154. The Sep 18 ceiling raise to $7 is still in place on the three biggest campaigns. No edits since Sep 25.

### Findings

- **Quality Score is the account's problem.** 29 enabled keywords sit at QS 1 to 3 and carried $581 of the $1,381 keyword spend. Nearly all are single-word or two-word exact terms: "interior shutters" QS 1 ($42), "faux wood blinds" QS 1 ($20), "vertical blinds" QS 1 ($13), "blackout curtains" QS 1 ($12), "roller shades" QS 2 ($42), "window shutters" QS 3 ($104, 0 conversions), "window shades" QS 3 ($51, 0), "outdoor patio shades" QS 3 ($112, 0), "automated shades" QS 3 ($34, 0). Expected CTR and landing page are BELOW_AVERAGE on almost every one. These are product-category searches landing on a general page; they convert at 0 in 30 days while "window covering company" ($258, 1), "window coverings near me" ($59, 1), "plantation shutters" ($70, 1) and "plantation shutters san diego" ($13, 1) do the converting.
- **Rank loss, not budget, caps every campaign**: 55 to 78 percent lost to rank. The $7 ceilings bought a $5 to $6 CPC without lifting rank enough to matter, and the CPA went $89 (Sep 14 week) to $300 to $200 to $209.
- **Every one of the nine enabled ad groups has one RSA**, three of them AVERAGE (Drapery, Shades, Window Treatments, Plantation Shutters). Google's own open recommendations include one RSA and six lead-form assets.
- **Search terms**: clean. "bamboo window shades" $18 and "bamboo shades" $7 are the only off-catalog terms unless Progetto sells woven wood (Tom added "woven wood shades" keywords Sep 25, so bamboo may be intended). "motorized tension blinds" $14. "smith noble shades" $7 got through although smith noble is a phrase negative (click predates or variant). Dedupe: technoline, smith noble, west elm, ikea, home depot, lowes, curtains (exact) present; bamboo, tension absent.
- **Conversions**: "Call ((858) 338-1678)" website call action is primary but excluded and has never recorded; "Lead form website" is secondary and recorded 1, 0, 0, 1, 1, 1 by week. If the website lead form is a real lead it should be primary.

### Prepared change list

1. Pause the QS 1 to 3 exact single-word product terms with 0 conversions in 30 days (window shutters, window shades, interior shutters, roller shades, faux wood blinds, vertical blinds, blackout curtains, automated shades, smart shades, motorized blinds, outdoor shades, patio shades, roman shades). Keep the phrase "company", "near me" and "san diego" variants that convert. This removes about $500 a month of QS 1 to 3 spend and should lift the campaign-level rank.
2. Ceilings back to $4 on Shades & Blinds, Shutters and Motorized (the Sep 14 setting). The $7 test ran 17 days and tripled CPA.
3. Second RSA in each ad group, written around the converting phrases ("window covering company San Diego", "plantation shutters San Diego").
4. Set "Lead form website" primary and included; test the (858) call action.
5. Phrase negatives: tension; bamboo only if woven wood is not sold.

## Deep dive 5: All Phase Pool Remodeling (103-111-7688), score 66 D, down 4

Context applied: two Ads accounts by design; 918-824-8896 holds the LSA.

| Category | Score |
|---|---|
| Conversion Tracking | 70 |
| Wasted Spend | 65 |
| Account Structure | 55 |
| Keywords & Targeting | 55 |
| Ads & Assets | 85 |
| Bidding & Settings | 60 |

Snapshot: one live campaign, "All Phase Pool Remodeling - M", Maximize Conversions with no target since Sep 25, $30 a day. 30 days: $694, 119 clicks, $5.84 CPC, 13 primary conversions (Calls From Ads 7, Call 888 4, Request quote 2) at $53. This week $256, 31 clicks, $8.26 CPC, 4 conversions; 53 percent lost to budget, 30 percent to rank (last week 0 and 86).

### Findings

- **Removing the $25 target CPA changed the auction behaviour, not the results.** Spend went $101, $169, $256 across the three weeks since Sep 25 while conversions went 2, 3, 4. CPC went $4.82, $4.34, $8.26. Daily spend hit $60 on Sep 28, 29 and 30 (twice the budget, which Google allows) then fell to $1.42 on Oct 3. Maximize Conversions without a target on 13 conversions a month is thin and is now spending the full budget by paying double for the same clicks.
- **The master negative list link is still REMOVED on the live campaign** (379 members; the live campaign runs on 91 campaign negatives and 11 ad-group negatives). Leaks this window: "leslie pool" $21, "pool cleaners near me" $9, "pool service deland" $5, "thompson pools and spas" $7, "pool deck resurfacing of central florida" $11, "average cost of pool resurfacing" $1.50. "pool service", "pool cleaning", "average cost" and "pool builders" are all in the unattached list.
- **Brand inside non-brand**: "all phase pool remodeling" broad sits in Pool Renovations ($242, 10 conversions) and Pool Resurfacing ($38, 2), and the brand search terms ("all phase pool remodeling", "all phase pool", "all phase pools", "all phase pools sanford fl") are $316 of the $447 visible spend. 12 of the account's 13 conversions came from brand terms. Non-brand spent about $380 for 1 conversion ("swimming pool renovations near me").
- **100 percent broad match.** "pool resurfacing companies near me" $145 for 0 primary (10.5 all-conversions), "swimming pool renovations" $131 for 0 (16.5 all-conversions). Those all-conversions are Google-hosted local actions, so intent exists; the primary actions just are not firing on these clicks.
- **Ads** are fine: two RSAs in every live group, GOOD to EXCELLENT. "Phone Calls 60s+" still has no data in 60 days (worklist item 12, manual test).

### Prepared change list

1. Re-attach "All Phase Master Negatives" to "All Phase Pool Remodeling - M" (the link exists with status REMOVED; recreate it). Then add phrase: leslie, thompson pools, deland, cleaners, coatings.
2. Put the brand keyword and brand terms in their own campaign (Target Impression Share, $8 a day) and take the broad brand keyword out of Pool Renovations and Pool Resurfacing. The non-brand campaign then has an honest conversion count to optimise on.
3. Put a target CPA back on the non-brand campaign ($40) or move it to Manual CPC at $4 to $5 while it has under 15 conversions a month. The no-target week doubled CPC.
4. Phrase-match the top non-brand terms: "pool resurfacing companies", "pool renovation", "pool resurfacing orlando", "pool tile repair".
5. Manual test on "Phone Calls 60s+".

## Filutowski Eye Institute (192-870-7876), score 40 F, unchanged (extended note, not a deep dive)

Scope note unchanged: no REK edits in 60 days; the only change in the window is Accalia Marketing's Sep 14 budget raise. Nothing should be touched until Tom decides whether REK manages, audits, or is only linked.

Numbers this window: $19,674 search in 30 days, 290.3 conversions, $68. The Brand Awareness catch-all (one broad keyword, "lasik treatment cost", $455 a day, Target CPA) spent $13,751 for 78.9 conversions ($174) and lost 80 percent of impressions to budget. By week: $3,503, $3,562, $3,750, $2,832 for 17.9, 22.3, 15.7, 22.0 conversions. Branded converts at $12.48 and loses 59 percent to budget at $50 a day; Eye Surgery at $26 loses 55 percent.

Visible search terms under the catch-all, 30 days, $9,071: named competitor practices, doctors and street addresses $5,768 (877 terms, 26 conversions), retail optical chains $1,736 (330 terms, 8), generic eye-care searches ("ophthalmologist", "eye doctor orlando", "eye exam near me") $922 (6), Spanish $207 (3), insurers $75 (0), LASIK or cataract intent $162 (0 conversions). Strict floor (named plus retail plus insurer plus Spanish): $7,786 in 30 days, $1,588 this week. This week's largest: "eye physicians of central florida metrowest park center drive 220 orlando fl" $134, "eye doctor davenport fl" $113, "florida eye clinic altamonte springs" $84, "florida eye clinic orlando" $71, "dr root ophthalmology" $48, "medical eye associates kissimmee" $43.

Dedupe of the Sep 14 and Sep 28 negative proposals against the live lists ("Search Terms" 22 members, "Brand Awareness" 15, plus 44 campaign negatives): pearle and eyeglass present; every other token absent (walmart, lenscrafters, america's best, costco, stanton, visionworks, warby, my eye doctor, target optical, total vision, glasses, contacts, optical, eyemed, cigna, aetna, medicaid, florida blue, tomoka, florida eye clinic, coan, precision eye, bayhead, eye place, mid florida eye, uptown eyecare, flud, cartwright, blanik, atlantic eye, shands, eye physicians, fishman, sheridan, eyedeal, premier eye, florida retina, retina, echegaray, perez, dawson, poulos, medical eye associates, vision one, ucf, keratoconus, cerca de mi, pediatric, kids). New this window: dr root, sakowitz, envision eyecare, fisher eye, eye avenue, vision source, correct vision, friendly eyes.

Everything else is as reported Sep 28: 18 hidden UA goals primary and included, three primary call actions, enhanced conversions for leads ON at a medical practice, one RSA per ad group, Cataracts and Eye Surgery flagged HAS_ADS_DISAPPROVED, Performance Max paused. Google's own open recommendations: 57 keywords and 5 budget raises, which would make this worse.

## New account note: Color Masters (426-092-9847), score 52 F provisional, down 5

Two weeks live. Residential Painting ($45 a day, Maximize Clicks, $11 ceiling) spent $763 of the $780; Commercial spent $10 on one click; Brand $6. 76 Residential clicks at $10.05, 1 conversion (lead form, Oct 4, on "painters port orange"). Impression share 50 percent, 47 percent lost to rank, so the ads show; the problem is what they show for.

- Tom paused seven keywords Sep 29 (exterior house painting $132, painting contractor $88, cabinet painting $85, cabinet refinishing $54, interior house painting $41 among them). What remains: "residential painters" phrase ($159, 0), "painters daytona beach" (QS 3, $56, 0), "exterior house painters" (QS 3, $40, 0), "painters ormond beach" (QS 3, $29, 0), "painters port orange" ($31, 1). Six keywords at QS 1 to 3; landing page BELOW_AVERAGE on all of them.
- Search terms: $260 of the $300 visible is research, DIY, color ideas or other painters: "j&b painting plus of florida inc port orange reviews" $21, "how much does it cost to repaint your kitchen cabinets" $21, "front door color idea" $21, "glidden premium interior" $20, "cost to paint house exterior" $11, "house exterior colors" $11, "white room paint ideas" $10, "jesus gil painting & maintenance" $10, "axis painting and decorating" $10, "faux painter near me" $10. Dedupe against the 92-member REK Painting Negatives: sherwin, behr, refacing, exterior paint, cabinet paint, paint ideas, color ideas, paint colors present; absent: glidden, idea (singular), how much, cost (standalone), colors (standalone), furniture, white, room, j&b, jesus gil, axis, faux, reviews, touch up, deland.
- Tom removed all 18 ad-schedule slots on Oct 2, so the campaigns now serve 24 hours. Nothing in the data argues for or against yet.
- Conversion tracking: 11 primary actions for a two-week-old account, including two smart-campaign call actions and "Calls from Smart Campaign Ads" with no smart campaign. Set those secondary. The GA4 generate_lead import also recorded the Oct 4 lead, so the lead form is tracked twice (one primary, one secondary; fine).

Suggested: phrase negatives glidden, idea, how much, cost, colors, color, furniture, room, reviews, faux, touch up, j&b, jesus gil, axis; cut the Maximize Clicks ceiling from $11 to $7; a second RSA per group; a painters landing page with the service areas named (Daytona, Port Orange, Ormond) to move the QS 3 terms off BELOW_AVERAGE.

## No action needed this week (one-liners)

- **Precision GPR (57 F, up 3):** the best 30-day window since the cleanup began, 23 conversions at $111 and 9 this week at $63. Nothing from the Sep 4 or Sep 28 lists has landed and the account improved anyway, which says the Sep 22 match-type tightening helped. Still open: "gprs" variants $157 this window ("gprs orlando" x3 $114, "gprs tampa" $21, "gprs service" $18, "gprs near me" $4), locate-service queries $51 (sunshine811, miss utility florida, 1800 dig), "julie wire locator" $28, "rebar finder in concrete" $18, "geoslice net" $18; none of gprs, sunshine, miss utility, 1800 dig, dig alert, julie, rebar, finder, geoslice, price, pricing is a negative (811, equipment, rental, locates present). Location ($2.62) and DSA ($313, 3 conversions) still enabled. QS 2 to 3 on "Ground Penetrating Radar" phrase and exact ($451) and "Underground Utility Survey" phrase and exact ($352). The (305) and (786) website call actions still have never recorded. Change list stands as written Sep 28.
- **Florida Sealcoating (59 F, down 3):** see attention item 4. Branded is the item: "florida sealcoating" phrase $351 for 2 conversions at $20.67 a click, "florida sealcoating llc" phrase $181 for 0, exact "florida sealcoating" $125 for 2 at $7.80. A brand phrase paying $20 a click is matching generic sealcoating queries; put Branded on exact only or restore the target CPA. Competitor and supplier negatives, four weeks outstanding and all still absent: ppg, absolute asphalt, gem seal, seal right, martin paving, kennedy, american asphalt, millings, cold mix, hot mix, who sells, hot patch, father and son, site development, concrete contractor, tack, hot shot, watson, infrared, striping machine, pavement marking, leveling, cosmonaut (exact), m&s asphalt (a REK client; $51 this week). "sealcoat florida" exists as a phrase negative in Commercial and Residential only; Branded, where "sealcoat florida inc" matched for $16, does not have it. QS 1 to 3 on eight keywords carrying $448 ("asphalt company orlando" QS 3 $167, "asphalt patch repair" QS 2 $67). The "Call (1-8-333-PAVEIT)" action still has no data; manual test. The Sep 11 and Sep 22 restructures: Residential went 1 to 2 conversions this week, Commercial flat at 3 with CPC $14 to $22.
- **Quality Paralegal Services (56 F, up 1):** search $273 for 7 conversions this week, same as last week, after Tom's Sep 23 keyword set (uncontested divorce, divorce papers, divorce forms, simplified dissolution, child support modification, parenting plan and seven more) and budget moves (English $23, Spanish $17, smart $5). Still 94 percent broad on the old lawyer and attorney terms: "family law attorney near me" QS 1 ($99, 2 conversions), "divorce lawyers near me" QS 1 ($62, 2), "support attorney" ($67, 0). "family mediation" ($228, 6 conversions) was paused Sep 22; it was the best converting keyword. Tom paused two ads Oct 1; the "Affordable and experienced Paralegal" group has one unrated ad and Ad group 1 carries a POOR RSA. "legal aid", "pro bono", "free", "tenant", "uscis", "yourforms" are now negatives and this window's $40 of those terms predates them. Absent and worth adding: melbourne, rockledge, polk, new smyrna, lake county, notario, notarios, notaria, public defender, fathers rights. The smart campaign ("QPS Non-Lawyer Services Orlando", $342, 44 conversions) counts Business Profile directions as conversions; keep it out of the search CPA.
- **The Counseling Group (63 D, down 4):** zero conversions for two weeks on 57 clicks and $255. Three in 30 days, all forms. Tel-tap action still zero at 54 days; the manual test (worklist item 10) is now eight weeks overdue, and with two zero weeks it matters. "help with depression" ($47, 0) and "stress therapy" (QS 2, $35, 0) still live although item 8 says pause; the Depression group's POOR RSA still live. Tom's Sep 21 negatives are working: no medication or author-name terms this week except "john gottman" ($4; "gottman" alone is not a negative and item 9 still needs Clark's answer) and "marriage counseling titusville fl" ($4; add titusville). QS 2 on "therapist near me" exact ($23) and "stress therapy", landing page BELOW_AVERAGE (item 11). Enhanced conversions confirmed OFF. Budget $25 a day, 45 percent lost to budget; on plan.
- **Aqua Coat (67 D, up 1):** 18 conversions at $28 in 30 days, 4 at $22 this week; the Sep 9 target CPA and Sep 16 geo tightening continue to hold. The 248-member master list is still attached only to the paused campaign (third report). Pool Equipment group still live: $137 for 1 conversion, this window matching "pentair pool pump" $19, "hayward pool pump tech support" $17, "pinch a penny" $20 across three variants, "pool ladder steps replacement" $9, "pool fountain near me" $3, "leslies near me" $2. Dave switched "hayward pool products" from phrase to broad on Oct 1; its first broad click was the $17 tech-support query. Dedupe: pinch a penny, leslies pool, pool pump, repair kit, kit, supplies, pool paint are in the unattached list (attach it); pentair, aqua pools, pcs pools, handrail, equipment, products, installers, grout, fresh finish, aqua dreams, ladder, fountain, tech support absent. "fiberglass pool repair" converted twice on $29 again and is still not a keyword.
- **M&S Asphalt Paving (66 D, up 2):** 3 conversions on $106 this week (two estimate forms, one call). Paving - Orlando Metro and Sealcoating & Repairs - Volusia are paused and the Volusia budget reads $39 a day; neither change appears in change history, so confirm they were intended. "driveway paving companies" phrase: $160, 2 conversions, bid $11 (down from $17.60). Terms clean apart from "christian brothers asphalt" $17, "cost to resurface driveway" $19, "driveway installation cost" $10, "sealmaster orlando" $5. One RSA in every group. The two call actions are still typed SUBMIT_LEAD_FORM.
- **Affordable Critter Solutions (75 C, down 1):** 12 conversions at $24 in 30 days, flat week. The only leak is government animal-control queries: "orlando animal control phone number" $10, "24 hour animal control orange county" $12, "animal control orange county number" $3, "mole animal control" $3; add phrase negatives "phone number", "orange county animal", "county animal control", "24 hour". "animal control longwood fl" converted, so do not block "animal control" itself. Tracking cleanup from Sep 28 (UA goal and smart-campaign actions primary) still open. $10 a day loses 26 percent to budget at a $24 CPA; $15 remains a fair ask.
- **All Phase Jacksonville:** LSA paused Sep 24 ($31 spent that day). The "Orlando" search campaign is still ENABLED and NOT_ELIGIBLE (worklist item 6).
- **Jupiter Boat Supply, REK Marketing:** paused, zero spend, nothing to do.

Out of scope, for the record only: Straightline Fence LSA $2,346 in 30 days for 18 leads at $130 ($1,476 this week, 11 leads); All Phase Orlando LSA has a $71.43 budget since Sep 28 and no spend recorded yet; the unnamed 163-445-9282 is Color Masters' LSA shell (colormasters88@gmail.com raised its LSA budget to $35.71 on Oct 3, Tom edited its criteria this morning); Byers Fence and the eight LSA-only accounts were not pulled.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Patio Style (deep dive 1 items 2 and 3), Scootz (scooterbug, how much, cost, price), Rover (deep dive 3 item 2, after attaching the master list), Progetto (tension; bamboo if not sold), All Phase (leslie, thompson pools, deland, cleaners, coatings, after re-attaching the master list), Color Masters (glidden, idea, how much, cost, colors, color, furniture, room, reviews, faux, touch up, j&b, jesus gil, axis), Precision GPR (gprs, sunshine, miss utility, 1800 dig, dig alert, julie, rebar, finder, geoslice, price, pricing), Florida Sealcoating (the 23 tokens in its one-liner plus "sealcoat florida" phrase in Branded), Quality Paralegal (melbourne, rockledge, polk, new smyrna, lake county, notario, notarios, notaria, public defender, fathers rights), Aqua Coat (pentair, aqua pools, pcs pools, handrail, equipment, products, installers, grout, ladder, fountain, tech support, after attaching the master list), Counseling Group (titusville; gottman pending Clark), Affordable Critter (phone number, orange county animal, county animal control, 24 hour), Filutowski (the 50 absent tokens above plus dr root, sakowitz, envision, fisher eye, eye avenue, vision source).

New keywords to add: Aqua Coat phrase "fiberglass pool repair" (2 conversions on $29, third report running); Rover exact "where to cremate a dog" (1 on $12) and "put dog down at home" (1 on $9); Patio Style exact "patio furniture clermont" is already there and converting (3 on $8), add exact "patio furniture altamonte springs" (2 on $10); Florida Sealcoating exact "asphalt sealcoating companies near me" (1 on $28) and "driveway sealing cost near me" (1 on $37); Quality Paralegal phrase "paralegal services near me" and Spanish "abogados de divorcio en orlando" converted (1 on $8); Progetto phrase "window covering company" variants with "san diego"; Color Masters exact "painters port orange" already present, add "painters ormond beach" exact and "house painters daytona beach" phrase.

Bid and budget adjustments: Patio Style revert Pergolas $5 to $2 and Brand $6 to $10; Rover In-Home back to $30 or raise bids; All Phase target CPA $40 back on or Manual CPC $4 to $5; Progetto ceilings $7 to $4; Color Masters ceiling $11 to $7; Florida Sealcoating Branded exact-only or target CPA restored, and confirm $125 a day against the $3,000 plan; Precision GPR cap GPR Scanning at $10 and pause Location and DSA; Filutowski Brand Awareness $455 to $200 and Branded $50 to $100 (if engaged); Aqua Coat $15 to $20 and Affordable Critter $10 to $15 (client asks).

Competitive read (rank-lost share as the proxy): Progetto loses 55 to 85 percent to rank on every campaign and the QS 1 to 3 floor is the cause; Rover holds 46 to 100 percent absolute top at manual bids and is not being outbid; All Phase swung from 86 percent rank-lost to 53 percent budget-lost in one week by paying double, which is the no-target strategy talking, not the auction; Filutowski's catch-all loses to budget (80 percent), not rank (7 percent), so more budget there would just buy more competitor-name clicks.

## Prioritized weekly action plan

1. **Critical, Tom today: Patio Style directions.** Set the GA4 get_directions import back to primary and included, retype the two Sep 29 actions, revert the Oct 1 Pergolas bid raise, remove "patio styles" phrase from Brand. Third week without the client's primary conversion counted.
2. **Critical, REK: Scootz.** Five weeks without an edit. Manual form test, restore GA4 form_submit, four phrase negatives, then the split.
3. **Critical, Tom: Filutowski scope.** Fourth report. Either REK is engaged and the Sep 14 list goes to Accalia, or the routine records the account as excluded from here on.
4. **High, REK (one click each): attach the master negative lists.** Rover (to In-Home and Pet Cremation), Aqua Coat (to the live campaign), All Phase (recreate the REMOVED link). Three accounts, same fault, about $225 a month of visible waste between them.
5. **High, REK: Florida Sealcoating.** Branded to exact only or target CPA back on; the 23 competitor and supplier negatives plus "sealcoat florida" in Branded; confirm the $125 a day with Tom.
6. **High, REK: Rover.** After item 4, the lap of love decision, pause "katie matzke", Pet Cremation keyword cuts, POOR RSA. Decide what the $50 In-Home budget is for.
7. **High, REK: Progetto.** Pause the QS 1 to 3 zero-conversion exact product terms, ceilings back to $4, second RSAs. Then rotation moves it to a monthly check.
8. **Medium, REK: All Phase.** Brand into its own campaign, target CPA back on the non-brand campaign, phrase-match the top terms.
9. **Medium, Tom: Color Masters.** The 14 research negatives, ceiling $11 to $7, second RSAs, and a decision on a service-area landing page.
10. **Medium, REK: The Counseling Group.** Tel-tap manual test (54 days), pause "help with depression" and "stress therapy", replace the POOR Depression RSA. Two zero weeks make this urgent for a $25 a day account.
11. **Medium, REK: Precision GPR.** The negative list and the Location and DSA pauses; the account is improving without them and would improve more with them.
12. **Low:** Quality Paralegal second RSAs and location negatives; M&S confirm the pauses and the $39 budget; Affordable Critter tracking cleanup and county-animal-control negatives; All Phase Jacksonville pause the Orlando campaign; Aqua Coat pause Pool Equipment and add "fiberglass pool repair".

## Rotation

Deep-dived this run: Patio Style, Scootz, Rover Veterinary Care, Progetto Shades, All Phase Pool Remodeling. Due next Monday (Oct 12): The Counseling Group (two zero weeks, and October per the Sep 4 note), Florida Sealcoating (Branded regression and the budget question), Quality Paralegal Services and Color Masters (both past 30 days by then), Precision GPR (measure whether the improvement holds). The week after: Aqua Coat, Affordable Critter Solutions, M&S Asphalt Paving, Filutowski if a scope decision has been made.

## Data notes

- Account discovery returned 30 client accounts, identical to the Sep 28 list. Compare next week against this run's list.
- The Sep 21 and Sep 28 reports exist only on their draft PR branches (claude/kind-wright-3dltju and claude/kind-wright-fz32l3); main still ends at the Sep 14 report. Deltas here are against the Sep 28 branch file. Merging those two PRs would keep the history in one place.
- tools/gaql.py on main still defaults to API v22, which the installed google-ads library (33.0.0) no longer ships; this run set GOOGLE_ADS_API_VERSION=v25. The Sep 28 branch carries the one-line default change.
- The recommendation and campaign_asset queries in this run's first pass used field names the v25 API rejected; both were re-run with corrected fields. Recommendation types are reported from the corrected pull. The ad_group_asset query failed on a missing campaign.status select and was not re-run; ad-group-level assets are unavailable this run.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor. The Filutowski strict floor counts only named practices, doctors and street addresses, retail optical chains, insurers and Spanish queries; generic eye-care searches ($922) and LASIK or cataract intent ($162) are excluded from it.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Sep 6 (the API allows 30 days). Conversion action edits, campaign pauses applied by some automated paths, and budget edits made through certain tools do not always appear; the M&S pauses and $39 budget and the Patio Style directions demotion are examples in this report.
- Weekly conversion-by-action tables use Google's Monday-start weeks. Conversion data for Oct 4 may still be incomplete at run time (Progetto's conversion-by-action rows ended Oct 3 while the campaign table already showed Oct 4).
- Week-over-week for Florida Sealcoating includes the display remarketing campaign ($35 this week, 1 conversion); search-only spend was $663 last week and $887 this week.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
