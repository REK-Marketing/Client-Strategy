# PPC Weekly Audit - 2026-10-19 (Google Ads fleet)

Run: Monday Oct 19, 2026, scheduled cloud session through tools/gaql.py (API v25) against MCC 656-695-7229. Windows: 30 days Sep 19 to Oct 18; this week Oct 12 to Oct 18; last week Oct 5 to Oct 11. Score deltas are against the Sep 14 report, the last run on record (no reports exist for Sep 21, Sep 28, Oct 5 or Oct 12). Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Patio Style (14-point drop, on rotation), Rover Veterinary Care (worst REK-managed score), Progetto Shades (first scored run after the relaunch), Color Masters (new account). Rotation notes for Affordable Critter Solutions and Aqua Coat. One-liners for the rest.

The google-ads.yaml in the Drive folder dave-ads-setup (last modified Sep 8) authenticated on the first try. It was copied with mode 600, read only by the client library, and deleted before this report was written. The installed client library no longer ships API v22, so this run used v25 through the GOOGLE_ADS_API_VERSION override; tools/gaql.py was not changed.

## Attention items (read first)

1. **No account vanished from the MCC since Sep 14.** All 26 accounts from that run are still linked. Five accounts are new under the MCC: Color Masters (426-092-9847, search, REK-built Sep 21), Color Masters LSA (163-445-9282), Quality Paralegal Services (447-153-2607, search, Tom active since Sep 21), MB Skin Care (179-731-0831, LSA only, Tom created Oct 5), and All Phase Pool Remodeling (Orlando LSA) (355-287-7099).
2. **Patio Style (596-555-8707) stopped counting its primary conversion on Sep 22.** Both directions actions, "Get directions (GTM) 11 Sep" and the GA4 get_directions import, are now secondary and excluded. The Sep 14 report flagged a double-count risk between the two; the fix applied set both to secondary instead of keeping one primary. Counted conversions fell from 21 a week (Sep 7 to 13) to 2 this week while directions taps continued at 8 to 14 a week in all_conversions. Score 66 to 52, the largest drop in the fleet. Deep dive 1.
3. **Rover Veterinary Care (750-667-5721) is converting less every week: 7, 4, 3, 2 over the last four weeks, CPA $33 to $236.** Two website actions, "Event|Contact|Calls From Website" and "Event|Contact|Form Submit", last recorded on Sep 15 and Sep 17 and have been zero since, while "Click to call (on website)" and "Book appointment" still fire. The manual trigger test asked for on Sep 14 is still due. Deep dive 2.
4. **Progetto Shades (416-010-8247) has spent $846 in the last 14 days with zero primary conversions**, $2,054 in 30 days for 8. 32 of its 105 keywords sit at Quality Score 1 to 3 and every ad group has a single RSA. Deep dive 3.
5. **Color Masters (426-092-9847), REK-built Sep 21, is at $1,435 for 3 conversions ($478 CPA)** on a Maximize Clicks campaign with an $11 CPC ceiling, and this week spent $425 for none. Deep dive 4.
6. **Filutowski Eye Institute (192-870-7876) is still unresolved on scope.** $19,381 in 30 days, 243 conversions at $80 (Sep 14 window: 354 at $49). The only editor in change history is catie@accaliamarketing.com (Oct 15: ad schedules and target CPA edits on four campaigns). No REK user has touched it. The broad keyword "lasik treatment cost" spent $13,409, 83 percent budget-lost at $455 a day, and $6,493 of its visible search-term cost produced no conversion. Enhanced conversions for leads is still on for a medical practice. Still scored 44 F, still excluded from the action plan until Tom says whether REK is engaged.
7. **Straightline Fence And Supply (550-094-8786) no longer has a search campaign.** Only the Local Services campaign remains in the account ($3,984 and 29 leads in 30 days, out of scope). The COMPROMISED_SITE search campaign from Sep 14 is gone from the campaign list. Straightline is now LSA-only and is excluded from scoring from this run on.
8. **M&S Asphalt Paving (827-724-4095) restarted.** Tom relaunched "Paving - Volusia" on Sep 24 at $31 a day, Manual CPC. $477 in 30 days, 5 conversions, $95 CPA; this week $155 for 0. Scored provisionally.
9. **Recommendations auto-apply removed a keyword at Scootz on Oct 8** (user "Recommendations Auto-Apply"). Check the auto-apply settings in that account; nothing else in the fleet shows that user.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 31 client accounts, 1 manager | 13 REK-managed + Filutowski (provisional) | Excluded: Byers Fence x2, Herrell Plumbing, 11 LSA-only accounts (incl. Straightline, MB Skin Care, Color Masters LSA, All Phase Orlando LSA). Not scorable: All Phase Jacksonville, Jupiter Boat Supply, REK Marketing (zero search spend). |

Search, Performance Max and display spend in the 30-day window: $18,228 across the 13 REK-managed scored accounts, plus $19,381 at Filutowski Eye Institute. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $19,381 | 243 | $80 | 44 | F | +2 | Critical (scope) | "lasik treatment cost" broad $13,409; $4,191 on other clinics, $1,667 on retail optical, $278 on insurers; enhanced conversions on | $6,285 |
| 2 | Progetto Shades | 416-010-8247 | $2,054 | 8 | $257 | 50 | F | new | Critical | 0 conversions in 14 days on $846; 32 keywords at QS 1 to 3; every group one RSA; Maximize Clicks everywhere | $85 |
| 3 | Patio Style | 596-555-8707 | $2,000 | 27 | $74 | 52 | F | -14 | Critical | Directions, the client's primary conversion, set secondary Sep 22; 13 of 14 groups one RSA; Pergolas 67% budget-lost | $65 |
| 4 | Color Masters | 426-092-9847 | $1,435 | 3 | $478 | 54 | F | new | Critical | $425 this week for 0; DIY, cost and paint-brand queries $200; Max Clicks paying $10.15 a click under an $11 ceiling | $200 |
| 5 | Rover Veterinary Care | 750-667-5721 | $1,531 | 17 | $90 | 55 | F | -6 | Critical | Two web actions silent since Sep 17; weekly conversions 7, 4, 3, 2; "lap of love" leaking $116 into In-Home Pet Euthanasia | $160 |
| 6 | Quality Paralegal Services | 447-153-2607 | $1,358 | 61 | $22 | 56 | F | new | Needs attention | Strong CPA, weak build: "family law attorney near me" broad QS 1 $261, one ad disapproved for unclear relevance, POOR RSA, 84% broad | $45 |
| 7 | Precision GPR | 554-113-4760 | $2,567 | 24 | $107 | 57 | F | +7 | Needs attention | Better month (24 conv vs 9) but 2 this week on $713; Location campaign woke up after its tCPA was removed Oct 10 ($112, $22 CPC); "gprs" still not a negative | $290 |
| 8 | Florida Sealcoating | 168-852-7101 | $3,176 | 26 | $122 | 60 | D | -3 | Needs attention | Spend on plan; 4 conversions this week on $847; Branded campaign paying $10.89 CPC on its own name; competitor and supplier queries still matching | $226 |
| 9 | M&S Asphalt Paving | 827-724-4095 | $477 | 5 | $95 | 62 | D | relaunch | Needs attention | Restarted Sep 24; 0 conversions this week on $155; 8 keywords at QS 3; 5 of 6 groups one RSA | $45 |
| 10 | Scootz | 185-574-5478 | $1,466 | 38 | $39 | 64 | D | +6 | Needs attention | Moved to Maximize Conversions Oct 6: CPC $0.70 to $2.50, clicks -72%, conversions 10 to 7; form_submit still secondary and silent | $30 |
| 11 | The Counseling Group | 657-069-3617 | $555 | 2 | $278 | 66 | D | 0 | Needs attention | Spend on plan; tel-tap tag now registers (2 taps since Oct 13) but they show only in all_conversions; 0 primary conversions this week | $50 |
| 12 | All Phase Pool Remodeling | 103-111-7688 | $864 | 13 | $66 | 67 | D | -5 | Needs attention | "Contact Form" is primary but excluded from Conversions (5 uncounted); brand term 42% of spend inside non-brand groups; master negatives still on the paused campaign | $40 |
| 13 | Aqua Coat Pool Plastering | 285-714-0527 | $451 | 13 | $35 | 67 | D | +3 | On target | Steady at $35 CPA; master negative list still attached only to the paused campaign; Pool Equipment group still live | $60 |
| 14 | Affordable Critter Solutions | 227-108-4521 | $293 | 18 | $16 | 77 | C | +1 | On target | Clean; $10/day losing 24% to budget at a $16 CPA | none confirmed |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | no search spend | n/a | Paused (search) | Tom paused the Jacksonville LSA campaign Sep 24. The "Orlando" search campaign is still ENABLED but NOT_ELIGIBLE (ad groups paused), spent nothing | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | LSA only | n/a | Excluded | Search campaign removed; LSA $3,984, 29 leads in 30 days | n/a |
| none | Jupiter Boat Supply, REK Marketing | | $0 | 0 | n/a | n/a | paused | n/a | Paused | No campaigns serving, no changes | n/a |

## Week over week (Oct 12 to 18 against Oct 5 to 11, search, PMax and display only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $5,171 to $4,489 (-13%) | 389 to 366 | 6.1% to 6.9% | $13.29 to $12.26 | 51.7 to 57 | $100 to $79 | Accalia added ad schedules Oct 15; Branded 21.7 to 26 conv |
| Florida Sealcoating | $700 to $847 (+21%) | 111 to 92 | 7.4% to 6.9% | $6.31 to $9.20 | 10 to 4 | $70 to $212 | Off target this week; Commercial $210 to $433 for 4 to 2 |
| Precision GPR | $606 to $713 (+18%) | 50 to 48 | 6.4% to 7.1% | $12.12 to $14.86 | 7 to 2 | $87 to $357 | Off target; Location campaign $0 to $112 |
| Rover Veterinary Care | $527 to $471 (-11%) | 67 to 63 | 10.1% to 10.0% | $7.86 to $7.48 | 3 to 2 | $176 to $236 | Off target, fourth weekly decline |
| Patio Style | $489 to $461 (-6%) | 200 to 213 | 7.3% to 6.9% | $2.45 to $2.16 | 4 to 2 | $122 to $230 | Counted conversions exclude directions since Sep 22; directions taps 13 to 14 |
| Progetto Shades | $406 to $439 (+8%) | 100 to 117 | 5.1% to 7.1% | $4.06 to $3.75 | 0 to 0 | none | Off target, second zero week |
| Color Masters | $230 to $425 (+85%) | 23 to 41 | 4.5% to 6.1% | $9.98 to $10.36 | 2 to 0 | $115 to none | Off target |
| Quality Paralegal Services | $286 to $358 (+25%) | 110 to 122 | 2.5% to 3.1% | $2.60 to $2.93 | 15 to 13 | $19 to $28 | On target; Immigration campaign started serving ($19) |
| Scootz | $354 to $335 (-5%) | 209 to 134 | 7.3% to 7.6% | $1.69 to $2.50 | 10 to 7 | $35 to $48 | Learning after the Oct 6 strategy change |
| All Phase Pool Remodeling | $220 to $211 (-4%) | 29 to 35 | 4.5% to 5.4% | $7.59 to $6.04 | 2 to 3 | $110 to $70 | Flat |
| M&S Asphalt Paving | $62 to $155 (+150%) | 6 to 14 | 4.2% to 8.0% | $10.33 to $11.08 | 2 to 0 | $31 to none | Small numbers, relaunch |
| Aqua Coat | $95 to $121 (+28%) | 18 to 22 | 2.9% to 4.7% | $5.25 to $5.49 | 3 to 3 | $32 to $40 | Flat |
| The Counseling Group | $183 to $117 (-36%) | 44 to 28 | 5.4% to 5.5% | $4.16 to $4.16 | 2 to 0 | $91 to none | Small numbers; 1 tel tap in all_conversions |
| Affordable Critter Solutions | $77 to $69 (-10%) | 25 to 18 | 14.9% to 7.8% | $3.09 to $3.85 | 6 to 5 | $13 to $14 | Flat |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss in 30 days: Progetto Drapery 82%, Progetto Shades & Blinds 61%, Affordable Critter 65%, Patio Style Outdoor Furniture 60%, All Phase 49%, Precision GPR DSA 42%. Highest CPC increases this week: Scootz ($1.69 to $2.50, strategy change), Florida Sealcoating ($6.31 to $9.20), Precision GPR ($12.12 to $14.86). Filutowski's LASIK keyword CPC is $20.53 for the window, up from $16.67 in the Sep 14 window.

## Changes made in the past five weeks (Sep 20 to Oct 19) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Patio Style | Sep 22 | not visible (conversion action edits are not in change history) | Both directions actions set secondary and excluded | Counted conversions 21/wk to 2/wk. Directions taps unchanged at 8 to 14/wk. See deep dive 1 |
| Patio Style | Sep 22 to Oct 16 | paidads@rekmarketing.com | 312 changes: 17 new ads Sep 25, new Patio Covers & Cabanas #2 and New Pergolas 07 Oct groups, New Outdoor Kitchens 14 Oct group, budgets shuffled twice (Pergolas $12 to $18 to $14, Kitchens $16 to $10 to $14, Brand $6 to $10), pergola group CPC $5 to $10 to $5, 83 Brand campaign negatives Oct 14 plus 29 Oct 16, groups paused and re-enabled Oct 9 and 13 | Brand campaign now holds generic queries out ("outdoor furniture" $41/0 still matched before the negatives). New Pergolas 07 Oct RSA is POOR. 13 of 14 groups still one RSA |
| Scootz | Oct 6 | Tom | Campaign updated (now Maximize Conversions, was Maximize Clicks), 7 ad-schedule rows added, 2 criteria updated | CPC $0.70 to $1.69 to $2.50; clicks 483 to 209 to 134; counted conversions 5, 10, 7. Two weeks is too little; the counted set (Booqable purchases plus calls) is about 9 a week |
| Scootz | Oct 8 | Recommendations Auto-Apply | One keyword removed | Auto-apply is on. See attention item 9 |
| Rover | Oct 2 | Tom | In-Home Pet Euthanasia budget $30 to $50 | Campaign spent $353 in 30 days, 0% budget-lost; the extra budget is not being used |
| Rover | Oct 3 | sheokand003@gmail.com | Pet Cremation Services: enhanced CPC turned off; campaign now Manual CPC (was Maximize Conversions on Sep 14) | $760 in 30 days, 5 conv, 40% rank-lost, 0% budget-lost. Its weekly conversions 1 to 2 |
| Rover | Oct 6 | sheokand003@gmail.com | Competitors budget $5 to $20; 8 keyword edits | Competitors $272 in two weeks, 0 conversions |
| Precision GPR | Sep 22 and Oct 10 | sheokand003@gmail.com | 14 keywords added, 5 removed, ads edited; target CPA ($14) removed from LP Search - Location Oct 10 | Location went from $0 (last week) to $112 this week at $22.37 CPC, 1 conversion. The Sep 4 list said pause Location |
| Florida Sealcoating | Sep 22 | sheokand003@gmail.com | 31 keywords added, 16 removed; Residential budget $30 to $40, Branded $30 to $35 | 30d budgets total $105/day, on the $3,000 plan |
| Florida Sealcoating | Oct 6 | sheokand003@gmail.com | Branded budget $35 to $20 | Branded still spent $171 this week at $10.71 CPC |
| Florida Sealcoating | Oct 10 | sheokand003@gmail.com | 9 keyword edits, 4 ad edits, 2 keywords added | Too early |
| All Phase | Sep 25 | sheokand003@gmail.com | Target CPA set on the campaign | Weekly conversions 3, 5, 2, 3 since. Flat |
| Aqua Coat | Oct 1 and 10 | sheokand003@gmail.com | 1 keyword swapped, 2 added, ads edited; 20 assets added across the window | Flat at $35 CPA |
| The Counseling Group | Sep 21 | Tom | 34 campaign negatives added | Visible waste this window $50. Nothing else changed since |
| Color Masters | Sep 21 to Oct 15 | Tom | Account built: CPC ceiling set Sep 21 and 24, budget Sep 24, 18 campaign negatives removed Oct 2, Commercial Painting paused Oct 12 | 3 conversions on $1,435. See deep dive 4 |
| Quality Paralegal | Sep 21 to Oct 19 | Tom | 257 changes: budgets, 12 assets, 106 campaign negatives (Oct 15, 16, 19), Immigration campaign launched | 61 conversions at $22 in 30 days |
| M&S Asphalt | Sep 24 and Oct 15 | Tom | Campaigns re-enabled, budgets changed, 1 keyword added | Relaunch; 5 conversions in 30 days |
| Progetto Shades | Sep 25, Oct 6, 15, 19 | Tom | 48 keywords added (31 of them today), 4 campaign criteria updated Oct 6 | No bidding or budget change; two zero weeks. See deep dive 3 |
| Filutowski | Oct 15 | catie@accaliamarketing.com | Ad schedules on four campaigns, target CPA changes on Cataracts (3 edits), Eye Surgery, Branded; 1 ad edit | Branded 21.7 to 26 conv this week; LASIK campaign $3,619 to $2,991 |
| Straightline | Sep 22 to Oct 15 | Robbie, joe611904@yahoo.com, Tom | LSA campaign assets and criteria only | Search campaign no longer exists |
| All Phase Jacksonville | Sep 24 | Tom | Jacksonville LSA campaign paused | Account now spends nothing |
| Affordable Critter | Sep 25, Oct 10 | sheokand003@gmail.com | 2 keywords added, 10 keyword edits, 1 ad edit | Flat at $16 CPA |

### Sep 14 attention items, where they stand

- Premium Walk-In Clinic and Premium Medication Refills: both still absent, both expected (Known account context).
- Filutowski scope: still open (attention item 6).
- Straightline COMPROMISED_SITE: the search campaign was removed rather than appealed. Account is LSA-only now.
- Scootz form_submit: still secondary and still silent (zero in all_conversions since Aug 16). Booqable Purchases is carrying the account (25 of 38 conversions).
- Rover zero-conversion week: conversions came back Sep 21 to 27 (7), then declined every week. Two web actions have been silent since mid-September (deep dive 2).

## Deep dive 1: Patio Style (596-555-8707), score 52 F, down 14

Context applied: the client's primary conversion is Get Directions to the showroom, then calls, then contact submissions. Directions counted as primary is intended.

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 60 |
| Account Structure | 65 |
| Keywords & Targeting | 55 |
| Ads & Assets | 40 |
| Bidding & Settings | 55 |

| Campaign | Bidding | Budget/day | Spend | Clicks | CPC | Counted conv | All conv | Search IS | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|---|
| PS / Search / Outdoor Furniture | Maximize Clicks | $30 | $906 | 643 | $1.41 | 20 | 600 | 15% | 25% | 60% |
| PS / Search / Outdoor Kitchens | Maximize Clicks | $14 | $424 | 110 | $3.86 | 3 | 25 | 27% | 25% | 47% |
| PS / Search / Pergolas & Louvered Roofs | Manual CPC | $10 | $423 | 45 | $9.39 | 1 | 9 | 15% | 67% | 18% |
| PS / Search / Brand | Target Impression Share | $10 | $248 | 77 | $3.22 | 3 | 10 | 12% | 59% | 28% |

### Findings

**The primary conversion is no longer counted.** On Sep 21 "Get directions (GTM) 11 Sep" counted 4 primary conversions; from Sep 22 it counts 0 while recording 1 to 5 taps a day in all_conversions. The GA4 get_directions import had already been secondary since Sep 18. Today both are primary false, included false. The remaining primary set is Calls from ads (8 in 30 days), Website Call Conversions (4) and Thank you page (3), plus a "Phone Call Click 29/ Sep" and "Send a messages landing page 29 Sep" pair created Sep 29 that are categorised GET_DIRECTIONS and have recorded nothing. Directions in the window: 50 GTM taps and 46 GA4 taps, mostly the same taps. The Sep 14 risk was that both counted; the state now is that neither does. Keep one (GTM, since it fires on the tap rather than through an import) as primary and included, leave the GA4 import secondary. Nothing in the account bids on conversions today (Maximize Clicks, Manual CPC, Target Impression Share), so this is a reporting and decision problem rather than a bidding one, but every CPA in this report for Patio Style is wrong until it is fixed.

**Ads.** 13 of 14 enabled ad groups carry one RSA. "New Pergolas 07 Oct" is POOR, "Premium Brands" AVERAGE. Google lists 5 RSA recommendations and one ad-strength recommendation.

**Keywords and waste.** 9 keywords at QS 1 to 3: "patio cover orlando" QS 3 ($108, 0 conversions, below-average expected CTR and ad relevance), "outdoor grill island" QS 3 ($59), "outdoor dining set" QS 2, "retractable pergola" QS 1 (new, no spend yet), "woodard outdoor furniture" QS 2. Pergola queries that will not convert for a furniture showroom: "pergola carport attached to house" $12, "show me a pergola" $12, "pergolas for sale" $11, "insulated porch roof panels" $8, "insulated pan roof" $8, "patio screen enclosures orlando" $8, "orlando pergolas and decks" $15. Brand campaign before the Oct 14 negatives: "outdoor furniture" $41 and "outdoor furniture stores near me" $13 (those now carry 25 directions taps each in all_conversions, so they were not wasted, just mis-filed). Confirmed irrelevant: about $65.

**Bidding and budget.** Pergolas & Louvered Roofs is Manual CPC at $10 a day and loses 67 percent of impressions to budget at a $9.39 CPC; it had its budget moved $12 to $18 to $14 and its bid $5 to $10 to $5 within a week. Outdoor Furniture is the volume engine: 643 clicks at $1.41 and 600 all-conversions (77 directions, 346 "other engagements", 73 website visits). Brand is Target Impression Share with 59 percent lost to budget at $10 a day.

### Prepared change list

1. Set "Get directions (GTM) 11 Sep" back to primary and included. Keep the GA4 get_directions import secondary. Delete or rename the two Sep 29 actions categorised GET_DIRECTIONS that are really a phone click and a message page, or set their categories correctly, so the goal grouping is readable.
2. Second RSA in the top five single-RSA groups by spend: Patio Furniture - Local, Outdoor Kitchens, Louvered Pergolas, Patio Covers & Cabanas, Brand. Rewrite New Pergolas 07 Oct (POOR).
3. Negatives, phrase, in Master Negatives: carport, insulated, roof panels, pan roof, screen enclosure, for sale, show me, ideas, decks. Dedupe: none present today (Master Negatives has 57 members; the Brand campaign's 116 are campaign-level and do not protect Pergolas or Kitchens).
4. Leave Pergolas budget and bid alone for two weeks so the Oct 13 settings ($14 a day, $5 group CPC) can be read.
5. After item 1 has two weeks of counted directions, move Outdoor Furniture to Maximize Conversions; it will see roughly 80 directions a month, enough to learn on.

## Deep dive 2: Rover Veterinary Care (750-667-5721), score 55 F, down 6

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 50 |
| Account Structure | 60 |
| Keywords & Targeting | 55 |
| Ads & Assets | 55 |
| Bidding & Settings | 55 |

| Campaign | Bidding | Budget/day | Spend | Clicks | CPC | Conv | CPA | This week |
|---|---|---|---|---|---|---|---|---|
| Pet Cremation Services | Manual CPC | $30 | $760 | 150 | $5.07 | 5 | $152 | $224, 2 conv |
| Competitors | Maximize Conversions | $20 | $354 | 51 | $6.94 | 3 | $118 | $141, 0 conv |
| In-Home Pet Euthanasia | Maximize Conversions | $50 | $353 | 49 | $7.20 | 6 | $59 | $104, 0 conv |
| Brand Campaign | Maximize Conversions | $10 | $64 | 17 | $3.77 | 3 | $21 | $2, 0 conv |

30 days: $1,531, 17 primary conversions (Book appointment 9, Click to call on website 8), $90 per conversion. Weekly conversions since Sep 21: 7, 4, 3, 2. Weekly CPA: $33, $60, $176, $236.

### Findings

- **Two primary website actions have been silent for a month.** "Event|Contact|Calls From Website" last fired Sep 15, "Event|Contact|Form Submit" Sep 17. Both are WEBSITE origin, one-per-click. "Click to call (on website)" (CALL_FROM_ADS origin) and "Book appointment" keep firing, so the site is reachable and clicks are happening; the GTM or GA4 events behind the two silent actions are the suspects. Not declared dead: trigger both manually this week. "Calls from ads" (call asset) has also recorded 0 in 30 days, which usually means the call asset is missing or its conversion is detached.
- **"lap of love" is leaking into the wrong campaign.** The exact keyword in Competitors spent $105 for 0 conversions (QS 3, below-average expected CTR; on Sep 14 it was 6 conversions on $271). The same queries, "lap of love" $53, "lap of love near me" $41, "laps of love" $22, "lapoflove near me" $8, "laps of love near me" $7, matched In-Home Pet Euthanasia through phrase keywords: $131 for 0 conversions outside the campaign built for them.
- **Cremation is the biggest spender and the weakest converter.** "pet cremation services" phrase $380 for 2; 15 cremation keywords with $10 or more and 0 conversions ($140); pet cemetery $27, "pet aquamation services near me" $8, "pet angel(s) cremation" $16, distant cities (naples $7, fort lauderdale $8, boca raton $7) $22. The campaign is Manual CPC since Oct 3, loses 40 percent to rank and nothing to budget.
- **Two $27 to $29 clicks.** "mobile dog put down service" phrase $58 on 2 clicks and "euthanasia dogs near me" phrase $54 on 2 clicks, both in Dog Euthanasia, both 0 conversions. In-Home Pet Euthanasia had its budget raised to $50 on Oct 2 and uses $12 a day of it.
- **Question searches**: "when to put your dog down quiz" $26, plus the "when to", "signs", "quality of life" family flagged Sep 14 (still not negatives).
- **Ads**: both Competitors RSAs still POOR and AVERAGE (Sep 14 item 16 still open). Cat Euthanasia and In-Home Pet Euthanasia groups still one RSA.
- Enhanced conversions for leads: off. Fine.

### Prepared change list

1. Manual trigger test today: website call button, contact form, and the call asset. Fix the GTM/GA4 events or re-import before any bid change.
2. Negatives, phrase, in "Rover – Core Exclusions" (attached to all four live campaigns) except where noted: when to, signs, quality of life, should i, quiz, aquamation, pet angel, pet angels, paws to health, naples, fort lauderdale, boca raton. Campaign-level phrase negatives "lap of love", "laps of love", "lapoflove" in In-Home Pet Euthanasia and Pet Cremation Services only (keep bidding on it in Competitors). Dedupe: pet cemetery, gentle pet crossing, monarch, peggy adams, stuart and boynton are already in Account Negatives - Master and are dropped from this list.
3. Pause "mobile dog put down service" and "euthanasia dogs near me" phrase, or cap the Dog Euthanasia group at a $10 CPC.
4. Pet Cremation: pause the 15 zero-conversion keywords ($140) and leave "pet cremation services", "pet cremation palm beach", "pet memorial services", "pet cremation" (the ones that converted).
5. Rebuild the two Competitors RSAs; second RSA in Cat Euthanasia and In-Home Pet Euthanasia.
6. Bidding: either return In-Home Pet Euthanasia to $30 a day (it does not use $50) or move the Competitors budget into it. Competitors at $20 a day has 0 conversions in two weeks.

## Deep dive 3: Progetto Shades (416-010-8247), score 50 F, first scored run

Context: Tom rebuilt the account Sep 8 to 10 (six search campaigns). 30 days: $2,054, 452 clicks, $4.54 CPC, 8 primary conversions (Contact 7, Calls from ads 1), $257 per conversion. Last primary conversion Oct 3.

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 45 |
| Account Structure | 70 |
| Keywords & Targeting | 35 |
| Ads & Assets | 45 |
| Bidding & Settings | 50 |

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | Search IS | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|
| Shades & Blinds | $25 | $919 | 208 | $4.42 | 3 | 15% | 24% | 61% |
| Shutters | $12 | $387 | 62 | $6.24 | 2 | 35% | 10% | 55% |
| Motorized & Smart | $10 | $370 | 70 | $5.29 | 1 | 24% | 23% | 53% |
| Exterior & Patio | $7 | $227 | 69 | $3.29 | 1 | 22% | 20% | 58% |
| Drapery & Curtains | $6 | $139 | 36 | $3.87 | 0 | 16% | 2% | 82% |
| Brand | $5 | $12 | 7 | $1.75 | 1 | 73% | 9% | 18% |

### Findings

- **Quality Score is the account's problem.** 32 of 105 enabled keywords sit at QS 1 to 3, and they carry about $900 of the $2,050: "window shutters" exact QS 3 $142/0, "outdoor patio shades" phrase QS 2 $140/0, "interior shutters" exact QS 3 $86/0, "hunter douglas" phrase QS 3 $65/1, "window shades" exact QS 3 $51/0, "automated shades" exact QS 3 $48/0, "roller shades" exact QS 2 $42/0, "smart shades" QS 3 $34/0, "blackout curtains" QS 1, "faux wood blinds" QS 1, "vertical blinds" QS 1. Landing page experience is BELOW AVERAGE on almost all of them and expected CTR is below average on all of them. Rank-lost share is 53 to 82 percent in every non-brand campaign, which is the same finding from the other side: the ads are not winning auctions at these bids because quality is low, not because budgets are small.
- **Zero-conversion keywords**: 27 with $10 or more, $1,089, more than half the account. The two biggest spenders, "window covering company" phrase ($319, 1 conversion) and "smart home shades" phrase ($256, 1 conversion), have no Quality Score reported yet.
- **Conversion tracking is thin.** "Call ((858) 338-1678)" (website call) is primary but excluded from the Conversions column and has never fired; "Lead form website" is secondary and recorded 3; "Financing inquiry" and "Web form (start)" are zero. Only "Contact" (7) and the call asset (1) count. Confirm the website call action and the lead form are meant to be excluded; if not, include them and the account has 11 conversions, not 8.
- **Ads**: every one of the nine groups has one RSA; Drapery, Shades, Window Treatments and Plantation Shutters are AVERAGE.
- **Waste**: the big negative list (330 members) is doing its job; visible irrelevant spend is small: "bamboo window shades" $18, "motorized tension blinds" $14, "patio shade cover" $11, "shutters for house" $13, "electric blinds for windows" $17 (on-topic but DIY-shaped). About $85.
- **Bidding**: Maximize Clicks on all six campaigns with CPC ceilings of $7 (Shutters, Shades & Blinds, Motorized & Smart), $4 (Drapery, Exterior & Patio) and $2 (Brand). Average CPCs are under the ceilings, so the ceilings are not what limits the account. 8 conversions in 30 days; Maximize Conversions is not available yet.

### Prepared change list

1. Landing pages first: map each ad group to a page that matches the keyword (shutters to the shutters page, motorized to the motorized page, exterior to the exterior page). The QS detail says landing page BELOW AVERAGE on the shutters, shades, motorized and drapery groups, which usually means one generic page.
2. Second RSA in every group, written against the group's keyword, and raise the four AVERAGE ads.
3. Pause the QS 1 keywords (blackout curtains, faux wood blinds, vertical blinds, retractable pergola) and the QS 2 ones that spent without converting (outdoor patio shades, roller shades).
4. Negatives, phrase, in iLP - Global Negatives: bamboo, tension, drapes, hunter douglas and norman only if the client does not sell those lines (they have a Designer Brands group, so confirm first). Dedupe: amazon, home depot, lowes, ikea, diy, cheap, budget blinds, 3 day blinds, sail, carport, jobs, repair are already present and are dropped.
5. Leave the ceilings where they are during the QS rebuild (lowering them would cut the already low impression share), and revisit bidding when the account has 15 counted conversions in a month.

## Deep dive 4: Color Masters (426-092-9847), score 54 F, new account

Context: REK-built, Tom's edits from Sep 21. Port Orange painter. 30 days: $1,435, 143 clicks, $10.03 CPC, 3 primary conversions (Call 2, Lead Form 1), $478 per conversion. This week $425, 41 clicks, 0 conversions.

| Category | Score |
|---|---|
| Conversion Tracking | 60 |
| Wasted Spend | 40 |
| Account Structure | 75 |
| Keywords & Targeting | 50 |
| Ads & Assets | 50 |
| Bidding & Settings | 50 |

| Campaign | Bidding | Budget/day | Spend | Clicks | CPC | Conv | Search IS | Lost to rank |
|---|---|---|---|---|---|---|---|---|
| REK / Search / Residential Painting | Maximize Clicks, $11 ceiling | $45 | $1,391 | 137 | $10.15 | 3 | 52% | 46% |
| REK / Search / Commercial Painting | Maximize Clicks (paused Oct 12) | $25 | $32 | 3 | $10.77 | 0 | | |
| REK / Search / Brand | Maximize Clicks | $8 | $12 | 3 | $3.88 | 0 | 79% | 17% |

### Findings

- **The CPC is within a dollar of the ceiling.** Average CPC $10.15 against an $11 ceiling means the campaign pays close to its maximum on most clicks and still loses 46 percent of impressions to rank. 20 keywords enabled, but only 8 have spent anything; 6 keywords are at QS 1 to 3 with no impressions ("painters near me" QS 2, "house painters near me" QS 1, "painting company near me" QS 3), and the spend is concentrated on three phrase keywords: "house painters" $179/1, "painting companies" $117/1, "painters port orange" $79/1.
- **Search terms are DIY, pricing and product.** Of $440 visible, $430 had no conversion. Cost questions: "how much does it cost to repaint your kitchen cabinets" $21, "how much does it cost to paint a door" $11, "cost to paint house exterior" $11, "cost of painting house exterior" $11, "labor cost to paint a 12x12 room" $11, "how much does it cost to get furniture painted" $11, "how much to paint exterior of house" $11, "kitchen cabinet refacing cost" $11. Ideas and products: "front door color idea" $21, "glidden premium interior" $20, "house exterior colors" $11, "colors to paint my kitchen cabinets" $11, "cabinet paint" $11, "exterior paint" $11. Competitors: "j&b painting plus of florida inc port orange reviews" $21, "all american painting company" $11. Wrong service: "equipment painters" $11, "commercial painters" $22 (the Commercial campaign, now paused). About $200 confirmed.
- **The negative list is close but phrase-shaped.** "REK | Painting Negatives" (92 members) has "how much does it cost to get house painted", "paint ideas", "color ideas", "paint colors", "colors to paint", "exterior colors", "sherwin", "behr", "diy", "refacing" as phrase negatives, so each new wording slips past. Tom also removed 18 campaign negatives on Oct 2.
- **Conversions**: the website call action and the lead form fire; "Calls from ads" is 0 in 30 days, so check that the call asset is attached to Residential Painting. The only converting visible term was "pool cage painting near me" $10.
- **Ads**: five groups, one RSA each (3 EXCELLENT, 2 GOOD).

### Prepared change list

1. Negatives, broad match, in REK | Painting Negatives: cost, costs, how much, price, prices, ideas, idea, colors, color, glidden, labor, furniture, equipment, reviews, deland, commercial (Residential campaign only), and phrase: j&b painting, all american painting. Dedupe: sherwin, behr, diy, refacing already present; the existing phrase versions of cost, ideas and colors stay but the broad single tokens above are the ones that will actually block the long-tail wordings. Flag: "color" as a broad negative would block "color masters" brand queries, so add it to Residential Painting only, never to Brand.
2. Drop the CPC ceiling from $11 to $7 and watch impression share for a week; at $11 the campaign buys every click it can near the cap. Alternatively move to Manual CPC with group bids ($8 Painters - General, $6 Interior and Exterior, $5 Cabinet).
3. Second RSA in Painters - General and Exterior Painting (the spenders).
4. Add exact-match versions of the three converting phrase keywords: [house painters port orange], [painting companies port orange], [painters port orange], and keep the "near me" exacts even though they have no impressions yet (QS will fill in).
5. Confirm the call asset. Then revisit after two weeks.

## Rotation notes

**Affordable Critter Solutions (227-108-4521), 77 C, +1.** $293 in 30 days, 18 conversions (website calls 9, calls from ads 6, web form 3), $16 CPA. Budget $10 a day, 24 percent lost to budget, 65 percent lost to rank. No QS below 4. Two zero-conversion keywords above $10 ("wildlife animal control" broad $31, "critter control near me" broad $20). Visible waste: "animal control ocoee" and "ocoee fl" $13 (county animal control), "dead raccoon removal" $8, "what to do if you see a bobcat" $2. Nothing urgent. Budget ask to the client ($10 to $15) stands from Sep 14. Enhanced conversions is on; not a healthcare client, no action.

**Aqua Coat Pool Plastering (285-714-0527), 67 D, +3.** $451 in 30 days, 13 conversions (Free Estimate 7, website call 5, 60s call 1), $35 CPA, target CPA since Sep 9 is working: weekly conversions 3, 4, 3, 3. Still open from Sep 14: the 248-member "Master Negative Lisst" is attached only to the paused campaign; the live campaign relies on 89 campaign negatives. Pool Equipment group is still live ("swimming pool equipment" broad $70 for 1, "hayward pool products" QS 3 $22 for 0, "hayward pool pump tech support" $17). New visible waste: "pool painter near me" $18, "paint my pool" $7, "pinch a penny" x4 $20, "leslie's" $5, "pool tile grout" $10. Prepared: attach the master list to the live campaign, pause Pool Equipment, add phrase negatives painter, paint, pinch a penny, leslie, grout, tech support, hayward (check the list first; it is not attached, so its members do not protect anything today). 92 percent of spend is broad match on a $15 a day budget losing 45 percent to budget; the budget is the lever if the client wants more.

## One-liners

- **Precision GPR (554-113-4760), 57 F, +7.** Better month: 24 conversions at $107 (Sep 14 window: 9 at $268), with "Michael Phone Number (305)" now recording 7 and lp_contact_form 8. The two other website call actions are still zero. This week fell to 2 conversions on $713. LP Search - Location, which the Sep 4 list said to pause, spent $112 this week at $22.37 a click after its $14 target CPA was removed on Oct 10. Waste this window: "gprs" variants $171 ("gprs orlando" $123 alone), 811/julie/sunshine/dig/miss utility $100, "gpr scanning price" $23, "rebar finder" $18. "gprs" is still not a negative in LP NKWs (only "gpr" exact and "811" broad). Underground Utility Survey phrase is QS 2 at $329 for 4. The Sep 4 change list stands: negatives (gprs, julie, sunshine, miss utility, dig, locator as phrase, price), pause Location and DSA, second look at the GPR Scanning keywords.
- **Florida Sealcoating (168-852-7101), 60 D, -3.** Spend $3,176 against $105 a day of budget: on the $3,000 plan. 26 conversions at $122; this week 4 on $847. Branded campaign: "florida sealcoating" phrase $353 for 1 at $17.65 a click and "florida seal coating services" $84 for 0; the brand campaign's CPC is $10.89 on Maximize Conversions with a $20 budget. Move Branded to exact plus phrase on Manual CPC or Target Impression Share with a $4 ceiling. Competitor and supplier queries still visible: "m&s asphalt paving" $51 (a REK client; the phrase negative exists in the master list, so these clicks predate it or the list needs checking), "seal master orlando" $27, "tru mark inc" $26, "hot mix asphalt near me" $23, "american sealcoating" $18, "hot shot sealcoating" $16, "striping machine" $16, "sealers for driveways" $11, "p&p striping" $10, "landmark paving" $8, "finish line sealcoating" $8, "angie's list" $7. New phrase negatives: tru mark, seal master, hot mix, millings, american sealcoating, hot shot, striping machine, sealers, p&p, landmark, finish line, g force, angie, builders, products. Dedupe: sealmaster (one word), preferred materials and m&s asphalt paving already present. "asphalt patch repair" phrase is QS 2 and QS 3 in two campaigns ($214, 0 conversions): pause the Commercial copy.
- **Scootz (185-574-5478), 64 D, +6.** 38 conversions at $39 (Booqable 25, calls 13). Tom moved the campaign to Maximize Conversions on Oct 6 with an ad schedule; CPC went $0.70 to $2.50 and clicks fell 72 percent while counted conversions held near 7 to 10 a week. Give it to Nov 2 before judging. GA4 form_submit is still secondary and still silent since Aug 16 (worklist item). Auto-apply removed a keyword Oct 8: turn auto-apply off. Negatives to consider: scooter bug (two words), ucf, gateway scooter, cloud of goods, stroller, phone number. Dedupe: scooterbug (one word, exact only), jobs, how much, can you rent already present.
- **The Counseling Group (657-069-3617), 66 D, 0.** $555 in 30 days on the $25 a day Mon to Fri schedule: on plan. 2 primary conversions (one form, one call) plus the tel-tap action, which has now recorded 2 taps (Oct 13 and this week) 62 days after it was built, so the tag works. Those taps show only in all_conversions although the action is primary and included; check the action's include setting and attribution in the UI. Enhanced conversions is off, as required. Visible waste $50: "medications for depression" $4 (medication is a phrase negative, this slipped as the plural wording), "ect therapy" $4, "pressure points on hands for anxiety" $4, "gottman method" and "john gottman" $8, other therapists' names $17, titusville and kissimmee $8. New negatives: ect, pressure points, gottman, titusville, kissimmee, quiz, therapist aid. Do not add "dr" (blocks nothing useful and risks "dr" in practitioner brand searches). The Sep 8 greenlit set remains open. "therapist near me" exact is QS 2 ($39, 0).
- **All Phase Pool Remodeling (103-111-7688), 67 D, -5.** 13 conversions at $66. "Contact Form" is primary but excluded from Conversions and recorded 5 in all_conversions: include it (unless the exclusion is deliberate), and the CPA is $48. "Phone Calls 60s+" still zero in 30 days. The brand term "all phase pool remodeling" broad sits in Pool Renovations and Pool Resurfacing ($359, 42 percent of spend) and produced 10 of the 13 conversions; "swimming pool renovations" broad $231 for 0 is the biggest non-brand line. The 379-member master negative list is attached only to the paused campaign. Sep 14 prepared changes (brand split, attach the list) stand. Enhanced conversions on, not healthcare.
- **Quality Paralegal Services (447-153-2607), 56 F, new.** 61 conversions at $22 in 30 days, 36 of them call-asset calls; the account works. Build issues: "family law attorney near me" broad is QS 1 and the top spender ($261 for 6), "divorce lawyers near me" broad QS 1 ($60); for a non-lawyer paralegal service, attorney and lawyer keywords invite the UNCLEAR_RELEVANCE and GOVERNMENT_DOCUMENTS policy flags already on one disapproved expanded text ad. Campaign names are ad headlines, "Ad group 1" exists, 392 keywords with 84 percent of spend on broad. One POOR RSA (Ad group 1), every group under two RSAs. Clicks to call (Google-hosted) counted 8 as primary. Suggested: move attorney and lawyer terms to a separate campaign with paralegal-specific ad copy or pause them, second RSAs, rename campaigns. Spanish queries convert ("abogado en kissimmee", "notario near me"), so no Spanish negatives.
- **M&S Asphalt Paving (827-724-4095), 62 D provisional, relaunch.** Paving - Volusia $461, 5 conversions, $95 CPA, Manual CPC at $12.13; this week $155 for 0. 8 keywords at QS 3 ("asphalt companies near me", "paving companies near me", "asphalt sealcoating", "driveway crack repair"), no spend on most. Visible waste: "cost to resurface driveway" $19, "christian brothers asphalt" $17, "buds asphalt milling" $12, "all asphalt services" $10, "ecogrid driveway" $10, "ways to pave a driveway" $10, "driveway cost" $10. New negatives: cost, ways to, ecogrid, christian brothers, buds, all asphalt services, milling. The website call action is categorised SUBMIT_LEAD_FORM; set it to PHONE_CALL_LEAD. 5 of 6 groups have one RSA. Sealcoating & Repairs at $8 a day spent $16.
- **Filutowski Eye Institute (192-870-7876), 44 F provisional.** See attention item 6. New since Sep 14: conversions 354 to 243 and CPA $49 to $80 across comparable windows; 14 disapproved ads in Cataracts and Eye Surgery groups for DESTINATION_NOT_WORKING (a landing page is down or redirecting; Sep 14 could not read the reason); Branded converts at $14 and loses 65 percent to budget at $50 a day while the LASIK catch-all gets $455 a day. The Sep 14 prepared list stands unchanged, plus: fix the broken destination URL. Coordinate with Accalia Marketing before anything is applied.
- **All Phase Pool Remodeling - Jacksonville (918-824-8896).** Tom paused the Jacksonville LSA campaign Sep 24. The leftover "Orlando" search campaign is still ENABLED but NOT_ELIGIBLE (ad groups paused, missing lead form) and spent nothing. Pause it so it cannot wake up (worklist item 6, still open).
- **Straightline Fence And Supply (550-094-8786).** LSA only now. Excluded.
- **Jupiter Boat Supply, REK Marketing (390-315-5264).** No campaigns serving. No changes.
- **LSA-only accounts** (Citrus Landscape Solutions x3, Herrell Plumbing, Spectrum Electric, Roeling Green Lawns, ABC Pressure Wash, Statewide Home Remodeling, Color Masters LSA, MB Skin Care, All Phase Orlando LSA, Byers Fence LSA): out of scope per Tom's Sep 4 note. Byers Fence (870-428-8862) and Herrell Plumbing excluded per Known account context.

## Optimization opportunities (fleet)

New negative keywords (deduped against live lists above): Patio Style 9, Rover 12 plus 3 campaign-level, Progetto 3 to 5 (confirm designer brands), Color Masters 18, Precision GPR 7, Florida Sealcoating 15, Scootz 6, Counseling Group 7, Aqua Coat 7, M&S Asphalt 7. Roughly 100 proposals in total; the ones that recover the most are Color Masters' cost and ideas tokens ($200/mo), Rover's lap of love campaign-level negatives ($130/mo) and Precision GPR's gprs family ($170/mo).

New keywords to add: Color Masters exact [house painters port orange], [painting companies port orange], [painters port orange]; Rover exact [in home pet euthanasia near me] (2 conversions on $13) and [mobile pet euthanasia near me] (from Sep 14); Florida Sealcoating exact [asphalt companies in orlando florida] (2 conversions on $15) and [asphalt sealcoating companies near me]; Quality Paralegal exact [divorce paralegal], [child support paralegal near me], [legal document preparation services]; Aqua Coat phrase "pool refinishing companies near me" and "pool ladder steps replacement" only if the client does that work.

Bid and budget adjustments: Color Masters ceiling $11 to $7; Rover In-Home Pet Euthanasia $50 back to $30 and Competitors $20 to $10 until it converts again; Florida Sealcoating Branded to exact plus phrase with a $4 ceiling; Precision GPR pause Location and DSA; Progetto keep its $7 and $4 ceilings during the QS rebuild; Patio Style leave Pergolas alone for two weeks; Filutowski LASIK $455 to $200 and Branded $50 to $100 (if engaged).

Competitive read (rank-lost share as the proxy): Progetto loses 53 to 82 percent to rank with QS 1 to 3 on a third of its keywords, which is a quality problem, not a budget one. Color Masters pays within a dollar of its $11 ceiling on most clicks and still loses 46 percent to rank, so the ceiling is below the market for "house painters" in Port Orange; a quality and copy fix is cheaper than raising it. Rover holds 59 percent absolute top in In-Home Pet Euthanasia and is not being outbid; its problem is tracking and query hygiene. Filutowski's LASIK CPC rose from $16.67 to $20.53 across windows while Google's CAMPAIGN_BUDGET recommendations (5) push for more.

## Prioritized weekly action plan

1. **Critical, REK (paidads): Patio Style.** Set Get directions (GTM) back to primary and included today. Then the five second RSAs and the pergola negatives. Until this lands every Patio Style number is understated.
2. **Critical, REK: Rover manual conversion test** (website call button, contact form, call asset). Then the lap of love campaign-level negatives, pause the two $27 to $29 keywords, trim Pet Cremation, rebuild the Competitors RSAs, and pull the unused In-Home budget back.
3. **Critical, Tom: Progetto Shades landing pages and ads.** Map groups to matching pages, second RSAs everywhere, pause the QS 1 keywords. Two zero weeks on $846.
4. **Critical, Tom: Color Masters negatives and ceiling.** The 18 broad negatives (color only in Residential), ceiling $11 to $7, confirm the call asset, second RSAs in the two spending groups.
5. **Critical, Tom: Filutowski scope decision** (fourth week open). If engaged, the Sep 14 list plus the broken destination URL recovers an estimated $6,300 a month at the floor.
6. **High, REK: Precision GPR.** Pause Location and DSA (Location spent $112 this week after the tCPA was removed), add the gprs family and 811 variants, and keep measuring; the account is better than Sep 14, do not undo that.
7. **High, REK: Florida Sealcoating.** Branded to exact plus phrase with a ceiling, the 15 competitor and supplier negatives, pause the Commercial copy of "asphalt patch repair".
8. **Medium, Tom: Scootz.** Turn off recommendations auto-apply. Hold the bidding change until Nov 2. Form_submit test still open.
9. **Medium, REK: All Phase** (include Contact Form, attach the master list, brand split), **Aqua Coat** (attach the master list, pause Pool Equipment, 7 negatives), **The Counseling Group** (verify the tel-tap include setting, 7 negatives), **M&S Asphalt** (7 negatives, call action category, second RSAs), **Quality Paralegal** (attorney and lawyer terms into their own campaign or paused, second RSAs).
10. **Low: All Phase Jacksonville** pause the Orlando campaign; **Affordable Critter** budget ask.

## Rotation

Deep-dived this run: Patio Style, Rover Veterinary Care, Progetto Shades, Color Masters, with rotation notes on Affordable Critter Solutions and Aqua Coat. Due next Monday: Precision GPR (to measure the cleanup and the Location change), Florida Sealcoating (branded campaign), Quality Paralegal Services (first full dive), The Counseling Group (October, per the Sep 4 note). The week after: All Phase Pool Remodeling, Scootz (bidding change at four weeks), M&S Asphalt Paving.

## Data notes

- Account discovery returned 31 client accounts; Sep 14 had 26. All 26 are still present; the five additions are listed in attention item 1. Compare next week against this run's list.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Sep 20 (the API allows 30 days). Conversion action edits are not included in change history, which is why the Patio Style directions demotion is dated from the daily conversion series (last primary count Sep 21) rather than from a change record.
- Patio Style's 30-day "primary conversions" (27) counts the GTM directions action for Sep 19 to 21 only (12 of the 27), since that is when it was still primary. Weekly figures after Sep 22 exclude directions entirely.
- Florida Sealcoating week-over-week CPC includes 44 display remarketing clicks this week at $0.87 and 56 last week at $0.61.
- The pull script stalled twice on a streaming call (The Counseling Group, All Phase); both accounts were re-pulled successfully with a 300-second timeout. No query returned an error in the final data set.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
