# PPC Weekly Audit - 2026-09-28 (Google Ads fleet)

Run: Monday Sep 28, 2026, scheduled cloud session through tools/gaql.py (API v25) against MCC 656-695-7229. Windows: 30 days Aug 29 to Sep 27; this week Sep 21 to Sep 27; last week Sep 14 to Sep 20. Score deltas are against the Sep 14 report. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Filutowski Eye Institute (worst score), Precision GPR (worst existing REK account), Patio Style (conversion tracking regression, on rotation), Aqua Coat and Affordable Critter Solutions (on rotation). First-look notes for the three new or reactivated search accounts. One-liners for the rest.

The credential file was copied from the Drive folder dave-ads-setup with mode 600, used only by the client library, and deleted before this report was written. The default v22 in gaql.py is no longer shipped by the current google-ads library; this run used GOOGLE_ADS_API_VERSION=v25.

## Attention items (read first)

1. **Patio Style (596-555-8707) lost its primary conversion.** Both directions actions, the GA4 "get_directions" import and "Get directions (GTM) 11 Sep", are now secondary and excluded from Conversions. The Known account context says Get Directions is the client's primary conversion by design. Counted conversions went 46, 21, 8 over the last three weeks while directions taps held at 15 a week. Conversion action edits are not in change history, so the API cannot say who changed it; paidads@rekmarketing.com made 154 other edits in the account between Sep 15 and Sep 25. Confirm with Tom and restore one directions action to primary. See deep dive 3.
2. **Filutowski Eye Institute (192-870-7876): $1,917 this week and $6,603 in 30 days went to named competitor clinics, retail optical chains, insurers and Spanish queries, almost all through the one broad keyword "lasik treatment cost".** Accalia Marketing raised that campaign's budget from $430 to $455 a day on Sep 14 and paused Performance Max. No REK user has edited the account. The scope decision from Sep 14 is still open.
3. **No account vanished from the MCC. Four are new since Sep 14**: Color Masters (426-092-9847, search, built by Tom, live since Sep 21), Quality Paralegal Services (447-153-2607, search plus smart, Tom editing since Sep 21), All Phase Pool Remodeling (Orlando LSA) (355-287-7099, created Sep 25), and an unnamed account 163-445-9282 (an LSA plus a not-eligible search campaign, edited by colormasters88@gmail.com and Tom, zero spend). One manager link to 116-301-0558 is PENDING. M&S Asphalt Paving (827-724-4095) was reported paused on Sep 14 and is serving again since Sep 15.
4. **Straightline Fence (550-094-8786) is no longer a search account.** Robbie removed the "vinyl fence" search campaign on Sep 22 (both ads were disapproved for COMPROMISED_SITE). A Local Services campaign went live Sep 23 at $71 a day and spent $870 in three days for 7 leads at $124. Out of scope from here under Tom's LSA rule; worklist item 18 closes.
5. **Rover Veterinary Care recovered.** After the Sep 14 alarm, Dave moved both service campaigns to Manual CPC, cut Competitors to $5 a day and Brand to $10, and raised In-Home and Cremation to $30. This week: 7 conversions on $231, $33 each, against 5 on $272 last week. No tag fault was found; the zero week was a volume gap.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 30 client accounts, 1 manager | 14 | 4 new since Sep 14, 0 vanished. Excluded: Byers Fence x2, 9 LSA-only accounts (the 8 from Sep 4 plus the new All Phase Orlando LSA), Straightline (LSA only now), the unnamed 163-445-9282. Not scorable: Jupiter Boat Supply, REK Marketing (paused), All Phase Jacksonville (search not eligible). |

Search, display and Performance Max spend in the 30-day window: $12,847 across the ten REK-managed accounts scored on Sep 14, plus $19,848 at Filutowski Eye Institute, $793 search at Quality Paralegal Services, $393 at Color Masters and $232 at M&S Asphalt Paving. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $19,848 | 310 | $64 | 40 | F | -2 | Critical (scope) | "lasik treatment cost" broad spent $13,712 at $211 per conversion; budget raised to $455/day Sep 14; $6,603 visible on competitor, retail, insurer and Spanish terms | $6,603 |
| 2 | Precision GPR | 554-113-4760 | $2,623 | 16 | $164 | 54 | F | +4 | Critical | First edits since Aug 26 landed Sep 22 (match-type swaps in GPR Scanning), but the negative list, the Location and DSA pauses and the bid caps are still not applied; this week 4 conversions on $622 | $391 |
| 3 | Quality Paralegal Services | 447-153-2607 | $793 search, $551 smart | 22 search | $36 | 55 | F | new | Needs attention (new) | 100 percent broad match on lawyer and attorney terms for a non-lawyer service; one ad DISAPPROVED (destination not working); two of four search ad groups have no RSA | $77 |
| 4 | Scootz | 185-574-5478 | $1,537 | 25 | $61 | 56 | F | -2 | Critical | No edits since Sep 2; GA4 form_submit still secondary and silent since Aug 16; this week 4 conversions on $326 after 11 last week | $22 |
| 5 | Color Masters | 426-092-9847 | $393 | 0 | n/a | 57 | F | new | Needs attention (new) | First week live: 39 clicks at $10.08 and zero conversions on 13 primary actions; idea, color and cost queries took $158 of $193 visible | $158 |
| 6 | Progetto Shades | 416-010-8247 | $1,017 | 6 | $169 | 58 | F | first score | Needs attention | Ceilings raised $4 to $7 on Sep 18, spend up 68 percent and CPA $89 to $300 this week; 23 keywords at QS 1 to 3; every ad group has one RSA | $79 |
| 7 | Patio Style | 596-555-8707 | $2,001 | 113 | $18 | 60 | D | -6 | Critical | Directions actions demoted to secondary (attention item 1); brand phrase keywords re-added Sep 16 and matching "ideas for screened in patio"; Pergolas campaign $502 with 0 primary conversions | $79 |
| 8 | Florida Sealcoating | 168-852-7101 | $2,321 search | 23 | $101 | 62 | D | -1 | Needs attention | Competitor and supplier negatives still missing after three weeks ($298 this window); Branded 0 conversions this week on $154; CPA $109 to $140 | $298 |
| 9 | M&S Asphalt Paving | 827-724-4095 | $232 | 2 | $116 | 64 | D | reactivated | Needs attention (new) | Serving again since Sep 15; "driveway paving companies" phrase $93 at $15.52 a click with 0 conversions; one RSA in all eight ad groups | $38 |
| 10 | Aqua Coat Pool Plastering | 285-714-0527 | $455 | 14 | $33 | 66 | D | +2 | Needs attention | Dave paused 11 keywords and tightened geo Sep 16; the 248-member master list is still attached only to the paused campaign; Pool Equipment group still live ($107) | $63 |
| 11 | Rover Veterinary Care | 750-667-5721 | $1,424 | 17 | $84 | 66 | D | +5 | Needs attention | Recovered (attention item 5); Brand still holds "katie matzke" phrase ($26 this week, 0 conv); both Competitors RSAs still POOR; the Sep 14 negatives not added | $73 |
| 12 | The Counseling Group | 657-069-3617 | $556 | 6 | $93 | 67 | D | +1 | Needs attention | Tom added 34 phrase negatives Sep 21; tel-tap action still zero 47 days after creation; 0 conversions this week on $137; three keywords at QS 2 | $20 |
| 13 | All Phase Pool Remodeling | 103-111-7688 | $606 | 13 | $47 | 70 | C | -2 | On target | Dave removed the $25 target CPA Sep 25; the 379-member master list is attached only to the paused campaign; brand term still 45 percent of spend inside non-brand groups | $39 |
| 14 | Affordable Critter Solutions | 227-108-4521 | $307 | 15 | $20 | 76 | C | 0 | On target | Clean; 15 conversions at $20 in 30 days; $10/day losing 18 percent to budget and 68 percent to rank | none confirmed |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | n/a | was no spend | Out of scope | Search campaign removed Sep 22; LSA live (attention item 4) | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | n/a | n/a | Paused (search) | LSA paused by Tom Sep 24; the "Orlando" search campaign is still ENABLED and NOT_ELIGIBLE (worklist item 6 open) | n/a |
| none | Jupiter Boat Supply, REK Marketing | | $0 | 0 | n/a | n/a | n/a | n/a | Paused | No changes | n/a |

Scores for the three new or reactivated accounts are provisional: Color Masters has seven days of data, Quality Paralegal Services and M&S Asphalt Paving are mid-rebuild by Tom.

## Week over week (Sep 21 to 27 against Sep 14 to 20, search, display and PMax only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $5,016 to $5,214 (+4%) | 511 to 508 | 6.3% to 6.3% | $9.82 to $10.26 | 75.3 to 71.7 | $67 to $73 | Brand Awareness LASIK $3,562 to $3,747, its conversions 22.3 to 15.7 |
| Precision GPR | $605 to $622 (+3%) | 53 to 41 | 6.8% to 7.5% | $11.42 to $15.18 | 7 to 4 | $86 to $156 | Off target; "Concrete Scanning" phrase $24 to $115 with 0 conversions after the Sep 22 edits |
| Florida Sealcoating (search) | $727 to $663 (-9%) | 50 to 47 | 3.7% to 5.1% | $14.55 to $14.11 | 7 to 4 | $104 to $166 | Off target; Branded 3 to 0 conversions |
| Patio Style | $488 to $480 (-2%) | 213 to 202 | 7.2% to 6.1% | $2.29 to $2.38 | 21 to 8 | $23 to $60 | Tracking change, not performance; directions taps 30 to 19 in all_conversions |
| Progetto Shades | $357 to $599 (+68%) | 76 to 107 | 4.4% to 4.1% | $4.70 to $5.60 | 4 to 2 | $89 to $300 | Ceiling raise took effect; CPA tripled |
| Scootz | $354 to $326 (-8%) | 555 to 540 | 6.9% to 7.1% | $0.64 to $0.60 | 11 to 4 | $32 to $81 | Booqable purchases 9 to 1; only purchases and ad calls count |
| Quality Paralegal (search) | $215 to $267 (+24%) | 39 to 59 | 2.3% to 4.2% | $5.52 to $4.52 | 2 to 7 | $108 to $38 | Tom's Sep 23 keyword additions; improving |
| Color Masters | $0 to $393 | 0 to 39 | n/a to 7.9% | n/a to $10.08 | 0 to 0 | n/a | Launch week, no conversions |
| Rover Veterinary Care | $272 to $231 (-15%) | 52 to 58 | 13.0% to 11.4% | $5.23 to $3.99 | 5 to 7 | $54 to $33 | On target after the Sep 16 changes |
| All Phase Pool Remodeling | $101 to $169 (+67%) | 21 to 39 | 3.8% to 5.3% | $4.82 to $4.34 | 2 to 2 | $51 to $85 | Target CPA removed Sep 25; spend rose, conversions did not |
| M&S Asphalt Paving | $83 to $149 (+80%) | 13 to 11 | 8.3% to 7.1% | $6.36 to $13.55 | 2 to 0 | $41 to none | Volusia budget $15 to $27 on Sep 24; CPC doubled |
| The Counseling Group | $115 to $137 (+19%) | 25 to 31 | 3.8% to 5.8% | $4.59 to $4.42 | 2 to 0 | $57 to none | Small numbers; budget lost share 57% |
| Aqua Coat | $166 to $128 (-23%) | 27 to 20 | 3.6% to 2.5% | $6.16 to $6.39 | 7 to 3 | $24 to $43 | Geo tightened Sep 16; budget lost share 65% at $15/day |
| Affordable Critter Solutions | $88 to $60 (-32%) | 23 to 19 | 9.5% to 6.5% | $3.83 to $3.15 | 4 to 2 | $22 to $30 | Flat, small numbers |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: All Phase 86 percent, Progetto Drapery 80 percent and Shades & Blinds 62 percent, Affordable Critter 68 percent, Patio Style Outdoor Furniture 57 percent, Precision GPR DSA 31 percent. Highest budget loss this week: Filutowski Brand Awareness 69 percent and Branded 50 percent, Aqua Coat 65 percent, Rover Competitors 61 percent (by design after the $5 cut), Counseling Group 57 percent, Precision GPR DSA 56 percent and Utility Mapping 55 percent. Highest CPC rises: M&S Volusia $6.32 to $15.29, Precision GPR Concrete Scanning $11.10 to $21.40, Florida Sealcoating Branded $11.40 to $15.43, Progetto Shutters $4.87 to $6.60. Rover's CPC fell from $5.23 to $3.99 after the move to Manual CPC with $3.50 to $6 bids, at the same absolute-top share.

## Changes made in the past two weeks (Sep 15 to Sep 28) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Rover Veterinary Care | Sep 16, Sep 22 | sheokand003@gmail.com | Budgets: Brand $20 to $10, Competitors $30 to $5, In-Home $20 to $30, Cremation $20 to $30. In-Home and Cremation to Manual CPC, enhanced CPC off, ad group bids $3 to $4, then keyword bids $3.50 to $6 on Sep 22. Five Competitors keywords paused. Two location criteria added to Cremation. | Conversions 5 to 7, CPA $54 to $33, CPC $5.23 to $3.99. Competitors now loses 61 percent to budget but "lap of love" still converts (2 on $85). Working. |
| Precision GPR | Sep 22 | sheokand003@gmail.com | GPR Scanning: five broad keywords removed and re-added as phrase plus broad pairs; "Gpr Scanning" and "Gpr Concrete Scanning" re-enabled; "concrete x ray services" added to Concrete Scanning; "concrete scanning services" added to Location; two RSAs rewritten. | Too early for the keywords. "Concrete Scanning" phrase went $24 to $115 with 0 conversions and Concrete Scanning CPC $11.10 to $21.40. None of the Sep 4 change list (negatives, pause Location and DSA, cap GPR Scanning) landed. |
| Florida Sealcoating | Sep 15, Sep 22 | sheokand003@gmail.com | Commercial budget $38 to $45; Branded target CPA $17 removed. Sep 22: Branded $30 to $35, Residential $30 to $40; 31 keywords added and 16 removed (broad and exact converted to phrase) in Residential and Commercial; six keyword pauses. | CPA $104 to $166 on search; Branded 3 to 0 conversions on $154. Daily budgets now $125, which is $3,750 a month against the $3,000 plan. Check with Tom whether the October plan changed. |
| Patio Style | Sep 15 to Sep 25 | paidads@rekmarketing.com | Sep 15: 20 keywords into Pergolas. Sep 16: phrase brand keywords "patio styles", "patio style longwood fl", "patio style orlando" added to Brand (reverses the Sep 4 exact-only fix); 20 exact negatives added to Outdoor Furniture and 8 chair keywords removed. Sep 17: 11 of those negatives removed again. Sep 23: HubSpot tracking templates on all four campaigns, 12 sitelinks. Sep 25: 17 new RSAs created, the previous RSAs paused. Undated: both directions actions set secondary. | Counted conversions 21 to 8 (tracking). Brand: "patio styles" $47 this week, 0 conversions, matching "ideas for screened in patio", "lanai furniture ideas", "patios decorations". RSA count per ad group unchanged at one because old ads were paused rather than kept. |
| Aqua Coat | Sep 16, Sep 22 | sheokand003@gmail.com | Geo targeting to Presence only with 30-mile radii around Tampa and Holiday; 11 keywords paused across Plastering, Renovations, Resurfacing; exact and phrase brand keywords added; four RSAs rewritten; four assets Sep 22. | Spend $166 to $128, conversions 7 to 3, budget lost share 65 percent at $15 a day. One week; measure again Oct 5. |
| All Phase Pool Remodeling | Sep 16, 18, 25 | sheokand003@gmail.com, tom@ | A keyword paused Sep 16; Tom paused and re-enabled the campaign on Sep 18 (four hours); Sep 25 Dave removed the $25 target CPA, re-enabled the Tile & Spillways keyword, rewrote two RSAs. | Spend $101 to $169, conversions flat at 2, CPA $51 to $85, rank-lost share 86 percent. |
| Progetto Shades | Sep 14, 18, 25 | tom@rekmarketing.com | $4 CPC ceilings on all five service campaigns Sep 14 (as recommended); raised to $7 on Shades & Blinds, Shutters, Motorized on Sep 18; two RSAs rewritten; 12 brand keywords (Hunter Douglas, Norman, woven wood) added Sep 25. | Spend $357 to $599, conversions 4 to 2, CPA $89 to $300. The $7 ceiling bought clicks, not leads. |
| The Counseling Group | Sep 21 | tom@rekmarketing.com | 34 phrase negatives: medication (antidepressant, ssri, spravato, supplements, med list), DIY (grounding, 54321, what helps, screening, curing, get rid of), age (teen, teenage, teenager, kids), and 14 competitor and author names. | Medication queries gone this week. "teen" and "kids" as standalone phrase negatives block "teen counseling" and "kids therapy"; fine if the practice is adults only, otherwise loosen. |
| Filutowski Eye Institute | Sep 14 | catie@accaliamarketing.com | Brand Awareness LASIK budget $430 to $455 a day; Performance Max paused. | Budget-lost share on the catch-all campaign still 69 percent; the campaign spent $3,747 this week. No REK edits. |
| Color Masters | Sep 18 to 24 | tom@rekmarketing.com | Three REK search campaigns built and enabled Sep 18 (Residential, Commercial, Brand), 93-member negative list, sitelinks and images; the client's own campaigns retired; Exterior Painting keyword paused Sep 21; Brand budget $5 to $8 and ceiling $3 to $8. | $393 in the first week, 0 conversions. See new-account note. |
| Quality Paralegal Services | Sep 21 to 25 | tom@rekmarketing.com | Seven negatives removed from the smart campaign; 13 keywords added Sep 23; budgets moved Sep 22, 23, 25; two ads edited; the second smart campaign paused Sep 25. | Search conversions 2 to 7, CPA $108 to $38. See new-account note. |
| M&S Asphalt Paving | Sep 15 to 24 | Bulk Actions, tom@ | Three campaigns re-enabled Sep 15; sitelinks and assets Sep 21; two Orlando Metro ads paused Sep 22; Volusia budget $15 to $27 Sep 24. | $149 this week, 0 conversions, CPC $6.36 to $13.55. See new-account note. |
| Straightline Fence | Sep 22 to 25 | robbie@rekmarketing.com, joe611904@yahoo.com | Search campaign removed; LSA assets added; 11 negatives on the LSA Sep 25. | LSA $870 in three days, 7 leads. Search side closed. |
| All Phase Jacksonville, All Phase Orlando LSA | Sep 24, 25, 28 | tom@rekmarketing.com | Jacksonville LSA paused; new Orlando LSA account created with five service categories and a Mon-Fri schedule, budget set to $71 a day this morning. | Out of scope; recorded so next week's discovery does not flag it. |
| Affordable Critter Solutions | Sep 25 | sheokand003@gmail.com | Two keywords added ("wild life animal control", "critter in attic"). | No effect yet. |
| Scootz | | | No changes since Sep 2. | The Sep 14 list has not been touched. |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

Landed: item 14 (YouTube actions secondary; the directions half overshot, see attention item 1), item 18 (closed by removing the campaign), item 21. Partly landed: item 3 (Brand on Target Impression Share holds, but phrase brand keywords came back Sep 16), item 7 (brand keyword is now exact; Pool Equipment and the master-list attachment still open), item 8 (negatives added Sep 21; the Depression RSA is still POOR and "help with depression" and "stress therapy" still run), item 13 (RSAs replaced, not added; Outdoor Furniture still Maximize Clicks), item 15 ("sealcoat florida" negatives exist in the service campaigns only; competitor negatives still missing), item 16 (budget cut and manual bids, but RSAs and negatives open). Not landed: items 4, 5, 6, 10, 11, 12, 17, 19. Client answers: still none recorded.

## Deep dive 1: Filutowski Eye Institute (192-870-7876), score 40 F, provisional

Scope note unchanged: no REK edits in 30 days, the editors are catie@accaliamarketing.com and web@filutowski.com. Nothing should be touched until Tom says whether REK manages, audits, or is only linked.

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 20 |
| Account Structure | 50 |
| Keywords & Targeting | 35 |
| Ads & Assets | 45 |
| Bidding & Settings | 45 |

| Campaign | Budget/day | 30d spend | Clicks | CPC | Conv | CPA | Search IS | Lost to budget | This week |
|---|---|---|---|---|---|---|---|---|---|
| S / Brand Awareness / LASIK | $455 | $13,712 | 775 | $17.69 | 64.9 | $211 | 18.1% | 65.9% | $3,747, 15.7 conv |
| S / Branded / Dr. F | $50 | $1,476 | 565 | $2.61 | 124.3 | $12 | 56.3% | 35.9% | $392, 33 conv |
| S / Lead Gen / Eye Surgery | $50 | $1,437 | 321 | $4.48 | 56.0 | $26 | 26.7% | 44.8% | $355, 14 conv |
| S / Lead Gen / Cataracts | $50 | $1,426 | 196 | $7.28 | 22.0 | $65 | 47.9% | 20.7% | $359, 7 conv |
| S / Lead Gen / LASIK | $50 | $1,409 | 105 | $13.42 | 8.7 | $163 | 58.1% | 17.3% | $359, 2 conv |
| Performance Max / Eye Surgery | paused Sep 14 | $387 | 126 | $3.07 | 34.1 | $11 | | | $0 |

### What changed since Sep 14

- The catch-all keyword got more money. "lasik treatment cost" broad is still the only keyword in Brand Awareness with spend ($13,675 of $13,712) and its budget went up $25 a day. Its conversions per week fell from 22.3 to 15.7 while spend rose. This week's visible terms under it: "dr jacqueline k flud do" $308, "florida eye clinic altamonte" $94, "uptown eyecare lake nona" $87, "atlantic eye consultants merritt island" $85, "total vision port orange" $76, "ophthalmologist" $66, "dr cartwright" $59, "shands ophthalmology department" $50, "blanik eye care" $48. Only $16 of the campaign's visible spend this week was on LASIK, laser or PRK terms, with 0 conversions.
- Strict waste floor, counting only named competitor clinics and doctors, retail optical chains, insurers and Spanish queries, and excluding any term with LASIK or cataract intent: $6,603 in 30 days ($4,494 competitors, $1,757 retail, $199 Spanish, $87 insurers, $66 pediatric and unrelated) for 23 conversions, and $1,917 this week. Google hides the low-volume remainder, so the true figure is higher.
- Performance Max, the account's cheapest source at $11 per conversion, was paused on Sep 14. Branded ($12) and Eye Surgery ($26) still lose 36 and 45 percent of impressions to budget.
- Conversion tracking is unchanged: 18 hidden Universal Analytics goals still primary and included, YouTube follow-on views primary and included, three call actions all primary, enhanced conversions for leads ON for a medical practice.
- Ads: every one of the five enabled ad groups still has a single RSA; Eye Surgery's is POOR. QS 3 on six "near me" keywords carrying $1,203 (expected CTR and ad relevance BELOW_AVERAGE), the largest of which convert well, so this is an ad copy problem, not a keyword problem.
- Negatives: the two shared lists attached to the live campaigns hold 37 terms. Of the 58 competitor, retail and insurer tokens proposed on Sep 14, only "pearle" and "eyeglass" exist; "glasses" exists only as "eyeglasses near me". Everything else is absent.

### Prepared change list (only if Tom confirms REK is engaged)

The Sep 14 list stands. Ordering by dollars: 1) replace the broad catch-all with the phrase and exact LASIK set and cut Brand Awareness to $200 a day; 2) the competitor, retail and insurer negative list (56 absent tokens, plus this week's new names: flud, cartwright, blanik, clearvue, atlantic eye, shands, eye physicians of central florida, fishman, sheridan, cohen, eyedeal, premier eye); 3) move the freed budget to Branded and Eye Surgery and re-enable Performance Max; 4) demote the UA goals and YouTube actions, one primary call action per line, enhanced conversions off; 5) second RSA in each ad group and rewrite the Eye Surgery RSA.

## Deep dive 2: Precision GPR (554-113-4760), score 54 F, up 4

Context applied: under active cleanup since Aug 2026. Dave's Sep 22 edits are the first since Aug 26.

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 45 |
| Account Structure | 50 |
| Keywords & Targeting | 45 |
| Ads & Assets | 75 |
| Bidding & Settings | 45 |

| Campaign | Budget/day | 30d spend | Clicks | CPC | Primary conv | CPA | This week |
|---|---|---|---|---|---|---|---|
| LP Search - GPR Scanning | $20 | $681 | 42 | $16.21 | 3.0 | $227 | $149, 0 conv |
| LP Search - Concrete Scanning | $18 | $564 | 32 | $17.64 | 3.5 | $161 | $171, 1 conv |
| LP Search - Services | $18 | $493 | 37 | $13.34 | 4.5 | $110 | $93, 2 conv |
| LP Search - Utility Mapping | $15 | $469 | 44 | $10.66 | 4.0 | $117 | $98, 1 conv |
| LP DSA - All Pages | $10 | $329 | 52 | $6.32 | 1.0 | $329 | $91, 0 conv |
| LP Branded | $10 | $82 | 14 | $5.88 | 0.0 | n/a | $20, 0 conv |
| LP Search - Location | $18 | $4 | 5 | $0.88 | 0.0 | n/a | $0 |

30 days: $2,623, 16 primary conversions (lp_contact_form 7, Calls from ads 6, Michael Phone Number 2, Calls from Smart Campaign Ads 1), $164 per conversion. Better than the Sep 14 window ($268), worse this week ($156 on 4).

### Findings

- **The Sep 22 edits were match-type housekeeping, not the change list.** The five GPR Scanning keywords Dave removed and re-added now exist as both phrase and broad, so the broad exposure is unchanged. "Ground Penetrating Radar" phrase is still the top cost line ($466, 3 conversions, QS 3, landing page BELOW_AVERAGE) and its exact twin spent $129 for 0. "Concrete Scanning" phrase, re-enabled Sep 22, spent $115 this week at $23 a click for 0 conversions.
- **Location and DSA are still enabled.** DSA - All Pages spent $329 for 1 conversion ($329) and this week matched "underground boring companies near me" $17 and "utility locator for gas lines" $4. Location spent $4; harmless but still a fourth home for "gpr scanning" (the query matched GPR Scanning, Services and DSA this window).
- **"gprs" is still not a negative anywhere.** Nine variants ("gprs orlando" x3, "gprs florida", "gprs tampa", "gprs service", "gprs scanning", "gprs company", "gprs near me") cost $200 this window, $100 of it this week. GPRS is a national competitor's name.
- **Locate-service queries**: "www sunshine811" $19, "sunshine utility locate" $10, "sunshine dig" $9, "miss utility florida" $23, "1800 dig" $9, "dig alert" $7. These searchers want the free 811 service. "811" is in the LP NKWs list but as a whole-token negative it does not catch these. Rebar detector and finder queries $39, Spanish "radar de penetración terrestre gpr" $30, "geoslice net" $18, "ground penetrating radar price" $19. Confirmed waste this window: $391.
- **Conversions**: the website call actions (305) and (786) still recorded zero in 30 days; "Michael Phone Number (305)" recorded 2 in the last two weeks, so at least that tag fires. "Contact Us", "Contact Us (1)" and "Contact us" still coexist as secondary. Enhanced conversions for leads is ON; not healthcare, acceptable.
- **Bidding**: seven campaigns on Maximize Conversions with 0 to 4.5 conversions each; Location carries a $14 target CPA. Budget-lost share 24 to 56 percent on the four service campaigns at $15 to $20 a day, so the strategy is both starved and thin.

### Prepared change list

1. Negatives, phrase, to LP NKWs: gprs, sunshine, miss utility, 1800 dig, dig alert, boring, rebar finder, finder, detector, radar de, penetración, geoslice, price, pricing, how much, for sale, gs9000, em locator. Dedupe: 811, equipment, rental, low cost already present; "underground radar detector" exists but does not cover "rebar finder".
2. Pause Location and DSA - All Pages. Move the $28 a day into GPR Scanning and Services.
3. Pause "Ground Penetrating Radar" exact ($129, 0 conv) and "Concrete Scanning" phrase ($345, 0 conv in 30 days). Keep the phrase GPR keyword but cap it: switch GPR Scanning to Manual CPC at $10 until the landing page score moves off BELOW_AVERAGE.
4. Consolidate GPR Scanning, Concrete Scanning and Services into one campaign so Maximize Conversions sees 11 conversions a month instead of 3 to 4.5 each. Or move all to Manual CPC as Dave did at Rover, which worked there.
5. Manual test on the (305) and (786) website call actions; remove the duplicate Contact Us actions.

## Deep dive 3: Patio Style (596-555-8707), score 60 D, down 6

Context applied: the client's primary conversion is Get Directions to the showroom, then calls, then contact forms. Outdoor Furniture on Maximize Clicks with a $2.50 cap is by design.

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 65 |
| Account Structure | 60 |
| Keywords & Targeting | 60 |
| Ads & Assets | 65 |
| Bidding & Settings | 70 |

| Campaign | Budget/day | Strategy | 30d spend | Clicks | CPC | Primary conv | All conv | This week |
|---|---|---|---|---|---|---|---|---|
| PS / Search / Outdoor Furniture | $30 | Maximize Clicks | $933 | 657 | $1.42 | 101 | 494 | $216, 6 conv |
| PS / Search / Pergolas & Louvered Roofs | $16 | Manual CPC | $502 | 75 | $6.69 | 0 | 3 | $116, 0 conv |
| PS / Search / Outdoor Kitchens | $12 | Maximize Clicks | $368 | 102 | $3.61 | 6 | 81 | $82, 2 conv |
| PS / Search / Brand | $6 | Target Impression Share | $199 | 81 | $2.45 | 6 | 63 | $66, 0 conv |

### Findings

**Directions are no longer a conversion.** Primary conversions by action by week, from the API:

| Action | Aug 17 | Aug 24 | Aug 31 | Sep 7 | Sep 14 | Sep 21 |
|---|---|---|---|---|---|---|
| GA4 get_directions (import) | 42 | 38 | 43 | 20 | 6 | 0 |
| Get directions (GTM) 11 Sep | 0 | 0 | 0 | 1 | 14 | 4 |
| Website Call Conversions 11 Sep | 0 | 0 | 0 | 0 | 0 | 2 |
| Calls from ads | 1 | 1 | 1 | 0 | 1 | 1 |
| Thank you page 11 Sep | 0 | 0 | 0 | 0 | 0 | 1 |

Both directions actions are now configured primary false, included false. The GA4 import stopped counting first (Sep 7 week onward), the GTM action was primary for about ten days and then demoted too. The taps did not stop: get_directions recorded 16 and 15 in all_conversions the last two weeks, the GTM action 14 and 15. So the store is getting the same foot-traffic signal; Google Ads just stopped counting it. The Sep 14 worklist asked to confirm the two did not double count; the outcome was that neither counts. With only calls and the thank-you page left as primary, the account now shows 8 conversions a week and any move to Maximize Conversions (worklist item 13) would optimise to phone calls only.

**Brand campaign drift.** On Sep 16 paidads@ added phrase "patio styles", "patio style longwood fl" and "patio style orlando" to Brand. "patio styles" phrase spent $98 in 30 days ($47 this week) with 0 primary conversions and matched "ideas for screened in patio", "lanai furniture ideas", "patios decorations", "patio makeover ideas", "summer patio". Tom's Sep 4 fix was exact-only for that reason. The campaign is BIDDING_STRATEGY_LIMITED at $6 a day.

**Pergolas & Louvered Roofs**: $502 in 30 days, 0 primary conversions, 3 all-conversions. "insulated patio cover" ($165, 28 clicks) and "patio cover orlando" ($157, QS 3) are the top two lines and neither converted. The panel queries ("aluminum patio roof panels", "snap lock insulated aluminum roof panels", "insulated pan roof", "lanai roof panels") still show $56 this window although "panels" and "roof panels" are in Master Negatives; the clicks predate the additions or match through plurals. The client's answer on insulated panels (worklist item 4) is still outstanding.

**Ads**: Dave created 17 new RSAs on Sep 25 and paused the old ones in the same ad groups, so 11 of 12 ad groups still have exactly one enabled RSA. Ad strength on the new ones is GOOD to EXCELLENT.

**Negatives dedupe**: panels, roof panels, mirador, lowes, home depot, diy, snap lock, prefabricated are present. Absent: big green egg, tru island, vestivium, hampton bay, polywood, azenco (keep, the store carries it), ideas, decorations, pan roof, sink, cabinets, daytona.

### Prepared change list

1. Today: set exactly one directions action back to primary and included. The GA4 import has the longer history; the GTM action fires on the same tap and should stay secondary. This restores the client's primary conversion and the week-over-week baseline.
2. Brand: remove the three phrase keywords added Sep 16 or add phrase negatives "ideas", "decorations", "makeover", "furniture ideas" to Brand. Raise the campaign to $10 a day so Target Impression Share is not LIMITED.
3. Pergolas: pause "insulated patio cover" and "patio cover orlando" until the client answers on panels. Add phrase negatives pan roof, ideas, cabinets, sink, daytona to Master Negatives.
4. Un-pause the previous RSA in each ad group so every group has two.
5. Hold item 13 (Maximize Conversions) until step 1 has two weeks of counted directions.

## Deep dive 4: Aqua Coat Pool Plastering (285-714-0527), score 66 D, up 2

| Category | Score |
|---|---|
| Conversion Tracking | 75 |
| Wasted Spend | 60 |
| Account Structure | 55 |
| Keywords & Targeting | 60 |
| Ads & Assets | 70 |
| Bidding & Settings | 70 |

Snapshot: one live campaign, "Aqua Coat Pool Plastering - M", Maximize Conversions, $15 a day, BUDGET_CONSTRAINED. 30 days: $455, 87 clicks, $5.23 CPC, 14 primary conversions (Free Estimate 6, Phone Calls 60+ 5, Call (813) 3, Contact Form 1), $33 each. This week $128 for 3.

### Findings

- **The target CPA test is over and the result is fine.** Since Dave set it on Sep 9, the account has produced 14 conversions in 30 days at $33, against 10 at $29 in the Sep 14 window with a smaller spend. On Sep 16 he also tightened geo to Presence with 30-mile radii around Tampa and Holiday, paused 11 keywords and added exact brand keywords. Budget-lost share is 65 percent this week; the constraint is now the $15 budget, not the settings.
- **The master negative list is still attached only to the paused campaign** (worklist item 7). The live campaign runs on 89 campaign negatives and 34 ad-group negatives. This is the same pattern as All Phase. Attach "Master Negative Lisst" (248 members) to the live campaign.
- **Pool Equipment group is still live**: "swimming pool equipment" $65 (1 conversion, and its converting term was "pool supply"), "pool products" $24, "swimming pool maintenance equipment" $11, "pool equipment maintenance" $9. $109 on a plastering company's equipment group. Terms this window: "pentair pool pump" $19, "pinch a penny" $20 across three variants (pinch a penny is in the unattached master list), "pool gutter drain" $5.
- **Match type**: 97 percent broad. With 14 conversions a month Maximize Conversions on broad is workable, but "pool resurfacing companies near me" ($47, 0 conversions) and "pool renovation companies" ($16, 0) are the two lines to watch.
- **Ads**: Pool Renovations has a POOR RSA next to an AVERAGE one; Resurfacing and Tile are AVERAGE and AVERAGE.
- Confirmed waste this window: $63 (pentair, pinch a penny x3, grout, plaster repair kit, leslie, gutter drain).

### Prepared change list

1. Attach the master negative list to the live campaign. Then add phrase: pentair, aqua pools, pcs pools, handrail, equipment, products, installers, grout, fresh finish, aqua dreams. Dedupe: repair kit, supplies, pinch a penny, fiberglass, gel coat, kit already in the list.
2. Pause the Pool Equipment ad group.
3. Rewrite the POOR Pool Renovations RSA.
4. Budget: at $33 a conversion with 65 percent lost to budget, $20 a day is a fair client ask.

## Deep dive 5: Affordable Critter Solutions (227-108-4521), score 76 C, unchanged

| Category | Score |
|---|---|
| Conversion Tracking | 65 |
| Wasted Spend | 85 |
| Account Structure | 70 |
| Keywords & Targeting | 75 |
| Ads & Assets | 90 |
| Bidding & Settings | 75 |

Snapshot: one live campaign, ACS - Search, Maximize Conversions, $10 a day. 30 days: $307, 91 clicks, $3.38 CPC, 7.7 percent CTR, 15 primary conversions (Calls From Ads 9, Website calls 6, web form 3 in all_conversions), $20 each. Search impression share 13 percent, 18 percent lost to budget, 68 percent lost to rank.

- Clean search terms: the top zero-conversion term is "wild animal control near me" at $10, and "cassan wildlife" ($6) and "allstar animal removal" ($4) are the only competitor names. "affordable wildlife control reviews" $9 is brand-adjacent. No negatives needed this week.
- Keywords: "bat removal" broad $24, 0 conversions in 30 days (flagged Sep 14, still the only watch item). Both ad groups have two EXCELLENT RSAs.
- **Conversion tracking is the weak category**: 17 conversion actions, ten of them primary. "Contact Us (Default Google Ads Profile)" is a Universal Analytics goal still primary and included; "Contact Us - M" and "web form contact" both track the form; two smart-campaign call actions are primary and included with no smart campaign running. Nothing is double-counting today because only three actions recorded anything, but set the UA goal and the smart-campaign actions to secondary before they do.
- Enhanced conversions for leads is ON; pest control, acceptable.
- The 11 paused campaigns are still there (worklist item 19). Dave added two keywords Sep 25.
- Budget: $10 a day with a $20 CPA and 18 percent budget loss. $15 a day remains a fair ask.

No change list beyond the tracking cleanup and the budget ask.

## New and reactivated search accounts (first look, provisional scores)

**Quality Paralegal Services (447-153-2607), 55 F provisional.** Two search campaigns (Maximize Conversions, $23 and $17 a day, both BUDGET_CONSTRAINED, 40 to 42 percent lost to budget) and one live smart campaign ($5 a day, $409 in 30 days, 57 conversions, almost all Google-hosted local actions). Search: $793, 22 conversions at $36; this week 7 at $38 after Tom's Sep 23 keyword additions. Findings: 100 percent of search spend is broad match and the top keywords are "family mediation" ($219), "paralegal" ($168), "support attorney" ($67, 0 conv), "family law attorney near me" ($56, QS 1), "divorce lawyers near me" ($39, QS 3). A non-lawyer document service bidding on attorney terms will keep drawing "i need a lawyer now" ($18), "pro bono" and "legal aid" queries ($40 visible); "pro bono divorce lawyers orlando" did convert twice, so the client may accept these. One ad in Paralegals Services is DISAPPROVED (DESTINATION_NOT_WORKING and ONE_WEBSITE_PER_AD_GROUP). Two of four search ad groups have no RSA (an old text ad only). Conversion actions are call-heavy and sensible. Enhanced conversions ON, fine. Ask Tom: is REK managing this, and is lawyer-term traffic wanted? Then: fix the disapproved ad's URL, add RSAs to the two groups without one, convert the top ten keywords to phrase, and add exact negatives for the geography outside Orlando (melbourne, rockledge, polk, new smyrna).

**Color Masters (426-092-9847), 57 F provisional, seven days of data.** Tom built three campaigns (Residential $45, Commercial $25, Brand $8 a day) on Maximize Clicks with a $5 keyword bid and enabled them Sep 18; first spend Sep 21. Week one: $393, 39 clicks, $10.08 CPC, 7.9 percent CTR, 0 conversions across 13 primary actions (lead form, website call, calls from ads). Residential holds 55 percent impression share, so the ads show; the question is the $10 click and the zero. Visible terms: "how much does it cost to repaint your kitchen cabinets" $21, "front door color idea" $21, "glidden premium interior" $20, "cost to paint house exterior" $11, "house exterior colors" $11, "white room paint ideas" $10, "jesus gil painting daytona beach" $10. $158 of $193 visible spend is research or DIY intent. The 93-member negative list already has paint ideas, color ideas, paint colors, sherwin, behr, diy, faux, refacing; missing are glidden, deland, furniture, white, room, and the phrase forms "ideas" and "cost" as standalone tokens. Every ad group has one RSA (EXCELLENT). Actions: manual test of the lead form and call actions before week two ends (zero on 39 clicks is not yet a tag finding, but it will be at 80); add the five negatives; consider a $6 ceiling on Maximize Clicks so a research click does not cost $10.

**M&S Asphalt Paving (827-724-4095), 64 D, reactivated.** Three Manual CPC campaigns re-enabled Sep 15 (Paving - Volusia $27 a day since Sep 24, Paving - Orlando Metro $12, Sealcoating & Repairs $12). 30 days: $232, 24 clicks, 2 conversions (Estimate Form, both in the Sep 14 week), $116 each; this week $149 for 0 with CPC $6.36 to $13.55 after the Volusia budget went $15 to $27. "driveway paving companies" phrase is $93 at $15.52 a click for 0 conversions; its bid is $17.60. "asphalt paving companies" $25, 0. Terms are clean apart from "christian brothers asphalt" $17, "driveway installation cost" $10, "sealmaster orlando" $5. All eight ad groups have one RSA, five of them AVERAGE. Conversion actions: three primary, all miscategorised as SUBMIT_LEAD_FORM (the two call actions should be PHONE_CALL_LEAD; cosmetic). Actions: cap "driveway paving companies" at $10, add negatives christian brothers, cost, sealmaster, diy; second RSA per group as the account earns spend.

## No action needed this week (one-liners)

- **Scootz (56 F):** nothing has changed since Sep 2. GA4 form_submit is still secondary and has recorded nothing since Aug 16; Booqable purchases fell 9 to 1 this week, Calls from ads 2 to 3. Search impression share 28 percent, 54 percent lost to rank at a $0.60 CPC, which is the Maximize Clicks cap doing its job. The Sep 14 list stands in order: form test, restore the action, five-way ad group split, then Maximize Conversions. New this window and worth a phrase negative each: "scooterbug" ($6, a competitor), "2 person" ($7, 13 clicks, 0 conversions, on-service so keep if they rent tandems), "how much" is already covered.
- **Rover Veterinary Care (66 D):** Dave's Sep 16 rebuild is working (attention item 5). Still open from Sep 14: "katie matzke" phrase in Brand ($70 in 30 days, $26 this week, 1 conversion) and "rover pet euthanasia" ($21, 0); both Competitors RSAs POOR and AVERAGE; negatives "when to", "signs", "quality of life", "should i", "paws to health", "pet angel", "urns" absent (banfield, oncologist, doula, palm city, hospice, peggy adams, taps, cemetery present). "humane pet euthanasia" in Competitors is now $320 for 4 conversions ($80), acceptable at the $5 budget. Cat Euthanasia and In-Home groups still one RSA each.
- **Florida Sealcoating (62 D):** the ramp is on plan but the daily budgets now total $125 ($3,750 a month) after Dave's Sep 15 and Sep 22 raises, above the $3,000 approved for September. Competitor and supplier negatives are still missing after three weeks: ppg, absolute asphalt, gem seal, seal right, martin paving, kennedy, american asphalt, millings, cold mix, who sells, hot patch all absent; new this window father and son paving $46, site development $40, concrete contractor $29, asphalt tack $25, hot shot sealcoating $16, watson paving $15, infrared $16. Branded: "florida sealcoating llc" phrase spent $115 for 0 conversions and "sealcoat florida inc" ($16) matched Branded, where the "sealcoat florida" negative does not exist (it is only in Commercial and Residential). QS 1 to 3 on eight keywords carrying $391, led by "asphalt company orlando" ($212, QS 3). The Sep 14 change list stands; add the Branded negative and revisit the budget with Tom.
- **The Counseling Group (67 D):** Tom's 34 negatives landed Sep 21. Tel-tap still zero, now 47 days after creation; the manual test (worklist item 10) is overdue. 0 conversions this week on 31 clicks is inside normal variance for this account (6 in 30 days). QS 2 on "stress therapy" ($51, 0 conv), "therapist near me" ($38, 0) and "therapist orlando" ($12, 0), all landing page BELOW_AVERAGE, which is worklist item 11. "help with depression" ($75, 0 conv, 19 clicks) and "stress therapy" are still live although item 8 says pause. The Depression group's POOR RSA is still live. Enhanced conversions confirmed OFF. "gottman method couples therapy" $4 this week: item 9 still needs Clark's answer.
- **All Phase Pool Remodeling (70 C):** Dave removed the $25 target CPA on Sep 25 and spend rose 67 percent for the same two conversions. The 379-member master negative list is attached only to the paused campaign, the same fault as Aqua Coat; the live campaign runs on 91 campaign negatives. "leslie pool" $21 and "pinch a penny mount dora" $8 leaked again because only the exact forms exist as negatives; add phrase "leslie" and "pinch a penny". Brand term "all phase pool remodeling" is $272 of $606 inside the non-brand Pool Renovations and Pool Resurfacing groups (worklist item 12). "Phone Calls 60s+" still zero in 30 days; test it.
- **Progetto Shades (58 F):** first full score. Tom set the $4 ceilings as recommended on Sep 14, then raised three to $7 on Sep 18; spend went $357 to $599 and conversions 4 to 2. Shades & Blinds is the only campaign with 3 conversions in 30 days; Exterior & Patio ($124) and Drapery ($22) have none and "outdoor patio shades" ($84, QS 3) is the top zero-conversion keyword. 23 keywords at QS 1 to 3 carry $317, mostly exact single-word terms ("interior shutters" QS 1, "faux wood blinds" QS 1, "roller shades" QS 2, "roman shades" QS 2) with landing page BELOW_AVERAGE. Every ad group has one RSA and "Designer Brands" (new Sep 25) is PENDING. Recommend going back to $4 on Motorized and Shutters, pausing Exterior & Patio and Drapery until Shades & Blinds proves out, and phrase negatives bamboo, tension, technoline (smith noble, west elm, ikea, home depot, lowes present). Enhanced conversions ON, not healthcare, fine.
- **All Phase Jacksonville:** LSA paused by Tom Sep 24. The "Orlando" search campaign is still ENABLED and NOT_ELIGIBLE with $49 a day attached; pause it (worklist item 6) so nothing leaks if an ad group is ever re-enabled.
- **Jupiter Boat Supply, REK Marketing:** paused, zero spend, nothing to do.

Out of scope, for the record only: Herrell Plumbing's two Smart campaigns spent $425 this week (up from $155) for 20 conversions alongside its LSA; Citrus Landscape Sanford LSA $2,807 to $1,880 and St. Pete $2,103 to $941 week over week; Byers Fence search $850 in 30 days with 0 conversions (not REK-managed); the unnamed account 163-445-9282 carries a search campaign named "Commercial leads chat gpt" that is NOT_ELIGIBLE (ad groups paused) and an LSA with no spend, and Tom added three assets to it this morning.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Filutowski (deep dive 1, 56 absent tokens plus 12 new names), Precision GPR (deep dive 2 item 1), Patio Style (deep dive 3 items 2 and 3), Aqua Coat (deep dive 4 item 1), Florida Sealcoating (the 11 from Sep 14 plus father and son, site development, tack, hot shot, watson, infrared, and "sealcoat florida" phrase in Branded), Rover (when to, signs, quality of life, should i, paws to health, pet angel, urns), All Phase (phrase leslie, phrase pinch a penny, cleaners, coatings), Color Masters (glidden, deland, furniture, white, room, and standalone ideas, cost), Quality Paralegal (melbourne, rockledge, polk, new smyrna, restraining, public defender), Progetto (bamboo, tension, technoline), M&S (christian brothers, cost, sealmaster), Scootz (scooterbug).

New keywords to add: Rover exact "in home pet euthanasia near me" (2 conversions on $13 this week through phrase) and "put dog down at home" (1 on $9); Aqua Coat phrase "fiberglass pool repair" (2 conversions on $29, still matched through broad); Florida Sealcoating exact "asphalt company near me" (1 on $38) and "orlando asphalt paving company" (1 on $38); Quality Paralegal phrase "paralegal divorce" and "paralegal document preparation" (converting terms under lawyer keywords); Filutowski the phrase and exact LASIK set from Sep 14.

Bid and budget adjustments: Filutowski Brand Awareness $455 to $200 and Branded $50 to $100; Precision GPR Manual CPC $10 on GPR Scanning, pause Location and DSA; Progetto ceilings back to $4 on Motorized and Shutters; M&S "driveway paving companies" bid $17.60 to $10; Patio Style Brand $6 to $10; Aqua Coat $15 to $20 (client ask); Affordable Critter $10 to $15 (client ask); Florida Sealcoating confirm the $125 a day total with Tom against the $3,000 plan; Color Masters $6 ceiling on Maximize Clicks.

Competitive read (rank-lost share as the proxy): Rover holds 61 to 90 percent absolute top on its own campaigns after the manual bids and is not being outbid. All Phase (86 percent rank loss), Progetto (54 to 80 percent) and Affordable Critter (68 percent) lose on rank at tight budgets; for Progetto the QS 1 to 3 floor is the cause, not the auction. Filutowski's catch-all loses on budget, not rank, which is the money leak in one number.

## Prioritized weekly action plan

1. **Critical, Tom today: Patio Style directions.** Confirm the demotion was not intended, set the GA4 get_directions import back to primary and included, keep the GTM action secondary. Then remove the three phrase brand keywords added Sep 16. Without step one the account's primary conversion is invisible to bidding and reporting.
2. **Critical, Tom: Filutowski scope decision.** Three weeks in, $6,603 visible waste in 30 days and the budget went up. Either REK is engaged and deep dive 1 items 1 to 3 go to Accalia this week, or the routine records the account as excluded.
3. **Critical, REK: Precision GPR.** The negative list (item 1), pause Location and DSA (item 2), cap or pause the GPR Scanning keywords (item 3). Dave's Sep 22 pass did not touch any of these and the account spent $622 this week for 4 conversions.
4. **Critical, REK: Scootz form test.** Four weeks without a change. Manual form submit, restore GA4 form_submit to primary, then the split.
5. **High, Tom: the three new accounts.** Confirm REK manages Quality Paralegal Services and decide on lawyer-term traffic; fix its disapproved ad and the two RSA-less groups. Color Masters: manual conversion test and the five negatives before the second week closes. M&S: cap "driveway paving companies".
6. **High, REK: Florida Sealcoating.** Competitor and supplier negatives (three weeks outstanding), "sealcoat florida" phrase negative in Branded, and confirm the $125 a day total with the client.
7. **High, REK: Aqua Coat and All Phase.** Attach each master negative list to the live campaign (one click each, both accounts have leaked the same retailer names for three weeks). Aqua Coat: pause Pool Equipment. All Phase: phrase leslie and pinch a penny.
8. **Medium, REK: Rover.** Pause "katie matzke" and "rover pet euthanasia", rebuild the POOR Competitors RSA, add the seven negatives.
9. **Medium, REK: Progetto.** Ceilings back to $4 on Motorized and Shutters, pause Exterior & Patio and Drapery, address the QS 1 landing pages before adding spend.
10. **Medium, REK: The Counseling Group.** Tel-tap manual test (47 days), pause "help with depression" and "stress therapy", replace the POOR Depression RSA.
11. **Low: Affordable Critter** tracking cleanup and the $15 ask; **All Phase Jacksonville** pause the Orlando campaign; **Patio Style** un-pause the second RSAs.

## Rotation

Deep-dived this run: Filutowski Eye Institute, Precision GPR, Patio Style, Aqua Coat, Affordable Critter Solutions. Due next Monday: Rover Veterinary Care (measure the Sep 16 rebuild at three weeks), Scootz (tracking check), Progetto Shades (first full dive), All Phase Pool Remodeling. The week after: The Counseling Group (October), Florida Sealcoating, Color Masters and Quality Paralegal Services once they have 30 days.

## Data notes

- Account discovery returned 30 client accounts; the Sep 14 list had 26 and all 26 are still present. Compare next week against this run's list.
- The google-ads Python library installed this run (33.0.0) supports API v23 to v25 only; tools/gaql.py defaults to v22 and was run with GOOGLE_ADS_API_VERSION=v25. Consider changing the default.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor. Filutowski's strict floor excludes any term containing lasik, laser, smile, prk, cataract or the practice name, and counts only named competitor practices and doctors, retail optical chains, insurers and Spanish queries.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Aug 30 (the API allows 30 days). Conversion action edits are not included in change history, which is why the Patio Style demotion cannot be attributed.
- Week-over-week for Florida Sealcoating is search only; the display remarketing campaign spent $34 this week for 1 conversion.
- Weekly conversion-by-action tables use Google's Monday-start weeks; the Aug 29 to 30 days of the 30-day window fall in the Aug 24 week, so 30-day totals and the sum of the six weekly columns differ slightly.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
