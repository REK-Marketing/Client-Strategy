# PPC Weekly Audit - 2026-11-02 (Google Ads fleet)

Run: Monday Nov 2, 2026, scheduled cloud session through tools/gaql.py (API v24) against MCC 656-695-7229. Windows: 30 days Oct 3 to Nov 1; this week Oct 26 to Nov 1; last week Oct 19 to Oct 25. Score deltas are against the Sep 14 report, the last run with Google Ads data (seven weeks ago, so the deltas cover seven weeks of changes, not one). Change history covers Oct 4 to Nov 2 only (the API limit is 30 days). Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every REK-managed search account was sweep-scored. Deep dives: Filutowski Eye Institute (worst score), Patio Style (12-point drop), Progetto Shades (new score, second worst), Precision GPR (third worst), Quality Paralegal Services (new under the MCC, REK-built). One-liners for the rest.

The Google Ads credential (google-ads.yaml dated Sep 8 in the Drive folder dave-ads-setup) authenticated on the first try. It was copied with mode 600, read only by the client library, and deleted before this report was written. The installed google-ads client (35.0.0) no longer ships API v22, so the run used v24; tools/gaql.py still defaults to v22 and needs GOOGLE_ADS_API_VERSION=v24 until the default is bumped.

## Attention items (read first)

1. **Nothing vanished from the MCC.** All 26 accounts from the Sep 14 list are still linked (30 active links, 16 inactive, 1 pending to customer 325-901-5827, which nobody has accepted yet). Four accounts are new since Sep 14: Color Masters (426-092-9847, search, REK-built, paused Oct 22), Color Masters LSA (163-445-9282), Quality Paralegal Services (447-153-2607, search, REK-built) and All Phase Pool Remodeling (Orlando LSA) (355-287-7099).
2. **Patio Style lost its primary conversion.** Every Get Directions action (the GA4 import, the GTM webpage action from Sep 11, and the Google-hosted local action) is now secondary and excluded from Conversions. The account recorded 12 primary conversions on $2,037 in 30 days ($170 each); directions-type actions recorded 153 in all_conversions over the same window. The protocol says Get Directions as primary is the client's intent. Conversion-action edits do not appear in change history, so the date and author are unknown. Either this was a deliberate decision after Sep 14 (then the protocol note needs updating) or the account's bidding and reporting have been running against the wrong goal for weeks. Score 66 to 54. Deep dive 2.
3. **Progetto Shades spent $2,501 for 3 primary conversions ($834 each), and $837 this week for zero.** Six Maximize Clicks campaigns with CPC ceilings, 39 enabled keywords at Quality Score 1 to 3 carrying $809, landing page experience BELOW_AVERAGE on almost every scored keyword, and the website call action excluded from Conversions. The search terms themselves are mostly on topic; this is a landing page and tracking problem, not a waste problem. Tom raised budgets Oct 20 and Oct 30 and lowered CPC ceilings Oct 26. Score 56 F. Deep dive 3.
4. **Filutowski Eye Institute is still spending $11,096 in 30 days on one broad keyword.** "lasik treatment cost" broad matched 702 visible competitor, optical-chain, insurer and doctor-name searches worth $4,297 (13 conversions, $330 each) and only $323 of LASIK-intent searches. Accalia Marketing cut the campaign budget from $455 to $211 a day on Oct 29, which is the first real change since the account appeared. Account conversions fell from 354 (Sep 14 window) to 174, CPA $49 to $94. Enhanced conversions for leads is still ON for a medical practice. Still no REK edits in change history; scope still needs Tom's call. Deep dive 1.
5. **Herrell Plumbing is no longer client-run only.** Tom paused a Smart campaign on Oct 30 and set a $33 a day budget on "Herrell Plumbing - Search", which is ENABLED, in bidding-strategy learning, has six ad groups with four POOR responsive search ads, and has spent nothing in 30 days. The protocol note says Herrell is LSA-only and client-run. Either the search campaign is intended (then it joins the scored list next week and needs ads work before it spends) or it should be paused. Not scored this week.
6. **The Counseling Group recorded zero primary conversions in 14 days on $291.** Two in 30 days on $590. The tel-tap action, which was zero for 33 days on Sep 14, now records (5 in all_conversions in 30 days), so the tag fires. Those 5 do not appear in the Conversions column at all, which points at the campaign-level conversion goal setting rather than the tag. Check the campaign's goals in the UI before anything else. Enhanced conversions confirmed off.
7. **Straightline Fence search is gone, not fixed.** The "vinyl fence" campaign (both ads DISAPPROVED, COMPROMISED_SITE) was removed; Tom removed its criteria Oct 15. The account now runs LSA only ($2,384, 18 leads in 30 days, Robbie raised the budget to $85.71 a day Oct 27). Out of scope from here; worklist item 18 closes.
8. **Recommendations auto-apply is removing keywords.** "Recommendations Auto-Apply" removed an exact keyword at Scootz on Oct 8 and 19 keywords at Byers Fence on Oct 8 and 18. Scootz is REK-managed; turn auto-apply off there.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 30 client accounts, 1 manager | 13 | 4 new since Sep 14. Excluded: Byers Fence x2 and Herrell Plumbing (not REK-managed PPC), 11 LSA-only or LSA-out-of-scope accounts. Not scorable: Color Masters (paused Oct 22), REK Marketing (own account, reported), Jupiter Boat Supply and Spectrum Electric (no campaigns), All Phase Jacksonville (no search spend). |

Search, Performance Max and display spend in the 30-day window: $34,852 across the 13 scored accounts, of which $16,363 is Filutowski Eye Institute and $18,489 is the other twelve REK-managed accounts. Components of the $18,489: Florida Sealcoating $3,031, Precision GPR $3,004, Progetto Shades $2,501, Rover $2,356, Patio Style $2,037, Scootz $1,473, Quality Paralegal $1,333, All Phase $833, The Counseling Group $590, M&S Asphalt $587, Aqua Coat $447, Affordable Critter $297. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $16,363 | 174 | $94 | 44 | F | +2 | Critical (scope) | One broad keyword is 68 percent of spend; $4,297 visible on competitor, chain, insurer and doctor-name searches; enhanced conversions ON | $4,297 |
| 2 | Patio Style | 596-555-8707 | $2,037 | 12 | $170 | 54 | F | -12 | Critical | All three Get Directions actions demoted to secondary; 11 of 12 ad groups still one RSA; bidding changed three times in ten days | $45 |
| 3 | Progetto Shades | 416-010-8247 | $2,501 | 3 | $834 | 56 | F | new | Critical | 0.5 percent conversion rate; 39 keywords at QS 1 to 3 ($809); landing pages BELOW_AVERAGE; website call action excluded | $101 |
| 4 | Precision GPR | 554-113-4760 | $3,004 | 21 | $143 | 56 | F | +6 | Needs attention | Sep 4 change list still not applied (gprs negatives, Location and DSA live); brand campaign broad keyword leaking generic terms; two website call actions still zero | $223 |
| 5 | Quality Paralegal Services | 447-153-2607 | $1,333 | 46 | $29 | 60 | D | new | Needs attention | Converts well, but top keyword "family law attorney near me" broad is QS 1 and lawyer-intent for a non-lawyer; 5 of 5 ad groups one RSA (one POOR); 77 percent broad | $125 |
| 6 | The Counseling Group | 657-069-3617 | $590 | 2 | $295 | 61 | D | -5 | Needs attention | Zero primary conversions in 14 days; tel-tap fires but is not counted; "therapist near me" exact QS 2 | $93 |
| 7 | Rover Veterinary Care | 750-667-5721 | $2,356 | 19 | $124 | 62 | D | +1 | Needs attention | Master negative list not attached to In-Home or Pet Cremation campaigns; new $45-CPC keyword spent $226 for 0; Competitors RSAs still POOR | $190 |
| 8 | Florida Sealcoating | 168-852-7101 | $3,031 | 29 | $105 | 63 | D | 0 | Needs attention | Sep 4 competitor negatives still absent; $960 on 16 zero-conversion keywords; QS 1 on "driveway repair near me" | $86 |
| 9 | Scootz | 185-574-5478 | $1,473 | 30 | $49 | 64 | D | +6 | On target | Conversions back (Booqable 20, calls 10); form_submit still dark; still one ad group; auto-apply removed a keyword | $49 |
| 10 | Aqua Coat Pool Plastering | 285-714-0527 | $447 | 14 | $32 | 65 | D | +1 | On target | 248-member master list still attached only to the paused campaign; Pool Equipment group still live | $93 |
| 11 | All Phase Pool Remodeling | 103-111-7688 | $833 | 12 | $69 | 69 | D | -3 | On target | Brand term still 51 percent of spend inside non-brand groups; 100 percent broad; 1 conversion this week | $72 |
| 12 | M&S Asphalt Paving | 827-724-4095 | $587 | 5 | $117 | 69 | D | reactivated | On target | Relaunched Oct 15; negatives landed; 5 of 6 ad groups one RSA; one call action categorized as a form | none confirmed |
| 13 | Affordable Critter Solutions | 227-108-4521 | $297 | 15 | $20 | 77 | C | +1 | On target | Clean; 11 paused campaigns still there; 60 percent rank-lost at $10 a day | $14 |
| none | Color Masters | 426-092-9847 | $919 | 3 | $306 | n/a | paused | new | Paused | REK-built Oct, paused Oct 22 after $892 for 3 conversions on Residential Painting; QS 2 on "painting companies" | n/a |
| none | REK Marketing | 390-315-5264 | $241 | 0 | n/a | n/a | own | was paused | Watch | GBP Verification campaign built Oct 23 to 29, $223 for 0 conversions, 70 percent lost to budget; Philadelphia and San Diego campaigns live Nov 1 | n/a |
| none | Herrell Plumbing | 113-422-7395 | $2,240 Smart (paused) | 215 | $10 | n/a | excluded | n/a | Scope | See attention item 5 | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 | 0 | n/a | n/a | no search spend | n/a | Paused (search) | "Orlando" campaign still ENABLED and NOT_ELIGIBLE (ad groups paused, missing lead form). Worklist item 6 still open, nothing leaking | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | LSA only now | n/a | Closed | Search campaign removed; see attention item 7 | n/a |
| none | Jupiter Boat Supply, Spectrum Electric | | $0 | 0 | n/a | n/a | no campaigns | n/a | Idle | No campaigns at all | n/a |

## Week over week (Oct 26 to Nov 1 against Oct 19 to Oct 25, search, PMax and display only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $3,367 to $3,071 (-9%) | 205 to 175 | 5.6% to 5.3% | $16.43 to $17.55 | 35 to 22 | $96 to $140 | Budget cut Oct 29; Branded 15 to 5 conversions; Lead Gen LASIK $249 for 0 |
| Precision GPR | $625 to $917 (+47%) | 42 to 68 | 4.7% to 6.1% | $14.89 to $13.48 | 5.5 to 5 | $114 to $183 | Off target; Location $241 for 0, Branded $134 for 0 |
| Patio Style | $436 to $502 (+15%) | 218 to 186 | 7.7% to 6.9% | $2.00 to $2.70 | 1 to 4 | $436 to $126 | Primary counts only calls and forms now; see deep dive 2 |
| Progetto Shades | $689 to $837 (+21%) | 132 to 177 | 5.3% to 5.7% | $5.22 to $4.73 | 2 to 0 | $345 to none | Off target |
| Quality Paralegal Services | $350 to $316 (-10%) | 112 to 93 | 5.4% to 5.3% | $3.13 to $3.39 | 13 to 5 | $27 to $63 | Calls from ads 9 to 5, forms 4 to 0 |
| The Counseling Group | $136 to $155 (+14%) | 32 to 37 | 6.5% to 5.4% | $4.26 to $4.18 | 0 to 0 | none | Off target, small numbers |
| Rover Veterinary Care | $597 to $683 (+14%) | 61 to 47 | 12.2% to 13.4% | $9.78 to $14.54 | 4 to 7 | $149 to $98 | Improving; CPC up 49 percent on In-Home ($381 this week) |
| Florida Sealcoating | $832 to $641 (-23%) | 82 to 75 | 7.0% to 5.5% | $10.15 to $8.55 | 8 to 7 | $104 to $92 | Flat; display remarketing included ($33 a week) |
| Scootz | $357 to $319 (-11%) | 250 to 378 | 7.8% to 7.0% | $1.43 to $0.84 | 5 to 5 | $71 to $64 | Flat |
| Aqua Coat | $90 to $119 (+33%) | 12 to 26 | 2.6% to 5.4% | $7.47 to $4.58 | 2 to 4 | $45 to $30 | Fine |
| All Phase Pool Remodeling | $223 to $168 (-25%) | 28 to 15 | 7.0% to 3.4% | $7.97 to $11.18 | 5 to 1 | $45 to $168 | Watch; one week |
| M&S Asphalt Paving | $186 to $183 (-2%) | 16 to 18 | 7.4% to 9.1% | $11.64 to $10.19 | 2 to 1 | $93 to $183 | Small numbers |
| Affordable Critter Solutions | $68 to $63 (-8%) | 22 to 13 | 11.6% to 8.5% | $3.10 to $4.85 | 1 to 2 | $68 to $32 | Flat |
| Color Masters | $168 to $0 | 18 to 0 | | | 0 to 0 | | Paused Oct 22 |
| REK Marketing | $55 to $186 | 5 to 20 | 6.1% to 4.0% | $10.96 to $9.31 | 0 to 0 | none | New campaigns, no conversions yet |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share (30 days) is the proxy. Highest rank loss: Progetto Drapery 73 percent, M&S Sealcoating 72 percent, Patio Style Outdoor Furniture 64 percent (by design, $2.50 ceiling), Affordable Critter 60 percent, Progetto Shades & Blinds 59 percent, Aqua Coat 53 percent, Patio Style Outdoor Kitchens 52 percent, M&S Paving 49 percent. Highest budget loss: Filutowski Brand Awareness 88 percent and Branded 80 percent, Patio Style Brand 66 percent and Pergolas 64 percent, Precision GPR Branded 58 percent, All Phase 55 percent, The Counseling Group 55 percent. Largest CPC increases this week: Rover ($9.78 to $14.54), All Phase ($7.97 to $11.18), Affordable Critter ($3.10 to $4.85).

## Changes made in the past week (Oct 26 to Nov 2) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Progetto Shades | Oct 26 | Tom | CPC ceilings lowered on three Maximize Clicks campaigns ($12 to $10, $12 to $9, $18 to $12) | Average CPC $5.22 to $4.73, clicks 132 to 177, conversions 2 to 0. More clicks, no leads. |
| Progetto Shades | Oct 30 | Tom | Shades & Blinds budget $40 to $50 a day | $325 this week for 0 conversions in that campaign. |
| Patio Style | Oct 27 and 28 | paidads@rekmarketing.com | Budgets: one campaign $10 to $25, another $14 to $5, then $5 to $20 | Current budgets: Outdoor Furniture $30, Pergolas $25, Outdoor Kitchens $20, Brand $10. |
| Patio Style | Nov 1 and 2 | paidads@rekmarketing.com | Two ad groups paused; a campaign moved from Maximize Clicks ($7 ceiling) to Manual CPC with Enhanced CPC off; ad group bids set to $5 and $10 | Too early to measure. Pergolas and Outdoor Kitchens are now Manual CPC, Outdoor Furniture is Maximize Clicks at $2.50, Brand is Maximize Conversions (moved off Target Impression Share Oct 23). |
| Filutowski Eye Institute | Oct 29 | catie@accaliamarketing.com | Brand Awareness budget $455 to $255 to $243 to $211 a day | Campaign spend $2,252 to $2,109 this week. The keyword is unchanged. |
| Precision GPR | Oct 29 | sheokand003@gmail.com | Two RSAs edited, one RSA added | 25 of 47 live RSAs now EXCELLENT. |
| Quality Paralegal | Oct 23 (just outside the week, listed because it is the latest change) | Tom | 18 price and immigration-status negatives (fee, fees, how long, how much, valid, expiration, lottery, bulletin, priority date, eoir, costo, cuesta, cuanto, precio, loteria, boletin); immigration RSA edited | Price queries gone from the Immigration campaign's visible terms this week. |
| Rover | Oct 29 | sheokand003@gmail.com | Pet Cremation RSA edited | Too early. |
| Florida Sealcoating | Oct 30 | sheokand003@gmail.com | Two new RSAs, a bid modifier, a budget change, two campaign criteria | Too early. Daily budgets now Commercial $38, Residential $30, Branded $15, Remarketing $5 ($88 a day). |
| Aqua Coat | Oct 27 to 30 | sheokand003@gmail.com | New RSA, one keyword, 15 assets | Conversions 2 to 4 this week. |
| Affordable Critter | Oct 29 | sheokand003@gmail.com | New RSA, two keywords, two campaign assets removed, campaign setting change | Conversions 1 to 2. |
| The Counseling Group | Oct 26 | Tom | Budget $25 to $26.50 a day | On plan; still 0 conversions. |
| REK Marketing | Oct 26 to Nov 2 | Tom | GBP Verification campaign built out (negatives, assets, ads), Philadelphia and San Diego campaigns live Nov 1 | $186 this week, 0 conversions. |
| Herrell Plumbing | Oct 28 to Nov 2 | Tom, Robbie | Smart campaign paused Oct 30, $33 a day on the search campaign, LSA budget $78.57 Nov 2, assets | See attention item 5. |
| Straightline Fence | Oct 27 | Robbie | LSA budget to $85.71 a day, five assets | LSA only. |
| Scootz, All Phase, M&S, Color Masters | | | No changes this week | |

Earlier in the window (Oct 4 to Oct 25), for the record: Tom rebuilt Progetto's geo targeting and removed four legacy campaigns (Oct 19), rebuilt Quality Paralegal (Oct 14 to 19: assets, call asset, campaign re-enabled, Smart campaign paused, about 100 negatives), paused Color Masters (Oct 22), relaunched M&S Asphalt (Oct 15), rewrote three Counseling Group RSAs (Oct 20), cut Precision GPR's GPR Scanning budget $20 to $15 (Oct 21), and added an exact "scooter rental near me" keyword at Scootz (Oct 22). Dave (sheokand003@gmail.com) raised Rover's Competitors budget $5 to $20 and set keyword bids (Oct 6), added seven euthanasia-question keywords at Rover (Oct 23), swapped 22 keywords in and 17 out at Aqua Coat (Oct 22), added seven keywords and bid modifiers at Florida Sealcoating (Oct 23), and added the "red rhino jacksonville" negative at All Phase (Oct 22). Catie (Accalia) raised Filutowski's target CPAs and added ad schedules (Oct 15).

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

Landed: item 3 (Patio brand, Sep 4; Brand has since moved to Maximize Conversions), item 14 YouTube half, item 18 (closed by removing the campaign), item 10 half (tel-tap tag fires; enhanced conversions off). Partly: item 4 ("panels" and "roof panels" are now phrase negatives in Patio Style's master list; "outdoor grill island" still live; retail-brand negatives absent), item 8 (three RSAs rewritten Oct 20; "help with depression" and "stress therapy" still enabled), item 15 ("sealcoat florida" is a phrase negative; competitor names still absent; remarketing serves). Not landed: items 5, 6, 7, 12, 13, 16, 17, 19. Item 16 note: the Oct 23 Rover additions are question-type positive keywords, not the negatives the item asked for.

## Deep dive 1: Filutowski Eye Institute (192-870-7876), score 44 F, provisional

Scope note: still no REK user in change history. Editors are catie@accaliamarketing.com and web@filutowski.com. Tom's Drive holds a sheet "FEI New Website URL Changes (for Google Ads)" dated Oct 19, which suggests REK is at least coordinating. Score and change list are prepared so Tom can decide; coordinate with Accalia before anything is applied.

| Category | Sep 14 | Now |
|---|---|---|
| Conversion Tracking | 45 | 55 |
| Wasted Spend | 25 | 25 |
| Account Structure | 50 | 50 |
| Keywords & Targeting | 35 | 35 |
| Ads & Assets | 50 | 45 |
| Bidding & Settings | 50 | 55 |

Snapshot, 30 days: five enabled search campaigns, $16,363, 174 primary conversions at $94. All five are BUDGET_CONSTRAINED. Twenty-two paused or removed legacy campaigns.

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | CPA | Search IS | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| S / Brand Awareness / LASIK | $211 (was $455) | $11,096 | 463 | $23.96 | 55.5 | $200 | 10.0% | 87.7% |
| S / Branded / Dr. F | $50 | $1,382 | 309 | $4.47 | 71.0 | $19 | 18.2% | 79.6% |
| S / Lead Gen / LASIK | $50 | $1,326 | 73 | $18.16 | 6.0 | $221 | 46.0% | 34.3% |
| S / Lead Gen / Cataracts | $50 | $1,284 | 148 | $8.68 | 12.0 | $107 | 35.0% | 46.4% |
| S / Lead Gen / Eye Surgery | $50 | $1,275 | 215 | $5.93 | 29.5 | $43 | 13.9% | 72.1% |

### Findings

**The broad keyword is still the account.** "lasik treatment cost" broad, Target CPA, is 68 percent of spend ($11,096, 55.5 conversions at $200). Of its $7,977 in visible search-term cost, $323 went to 159 LASIK, laser, SMILE or PRK searches (2 conversions) and $4,297 went to 702 searches naming other practices, optical chains, insurers or individual doctors (13 conversions, $330 each). Largest buckets: Florida Eye Clinic 88 terms $902, doctor names ("dr ...") 158 terms $438, optometrist 38 terms $436, Tomoka Eye 12 terms $403, My Eye Doctor 23 terms $285, Florida Blue $205 on one click, America's Best 57 terms $188, Lasik Vision Institute $140, Medicaid 14 terms $131, Total Vision $104, Target Optical $100, Garay $100. Spanish queries $109. The campaign is a catch-all for any eye search in Central Florida at $24 a click.

**Brand and Eye Surgery are still starved.** Branded converts at $19 and loses 80 percent of impressions to budget at $50 a day; Eye Surgery converts at $43 and loses 72 percent. Those two campaigns produced 100 of the 174 conversions on $2,657.

**Conversion tracking improved, two items remain.** The 18 hidden Universal Analytics goals from Sep 14 are no longer enabled (resolved). Still open: enhanced conversions for leads is ON (medical practice, no BAA on file per protocol); "YouTube follow-on views" is still primary and included; three call actions are all primary (800 general line, 407 CallRail LASIK line, Phone Link Click), so one caller can count up to twice; "Phone Calls (Dialed From Website)" recorded 9 in all_conversions and 0 in Conversions.

**Keywords and ads.** 1,296 enabled keywords, 68 percent of spend on broad. Eleven enabled keywords at QS 1 to 3 carry $1,103, led by "eye specialist near me" ($318, 4 conv), "ophthalmologist near me" ($280, 8 conv) and "eye doctor near me" QS 1 ($211, 5 conv), all BELOW_AVERAGE expected CTR and ad relevance. "lasik eye surgery" exact in Lead Gen LASIK spent $540 on 31 clicks for 0 conversions. Every one of the five live ad groups still has a single RSA; the Branded RSA is POOR and the Cataracts RSA AVERAGE. Cataracts and Eye Surgery still report HAS_ADS_DISAPPROVED; the live ads are all APPROVED, so the disapproved ads are in paused groups or are not RSAs; detail unavailable this run.

**Changes by Accalia.** Oct 15: target CPAs raised on all five campaigns (for example $15 to $50 on Branded, $30 to $50 on Eye Surgery, $100 to $200 then $200 to $150 on Cataracts), 20 ad-schedule criteria added, one RSA rewritten. Oct 29: Brand Awareness budget $455 to $211. The budget cut is the right direction; the keyword is the problem.

### Prepared change list (only if Tom confirms REK is engaged)

1. Replace "lasik treatment cost" broad with a phrase and exact LASIK set (lasik, lasik cost, lasik near me, lasik orlando, lasik lake mary, smile eye surgery, prk surgery, laser eye surgery). Hold the campaign at $211 a day or lower until two weeks of data exist.
2. Shared negative list on all live campaigns, phrase match. New this run and absent from the 34-member "Search Terms" list: florida eye clinic, florida eye, tomoka, mid florida eye, my eye dr, total vision, lasik vision institute, eye physicians, eyephy, elite eye, innovation eye, fishman, true eye, coan, garay, uptown, florida blue, medicaid, eyemed, cigna, aetna, spectera, ambetter, humana, zocdoc, optometrist, oftalmologo, oftalmologos, cerca de mi, pediatric, kids, retina, contacts, warby, and the doctor names seen this window (samantha xavier, dr george, dr yip, dr pal, dr blick, sunali goyal, den beste). Already present, skipped: my eye doctor, target optical, stanton optical, america's best, americas best, walmart, lenscrafters, costco, visionworks, pearle, eyeglasses near me. Note "optometrist near me" exists only as an exact ad-group negative; the phrase form is still needed.
3. Move the freed budget to Branded ($50 to $100 a day) and Eye Surgery ($50 to $80).
4. Turn enhanced conversions for leads off unless a BAA exists. Set YouTube follow-on views secondary. Keep one primary call action per phone line.
5. Second RSA in each of the five live ad groups; rebuild the POOR Branded RSA first.

## Deep dive 2: Patio Style (596-555-8707), score 54 F, down 12

Context applied: the client's primary conversion is Get Directions, then calls, then contact forms (protocol). Directions counted as primary is intended, so the demotion is the finding.

| Category | Sep 14 | Now |
|---|---|---|
| Conversion Tracking | 60 | 35 |
| Wasted Spend | 70 | 75 |
| Account Structure | 65 | 65 |
| Keywords & Targeting | 60 | 55 |
| Ads & Assets | 50 | 45 |
| Bidding & Settings | 70 | 55 |

| Campaign | Bidding now | Budget/day | Spend | Clicks | CPC | Primary conv | All conv | Search IS | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|---|
| Outdoor Furniture | Maximize Clicks, $2.50 ceiling | $30 | $891 | 638 | $1.40 | 8 | 493 | 12.4% | 24.1% | 63.5% |
| Pergolas & Louvered Roofs | Manual CPC (since Nov 1) | $25 | $458 | 46 | $9.96 | 1 | 15 | 13.7% | 63.7% | 22.6% |
| Outdoor Kitchens | Manual CPC (since Nov 1) | $20 | $458 | 128 | $3.58 | 0 | 18 | 25.2% | 22.8% | 52.0% |
| Brand | Maximize Conversions (since Oct 23) | $10 | $230 | 75 | $3.07 | 3 | 53 | 10.8% | 65.5% | 23.7% |

### Findings

**Conversion goals.** Primary and included today: Calls from ads (6), Website Call Conversions 11 Sep (3), Thank you page 11 Sep (3). Twelve primary conversions in 30 days. Secondary and excluded: www.patiostyle.com GA4 get_directions (42 in all_conversions), Get directions (GTM) 11 Sep (37), Local actions Directions (74), Store visits (12), GA4 click_to_call (6), GA4 generate_lead (3). On Sep 14 the GA4 directions import was primary and the account showed 166 conversions at $12. Whoever demoted directions solved the Sep 14 double-count question by removing both actions from Conversions. The Brand campaign is now on Maximize Conversions with 3 countable conversions in 30 days, so it is optimizing to calls and forms only. Two actions created Sep 29, "Phone Call Click 29/ Sep" and "Send a messages landing page 29 Sep", are categorized GET_DIRECTIONS; they recorded nothing and should be recategorized or removed.

**Bidding churn.** Oct 23: AI Max turned off, Brand moved off Target Impression Share. Oct 27 and 28: three budget changes. Nov 1: a campaign moved from Maximize Clicks ($7 ceiling) to Manual CPC, two ad groups paused. Nov 2: ad group bids set to $5 and $10. None of this can be judged yet, and none of it addresses the goal problem above. Worklist item 13 (Outdoor Furniture to Maximize Conversions) is moot until directions is primary again.

**Keywords.** 26 keywords spent more than $10 with zero primary conversions ($1,052), but 20 of them carry directions or call all_conversions, so this list is unreliable until the goals are fixed. Ten enabled keywords at QS 1 to 3 carry $148: "patio cover orlando" QS 3 $49, "built in outdoor kitchen" QS 1 $28, "outdoor fire pit" QS 3 $24, "outdoor grill island" QS 3 $22 (worklist item 4 asked to pause it), "outdoor dining set" QS 2 $14. "pergola contractor" phrase (New Pergolas 07 Oct group) spent $148 at $14.80 a click for 0 primary and 2 all_conversions. The paused "patio styles" phrase keyword spent $104 on 28 clicks before it was paused (Oct 15).

**Search terms.** Clean. Confirmed waste $45: "handyman to install pergola" $13, "four seasons aluminum patio cover" $17 (a competitor manufacturer, 2 all_conversions, confirm with the client), "outdoor kitchen ideas" $15. "azenco" and "mirador" are brands the store carries; "mirador" is now a phrase negative in the master list, which will block "miradoroutdoor pergola" ($13, 2 all_conversions) if that is a stocked brand; confirm.

**Ads.** 11 of 12 live ad groups have one RSA (unchanged since Sep 4). "New Pergolas 07 Oct" is POOR, "Premium Brands" AVERAGE.

### Prepared change list

1. Decide the goal first. If directions is still the client's primary conversion, set one directions action primary and included (the GTM webpage action from Sep 11 or the GA4 import, not both) and leave the Google-hosted local action secondary. Then let Brand's Maximize Conversions and any later Outdoor Furniture bidding change learn from it. If REK decided to count only calls and forms, update the protocol's Patio Style note so this stops being flagged.
2. Recategorize or remove the two Sep 29 actions labelled GET_DIRECTIONS.
3. Stop changing bidding until two weeks after item 1 lands.
4. Pause "outdoor grill island" (worklist item 4), rewrite the POOR New Pergolas RSA, second RSA in the three highest-spend single-ad groups (Patio Furniture - Local, New Outdoor Kitchens, Louvered Pergolas).
5. Negatives, phrase: handyman, ideas (phrase; only three exact "ideas" negatives exist), big green egg, tru island, vestivium, hampton bay, polywood. Confirm "four seasons" and "mirador" with the client before blocking.

## Deep dive 3: Progetto Shades (416-010-8247), score 56 F, first score

Context: San Diego window-covering retailer (858 area code; geo criteria rebuilt by Tom Oct 19). Six search campaigns relaunched Sep 10, all Maximize Clicks with CPC ceilings. Sep 14 one-liner recommended Maximize Clicks with a $4 ceiling during learning; the ceilings are $9 to $12 on the four main campaigns.

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 65 |
| Account Structure | 75 |
| Keywords & Targeting | 35 |
| Ads & Assets | 50 |
| Bidding & Settings | 55 |

| Campaign | Ceiling | Budget/day | Spend | Clicks | CPC | Conv | All conv | Search IS | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|---|
| Shades & Blinds | $10 | $50 | $1,008 | 267 | $3.78 | 1 | 22 | 14.4% | 26.9% | 58.6% |
| Shutters | $12 | $30 | $598 | 95 | $6.30 | 0 | 1 | 29.5% | 29.6% | 40.8% |
| Motorized & Smart | $9 | $16 | $401 | 68 | $5.90 | 0 | 2 | 23.1% | 23.7% | 53.3% |
| Drapery & Curtains | $12 | $12 | $281 | 54 | $5.20 | 1 | 6 | 19.1% | 7.5% | 73.4% |
| Exterior & Patio | $4 | $7 | $204 | 66 | $3.08 | 0 | 1 | 17.0% | 25.4% | 57.6% |
| Brand | $2 | $5 | $10 | 6 | $1.66 | 1 | 7 | 80.0% | 5.0% | 15.0% |

30 days: $2,501, 556 clicks, 3 primary conversions ($834 each), 39 all_conversions of which 31 are Google-hosted local actions. This week $837 for 0. Mobile is 91 percent of spend ($2,286, all 3 conversions).

### Findings

**The traffic is on topic; the pages do not convert it.** Of $1,517 in visible search-term cost, $1,170 is generic window-covering intent (shutters, plantation shutters, blackout curtains, drapes, window shutters interior, electric blinds, motorized blinds), $197 is designer-brand searches (Hunter Douglas, Norman, Somfy, Silhouette), $70 is informational, $31 is retailers (Macy's), $50 is San Diego-qualified. Zero of the 2,606 visible terms converted. A 0.5 percent conversion rate on 556 clicks of commercial intent is a landing page or offer problem.

**Quality Score confirms it.** 39 enabled keywords at QS 1 to 3 carry $809. Landing page experience is BELOW_AVERAGE on "window shutters" exact (QS 3, $119), "shutters for windows" phrase (QS 1, $105), "hunter douglas" (QS 3, $76), "outdoor patio shades" (QS 2, $72), "blackout curtains" exact (QS 2, $59), "smart shades" (QS 3, $45), "somfy shades" (QS 1, $33), "automated shades" (QS 3, $30), "roller shades" (QS 2, $27). The landing pages are /lp/shutters, /lp/shades, /lp/blinds, /lp/motorized, /lp/drapery, /lp/exterior. Expected CTR is BELOW_AVERAGE on every one of them, so the ads are not winning the click either.

**Tracking is under-counting the leads that do happen.** "Call ((858) 338-1678)" (website call) is primary but excluded from Conversions (1 call in all_conversions, 0 counted). "Lead form website" (GA4) is secondary (1). "Web form (start)" secondary (1). "Financing inquiry" secondary (1). Primary and counted: Contact (2), Calls from ads (1). Before judging the account on 3 conversions, make the website call action count and decide whether the GA4 lead form duplicates "Contact".

**Ads.** 12 of 15 live RSAs are AVERAGE; Exterior, Brand and Designer Brands have one RSA each.

**Bidding.** Maximize Clicks is right for an account with no conversion history, but $2,501 a month at $4.50 a click with the ceilings at $9 to $12 is buying volume the pages cannot close. Budgets went up Oct 20 (Shutters $22 to $30) and Oct 30 (Shades & Blinds $40 to $50) while the conversion rate was collapsing.

### Prepared change list

1. Tracking first: include the (858) website call action in Conversions; decide whether "Lead form website" (GA4) or "Contact" is the form action and keep one primary; check that the call-tracking number on the /lp/ pages is the one the action watches.
2. Landing pages: the six /lp/ pages need a visible phone number, a short quote form above the fold, San Diego in the headline and reviews. Until that is done, cut Shades & Blinds to $30 and Shutters to $20 a day (saves about $900 a month at current pace) rather than feeding more clicks to the same pages.
3. Pause the QS 1 and QS 2 keywords that have spent more than $25 with no lead: "shutters for windows" phrase, "outdoor patio shades", "blackout curtains" exact, "somfy shades", "roller shades". Leave QS 3 keywords until the pages are fixed.
4. Negatives, phrase, to iLP Global Negatives (329 members): macy's, macys, what are, what is, recommend, attach, configuration, arched, fabrics, for sale, metal, hurricane, the blind and shutter pros, smart wings. Already present, skipped: how to, ideas, diy, amazon, ikea, home depot, lowes, walmart, target, wayfair, costco, curtain rod, fabric, wholesale, jobs, cheap, clearance, exterior shutters. Do not block hunter douglas, norman or somfy; those are products the store sells and "hunter douglas" carried 1 all_conversion.
5. Second RSA in Exterior, Brand and Designer Brands; rewrite the AVERAGE Shades, Blinds, Motorized and Drapery RSAs with the keyword in headline 1.
6. Keep Maximize Clicks until 15 counted conversions exist in 30 days.

## Deep dive 4: Precision GPR (554-113-4760), score 56 F, up 6

Context applied: under active cleanup since Aug 2026. Change history shows Dave's ad and keyword work Oct 10, 23 and 29 and Tom's budget cut Oct 21. The Sep 4 change list (negatives, pause Location and DSA, cap GPR Scanning) is still not applied.

| Category | Sep 14 | Now |
|---|---|---|
| Conversion Tracking | 55 | 60 |
| Wasted Spend | 40 | 50 |
| Account Structure | 50 | 50 |
| Keywords & Targeting | 40 | 45 |
| Ads & Assets | 70 | 80 |
| Bidding & Settings | 40 | 45 |

| Campaign | Budget/day | Spend | Clicks | CPC | Primary conv | CPA | This week |
|---|---|---|---|---|---|---|---|
| LP Search - Services | $18 | $542 | 31 | $17.48 | 4.0 | $135 | $149, 1 conv |
| LP Search - Concrete Scanning | $18 | $533 | 27 | $19.74 | 3.5 | $152 | $108, 2 conv |
| LP Search - GPR Scanning | $15 (was $20) | $520 | 36 | $14.44 | 2.0 | $260 | $111, 1 conv |
| LP Search - Location | $18 | $470 | 19 | $24.72 | 2.0 | $235 | $241, 0 conv |
| LP Search - Utility Mapping | $15 | $461 | 42 | $10.97 | 3.5 | $132 | $100, 0 conv |
| LP DSA - All Pages | $10 | $311 | 43 | $7.24 | 3.5 | $89 | $74, 1 conv |
| LP Branded | $10 | $168 | 20 | $8.40 | 2.5 | $67 | $134, 0 conv |

30 days: $3,004, 21 primary conversions (Michael Phone Number 8, lp_contact_form 7, Calls from ads 5, Smart campaign call 1), $143 per conversion. Sep 14 window was $2,409 for 9 at $268, so the account is better, mostly because the "Michael Phone Number (305)" website call action now records.

### What is still open and what is new

- **Negatives.** "gprs" in five visible variants cost $107 this window ("gprs orlando" $40, "gprs scanning" $27, "gprs locating" $17, "gprs orlando" $23 in Services with 1 all_conversion, "gprs" $1) and is still not a negative anywhere. Price and cost queries $35 ("gpr scanning price" $23, "ground penetrating radar price" $12). Call-before-you-dig queries $37 ("sunshine locate" $14, "who to call before digging in florida" $13, "call before digging florida" $11); "811" and "before you dig" exist as negatives but do not catch these. Engineering and competitor names $44 (beryl project engineering $14, s&n locating $12, directional boring company $12, structural engineer $6). Confirmed waste $223. Dedupe: low cost, 811, before you dig, rental, rentals, equipment, underground radar detector and three locator exacts already exist in LP NKWs; everything above is new.
- **The brand campaign's broad keyword leaks.** "precision gpr" broad ($133, 13 clicks, 0 primary conversions) matched beryl project engineering, structural engineer, directional boring company, underground company, civil engineering companies in orlando, cable locator and "underground utility locating services near me". Convert it to phrase and exact; the exact term "precision gpr" converted twice on $35.
- **Location and DSA are still enabled.** Location spent $470 for 2 conversions at $24.72 a click, $241 this week for 0; its two spending keywords are "concrete scanning services" phrase ($375, 2 conv, also served by the Concrete Scanning campaign) and "Gpr Scanning Near Me" exact (QS 3, $95, 0 conv). DSA is now the cheapest conversion source ($89), so keep it and pause Location instead.
- **Quality Score.** Six enabled keywords at QS 3 carry $268: "Gpr Scanning Near Me" exact $95, "Ground Penetrating Radar" exact $90 and phrase $84 (landing page BELOW_AVERAGE on both). "ground penetrating radar surveys" phrase spent $175 on 7 clicks at $25 for 0 conversions.
- **Conversions.** The (305) 490-0593 and (786) 508-9082 website call actions are still zero while "Michael Phone Number (305)" records 8, so the site tag works and the two silent actions watch numbers that are not on the page. Set them secondary or remove them. "Contact Us", "Contact Us (1)" and "Contact us" still coexist as secondary. Enhanced conversions is ON; not healthcare, acceptable.
- **Bidding.** Seven campaigns on Maximize Conversions with 2 to 4 conversions each; Dave removed a $14 target CPA on Oct 10. Consolidating GPR Scanning, Concrete Scanning and Services into one campaign would give the strategy about 10 conversions a month to learn from.
- **Ads improved.** Dave's Oct 10 to 29 rewrites: 25 EXCELLENT, 17 GOOD, 3 AVERAGE across 47 live RSAs.

### Prepared change list

1. Negatives, phrase, to LP NKWs: gprs, price, prices, pricing, cost, how much, sunshine, call before, who to call, locating companies, beryl, s&n, structural engineer, civil engineering, directional boring, for sale, florida (only if out-of-state queries appear; skip otherwise).
2. Brand campaign: "precision gpr" broad to phrase plus exact; add phrase negatives engineering, boring, locator to Branded.
3. Pause Location. Keep DSA. Move "concrete scanning services" to the Concrete Scanning campaign if it is not already there.
4. Pause "ground penetrating radar surveys" phrase; cap "Ground Penetrating Radar" exact and phrase at $10 or move them to Manual CPC.
5. Set the two silent website call actions secondary; merge the three Contact Us actions.

## Deep dive 5: Quality Paralegal Services (447-153-2607), score 60 D, first score

Context: new under the MCC, built and rebuilt by Tom (217 change events Oct 5 to 23, plus ines@qualitylegalservices.org and Robbie). Orlando non-lawyer document-preparation service, English and Spanish.

| Category | Score |
|---|---|
| Conversion Tracking | 70 |
| Wasted Spend | 70 |
| Account Structure | 60 |
| Keywords & Targeting | 45 |
| Ads & Assets | 40 |
| Bidding & Settings | 70 |

| Campaign | Bidding | Budget/day | Spend | Clicks | CPC | Conv | CPA | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|---|
| Looking for an experienced yet affordable Paralegal? | Max Conv, tCPA $27 | $28 | $735 | 187 | $3.93 | 29 | $25 | 31.5% | 62.3% |
| Experienced yet affordable Paralegal / con 25 anos de experiencia | Max Conv | $17 | $455 | 119 | $3.83 | 10 | $46 | 57.6% | 35% |
| QPS Immigration Document Prep | Maximize Clicks | $5 | $86 | 49 | $1.76 | 0 | n/a | 43.7% | 54.3% |
| QPS Non-Lawyer Services Orlando (Smart, paused Oct 15) | | $5 | $56 | 93 | $0.61 | 7 | $8 | | |

30 days: $1,333, 46 primary conversions at $29 (Calls from ads 34, Contact form 4, Clicks to call 2 counted of 24, Local actions Directions 5 counted of 38, website call 1). Mobile is 99.7 percent of spend. This week: 5 conversions on $316 after 13 on $350.

### Findings

- **The account converts, but on lawyer intent.** The top keyword is "family law attorney near me" broad: $306, 72 clicks, 6 conversions, QS 1 (BELOW_AVERAGE on CTR, relevance and landing page). Other enabled broad keywords: "family attorney", "family lawyers near me", "best family lawyers", "best lawyers in orlando" ($28, 0 conv), "child custody lawyers", "custody lawyers", "divorce lawyers near me" (QS 1), "family court attorney". The matched terms are "abogado de divorcio", "abogados de familia en espanol cerca de mi", "divorce lawyers orlando", "custody lawyers in orlando". A non-lawyer service buying attorney searches is both a relevance problem (QS 1) and something the client's compliance posture should confirm. Spanish attorney queries alone cost $87 in visible terms for 0 primary conversions.
- **Wasted spend floor $125:** the $87 above, "clerk of the court seminole county" $6 ("clerk of courts" phrase exists but does not match "clerk of the court"), "how to get emancipation at 17" $5, "process server" $4, "child support en espanol numero de telefono" and variants $11 (state agency phone lookups), green card fee and "how long" queries $11 (now blocked by Tom's Oct 23 negatives). Notary and apostille queries convert ("apostille orlando", "notarios cerca de mi", "kissimmee notary services" each 1 conversion) and should stay.
- **Structure.** Campaign names are ad headlines; one ad group is "Ad group 1". 978 enabled keywords, 77 percent of spend on broad.
- **Ads.** All five live ad groups have one RSA; "Ad group 1" (Spanish, $455) is POOR, the rest AVERAGE. The main campaign carries HAS_ADS_DISAPPROVED from a disapproved ad in a paused ad group ("Affordable and experienced Paralegal"); three Smart-campaign ads are APPROVED_LIMITED.
- **Bidding.** Target CPA $27 with 29 conversions in 30 days is sound. The Spanish campaign has no target and loses 58 percent of impressions to budget at $17 a day with a $46 CPA; it is the one to fund if the client wants more volume.
- **Tracking.** Enhanced conversions ON (legal services, acceptable). Four Smart-campaign conversion actions are still primary after the Smart campaign was paused; harmless but noisy.

### Prepared change list

1. Confirm with the client (and Tom) that attorney and lawyer searches are wanted. If not, pause the eleven attorney and lawyer keywords and add phrase negatives abogado, abogados, lawyer, lawyers, attorney, attorneys (only "free lawyer", "free attorney", "abogado gratis" and "rocket lawyer" exist today). If yes, rewrite the Spanish "Ad group 1" RSA (POOR) and the English "Paralegals Services #2" RSA to say non-lawyer document preparation plainly, which is also what the QS 1 scores are asking for.
2. Negatives, phrase: clerk of the court, emancipation, process server, numero de telefono, telefono, broward, iceout. Keep notary, notario and apostille.
3. Rename the campaigns and "Ad group 1"; split the main campaign's "Paralegals Services #2" group into Paralegal, Divorce, Custody and Notary groups so the ads can match.
4. Second RSA in all five ad groups. Remove the disapproved ad in the paused group so the campaign flag clears.
5. Spanish campaign: set a target CPA of $40 and raise the budget to $25 a day if the client wants volume; it is budget-capped at a $46 CPA.

## No action needed this week (one-liners)

- **The Counseling Group (61 D):** zero primary conversions Oct 19 to Nov 1 on $291, two in 30 days. The tel-tap action recorded 5 in all_conversions (Oct 19, 20, 29 and two earlier) and 0 in Conversions, which is the pattern of an action excluded by the campaign's conversion-goal setting, not a dead tag. Check the campaign goals in the UI (worklist item 10 closes on the tag, stays open on the counting). Tom rewrote the three RSAs Oct 20; Anxiety & Stress still has one POOR RSA. "therapist near me" exact is QS 2 ($47, 0 conv, landing page BELOW_AVERAGE), which is the landing page item (worklist 11). Negatives, phrase, new this window and absent from all four lists: dr gorman (only "patrick gorman" exists), dr cubano, samantha bickham, john gallagher, marianne vernacchia, la amistad, orlando thrive, livethelife, medications, medicine, ect, tmz, metacognitive, deep breathing, relaxation techniques, hotline, how many sessions, at home, struggling with, er for, cured, cures, kissimmee. Already present: antidepressant, supplements, medication, tms, psychiatrist, worksheets, massage therapy. Confirmed waste $93 of $590. Budget $26.50 a day since Oct 26, about $575 a month on the Monday-to-Friday schedule; on plan. Enhanced conversions off.
- **Rover Veterinary Care (62 D):** conversions recovering (7 this week, 19 in 30 days at $124). The 332-member "Account Negatives - Master" list (peggy adams, pet cemetery, gentle pet crossing, monarch, taps, out-of-area cities) is attached only to Brand and Competitors, not to In-Home Pet Euthanasia or Pet Cremation Services, which is why "peggy adams euthanasia" $13, "pet cemetery near me" $16, "gentle pet crossing" $15 and "pet cremation stuart/port st lucie/naples" $29 came through Pet Cremation. Attach it. New, absent everywhere: heaven at home ($55 on one click), pet angel ($21), pawsetrack, quiz ($26 on "when to put your dog down quiz"), aquamation, login, naples, boca (if out of area), when to, signs, should i. Dave's Oct 23 keyword additions include "mobile dog put down service" phrase ($226, 5 clicks at $45, 0 conv) and "dog put to sleep" phrase ($109, 0 conv); cap or pause the first. "Calls from ads" and "Event|Contact|Calls From Website" are both zero in 30 days while "Click to call (on website)" records 10; manual test or retire. Competitors RSAs still POOR (worklist 16). "lap of love" exact spent $154 for 0 this window but "laps of love" converted twice on $99; competitor bidding still pays, barely.
- **Florida Sealcoating (63 D):** spend $3,031 on an $88 a day budget set ($2,676 a month at full delivery); the $3,000 ramp is on plan, and Branded was cut from $30 to $15 a day. Sep 4 competitor and supplier negatives still absent (ppg, gem seal, absolute, martin, seal right, kennedy, american asphalt, millings, cold mix, who sells, hot patch); new this window: tru mark ($26), seal master orlando ($27; only an exact "seal master" ad-group negative exists), road paving ($33), driveway builders ($46). Zero-conversion keywords over $10: 16 for $960, led by "asphalt paving company near me" phrase ($229, 7 clicks at $33, 3 all_conversions) and "asphalt patch repair" QS 3 ($112). "driveway repair near me" is QS 1. "Call (1-8-333-PAVEIT)" still zero in 30 days; manual test still due. Dave's Oct 23 and 30 keyword, bid-modifier and RSA work needs two weeks before judging.
- **Scootz (64 D):** conversions are back without the form: Booqable Purchases 20, Calls from ads 10, 30 at $49. The GA4 form_submit action is still secondary, excluded and silent (worklist 17 first step still open). Still one ad group of 30 keywords on Maximize Clicks with no ceiling. Recommendations auto-apply removed an exact keyword Oct 8; turn it off. Negatives, phrase, new: scooterbug, scooter bug, gateway, buena vista scooter, knee scooter, stroller, st augustine, phone number (only an exact "scooterbug orlando photos" negative exists). "scooter king" converted once, leave it. Tom's Oct 22 exact "scooter rental near me" with its own final URL recorded 1 conversion on $12.
- **Aqua Coat (65 D):** the 248-member "Master Negative Lisst" is still attached only to the paused campaign, seven weeks after Sep 14; the live campaign relies on 89 campaign and 36 ad-group negatives, which is why "pool painter near me" $18, "aquastrong pool pump" $12, "pool rails" $12, "leslies pool" $9, "hayward pool heater" $11, "pinch a penny" $11 and "pool handrail installation" $7 got through (all of pump, heater, leslie, pinch a penny, kit, supplies sit in the orphaned list). Attach the list and add painter, painters, paint my pool, rails, handrail, sekas, aquastrong, equipment. Pool Equipment group still live (worklist 7); "swimming pool equipment" broad is the top keyword ($125, 2 conv at $63). 14 conversions at $32; Dave's target CPA from Sep 9 is working.
- **All Phase Pool Remodeling (69 D):** brand term "all phase pool remodeling" broad still sits in Pool Renovations ($232, 7 conv) and Pool Resurfacing ($194, 3 conv), 51 percent of spend; 100 percent of spend is broad (worklist 12 open). The 379-member master list is attached only to the paused campaign (same pattern as Aqua Coat). "red rhino jacksonville" spent $29 before Dave's Oct 22 exact negative; add phrase "red rhino", "pinch a penny" phrase (only exact exists; "pinch a penny orlando" $16 and "sanford" $5 got through), tempool, aqua pool, pool deck resurfacing of central florida. "Phone Calls 60s+" and "Request quote" still zero; "Contact Form" records 3 in all_conversions and 0 counted (same goal-setting question as the Counseling Group). One conversion this week on $168; watch.
- **M&S Asphalt Paving (69 D, reactivated Oct 15):** Paving - Volusia $559 for 5 conversions at $112, Manual CPC at $11.41, 49 percent rank-lost. The negatives Tom added Oct 15 and 21 (buds asphalt, millings, ecogrid, ways to, quikrete, chip seal, cost to) already cover this window's leaks; $65 of those clicks predate them. Five of six ad groups have one RSA. "Calls from ads" (the one with 0) is categorized SUBMIT_LEAD_FORM; recategorize. Nothing else to do until two more weeks of data.
- **Affordable Critter Solutions (77 C):** 15 conversions at $20, clean terms, two RSAs per group. "wildlife animal control" broad $24 for 0 is the only keyword to watch. 11 paused campaigns still there (worklist 19). 60 percent rank-lost and 29 percent budget-lost at $10 a day; $15 a day is still a fair client ask. Dave's Oct 29 RSA and keywords: measure next week.
- **Color Masters (paused):** REK-built in October, Residential Painting spent $892 for 3 conversions ($297 each) before Tom paused all three campaigns Oct 22. If it restarts: "painting companies" phrase is QS 2 ($126), "house painters near me" QS 1, and the zero-conversion keywords ($474) are mostly generic painter terms at $10 a click. The 92-member negative list is attached. Nothing to do while paused.
- **REK Marketing (own account):** GBP Verification Search campaign $223 for 0 conversions at $9.71 a click, 70 percent lost to budget at $20 a day; "google business profile suspended" phrase ($82) was paused; "google business profile expert" exact is QS 1. Philadelphia and San Diego lead campaigns went live Nov 1 at $25 a day each. All eight ad groups have one RSA. Reported, not scored.
- **All Phase Jacksonville:** search side spent nothing; the "Orlando" campaign is still ENABLED and NOT_ELIGIBLE. Pause it when convenient (worklist item 6). LSA out of scope.
- **Herrell Plumbing, Byers Fence, Byers Fence (LSA), Straightline Fence:** excluded; see attention items 5 and 7. Byers Fence is edited only by byersfence83@gmail.com; auto-apply removed 19 keywords there in October, which is the client's problem unless Tom says otherwise.
- **Jupiter Boat Supply, Spectrum Electric:** no campaigns in the account. Nothing to do.

Out of scope, for the record only: Citrus Landscape Solutions Sanford LSA $8,056 and 83 leads in 30 days, St. Pete $4,706 and 39, Sarasota $1,154 and 10 (no enabled campaign); Byers Fence (LSA) $1,671 and 14; Herrell LSA $2,520 and 37; All Phase Orlando LSA $314 and 5 (new); Roeling Green Lawns $227 and 7; ABC Pressure Wash, Statewide Home Remodeling and Color Masters LSA $0.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Filutowski (deep dive 1 item 2), Progetto (deep dive 3 item 4), Precision GPR (deep dive 4 item 1), Patio Style (deep dive 2 item 5), Quality Paralegal (deep dive 5 item 2), Counseling Group, Rover, Florida Sealcoating, Scootz, Aqua Coat and All Phase (one-liners above). Two accounts, Aqua Coat and All Phase, have their master lists attached only to paused campaigns, and Rover's master list is missing from its two largest campaigns; attaching three lists is the cheapest fix in the fleet.

New keywords to add: Precision GPR exact "precision gpr" (converted twice on $35) and phrase "utility locating companies" (2 all_conversions on $33); Quality Paralegal exact "apostille orlando", "notario publico cerca de mi", "divorce paralegal" (each converted once); Rover exact "laps of love" (2 conversions on $99) and "at home pet euthanasia services near me" (2 conversions on $40); Scootz exact "scooter rental in orlando" (6 all_conversions on $10); Aqua Coat exact "aqua coat pool plastering" already exists and is the best keyword in the account ($31, 4 conv), add phrase "pool resurfacing near me" exact to its own group; Florida Sealcoating exact "paving companies near me" converted through two phrase keywords (3 and 2 all_conversions), give it a home.

Bid and budget adjustments: Filutowski Brand Awareness keyword swap and Branded $50 to $100; Progetto Shades & Blinds $50 to $30 and Shutters $30 to $20 until the pages convert; Precision GPR pause Location, cap Ground Penetrating Radar at $10, brand broad to phrase; Patio Style freeze bidding until the directions goal is settled; Rover cap "mobile dog put down service"; Quality Paralegal Spanish campaign target CPA $40 and $25 a day; Affordable Critter $10 to $15 a day (client decision).

Competitive read (rank-lost share as the proxy): Progetto loses 41 to 73 percent to rank on every campaign with ceilings of $9 to $12, so it is being outranked by Quality Score, not outbid. Patio Style Outdoor Furniture and Affordable Critter lose 60 to 64 percent at low caps by design. Filutowski is budget-limited, not rank-limited, on every campaign (rank loss 2 to 20 percent). Rover holds 79 percent absolute top on In-Home at $19 a click and is not being outbid. M&S Sealcoating loses 72 percent to rank on an $8 budget; raise bids or fold it into Paving.

## Prioritized weekly action plan

1. **Critical, Tom today: Patio Style conversion goal.** Decide whether Get Directions is primary (protocol says yes). If yes, set one directions action primary and included and stop the bidding changes for two weeks. If no, update the protocol note. Everything else in the account waits on this.
2. **Critical, Tom: Progetto Shades.** Include the (858) website call action in Conversions, cut Shades & Blinds and Shutters budgets to $30 and $20 until the /lp/ pages are rebuilt with a phone number and a form above the fold, pause the five QS 1 to 2 keywords in deep dive 3 item 3. $837 this week for zero leads.
3. **Critical, Tom: Filutowski scope.** Same question as Sep 14. If REK is engaged, deep dive 1 items 1 to 3 recover an estimated $4,300 a month at the floor and put it on Branded and Eye Surgery, which convert at $19 and $43. Turn enhanced conversions off either way if REK has any say.
4. **High, Tom: Herrell Plumbing search campaign.** Pause it or finish it (four POOR RSAs, zero spend in learning) and tell the routine which. Update the protocol note.
5. **High, REK (Dave): Precision GPR.** Apply deep dive 4 items 1 to 3. The negative list and pausing Location are an hour of work and have been open since Sep 4.
6. **High, REK: attach three negative lists.** Aqua Coat "Master Negative Lisst" to the live campaign, All Phase "All Phase Master Negatives" to the live campaign, Rover "Account Negatives - Master" to In-Home Pet Euthanasia and Pet Cremation Services. Ten minutes, about $250 a month at the floor across the three.
7. **High, Tom: Quality Paralegal.** Decide on attorney and lawyer keywords (deep dive 5 item 1), then the Spanish RSA (POOR) and second RSAs.
8. **Medium, REK: The Counseling Group.** Check the campaign conversion goals in the UI (tel-tap fires, is not counted). Add the name and self-help negatives. Then worklist 11 (landing page) is the lever.
9. **Medium, REK: Rover.** Cap "mobile dog put down service", add heaven at home, pet angel, quiz and the question negatives, rebuild the two POOR Competitors RSAs (open since Sep 4), test or retire the two zero call actions.
10. **Medium, REK: Florida Sealcoating.** The Sep 4 competitor negatives plus tru mark, seal master phrase, road paving. PAVEIT manual test.
11. **Low: Scootz** turn off auto-apply, add the scooterbug negatives, then worklist 17; **All Phase** brand split (worklist 12) and the phrase negatives; **Aqua Coat** Pool Equipment group (worklist 7); **M&S** recategorize the call action and second RSAs; **Affordable Critter** paused-campaign cleanup; **All Phase Jacksonville** pause the Orlando campaign; **REK Marketing** second RSAs and a bid ceiling on GBP Verification.
12. **Housekeeping:** bump the default API version in tools/gaql.py from v22 to v24 (v22 is no longer shipped by the client library); the pending MCC link to 325-901-5827 needs someone to accept or cancel it.

## Rotation

Deep-dived this run: Filutowski Eye Institute, Patio Style, Progetto Shades, Precision GPR, Quality Paralegal Services. Due next Monday: The Counseling Group (zero conversions, October deep dive was never done), Rover Veterinary Care (to measure Dave's Oct 23 keywords), Florida Sealcoating (to measure the Oct 23 and 30 changes). The week after: Scootz, Aqua Coat, All Phase Pool Remodeling, Affordable Critter Solutions (carried since Sep 4), M&S Asphalt Paving (first deep dive since relaunch). Color Masters and Herrell join the rotation if they restart or are confirmed REK-managed.

## Data notes

- Account discovery returned 30 client accounts; Sep 14 had 26. All 26 are still present; 4 are new (listed in attention item 1). Compare next week against this run's list.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor. Visible-term coverage this window: Filutowski 73 percent of spend, Progetto 61 percent, Rover 52 percent, Scootz 48 percent, Quality Paralegal 39 percent, Counseling Group 30 percent, Precision GPR 26 percent, M&S 26 percent.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Oct 4 (the API allows 30 days). Conversion action edits are not included in change history, which is why the Patio Style directions demotion cannot be dated or attributed.
- "Primary conv" in this report is metrics.conversions (actions included in Conversions). Several accounts show actions that are primary_for_goal but include_in_conversions_metric false and record only in all_conversions (Counseling Group tel-tap, All Phase Contact Form, Progetto website call, Quality Paralegal Clicks to call); the report treats those as counting problems to check in the UI, not as dead tags.
- Fleet spend totals were reconciled against the per-account campaign totals listed in the coverage section.
- Week-over-week CPC for Florida Sealcoating includes 200 display remarketing clicks at $0.74 over 30 days.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
