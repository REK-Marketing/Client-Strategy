# PPC Weekly Audit - 2026-09-14 (Google Ads fleet)

Run: Monday Sep 14, 2026, scheduled cloud session through tools/gaql.py against MCC 656-695-7229. Windows: 30 days Aug 15 to Sep 13; this week Sep 7 to Sep 13; last week Aug 31 to Sep 6. Score deltas are against the Sep 4 report, the last run with Google Ads data. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Filutowski Eye Institute (new, worst score), Precision GPR (worst existing score), Scootz (10-point drop, on rotation), Rover Veterinary Care and Florida Sealcoating (on rotation). One-liners for the rest.

The Google Ads credential works again. The google-ads.yaml in the Drive folder dave-ads-setup was updated Sep 8 and authenticated on the first try. It was copied with mode 600, used only by the client library, and deleted before this report was written.

## Attention items (read first)

1. **Two accounts vanished from the MCC since Sep 4: Premium Walk-In Clinic (279-265-7852) and Premium Medication Refills (722-095-3380).** Both are gone from customer_client, and a direct query on each returns "user doesn't have permission". The MCC link table shows the Premium Walk-In Clinic link as INACTIVE (three link records: two inactive, one refused) and the Premium Medication Refills link as INACTIVE. This is a removed manager link, not a hidden account. Premium Walk-In Clinic was spending about $2,500 a month on Sep 4 with a third party (Power Couch Media) editing it, and worklist items 1, 2 and 20 depended on access. Premium Medication Refills was already paused. Find out who removed the links and whether REK still has these clients.
2. **Filutowski Eye Institute (192-870-7876) is new under the MCC and is the largest account in the fleet.** $19,176 in 30 days, 58 percent of it on one broad keyword. No REK user appears in its 30-day change history; the editors are catie@accaliamarketing.com and web@filutowski.com. It is scored below as 42 F and deep-dived because the numbers are large, but nothing should be touched until Tom says whether REK manages it, audits it, or is only linked.
3. **Straightline Fence And Supply (550-094-8786) is still not serving, and the reason is now known: both ads are DISAPPROVED under the COMPROMISED_SITE policy.** Google thinks the website is hacked. Robbie added 15 assets on Sep 10 and toggled the campaign status on Sep 10 and Sep 14, which will not help until the site is cleaned and the policy appeal is filed. Zero spend for the whole window.
4. **Scootz (185-574-5478) lost its form conversion action.** The GA4 form_submit action recorded 11 conversions on Aug 15 and 16 and none since. Its configuration is now secondary and excluded from Conversions. Counted conversions fell from 48 in the Sep 4 window to 20 in this one, and the account dropped 10 points. See deep dive 3.
5. **Rover Veterinary Care recorded zero conversions on 42 clicks from Sep 7 to Sep 13** across all five primary actions, after 5 in the previous week. Spend rose 57 percent. Not declared dead; manual trigger test on the website call and Book appointment actions this week.
6. **Byers Fence (LSA) (276-105-5321) is also new under the MCC.** Excluded like Byers Fence, for the record only.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 26 client accounts, 1 manager | 10 | 2 vanished, 2 new since Sep 4. Excluded: Byers Fence x2, 8 LSA-only accounts. Not scorable: 5 paused or zero-spend accounts and 1 relaunch. |

Search and Performance Max spend in the 30-day window: $11,601 across the nine REK-managed scored accounts, plus $17,496 at Filutowski Eye Institute. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 4. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $17,496 | 354 | $49 | 42 | F | new | Critical (scope) | One broad keyword, "lasik treatment cost", spent $11,120 and matched other clinics, retail optical chains and insurers; $3,452 visible on 509 such terms | $3,452 |
| 2 | Precision GPR | 554-113-4760 | $2,409 | 9 | $268 | 50 | F | -5 | Critical | Cleanup stalled since Aug 26; none of the Sep 4 list has landed; 1 conversion this week on $613 | $274 |
| 3 | Scootz | 185-574-5478 | $1,561 | 20 | $78 | 58 | F | -10 | Critical | GA4 form_submit silent since Aug 16, now set secondary; Maximize Clicks on one 34-keyword ad group | none confirmed |
| 4 | Rover Veterinary Care | 750-667-5721 | $1,956 | 19 | $103 | 61 | D | -6 | Needs attention | Zero conversions this week; Brand campaign $305 with 0 conversions matching generic vet queries; both Competitors RSAs still POOR | $160 |
| 5 | Florida Sealcoating | 168-852-7101 | $1,647 | 21 | $78 | 63 | D | -6 | Needs attention | Competitor and supplier negatives from Sep 4 still not added; eight keywords at QS 2 to 3 carrying $400; Branded campaign matches generic paving terms | $103 |
| 6 | Aqua Coat Pool Plastering | 285-714-0527 | $287 | 10 | $29 | 64 | D | -3 | Needs attention | The 215-member master negative list is attached only to the paused campaign, not the live one; Pool Equipment group still live | $90 |
| 7 | The Counseling Group | 657-069-3617 | $590 | 5 | $118 | 66 | D | -7 | Needs attention | Tel-tap action still zero 33 days after it was built; greenlit change set from Sep 8 not applied; medication queries this week | $17 |
| 8 | Patio Style | 596-555-8707 | $2,074 | 166 | $12 | 66 | D | +1 | Needs attention | Brand fix landed Sep 4; new "Get directions (GTM) 11 Sep" action is primary alongside the GA4 directions import, a double-count risk; 11 of 12 ad groups still one RSA | $85 |
| 9 | All Phase Pool Remodeling | 103-111-7688 | $779 | 30 | $26 | 72 | C | -3 | On target | Unchanged since Sep 4; brand term now 62 percent of spend inside non-brand groups; "Phone Calls 60s+" still zero | $59 |
| 10 | Affordable Critter Solutions | 227-108-4521 | $298 | 13 | $23 | 76 | C | +1 | On target | Clean; $10/day budget losing 23 percent of impressions at a $23 CPA | none confirmed |
| none | Straightline Fence And Supply | 550-094-8786 | $0 | 0 | n/a | n/a | no spend | n/a | Critical | Ads disapproved, COMPROMISED_SITE. See attention item 3 | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | no search spend | was 42 | Paused (search) | The leftover "Orlando" campaign is still ENABLED but NOT_ELIGIBLE and spent nothing. Worklist item 6 still open, nothing leaking | n/a |
| none | Progetto Shades | 416-010-8247 | $299 | 1 | n/a | n/a | relaunch | n/a | Watch | Tom rebuilt the account Sep 8 to 10: six new search campaigns, all in learning, $10 spent this week | n/a |
| none | Jupiter Boat Supply, M&S Asphalt Paving, REK Marketing | | $0 | 0 | n/a | n/a | paused | n/a | Paused | Fully paused, no changes | n/a |

Vanished since Sep 4: Premium Walk-In Clinic (was 46 F) and Premium Medication Refills (was 60 D, paused). See attention item 1.

## Week over week (Sep 7 to 13 against Aug 31 to Sep 6, search and PMax only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $4,329 to $5,050 (+17%) | 497 to 490 | 6.8% to 6.2% | $9.46 to $10.31 | 75 to 84 | $58 to $60 | LASIK cost keyword up $800, CPC $16.32 to $20.40 |
| Precision GPR | $670 to $613 (-9%) | 67 to 53 | 8.0% to 6.6% | $10.00 to $11.57 | 4 to 1 | $168 to $613 | Off target |
| Patio Style | $467 to $441 (-6%) | 231 to 198 | 7.6% to 6.5% | $2.02 to $2.23 | 46 to 21 | $10 to $21 | GA4 directions 43 to 28; Brand campaign now 78% share at $2.38 |
| Aqua Coat | $40 to $108 (+167%) | 17 to 19 | 3.5% to 3.6% | $2.37 to $5.66 | 0 to 4 | n/a to $27 | Dave set a target CPA on Sep 9; spend and CPC jumped, conversions came with it |
| Rover Veterinary Care | $327 to $515 (+57%) | 49 to 42 | 15.5% to 16.4% | $6.67 to $12.25 | 5 to 0 | $65 to none | Off target, see attention item 5 |
| Scootz | $361 to $390 (+8%) | 496 to 621 | 7.0% to 7.6% | $0.73 to $0.63 | 2 to 2 | $181 to $195 | Only Booqable purchases counting |
| Florida Sealcoating (search) | $452 to $479 (+6%) | 40 to 37 | 3.1% to 3.6% | $6.75 to $3.15 (display included) | 6 to 7 | $79 to $74 | Ramp on plan; Commercial CPC $23 |
| The Counseling Group | $173 to $131 (-24%) | 41 to 31 | 4.3% to 5.3% | $4.21 to $4.23 | 3 to 1 | $58 to $131 | Small numbers, budget lost share 62% |
| All Phase Pool Remodeling | $165 to $165 (0%) | 25 to 27 | 5.7% to 5.7% | $6.61 to $6.10 | 5 to 4 | $33 to $41 | Flat |
| Affordable Critter Solutions | $79 to $59 (-25%) | 22 to 19 | 9.6% to 6.2% | $3.60 to $3.11 | 4 to 4 | $20 to $15 | Flat |
| Progetto Shades | $9 to $10 | 22 to 3 | | | 0 to 0 | | Relaunch, learning |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: Aqua Coat 78 percent, Affordable Critter 80 percent, All Phase 75 percent, Patio Style Outdoor Furniture 65 percent, Scootz 53 percent. Highest CPC increases: Rover ($6.67 to $12.25), Aqua Coat ($2.37 to $5.66), Filutowski LASIK cost keyword ($16.32 to $20.40).

## Changes made in the past week (Sep 5 to Sep 14) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Patio Style | Sep 4 | Tom | Brand campaign moved to Target Impression Share with a CPC ceiling; two phrase brand keywords paused (worklist item 3) | Brand campaign this week: 78.4% impression share, 48.6% absolute top, $2.38 CPC, 3 conversions on $26. Last week 10.9% share at $1.35. Working as intended. |
| Patio Style | Sep 11 | paidads@rekmarketing.com | New call asset with call conversion, new conversion actions (Website Call Conversions, Get directions GTM, Send us a message, Thank you page), Patio Furniture RSA edited, three campaign assets added | Get directions (GTM) recorded 1 this week and is primary and included next to the GA4 get_directions import (28 this week). Confirm only one fires per tap or directions will double count. YouTube actions are now secondary (worklist item 14 done). |
| Florida Sealcoating | Sep 11 | sheokand003@gmail.com | 32 keywords added and 24 removed across Asphalt Patching (both campaigns) and Parking Lot Striping; budgets on Branded and Residential changed (now $30 and $30) | Too early to measure. "Asphalt Patch Contractor" broad spent $25.55 this week with 0 conversions. |
| Aqua Coat | Sep 9 | sheokand003@gmail.com | Target CPA set on the Maximize Conversions campaign | Spend $40 to $108, CPC $2.37 to $5.66, conversions 0 to 4. One week is too little; check again next Monday. |
| Progetto Shades | Sep 8 and 10 | Tom | Six new search campaigns (Shutters, Shades & Blinds, Motorized & Smart, Drapery & Curtains, Exterior & Patio, Brand) enabled Sep 10 with geo, network, negatives, callouts, sitelinks and a promotion; old campaign assets removed | $10 spent, all campaigns LIMITED by bidding strategy learning. Max Conversions with zero history will learn slowly; see one-liner. |
| Straightline Fence | Sep 10 and 14 | robbie@rekmarketing.com | 15 assets added, campaign status toggled twice | No effect. Ads remain DISAPPROVED for COMPROMISED_SITE. |
| Precision GPR, Rover, Scootz, Counseling Group, All Phase, Affordable Critter, Filutowski | | | No bid, keyword, budget or negative changes since Sep 5 | The Sep 8 worklist items for these accounts have not been applied. |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

Landed: item 3 (Patio Style brand, Sep 4) and the YouTube half of item 14. Item 15 partly: "sealcoat florida" is a phrase negative in Commercial and Residential (not exact in Branded as written) and the FL Remarketing campaign now serves (4,761 impressions, 158 clicks, $62, 1 conversion). Not landed: items 4 through 13, 16 through 19. Items 1, 2 and 20 are blocked because Premium Walk-In Clinic is no longer under the MCC. Item 21 (Dave re-copy the yaml) is presumably done since the Sep 8 file works.

## Deep dive 1: Filutowski Eye Institute (192-870-7876), score 42 F, provisional

Scope note: new to the MCC since Sep 4. No REK edits in 30 days. Score and change list are prepared so Tom can decide; coordinate with Accalia Marketing before anything is applied.

| Category | Score |
|---|---|
| Conversion Tracking | 45 |
| Wasted Spend | 25 |
| Account Structure | 50 |
| Keywords & Targeting | 35 |
| Ads & Assets | 50 |
| Bidding & Settings | 50 |

Snapshot, 30 days: six enabled campaigns. Search $16,804, Performance Max $692, a paused LSA campaign $1,680. 354 search and PMax conversions at $49. Twelve paused legacy campaigns.

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | CPA | Search IS | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| S / Brand Awareness / LASIK | $430 | $11,120 | 667 | $16.67 | 64.9 | $171 | 12.6% | 80.8% |
| S / Lead Gen / Cataracts | $50 | $1,463 | 188 | $7.78 | 17.0 | $86 | 44.1% | 27.7% |
| S / Branded / Dr. F | $50 | $1,426 | 587 | $2.43 | 149.3 | $9.55 | 39.9% | 56.7% |
| S / Lead Gen / Eye Surgery | $50 | $1,406 | 307 | $4.58 | 52.0 | $27 | 21.5% | 58.6% |
| S / Lead Gen / LASIK | $50 | $1,388 | 79 | $17.57 | 7.7 | $180 | 41.6% | 38.0% |
| Performance Max / Eye Surgery | $25 | $692 | 276 | $2.51 | 63.1 | $11 | 10.0% | 82.0% |

### Findings

**One broad keyword is 58 percent of the account.** "S / Brand Awareness / LASIK" has a single keyword, "lasik treatment cost", broad match, on Target CPA with a $430 daily budget. Of the $6,842 in visible search-term cost, $5,470 went to terms with zero conversions. Only $180 of visible spend was on terms that contain lasik, laser, smile or prk. $3,452 went to 509 terms naming other clinics (Tomoka Eye, Florida Eye Clinic, Coan, Precision Eye Institute, Bayhead, The Eye Place, Mid Florida Eye), retail optical chains (Walmart Vision Center, LensCrafters, America's Best, Costco Optical, Stanton, Visionworks, Warby Parker, Target Optical) and insurers (EyeMed, Cigna, Aetna, Spectera, Medicaid, Ambetter, Florida Blue), producing 13 conversions. Another $169 went to Spanish queries. The keyword works as a catch-all for any eye-related search in Central Florida. Google withholds the low-volume remainder, so $3,452 is the floor.

**Brand is starved while the catch-all is funded.** The Branded campaign converts at $9.55 and loses 57 percent of its impressions to budget at $50 a day. The Eye Surgery campaign converts at $27 and loses 59 percent to budget.

**Conversion tracking needs a cleanup.** 18 hidden Universal Analytics goals are still set primary and included, among them "Average Page per Session", "Average Visit Duration" and "Smart Goal". "YouTube follow-on views" is primary and included on a search account. Two call actions (800 general line, 407 CallRail LASIK line) plus "Phone Link Click (From Mobile)" are all primary, so one call can count more than once. Enhanced conversions for leads is ON. This is a medical practice; the protocol says it stays off without a BAA.

**Keywords and ads.** 1,296 enabled keywords, 66 percent of spend on broad match. QS 3 on "eye specialist near me", "ophthalmologist near me" and "eye doctor near me" ($876 combined, 34.5 conversions, so the low score is expected-CTR driven, not a waste problem). Every one of the five enabled ad groups has a single RSA. The Cataracts and Eye Surgery campaigns report HAS_ADS_DISAPPROVED; the visible policy entries are HEALTH_IN_PERSONALIZED_ADS limitations, which are normal for healthcare. Full disapproval detail: unavailable this run.

### Prepared change list (only if Tom confirms REK is engaged)

1. Replace "lasik treatment cost" broad with a phrase and exact LASIK set: lasik, lasik cost, lasik near me, lasik orlando, lasik lake mary, smile eye surgery, prk surgery, laser eye surgery. Cut the campaign budget from $430 to $200 a day until the change has two weeks of data.
2. New shared negative list on all live campaigns, phrase match: walmart, lenscrafters, america's best, americas best, costco, stanton, visionworks, warby, my eye doctor, target optical, total vision, pearle, eyeglass, glasses, contacts, optical, eyemed, cigna, aetna, spectera, medicaid, ambetter, florida blue, zocdoc, oftalmologo, cerca de mi, tomoka, florida eye clinic, coan, precision eye, bayhead, eye place, mid florida eye, lake eye, uptown eyecare, garay, pediatric, kids, retina, chalazion. Dedupe result: walmart, lenscrafters, costco and medicaid exist only as negatives on the paused campaign "1"; florida eye clinic only on Performance Max; oftalmologo and pediatric only on the paused Dynamic campaign. None protect the live search campaigns today.
3. Raise Branded from $50 to $100 a day and Eye Surgery from $50 to $80 a day with the money from item 1.
4. Set the 18 hidden UA goals and YouTube follow-on views to secondary. Keep one primary call action per phone line. Turn Enhanced conversions off unless a BAA exists.
5. Add a second RSA to each of the five enabled ad groups.
6. Review the disapproved ads in Cataracts and Eye Surgery in the UI.

## Deep dive 2: Precision GPR (554-113-4760), score 50 F, measuring the cleanup

Context applied: under active cleanup since Aug 2026. The change history shows no edits since Aug 26. The Sep 4 change list has not been applied, and the account got worse.

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 40 |
| Account Structure | 50 |
| Keywords & Targeting | 40 |
| Ads & Assets | 70 |
| Bidding & Settings | 40 |

| Campaign | Budget/day | Spend | Clicks | CPC | Primary conv | This week |
|---|---|---|---|---|---|---|
| LP Search - GPR Scanning | $20 | $632 | 33 | $19.16 | 1.0 | $132, 0 conv |
| LP Search - Services | $18 | $479 | 50 | $9.58 | 2.5 | $106, 0 conv |
| LP Search - Concrete Scanning | $18 | $472 | 27 | $17.47 | 2.5 | $155, 0 conv |
| LP Search - Utility Mapping | $15 | $448 | 56 | $8.01 | 2.0 | $111, 0 conv |
| LP DSA - All Pages | $10 | $199 | 42 | $4.73 | 1.0 | $101, 1 conv |
| LP Branded | $10 | $127 | 18 | $7.04 | 0.0 | $4, 0 conv |
| LP Search - Location | $18 | $51 | 8 | $6.43 | 0.0 | $3, 0 conv |

30 days: $2,409, 9 primary conversions (lp_contact_form 6, Calls from ads 3), $268 per conversion. This week: $613 for 1 conversion.

### What is still open from Sep 4

- "Ground Penetrating Radar" exact and phrase in GPR Scanning: $623 for 1 conversion at $19.36 to $19.63 a click, QS 3, landing page BELOW_AVERAGE. Still the biggest cost line. The same query "gpr scanning" ($161, 0 conversions) still matches four campaigns.
- DSA - All Pages and Location still enabled.
- Brand budget still $10 a day with 18.5 percent lost to budget.
- Negatives: "gprs" in six variants cost $108 this window and is still not a negative anywhere. Price and cost queries $37, rebar and detector queries $28, Spanish "radar de penetración terrestre" $30, "no cuts florida" $18, "geoslice net" $18, "sunshine utility locate" and "dig alert" $27 ("811" is a broad negative but did not catch these). Dedupe: "equipment", "rental", "rentals", "low cost" and "811" already exist in the LP NKWs list; everything else above is new. Confirmed waste this window: $274.
- New this window: "Underground Utility Survey" phrase and exact in Utility Mapping, QS 2, $240 for 1 conversion.
- Conversions: the three website call actions (305, 786, "Michael Phone Number") still recorded zero; "Contact Us", "Contact Us (1)" and "Contact us" still coexist. Manual test still due.
- Bidding: seven campaigns on Maximize Conversions with 0 to 2.5 conversions each.

The Sep 4 prepared change list stands as written. Priority order if only one hour is available: the negative list (item 1), pause Location and DSA (item 2), cap or pause the GPR Scanning keywords (items 3 and 4).

## Deep dive 3: Scootz (185-574-5478), score 58 F, down 10

| Category | Score |
|---|---|
| Conversion Tracking | 50 |
| Wasted Spend | 60 |
| Account Structure | 45 |
| Keywords & Targeting | 70 |
| Ads & Assets | 75 |
| Bidding & Settings | 50 |

Snapshot: one search campaign, Maximize Clicks, $50 a day. 30 days: $1,561, 30,804 impressions, 2,180 clicks, $0.72 CPC, 7.1 percent CTR, 20 primary conversions. Search impression share 26.9 percent, 19.9 percent lost to budget, 53.2 percent lost to rank.

### Findings

**The form action went silent on Aug 16.** "scootzrentals.com - GA4 (web) form_submit" recorded 6 conversions on Aug 15 and 5 on Aug 16, then nothing for 28 days, in all_conversions as well as primary. Its configuration today is primary false, included false. Conversion action edits do not appear in change history, so it is not possible to say from the API whether someone demoted it after it stopped or whether it stopped after being demoted. Either way, Scootz's counted conversions are now Booqable Purchases (7 in 30 days, about one a week) and Calls from ads (2). Not declared dead: manual form submit test, then check the GA4 event name and the Ads import.

**Because the form is dark, "zero-conversion keywords" is unreliable this month.** 16 keywords spent $847 (55 percent of spend) with zero primary conversions, led by "scooter rental disney world" exact ($164, 229 clicks) and "disney scooter rental" ($125). Most of them carry Google-hosted local actions in all_conversions, so intent is present. Do not pause on this data. Fix tracking first.

**Structure unchanged since Sep 4.** 34 keywords in one ad group, brand ("scootz orlando", "scootz rentals") mixed with Disney, Universal, wheelchair and general Orlando terms. Three RSAs, EXCELLENT, GOOD, GOOD. Price-shopping queries ("how much", "can you rent") are already negatives; "2 person scooter rental orlando" ($8, 11 clicks) and "wheelchair rental orlando" ($10, 14 clicks) are on-service.

**Bidding.** Maximize Clicks at $0.72 is buying volume, and with only Booqable purchases counting, Maximize Conversions is not an option until the form action is back. Worklist item 17 (split into Brand, Disney, Universal, Orlando, Wheelchair, then Maximize Conversions) still applies, in that order, after tracking is repaired.

### Prepared change list

1. Manual form test on scootzrentals.com today. Confirm the GA4 form_submit event still fires and is still linked. Once it records again, set it back to primary and included.
2. Then the Sep 4 restructure: five ad groups by theme, brand into its own group with exact and phrase, negatives cross-applied.
3. Move to Maximize Conversions only after two weeks with 15 or more counted conversions.

## Deep dive 4: Rover Veterinary Care (750-667-5721), score 61 D, down 6

| Category | Score |
|---|---|
| Conversion Tracking | 70 |
| Wasted Spend | 55 |
| Account Structure | 65 |
| Keywords & Targeting | 60 |
| Ads & Assets | 50 |
| Bidding & Settings | 60 |

Snapshot: four enabled search campaigns, all Maximize Conversions. 30 days: $1,956, 218 clicks, $8.97 CPC, 19 primary conversions at $103.

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | This week |
|---|---|---|---|---|---|---|
| Competitors | $30 | $835 | 117 | $7.14 | 8 | $236, 0 conv |
| In-Home Pet Euthanasia | $20 | $451 | 44 | $10.25 | 4 | $128, 0 conv |
| Pet Cremation Services | $20 | $365 | 24 | $15.21 | 7 | $114, 0 conv |
| Brand Campaign | $20 | $305 | 33 | $9.25 | 0 | $37, 0 conv |

### Findings

- **Zero conversions Sep 7 to 13** on 42 clicks, after 1, 2, 0, 1, 0, 1 on the days Sep 1 to 6. All five primary actions (Calls From Website, Book appointment, Form Submit, Calls from ads, Thank you page view) went to zero at once. A simultaneous stop across website and call actions can be a tag or site change. Manual trigger test this week before any bid change.
- **The Brand campaign spent $305 with 0 conversions and matched non-brand queries.** Visible terms: "paws to health" $29, "palm city animal" $17, "dog clinic near me" $17, "dog cremation near me" $25, "pet cremation" $15, "canine oncologist near me" $7, "pet death doula" $5. Enabled keyword "katie matzke" phrase spent $51 on 5 clicks with 0 conversions at 100 percent impression share, and "rover pet euthanasia" $29. Dedupe: oncologist, doula and "palm city animal" are already phrase negatives in Rover Core Exclusions (added Sep 3, after most of these clicks); "paws to help" exists only as exact variants, so "paws to health" is new.
- **The generic term "humane pet euthanasia" lives in the Competitors campaign**: $412, 51 clicks, 2 conversions, $206 each. It is the most expensive keyword in the account and is not a competitor term.
- **Cat-question and end-of-life-question searches, $67**: "does banfield euthanize cats" $22 (banfield is a negative, click predates it), "when to put down a cat" $17, "signs its time to put your cat down" $9, "when to know to put your cat down" $6, "i think i need to put my dog down" $6, "laps of love quality of life" $7. "when to", "signs", "quality of life" are not negatives.
- **Both Competitors RSAs are still POOR** (worklist item 16 open). Cat Euthanasia and In-Home Pet Euthanasia groups have one RSA each.
- Competitor bidding itself is working: "lap of love" exact produced 6 conversions on $271 ($45 each), and "laps of love", "lap of love" and "mobile pet euthanasia near me" are the top converting terms.

### Prepared change list

1. Manual conversion test (website call, Book appointment, form) today.
2. Brand campaign: keep exact brand only ([rover veterinary care], [rover vet care], [rover vet], [rovervetcare]). Pause "katie matzke" and "rover pet euthanasia" phrase. Add phrase negatives to Brand: euthanasia, cremation, clinic, near me, animal hospital.
3. Move "humane pet euthanasia" out of Competitors into In-Home Pet Euthanasia at a lower bid, or pause it; $206 per conversion is three times the account average.
4. Negatives, phrase, in Rover Core Exclusions: when to, signs, quality of life, should i, paws to health, paws 2 help, west palm animal clinic, baton rouge. Already present, skipped: banfield, oncologist, doula, palm city animal, hospice.
5. Rebuild the two POOR Competitors RSAs. Add a second RSA to Cat Euthanasia and In-Home Pet Euthanasia.
6. Bidding: with 4 to 8 conversions per campaign, Maximize Conversions is thin everywhere. Consider consolidating In-Home Pet Euthanasia and Pet Cremation into one campaign so the strategy sees 11 conversions a month instead of 4 and 7.

## Deep dive 5: Florida Sealcoating (168-852-7101), score 63 D, down 6

Context applied: the September ramp to $3,000 a month is intended. Daily budgets total $103 (Commercial $38, Residential $30, Branded $30, Remarketing $5), which is $3,090 a month. Spend is on plan, not a finding.

| Category | Score |
|---|---|
| Conversion Tracking | 75 |
| Wasted Spend | 45 |
| Account Structure | 70 |
| Keywords & Targeting | 45 |
| Ads & Assets | 80 |
| Bidding & Settings | 55 |

| Campaign | Spend | Clicks | CPC | Conv | CPA | Search IS | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|---|
| Commercial Services | $835 | 47 | $17.76 | 9 | $93 | 28.8% | 37.3% | 33.9% |
| Residential Services | $527 | 50 | $10.53 | 5 | $105 | 19.3% | 48.7% | 32.0% |
| Branded | $223 | 53 | $4.22 | 6 | $37 | 19.6% | 18.0% | 62.4% |
| FL - Remarketing (display) | $62 | 158 | $0.40 | 1 | $62 | n/a | n/a | n/a |

### Findings

- **The Sep 4 competitor negatives have not been added.** Visible this window: "ppg traffic solutions" $18, "absolute asphalt" $12, "gem seal orlando" $11, "seal right sealcoating" $7, "martin paving florida" $7, plus supplier and DIY queries "asphalt millings" $14, "cold mix asphalt near me" $9, "who sells asphalt" $7, "garage and driveway coatings" $6, and a street address "10705 cosmonaut blvd" $12. Total $103. Dedupe: none of ppg, absolute, gem seal, martin, seal right, kennedy, american asphalt, millings, cold mix, who sells exist in the 250-member master list or the 296 campaign negatives. "baker paving" is present. "sealcoat florida" is now a phrase negative in Commercial and Residential (worklist item 15, partly done).
- **The Branded campaign matches generic paving queries.** "orlando paving companies" $29, "asphalt paving orlando" $25, "paving companies orlando" $20, "asphalt driveway" $16 and "gem seal orlando" all show Branded among the matching campaigns, which is why Branded has 62 percent rank-lost share while the exact keyword "florida sealcoating" alone has 73 percent impression share. The broad keyword "florida sealcoating llc" is the likely path. Move Branded to exact and phrase only and add phrase negatives for paving, sealcoating, asphalt to Branded.
- **Quality Score floor, eight keywords at QS 2 to 3 carrying $400**: driveway repair near me (broad, $126, 1 conv), asphalt company orlando (phrase, $93, 0), asphalt paving company near me (broad, $84, 2), paving companies near me (broad, $63, 0), driveway sealcoating (broad, $25), asphalt patch repair (phrase QS 2, $9). All show BELOW_AVERAGE expected CTR and BELOW_AVERAGE ad relevance, which points at the ad copy in Driveway Paving & Repair and Commercial Paving, not the landing page.
- **Zero-conversion keywords over $10, $691**: "asphalt services" phrase $233 (10 clicks at $23.28, 12 all-conversions from local actions), "asphalt company orlando" $93, "asphalt sealcoating" broad $86, "paving companies near me" $63, "Asphalt Patch Contractor" broad $53, "paving and sealcoating services" $53, "asphalt paving sanford" $39, "florida sealcoating" exact $56 (0 primary, 6 all-conversions; the Branded campaign's 6 primary conversions came from other brand variants).
- **Sep 11 restructure by Dave**: 32 keywords added, 24 removed in Asphalt Patching (both campaigns) and Parking Lot Striping, Branded and Residential budgets set to $30. Measure next week.
- **Resolved from Sep 4**: FL Remarketing now serves (4,761 impressions, 158 clicks, $62, 1 conversion).
- **Conversions**: Calls from ads 10, Call (407) 7, Free Estimate Form 4. "Call (1-8-333-PAVEIT)" recorded zero; creation date unknown, manual test rather than a finding.

### Prepared change list

1. Negatives, phrase, to the master list: ppg, absolute asphalt, gem seal, seal right, martin paving, kennedy concrete, american asphalt, millings, cold mix, who sells, coatings, hot patch, diy. Exact: the cosmonaut address string.
2. Branded: pause or convert "florida sealcoating llc" broad to phrase; add phrase negatives paving, sealcoating, asphalt, driveway to the Branded campaign so generic queries route to the service campaigns.
3. Rewrite the RSA in Driveway Paving & Repair and Commercial Paving with the keyword phrases in headlines (driveway repair, asphalt paving company, paving companies) to lift expected CTR and ad relevance off BELOW_AVERAGE.
4. Cap "asphalt services": $23 a click for a vague term. Convert to exact "asphalt services orlando" or pause and let "asphalt paving contractor" (4 conversions, $36 each) take the intent.
5. Manual test on the 1-8-333-PAVEIT call action.

## No action needed this week (one-liners)

- **Aqua Coat (64 D):** the 215-member "Master Negative Lisst" is attached only to the paused "Aqua Coat | Search" campaign; the live "- M" campaign runs on 89 campaign negatives and 34 ad-group negatives. Attach the list. Pool Equipment group ($27, 0 conv) and "pool cleaning services" ($22, 0 conv) are still live (worklist item 7). New leaks: "aqua pools" $14, "pcs pools" $9, "pool plaster repair kit" $8, "inground pool handrail" $6. Dave set a target CPA on Sep 9; four conversions this week at $27, re-check next Monday before judging.
- **The Counseling Group (66 D):** no changes since Sep 4 except the callout. Tel-tap still zero 33 days after it was built; the manual test (worklist item 10) is the one thing to do this week. This week's terms include "best antidepressant for anxiety and depression" $4 and "best supplements for depression" $4; add phrase negatives antidepressant, supplements, medicine (medication and psychiatrist already exist). "dr patrick gorman winter park" and "dr stan tatkin" are name searches to add exact. Enhanced conversions confirmed OFF. Budget lost share hit 62 percent this week at $25 a day; on plan, small numbers.
- **Patio Style (66 D):** brand fix confirmed working (see changes table). Check that "Get directions (GTM) 11 Sep" and the GA4 get_directions import do not both fire on one tap; both are primary and included. Conversions 46 to 21 this week is mostly GA4 directions 43 to 28 with steady spend, worth watching one more week. Panel queries still leaking ($55) pending the client's answer on insulated roof panels; "azenco" and "mirador" queries are pergola brands the store carries, not waste. 11 of 12 ad groups still have one RSA. Outdoor Furniture still on Maximize Clicks with 144 conversions in 30 days (worklist item 13).
- **All Phase Pool Remodeling (72 C):** unchanged. Brand term is now $479 of $779 inside non-brand groups. "leslie pool" $21 (only "leslie's pool supplies orlando fl" exact exists as a negative; add phrase "leslie"), "pool repair lake mary fl" $20, "pool cleaners near me" $9, "pinch a penny mount dora" $8 (exact "pinch a penny" exists; use phrase). "Phone Calls 60s+" still zero in 30 days; test. Sep 4 change list stands.
- **Affordable Critter Solutions (76 C):** 13 conversions at $23, two EXCELLENT RSAs, clean terms. "bat removal" broad $19 with 0 conversions is the only keyword to watch. The 11 paused campaigns are still there. At 23 percent lost to budget and a $23 CPA, $10 a day is the constraint; $15 a day is a fair client ask.
- **All Phase Jacksonville:** search side spent nothing; the "Orlando" campaign is ENABLED but NOT_ELIGIBLE. Pause it when convenient (worklist item 6). LSA is out of scope.
- **Progetto Shades:** relaunched Sep 10 with six themed campaigns on Maximize Conversions, all learning, $10 spent, 90 percent rank-lost share. With one conversion in 30 days of history there is nothing for Maximize Conversions to learn from. Put the five service campaigns on Maximize Clicks with a $4 ceiling for the first two weeks, then switch the one that converts. Brand is on Maximize Clicks already. Enhanced conversions is ON here; not healthcare, fine.
- **Straightline Fence:** see attention item 3. The fix is a site security cleanup, then "Appeal" on the disapproved ads. Robbie's status toggles do not re-review a policy disapproval.
- **Jupiter Boat Supply, M&S Asphalt Paving, REK Marketing:** paused, zero spend, nothing to do.

Out of scope, for the record only: Citrus Landscape Solutions Sarasota LSA spend fell 85 percent week over week ($833 to $124, 7 leads to 1); Roeling Green Lawns LSA is serving again ($63 this week after $0), which answers the worklist question about its pause; Byers Fence (LSA) is a new account under the MCC.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Filutowski (item 2 of deep dive 1), Precision GPR (gprs, price, cost, pricing, how much, rebar, detector, radar de, penetración, no cuts, geoslice, sunshine, dig alert, gs9000, em locator, for sale), Florida Sealcoating (deep dive 5 item 1), Rover (deep dive 4 item 4), Aqua Coat (aqua pools, pcs pools, repair kit, handrail, equipment, supplies, fresh finish, aqua dreams), All Phase (leslie, pinch a penny phrase, lake mary if not served, cleaners, coatings), Counseling Group (antidepressant, supplements, medicine, plus the two name searches), Patio Style (panels, roof panels, big green egg, tru island, vestivium, hampton bay, polywood; keep azenco and mirador).

New keywords to add: Florida Sealcoating exact "asphalt paving contractor orlando" and "commercial asphalt orlando" (the converting terms this week), Rover exact "mobile pet euthanasia near me" (3 conversions on $27), Aqua Coat phrase "fiberglass pool repair" (2 conversions on $33 this week, matched through broad), Filutowski phrase and exact LASIK set (deep dive 1).

Bid and budget adjustments: Filutowski Brand Awareness $430 to $200 and Branded $50 to $100; Precision GPR cap GPR Scanning at $10 and Brand to $15 a day; Rover pause "humane pet euthanasia" or cap it; Florida Sealcoating cap "asphalt services"; Progetto Maximize Clicks with a $4 ceiling during learning; Affordable Critter $10 to $15 a day (client decision).

Competitive read (rank-lost share as the proxy): Rover holds 65 to 70 percent absolute top on its core terms and is not being outbid; the problem is conversion, not rank. Aqua Coat, All Phase and Affordable Critter lose 66 to 80 percent to rank on tight budgets, which is a budget and Quality Score story, not an auction one. Patio Style Outdoor Furniture loses 65 percent to rank at a $2.50 cap by design.

## Prioritized weekly action plan

1. **Critical, Tom today: the two unlinked Premium accounts.** Confirm with the clients or Power Couch Media whether the manager links were removed on purpose. If REK still has the Premium Walk-In Clinic engagement, request a new link; worklist items 1, 2 and 20 are blocked until then.
2. **Critical, Tom: decide Filutowski Eye Institute's scope.** If REK is engaged, deep dive 1 items 1 to 3 recover an estimated $3,400 a month at the floor and put it on brand and Eye Surgery, which convert at $10 and $27. If REK is only linked, say so and the routine will report it as excluded.
3. **Critical, Robbie or REK web: Straightline Fence.** Site security cleanup for the COMPROMISED_SITE policy, then appeal both ads. Five weeks with no ads.
4. **Critical, REK: Scootz form_submit manual test.** Then restore it to primary and included, then the ad-group split.
5. **High, REK: Precision GPR.** Apply the Sep 4 change list, starting with the negative list, pausing Location and DSA, and capping GPR Scanning. Nothing has moved since Aug 26 and this week's CPA was $613.
6. **High, REK: Rover.** Manual conversion test first. Then Brand to exact only, "humane pet euthanasia" out of Competitors, the negatives in deep dive 4, and the two POOR RSAs.
7. **High, REK: Florida Sealcoating.** Competitor and supplier negatives (still missing after two weeks), Branded to exact and phrase with generic-term negatives, rewrite the two QS 3 ad groups' RSAs.
8. **Medium, REK: Aqua Coat.** Attach the master negative list to the live campaign, pause Pool Equipment and "pool cleaning services", add the four new competitor and product negatives.
9. **Medium, REK: The Counseling Group.** Tel-tap manual test and the three medication negatives. The greenlit set (worklist item 8) remains open.
10. **Medium, REK: Patio Style.** Confirm the GTM directions action does not double count the GA4 import. Second RSAs in the top three single-ad groups.
11. **Low: All Phase Pool Remodeling** brand split and negatives, **Affordable Critter** paused-campaign cleanup and budget ask, **Progetto** bidding during learning, **All Phase Jacksonville** pause the Orlando campaign.

## Rotation

Deep-dived this run: Filutowski Eye Institute, Precision GPR, Scootz, Rover Veterinary Care, Florida Sealcoating. Due next Monday: Affordable Critter Solutions (carried from Sep 4), Aqua Coat (to measure the target CPA change), Patio Style (to measure the brand change and the Sep 11 conversion actions). The week after: All Phase Pool Remodeling, The Counseling Group (October per the Sep 4 note).

## Data notes

- Account discovery returned 26 client accounts; the Sep 4 list had 26 with two different members. Compare next week against this run's list, not Sep 4's.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Aug 16 (the API allows 30 days). Conversion action edits are not included in change history, which is why the Scootz form_submit demotion cannot be dated.
- The Filutowski policy detail query was truncated in this session; the disapproval reasons beyond HEALTH_IN_PERSONALIZED_ADS are unavailable.
- Week-over-week CPC for Florida Sealcoating includes 128 display remarketing clicks at $0.33 this week; search-only CPC was $11.29 last week and $12.94 this week.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
