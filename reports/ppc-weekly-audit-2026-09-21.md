# PPC Weekly Audit - 2026-09-21 (Google Ads fleet)

Run: Monday Sep 21, 2026, scheduled cloud session through tools/gaql.py against MCC 656-695-7229. Windows: 30 days Aug 22 to Sep 20; this week Sep 14 to Sep 20; last week Sep 7 to Sep 13. Score deltas are against the Sep 14 report. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Filutowski Eye Institute (worst score), Quality Paralegal Services (new, second worst), Patio Style (11-point drop), All Phase Pool Remodeling (12-point drop), Precision GPR (third worst). One-liners for the rest.

The google-ads.yaml in the Drive folder dave-ads-setup authenticated on the first try. It was copied with mode 600, used only by the client library, and deleted before this report was written. No credential value appears anywhere in this file.

Scoring note: the six-category rubric was applied fresh this run. Treat deltas inside plus or minus 5 points as run-to-run noise and read the named findings instead. Three deltas this week are larger than that and each is explained in its deep dive.

## Attention items (read first)

1. **Straightline Fence And Supply (550-094-8786) has now been unable to serve for three weeks.** Both ads are still DISAPPROVED under the PROHIBITED policy topic COMPROMISED_SITE, reviewed and final. The campaign says SERVING and the account spent nothing for the third consecutive window. Robbie toggled the campaign status again on Sep 14, which cannot help. Google believes the website is hacked. Nothing in Google Ads will fix this. The site has to be cleaned and an appeal filed. This is the oldest unresolved item in the fleet and it should go to the client today.

2. **Florida Sealcoating's brand campaign lost its cost control on Sep 15 and spend went up ten times in one week.** sheokand003@gmail.com removed the $17 target CPA from the Branded campaign (id 23396500289) and raised the Commercial Services budget from $38 to $45 the same minute. Branded spend went from $21.48 to $216.63 week over week at an $11.40 average CPC for 3 conversions. Account CPA went from $74 to $109. The target CPA should go back on Branded before another week runs.

3. **Filutowski Eye Institute is not counting its form conversions at all, and its budget moved the wrong way.** All eleven current GA4 actions, including every form fill and every Calendly booking, are HIDDEN and excluded from the Conversions metric. Nineteen dead Universal Analytics goals are still flagged primary and included. 307 of the 323 counted conversions in 30 days are phone calls, and three separate call actions all count, so one call can be counted more than once. Target CPA on the catch-all campaign is therefore optimising toward a phone number, not toward patients. Separately, catie@accaliamarketing.com raised the LASIK catch-all budget from $430 to $455 a day on Sep 14. See deep dive 1.

4. **Two accounts are new under the MCC: Quality Paralegal Services (447-153-2607) and Color Masters (426-092-9847).** Quality Paralegal is already spending $1,262 a month with a tracking setup that counts Google Business Profile directions taps as leads. Color Masters is a fresh REK build that went live Sep 18 and has spent nothing yet. Both are scored or noted below. Confirm the engagement terms for Quality Paralegal before any change is applied.

5. **Patio Style is now double counting directions.** Both the GA4 get_directions import and the new "Get directions (GTM) 11 Sep" action are being counted in the Conversions metric. Last week this was a risk; this week both fired. See deep dive 3.

6. **Two master negative lists are attached to the wrong campaigns.** At All Phase Pool Remodeling the 379-member All Phase Master Negatives link to the live campaign is set to REMOVED, so the list protects only the paused campaign. At Aqua Coat the 248-member Master Negative Lisst is still attached only to the paused campaign, unchanged since it was flagged on Sep 14.

7. **No account vanished from the MCC this week.** Premium Walk-In Clinic remains absent and that is expected. Premium Medication Refills, reported as vanished on Sep 14, is still not visible.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 28 client accounts, 1 manager | 13 | 2 new since Sep 14, none vanished. Excluded: Byers Fence x2, 8 LSA-only accounts. Not scored: Straightline and Color Masters (no spend), All Phase Jacksonville (LSA only), Jupiter Boat Supply and REK Marketing (paused). |

Search, Display and Performance Max spend in the 30-day window: $13,552 across the twelve REK-managed scored accounts, plus $18,358 at Filutowski Eye Institute. Local Services campaigns are excluded from every figure in this report.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Conv is the counted primary conversion total for 30 days. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status reflects urgency, not score alone.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $18,358 | 323.3 | $57 | 32 | F | -10 | Critical (scope) | Every current GA4 form action is hidden and uncounted; one broad keyword took $12,247 and matched 153 competitor, retail optical and insurer terms | $4,755 |
| 2 | Quality Paralegal Services | 447-153-2607 | $1,262 | 98.0 | $13 | 42 | F | new | Critical | 58 of 98 counted conversions are Business Profile directions taps; 100 percent of keyword spend is broad match | $184 |
| 3 | Precision GPR | 554-113-4760 | $2,672 | 16.0 | $167 | 52 | F | +2 | Needs attention | Seven campaigns each on Maximize Conversions with about 2 conversions a month apiece; $213 to the competitor brand GPRS and two directory sites | $213 |
| 4 | Progetto Shades | 416-010-8247 | $500 | 4.0 | $125 | 54 | F | new | Watch (relaunch) | All ten enabled ad groups carry a single RSA; 14 keywords at QS 1 to 3 | none confirmed |
| 5 | Patio Style | 596-555-8707 | $1,954 | 141.0 | $14 | 55 | F | -11 | Critical | GA4 and GTM directions actions both counting; Pergolas campaign spent $500 for 1 conversion; 11 of 12 ad groups still one RSA | $33 |
| 6 | Scootz | 185-574-5478 | $1,556 | 18.0 | $86 | 58 | F | 0 | Needs attention | Own brand costs $36 a month inside the non-brand campaign; still one campaign, one ad group, 32 keywords, on Maximize Clicks | $53 |
| 7 | Florida Sealcoating | 168-852-7101 | $2,074 | 24.0 | $86 | 59 | F | -4 | Needs attention | Branded target CPA removed Sep 15, brand spend up ten times; QS 1 on "driveway repair near me" carrying $217 | $192 |
| 8 | All Phase Pool Remodeling | 103-111-7688 | $660 | 21.0 | $31 | 60 | D | -12 | Needs attention | Master negative list link to the live campaign is REMOVED; 100 percent of keyword spend is broad match | $79 |
| 9 | M&S Asphalt Paving | 827-724-4095 | $83 | 2.0 | $41 | 61 | D | new | Watch (restarted) | Restarted Sep 15; all eight ad groups carry a single RSA; two call actions are mis-typed as lead forms | none confirmed |
| 10 | Rover Veterinary Care | 750-667-5721 | $1,581 | 13.0 | $122 | 62 | D | +1 | Needs attention | Recovered from zero, but In-Home Pet Euthanasia has taken $347 in 30 days for 0 conversions | $204 |
| 11 | Aqua Coat Pool Plastering | 285-714-0527 | $357 | 14.0 | $25 | 63 | D | -1 | On target | Master negative list still attached only to the paused campaign; 98 percent broad match | $46 |
| 12 | The Counseling Group | 657-069-3617 | $540 | 7.0 | $77 | 64 | D | -2 | On target | Tel-tap action still zero 40 days after it was built; book and medication research queries still arriving | $32 |
| 13 | Affordable Critter Solutions | 227-108-4521 | $313 | 15.0 | $21 | 69 | D | -7 | On target | Cleanest account in the fleet; $10 a day loses 45 percent of impressions to budget at a $21 CPA | $24 |
| none | Straightline Fence And Supply | 550-094-8786 | $0 | 0 | n/a | n/a | no spend | n/a | Critical | Ads disapproved, COMPROMISED_SITE, third week. See attention item 1 | n/a |
| none | Color Masters | 426-092-9847 | $0 | 0 | n/a | n/a | new build | n/a | Watch | Three REK search campaigns went live Sep 18. 17 impressions, no clicks, no spend yet | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | LSA only | n/a | Out of scope | Holds the Jacksonville LSA by design. No search activity | n/a |
| none | Jupiter Boat Supply, REK Marketing | | $0 | 0 | n/a | n/a | paused | n/a | Paused | Fully paused, no changes | n/a |

Confirmed waste across the fleet: $5,815 a month, of which $4,755 sits in Filutowski Eye Institute. Excluding Filutowski the figure is $1,060.

No account cleared 70 this week. The three marked On target have no blocking defect and are converting on plan; they are healthy relative to the fleet, not absolutely.

## Week over week (Sep 14 to 20 against Sep 7 to 13, search, Display and PMax)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $5,050 to $5,016 (-1%) | 490 to 511 | 6.2% to 6.3% | $10.31 to $9.82 | 84.0 to 75.3 | $60 to $67 | Flat spend, fewer conversions. The catch-all took $3,562 of the $5,016 |
| Quality Paralegal Services | $307 to $360 (+17%) | 204 to 183 | 1.1% to 1.0% | $1.50 to $1.97 | 20.0 to 23.0 | $15 to $16 | Smart campaign drove the gain; the two search campaigns went 5 to 2 |
| Precision GPR | $613 to $605 (-1%) | 53 to 53 | 6.6% to 6.8% | $11.57 to $11.42 | 1.0 to 7.0 | $613 to $86 | Best week since the cleanup began. Four of seven campaigns converted |
| Progetto Shades | $10 to $357 | 3 to 76 | 2.9% to 4.4% | $3.34 to $4.70 | 0.0 to 4.0 | none to $89 | Relaunch is now serving. Five of six campaigns spent |
| Patio Style | $441 to $488 (+11%) | 198 to 213 | 6.5% to 7.2% | $2.23 to $2.29 | 21.0 to 21.0 | $21 to $23 | Brand spend doubled to $62 for 0 conversions after three brand keywords were added Sep 16 |
| Scootz | $390 to $354 (-9%) | 621 to 555 | 7.6% to 6.9% | $0.63 to $0.64 | 4.0 to 7.0 | $98 to $51 | Best CPA in six weeks. Booqable purchases 5, calls 2 |
| Florida Sealcoating | $519 to $765 (+47%) | 164 to 107 | 3.6% to 5.5% | $3.16 to $7.15 | 7.0 to 7.0 | $74 to $109 | See attention item 2. Branded $21 to $217 |
| All Phase Pool Remodeling | $165 to $107 (-35%) | 27 to 22 | 5.7% to 3.9% | $6.10 to $4.87 | 4.0 to 2.0 | $41 to $54 | Rank lost impression share 87.8 percent, the highest in the fleet |
| M&S Asphalt Paving | $0 to $83 | 0 to 13 | none to 8.3% | none to $6.36 | 0.0 to 2.0 | none to $41 | Restarted by a bulk action Sep 15. Two estimate forms in six days |
| Rover Veterinary Care | $515 to $272 (-47%) | 42 to 52 | 16.4% to 13.0% | $12.25 to $5.23 | 0.0 to 3.0 | none to $91 | The Sep 16 budget and bid rebuild worked. See changes table |
| Aqua Coat Pool Plastering | $108 to $166 (+54%) | 19 to 27 | 3.6% to 3.6% | $5.66 to $6.16 | 4.0 to 7.0 | $27 to $24 | The Sep 9 target CPA continues to hold. Second good week |
| The Counseling Group | $131 to $115 (-12%) | 31 to 25 | 5.3% to 3.8% | $4.23 to $4.59 | 1.0 to 2.0 | $131 to $57 | Small numbers. Budget lost impression share 56.5 percent |
| Affordable Critter Solutions | $59 to $88 (+49%) | 19 to 23 | 6.2% to 9.5% | $3.11 to $3.83 | 4.0 to 4.0 | $15 to $22 | Steady. Budget lost impression share 45.1 percent |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: All Phase 87.8 percent, Progetto Shades & Blinds 78.0 percent, Motorized & Smart 72.0 percent, Shutters 69.3 percent, Patio Style Outdoor Furniture 66.4 percent, Aqua Coat 60.1 percent, Scootz 59.2 percent. Highest budget loss: Quality Paralegal 62.3 and 65.8 percent on its two search campaigns, The Counseling Group 56.5 percent, Filutowski catch-all 80.4 percent, Filutowski Branded 48.8 percent. Highest CPC increases: Florida Sealcoating Commercial ($16.04) and Residential ($17.08) against a $3.16 account average last week, Quality Paralegal ($1.50 to $1.97).

## Changes made in the past week (Sep 14 to Sep 21) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Rover Veterinary Care | Sep 16 | sheokand003@gmail.com | Competitors budget cut $30 to $5, Brand cut $20 to $10, In-Home Pet Euthanasia and Pet Cremation raised $20 to $30. Four ad group default bids raised from $0.01 to $3.00 and $4.00, five keyword bids set to $4.00. Two campaign criteria added | The clearest win of the week. Competitors spend fell $236 to $63, account spend fell 47 percent, and conversions went 0 to 3. The $0.01 ad group bids were a real defect and are now fixed. Watch that the euthanasia campaign, now at $30 a day, has still produced 0 conversions in 30 days |
| Florida Sealcoating | Sep 15 | sheokand003@gmail.com | Target CPA of $17 removed from the Branded campaign; Commercial Services budget raised $38 to $45 | Harmful. Branded spend $21 to $217 at an $11.40 CPC for 3 conversions, account CPA $74 to $109. See attention item 2 |
| Filutowski Eye Institute | Sep 14 | catie@accaliamarketing.com | LASIK catch-all daily budget raised $430 to $455 | The catch-all took $3,562 of the account's $5,016 this week and still lost 80.4 percent of impressions to budget. More money into the least efficient campaign in the fleet |
| Patio Style | Sep 15 to 17 | paidads@rekmarketing.com | 23 keywords added, 20 campaign negatives added and 19 removed, three brand keywords added to the Brand campaign, a Target Spend CPC ceiling of $8.00 removed | Mixed. Adding then removing "outdoor chairs" and "outdoor dining chairs" as exact negatives on a patio furniture retailer was caught and reverted within minutes, which is correct. But the competitor negatives added Sep 16 (homegoods, highland dunes, ebel, sunvilla, polywood, room to go) were all removed Sep 17 and only "kanes patio furniture" survives. Those brands are unprotected again. The three new brand keywords doubled Brand spend to $62 for 0 conversions |
| Color Masters | Sep 14 to 19 | tom@rekmarketing.com and colormasters88@gmail.com | 212 changes. The client removed 18 keywords from an old campaign and created a $75 a day campaign of seven broad "near me" keywords on Sep 16. Tom built three REK campaigns (Residential, Commercial, Brand) live Sep 18 with a shared negative list, 62 assets and 30 campaign assets | The client campaign and the older campaign are no longer enabled. Only the three REK campaigns remain, at $45, $25 and $5 a day. 17 impressions, no clicks, no spend in three days. Too early to read |
| Progetto Shades | Sep 14 and 18 | tom@rekmarketing.com | Target Spend CPC ceilings set to $4.00 on five campaigns Sep 14, then raised to $7.00 on three of them Sep 18 | Worked. The account went from $10 to $357 and from 0 to 4 conversions. The $4.00 ceiling was holding the relaunch out of the auction |
| Aqua Coat Pool Plastering | Sep 14 and 16 | sheokand003@gmail.com | Three brand keywords added ([aqua coat], [aqua coat pool plastering], "aqua coat pool"), the broad keyword "pool plastering services" removed, four campaign criteria added and two removed including a proximity target, two assets added | Sensible. Conversions 4 to 7 and CPA $27 to $24. The brand keywords should be split into their own campaign rather than sitting beside broad service terms |
| Quality Paralegal Services | Sep 16 and 18 | tom@rekmarketing.com, plus Google | Tom removed four campaign criteria and updated six assets. Google auto-paused 139 keywords on Sep 18 as a low activity system bulk change | The auto-pause is Google clearing dead broad keywords, not a REK action. Worth reviewing what it paused before adding anything back |
| All Phase Pool Remodeling | Sep 16 and 18 | tom@rekmarketing.com, sheokand003@gmail.com | Two campaign status updates and one ad group criterion status update | No measurable effect. Spend fell 35 percent and conversions 4 to 2 |
| M&S Asphalt Paving | Sep 15 | Bulk Actions | Three campaigns re-enabled | Account restarted after a dormant period. $83 and 2 conversions in six days |
| Straightline Fence | Sep 14 | robbie@rekmarketing.com | One campaign status update | No effect. Ads remain DISAPPROVED |
| Scootz, Affordable Critter, The Counseling Group, Precision GPR | | | No changes recorded in the window | The Sep 8 worklist items for these accounts have not been applied |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md)

Landed this week: the Rover bid and budget rebuild (items covering the $0.01 ad group bids and the Competitors overspend). Partly landed: the Patio Style competitor negatives were added and then removed, so item 5 is back to open. Not landed: the Florida Sealcoating competitor and supplier negatives, the Precision GPR change list, the Scootz account split, the Aqua Coat shared list reattachment, the All Phase brand split. Items 1, 2 and 20 stay blocked because Premium Walk-In Clinic is no longer under the MCC.

## Deep dive 1: Filutowski Eye Institute (192-870-7876), score 32 F, delta -10

Scope note: still new to the MCC. The only edits in 30 days are by catie@accaliamarketing.com and web@filutowski.com. No REK user has touched it. The change list below is prepared so Tom can decide; coordinate with Accalia Marketing before anything is applied.

| Category | Score | Last week |
|---|---|---|
| Conversion Tracking | 30 | 45 |
| Wasted Spend | 20 | 25 |
| Account Structure | 40 | 50 |
| Keywords & Targeting | 30 | 35 |
| Ads & Assets | 45 | 50 |
| Bidding & Settings | 35 | 50 |

Most of the 10-point drop is better information rather than deterioration. The hidden GA4 actions and the triple-counted call actions were not visible in the Sep 14 pull. The one real deterioration is the budget increase on the worst campaign.

Snapshot, 30 days: five enabled search campaigns, $17,809. Performance Max is now PAUSED and took $549. The LSA campaign is PAUSED and took $880, excluded here. 323.3 counted conversions at $57.

| Campaign | Budget/day | Spend | Clicks | CPC | Conv | CPA | Search IS | Lost to budget |
|---|---|---|---|---|---|---|---|---|
| S / Brand Awareness / LASIK | $455 | $12,247 | 679 | $18.04 | 65.3 | $188 | 11.3% | 82.0% |
| S / Branded / Dr. F | $50 | $1,416 | 546 | $2.59 | 124.3 | $11.39 | 40.1% | 55.8% |
| S / Lead Gen / Eye Surgery | $50 | $1,393 | 310 | $4.49 | 50.0 | $27.86 | 20.4% | 58.0% |
| S / Lead Gen / Cataracts | $50 | $1,392 | 193 | $7.21 | 18.0 | $77 | 43.9% | 27.3% |
| S / Lead Gen / LASIK | $50 | $1,360 | 97 | $14.02 | 10.7 | $127 | 45.3% | 33.6% |

### Findings

**The account cannot see its own leads.** Eleven conversion actions named "CURRENT - filutowskieye.com - GA4 (web)" and "CURRENT - Calendly - GA4 (web)", covering general_form_fill, rsx_form_fill, cataract_form_fill, od_referral, purchase and both virtual consultation bookings, are all in HIDDEN status and excluded from the Conversions metric. Nineteen Universal Analytics goals from the dead All Web Site Data view, including "Average Page per Session", "Average Visit Duration" and "Smart Goal", are still flagged primary and included; they record nothing because the view no longer exists. The result is that 307 of the 323 counted conversions in 30 days are phone calls, and only 5 are forms or bookings. Every automated bidding decision in the account is made on call volume alone.

**Calls can count more than once.** Three call actions are primary and included at the same time: "Calls to (800) 393-3926 (GENERAL)" at 167, "Calls to 407-602-6599 (LASIK CALL RAIL)" at 112.3, and "Phone Link Click (From Mobile)" at 28. A mobile tap that connects through the CallRail line will register the click action and the call action. The 28 mobile-tap conversions should be treated as suspect until one of the three is made secondary.

**Enhanced conversions for leads is ON.** The protocol is explicit: this is a medical practice and Google has no BAA in place, so it stays off. It is on today. This is the item to raise first with Accalia Marketing because it is a compliance question, not an optimisation one.

**One broad keyword is 67 percent of the account.** "S / Brand Awareness / LASIK" still runs a single broad keyword, "lasik treatment cost", on Target CPA, now at $455 a day. Of $11,230 in visible search-term cost across the account, $4,755 went to 153 terms that name other practices, retail optical chains or vision insurers, producing 18 conversions. The largest single items are "tomoka eye ormond beach" at $121.19, "bayhead eye center" at $120.44, "the eye place windermere" at $115.16, "america's best contacts & eyeglasses orlando" at $104.60 and "spectera vision providers" at $99.01. Broken down: competitor practices $3,008.42, retail optical $1,408.19, insurers $176.46, Spanish-language queries $161.81. Google withholds the low-volume remainder, so $4,755 is a floor, not a total.

**Brand and the working campaigns are starved while the catch-all is funded.** Branded converts at $11.39 and loses 55.8 percent of impressions to budget at $50 a day. Eye Surgery converts at $27.86 and loses 58.0 percent. The catch-all converts at $188 and just received a raise.

**Keywords and ads.** 69 percent of keyword spend is broad match. Ten keywords sit at QS 3 carrying $1,181, led by "eye specialist near me" at $391.69 and "ophthalmologist near me" at $314.09; both convert well, so the low score is expected-CTR driven rather than a waste problem. Eleven of 23 enabled ad groups carry a single RSA. Twenty enabled ads are POOR or AVERAGE strength.

### Prepared change list (only if Tom confirms REK is engaged)

1. Turn enhanced conversions for leads OFF at the account level. No BAA, no exception.
2. Set the eleven "CURRENT - GA4" actions to enabled, primary and included. Set all nineteen "All Web Site Data" goals to secondary and excluded. Do this before any bidding change so the new data starts accumulating.
3. Make "Phone Link Click (From Mobile)" secondary. Keep the two tracked lines primary.
4. Cut the LASIK catch-all budget from $455 to $200 a day and hold it there for two weeks.
5. Replace "lasik treatment cost" broad with a phrase and exact set: lasik, lasik cost, lasik near me, lasik orlando, lasik lake mary, smile eye surgery, prk surgery, laser eye surgery.
6. Raise Branded from $50 to $100 a day and Eye Surgery from $50 to $80. Both are budget-constrained at CPAs the catch-all cannot approach.
7. Add a shared negative list to all five live campaigns, phrase match: tomoka, bayhead, eye place, florida eye clinic, coan, mid florida eye, precision eye, clearvue, cohen eye, central florida eye, my eye doctor, lake eye, uptown eyecare, garay, fhcp, walmart, lenscrafters, america's best, americas best, costco, visionworks, warby, target optical, pearle, stanton, eyeglass, glasses, contacts, optical, eyemed, cigna, aetna, spectera, medicaid, medicare, ambetter, florida blue, humana, vsp, oftalmologo, cerca de mi, pediatric, retina, chalazion.
   Dedupe result: the account has two shared lists, "Search Terms" and "Brand Awareness", carrying 38 criteria between them. None of the names above is present on either list today, so all 44 are new. Check "contacts" and "glasses" against any optical retail arm before adding; if the practice sells eyewear, drop those two.

## Deep dive 2: Quality Paralegal Services (447-153-2607), score 42 F, new

Scope note: new under the MCC since Sep 14. tom@rekmarketing.com made edits on Sep 16 and Sep 18, so REK appears to be engaged, but the terms are not recorded anywhere in this repository. Confirm before applying.

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 45 |
| Account Structure | 40 |
| Keywords & Targeting | 30 |
| Ads & Assets | 55 |
| Bidding & Settings | 45 |

Snapshot, 30 days: four enabled campaigns, $1,262, 98 counted conversions at $13.

| Campaign | Type | Budget/day | Spend | Clicks | CTR | Conv |
|---|---|---|---|---|---|---|
| QPS Non-Lawyer Services Orlando | Smart | $15 | $447 | 418 | n/a | 64.0 |
| Experienced yet affordable Paralegal/Paralegal | Search | $13 | $344 | 81 | | 7.0 |
| Looking for an experienced yet affordable Paralegal? | Search | $12 | $323 | 99 | | 11.0 |
| Experienced Paralegal Services Provider | Smart | $5 | $148 | 382 | | 16.0 |

### Findings

**The $13 CPA is not a lead CPA.** Of 98 counted conversions in 30 days, 58 are "Local actions - Directions", which is a tap on directions in the Google Business Profile, and 10 more are "Clicks to call" from the profile rather than tracked calls. The genuinely tracked lead actions are "Calls from ads" at 26, "Calls from Smart Campaign Ads" at 3 and "Business profile - Tracked call" at 1. On 30 tracked calls the real CPA is $42, not $13. The protocol says to ask what the client's primary conversion is before scoring this category, and for a showroom a directions tap can legitimately be primary. A paralegal service that clients reach by phone is a different case. This needs one question answered before anything else in the account is judged.

**Every dollar of keyword spend is on broad match.** All 179 keywords with impressions are broad. There is no phrase or exact keyword anywhere in the account. This is why $216 went to terms that describe someone looking for a lawyer rather than a paralegal: "i need a lawyer now" $21.52, "civil attorney" $15.19, "the number to legal aid" $10.15, "legal aid melbourne fl" $10.07, "fathers rights legal aid" $8.43, "pro bono lawyers" $6.15, "free divorce lawyer" $5.46. Six of these terms did convert, which is worth understanding: if the practice is converting people who wanted a lawyer and settled for a paralegal, that is a positioning decision the client should make deliberately.

**QS 1 keywords point at the wrong service.** "immigration office near me" at QS 1 took $10.75, and "uscis contact number" and "citizenship and immigration services" are both QS 1 with no spend. These describe a government office, not a paralegal.

**Nearly half the spend is in Smart campaigns.** $595 of $1,262 sits in two Smart campaigns whose keywords, search terms, bids and ad content are not visible through the API. Their combined CTR is 1.2 percent on 82,948 impressions. Smart campaigns cannot be audited and cannot be tuned. Google auto-paused 139 low-activity keywords on Sep 18, which suggests the search campaigns are also carrying a large dead tail.

**Budget-constrained where it can be measured.** Both search campaigns lose over 62 percent of impressions to budget at $12 and $13 a day.

### Prepared change list

1. Ask the client whether a directions tap counts as a lead. If not, set "Local actions - Directions", "Clicks to call", "Local actions - Website visits" and "Local actions - Other engagements" to secondary and excluded, then re-baseline the CPA.
2. Convert the two search campaigns from all-broad to a phrase and exact core: "paralegal services", "paralegal near me", "document preparation services", "legal document preparer", "divorce paperwork help", "uncontested divorce forms", [paralegal orlando], [paralegal services orlando].
3. Add a shared negative list to both search campaigns, phrase match: lawyer, attorney, abogado, legal aid, pro bono, free, law firm, uscis, immigration office, citizenship, jobs, salary, school, certification, course, degree.
   Dedupe result: the existing list "QPS Search Negatives Tier 1" holds 114 criteria. Check "free" before adding as a standalone broad token; if the practice offers a free consultation, use phrase negatives such as "free lawyer" and "free legal advice" instead so a free-consultation query is not blocked. The same care applies to "attorney", which will block "paralegal for attorney" if the practice takes overflow work from law firms.
4. Rebuild the two Smart campaigns as standard Search campaigns so they can be audited. This is the single largest structural improvement available in the account.
5. If the tracked-call CPA of $42 is acceptable to the client, raise both search campaign budgets from $12 and $13 to $25 to recover the 62 percent lost to budget.

## Deep dive 3: Patio Style (596-555-8707), score 55 F, delta -11

| Category | Score | Last week |
|---|---|---|
| Conversion Tracking | 50 | 65 |
| Wasted Spend | 65 | 70 |
| Account Structure | 65 | 70 |
| Keywords & Targeting | 60 | 65 |
| Ads & Assets | 35 | 50 |
| Bidding & Settings | 55 | 70 |

### Findings

**The directions double count predicted on Sep 14 is now live.** Both the GA4 import "www.patiostyle.com - GA4 (web) get_directions" and the GTM action "Get directions (GTM) 11 Sep" are counted in the Conversions metric. Over 30 days they contributed 119 and 15. This week they contributed 6 and 14. The pattern is consistent with the GTM tag taking over from the GA4 import rather than doubling every tap, but both are counting and the handover is mid-flight, so any tap captured by both is counted twice. The fix is one line: make one of them secondary. Directions as a primary conversion is correct for this client and is not the issue.

**Two actions built on Sep 11 have never fired.** "Website Call Conversions 11 Sep (407) 862-4600" and "Thank you page 11 Sep" are both primary and included and both sit at zero for the ten days they have existed. Following the protocol these are not declared dead; they need a manual trigger test, a call to the tracked number and a test form submission, before the next run.

**The Pergolas campaign has taken $500 in 30 days for 1 conversion.** "insulated patio cover" at $162.70 and "louvered pergola" at $156.44 have produced nothing across 31 and 25 clicks. The campaign runs Manual CPC at an $8.85 average CPC, the highest in the account, and lost 44.5 percent of impressions to budget this week, meaning the account is queuing to spend more on it. Research and competitor queries are visible inside it: "louvered pergola cost" $10.08, "best louvered pergola 2026" $10.02, "azenco r blade" $7.94 and "azenco pergola" $5.09.

**A week of negative keyword work netted one negative.** Twenty campaign negatives were added on Sep 16 and nineteen removed on Sep 17. Only "kanes patio furniture" survives. The competitor brands homegoods, highland dunes, ebel, sunvilla and polywood are unprotected again, and the master list does not carry them; it holds "rooms to go" as a phrase negative, which does not block the singular spelling "room to go patio furniture" that was being negated. Adding "outdoor chairs" and "outdoor dining chairs" as exact negatives to a patio furniture retailer was reverted within minutes, which was the right call.

**Three brand keywords doubled brand spend for nothing.** "patio styles", "patio style longwood fl" and "patio style orlando" were added as phrase keywords to the Brand campaign on Sep 16. Brand spend went $26.13 to $61.54 week over week and conversions went 3 to 0. Over 30 days "patio styles" alone has taken $51.18 with no conversions. The Target Impression Share strategy set on Sep 4 is working (29.6 percent impression share this week) but it is now buying a broader set of queries than the brand.

**Ads are the oldest unaddressed item.** Eleven of twelve enabled ad groups still carry a single RSA. This has been reported on Sep 4, Sep 14 and now Sep 21.

### Prepared change list

1. Set "www.patiostyle.com - GA4 (web) get_directions" to secondary and excluded, leaving the GTM action as the single counted directions source. Do this before reading next week's numbers.
2. Run a manual trigger test on the 11 Sep call and thank-you actions.
3. Pause "insulated patio cover" and "louvered pergola" phrase keywords. Cut the Pergolas budget from $16 to $8 a day until the campaign produces a conversion.
4. Pause the phrase keyword "patio styles" in the Brand campaign. Keep the two location brand keywords.
5. Add to the Master Negatives shared list, phrase match: homegoods, home goods, highland dunes, ebel, sunvilla, polywood, room to go, azenco, pergolux, sunsetter, struxure.
   Dedupe result: "rooms to go" (plural), "pergolux", "wayfair", "amazon", "costco", "big lots", "home depot", "lowes", "walmart", "ikea" and "palm casual" are already on the 52-member list. New additions are homegoods, home goods, highland dunes, ebel, sunvilla, polywood, room to go (singular), azenco, sunsetter and struxure. None of these would block a relevant query for this retailer.
6. Add a second RSA to the eleven single-ad ad groups. This is the third week it has been listed.

## Deep dive 4: All Phase Pool Remodeling (103-111-7688), score 60 D, delta -12

| Category | Score | Last week |
|---|---|---|
| Conversion Tracking | 60 | 70 |
| Wasted Spend | 70 | 80 |
| Account Structure | 60 | 75 |
| Keywords & Targeting | 50 | 65 |
| Ads & Assets | 55 | 70 |
| Bidding & Settings | 60 | 70 |

The 12-point drop is driven by one newly-found defect. The detached negative list is almost certainly not new; it was not checked at campaign-link level before this run. Read this as a correction to the score rather than a week of decline.

### Findings

**The master negative list does not protect the live campaign.** The account has a 379-member shared list, "All Phase Master Negatives". It is linked ENABLED to the paused campaign "All Phase - Pool Remodeling | Search" and the link to the live campaign "All Phase Pool Remodeling - M" is set to REMOVED. The live campaign is therefore defended only by 91 campaign-level negatives. This is the same class of fault as Aqua Coat and it should be checked across the fleet.

**Every dollar of keyword spend is broad match.** All 19 keywords with impressions are broad. With the shared list detached, that combination is why "leslie pool" took $21.30 and "pinch a penny mount dora" took $8.17, both pool supply retailers, and "pool cleaners near me" took $9.33 for a remodelling company. Confirmed irrelevant spend is $79.26 in 30 days.

**Brand queries are being paid for inside the non-brand campaign.** "all phase pools" appears twice in the search terms at $23.26 and $13.39 with no conversions, plus smaller variants. There is no brand campaign.

**The account is losing the auction, not the budget.** Rank-lost impression share was 87.8 percent this week, the highest in the fleet, against 0.0 percent lost to budget at $30 a day. The campaign is not spending its budget because its bids are not competitive, so raising the budget would do nothing.

**"Phone Calls 60s+" has never recorded a conversion.** It is primary and included and sits at zero. Its creation date is not recorded in the known-context section, so per the protocol it is flagged for a manual trigger test rather than declared dead.

### Prepared change list

1. Re-link "All Phase Master Negatives" to the live campaign "All Phase Pool Remodeling - M". This is a two-click fix and the highest-value item in the account.
2. Convert the top spending broad keywords to phrase: "pool remodeling", "pool resurfacing", "pool renovation", "pebble tec", "pool refinishing". Leave one broad keyword for discovery.
3. Add campaign negatives, phrase match: leslie pool, pinch a penny, pool cleaner, pool cleaning, pool service, pool paint, pool chemicals, pool supplies, all phase pools.
   Dedupe result: the 91 existing campaign negatives and the detached 379-member list were both checked; none of these nine is live on the serving campaign today. Note that "all phase pools" as a negative only makes sense once a brand campaign exists to catch it, so add it last.
4. Build a small brand campaign on exact match at $5 a day rather than paying non-brand bids for brand queries.
5. Raise the ad group default bid or move to Target CPA. With 87.8 percent rank loss and 21 conversions a month, Maximize Conversions has enough signal to work but is bidding too low to enter the auction.
6. Add a second RSA to the two single-ad ad groups and replace the POOR ad in Pool Renovation.

## Deep dive 5: Precision GPR (554-113-4760), score 52 F, delta +2

Context: under active cleanup since Aug 2026, so deliberate week-over-week movement is expected.

| Category | Score | Last week |
|---|---|---|
| Conversion Tracking | 60 | 55 |
| Wasted Spend | 55 | 45 |
| Account Structure | 45 | 50 |
| Keywords & Targeting | 55 | 50 |
| Ads & Assets | 50 | 50 |
| Bidding & Settings | 30 | 50 |

### Findings

**The best week since the cleanup started.** 7 conversions on $605, a CPA of $86 against $613 the week before and $167 across 30 days. Four of the seven campaigns converted this week, where none did last week. Nothing was changed in the account during the window, so this is the earlier work landing rather than a new intervention.

**Seven campaigns share 16 conversions a month.** Every one runs Maximize Conversions. That is roughly two conversions per campaign per month, far below the threshold at which the strategy has anything to learn from. Five of the seven lose 30 to 52 percent of impressions to budget at $10 to $20 a day each. The account is spread too thin for its conversion volume, and this is the reason the Bidding score fell.

**$213 went to a competitor brand and two directory sites.** GPRS is a national ground penetrating radar company and its name is being bought across nine terms: "gprs utility locating" $38.87 and $7.33, "gprs florida" $20.86, "gprs tampa" $20.58, "gprs service" $18.23, "gprs scanning" $15.08, "gprs orlando" $14.32, "gprs company" $7.21, "gprs" $4.23. Add "www sunshine811" at $18.71, which is the Florida utility notification service, "geoslice net" at $17.85, and a Spanish-language query at $30.14. None converted.

**Quality Score is low on the two largest keywords.** "Ground Penetrating Radar" carries QS 3 on $757.79 of spend across two instances, and "Underground Utility Survey" carries QS 2 on $288.89. Together with the others, six keywords at QS 1 to 3 carry $1,048, which is 39 percent of account spend.

**The branded campaign is not converting.** "Precision Gpr" exact took $138.79 across 18 clicks with no conversions, and the search term "precision gpr" took $138.74. Someone searching the company name and not converting points at the landing page, not the ad.

**Negatives are in place but not doing this job.** The shared list "LP NKWs" holds 227 criteria and is linked ENABLED to all seven live campaigns, which is correct. None of the GPRS terms is on it.

### Prepared change list

1. Consolidate the four service campaigns (GPR Scanning, Concrete Scanning, Utility Mapping, Services) into one campaign with four ad groups on a single $60 a day budget. One campaign with 16 conversions a month can run Maximize Conversions; four campaigns with four each cannot.
2. Add to the "LP NKWs" shared list, phrase match: gprs, sunshine811, sunshine 811, geoslice, 811, radar de, penetracion, penetración.
   Dedupe result: none of these eight is on the 227-member list today. Take care with "811" as a standalone token; use "sunshine 811" and "811 locate" instead so it cannot block an address or phone number in a longer query.
3. Review the landing page behind the branded campaign before spending more there. $139 of brand clicks with no conversion is a page problem.
4. Rewrite the ads in the three POOR ad groups in the Sharp Advantage Campaign and the branded ad group.
5. Leave the QS 2 and 3 keywords alone for now. They carry the account's volume and the low scores are expected-CTR driven.

## No action needed this week

- **Aqua Coat Pool Plastering (285-714-0527), 63 D.** Second consecutive good week. The Sep 9 target CPA is holding and the Sep 16 brand keywords are sensible. Conversions 4 to 7 at a $24 CPA. One open item carries over: reattach the 248-member "Master Negative Lisst" to the live campaign, and consider splitting the three new brand keywords into their own campaign. Confirmed waste is $46, mostly pool equipment retail queries.
- **The Counseling Group (657-069-3617), 64 D.** On plan. $540 in 30 days against a $25 a day budget on a Monday to Friday schedule, which is the expected $650 a month. Enhanced conversions for leads is confirmed OFF, which is correct with no BAA. Two open items: the tel-tap action built Aug 12 has still recorded nothing after 40 days and needs a manual trigger test, and $32 a month is going to book, author and medication research queries such as "healing anxiety and depression daniel g amen pdf" and "best antidepressant for anxiety and depression". Suggested phrase negatives: pdf, book, supplements, antidepressant, medication, worksheet. Do not add "free" as a standalone token because the practice advertises a free 15-minute consultation.
- **Affordable Critter Solutions (227-108-4521), 69 D.** The cleanest account in the fleet. No low Quality Score keywords, a 45-member and 143-member negative structure attached correctly, a $21 CPA. Two things to look at: $10 a day is losing 45.1 percent of impressions to budget at that CPA, which is the clearest case in the fleet for more money, and "Website calls" and "Calls From Ads" both recorded exactly 6 conversions in 30 days, which may be the same calls counted twice. Competitor brand terms took $23.57 and should be negated: critter control, cassan, allstar animal.
- **Scootz (185-574-5478), 58 F.** Best CPA in six weeks at $51 and conversions up 4 to 7. The structural finding is unchanged: one campaign, one ad group, 32 keywords, running Maximize Clicks with 18 conversions a month. Own-brand queries cost $36 inside the non-brand campaign and competitor brand Scooterbug took $17. The GA4 form_submit action reported dead on Sep 14 is still excluded and still at zero.
- **Rover Veterinary Care (750-667-5721), 62 D.** Recovered. The Sep 16 rebuild fixed ad group bids that had been sitting at $0.01 and cut the Competitors budget from $30 to $5. Spend fell 47 percent and conversions went 0 to 3. One thing to watch: In-Home Pet Euthanasia has now taken $347 over 30 days with zero conversions and its budget was just raised from $20 to $30. Competitor brand terms that did not convert took $204.
- **Progetto Shades (416-010-8247), 54 F.** The relaunch is working. The $4.00 CPC ceilings set Sep 14 were holding the account out of the auction; raising three of them to $7.00 on Sep 18 took the account from $10 to $357 and from 0 to 4 conversions. Score is low because all ten ad groups carry a single RSA and fourteen keywords sit at QS 1 to 3. Both are normal for a two-week-old build. Leave it to run another week before changing anything.
- **M&S Asphalt Paving (827-724-4095), 61 D.** Restarted by a bulk action on Sep 15 after a dormant period. $83 and 2 estimate forms in six days. Two findings worth noting now: all eight ad groups carry a single RSA, and two conversion actions named "Call ((386) 215-7466)" and "Calls from ads" are typed as SUBMIT_LEAD_FORM rather than as phone call actions, which will misreport them. Neither has recorded anything yet.
- **Color Masters (426-092-9847).** New. Three REK campaigns went live Sep 18 at $45, $25 and $5 a day with a shared negative list attached to all three. 17 impressions, no clicks, no spend in three days. The client's own $75 a day campaign created Sep 16 is no longer enabled. Nothing to score. Check next Monday that it has started serving.
- **All Phase Pool Remodeling - Jacksonville (918-824-8896).** Holds the Jacksonville LSA by design. No search activity, nothing leaking.
- **Jupiter Boat Supply (216-859-2093) and REK Marketing (390-315-5264).** Fully paused, no changes.
- **Byers Fence (870-428-8862) and Byers Fence LSA (276-105-5321).** Under the MCC, not managed by REK. Excluded.

## Prioritized weekly action plan

Ordered by money at risk and by how quickly the fix can be applied.

| # | Account | Action | Owner | Why now |
|---|---|---|---|---|
| 1 | Straightline Fence | Tell the client the site is flagged COMPROMISED_SITE and must be cleaned before an appeal can be filed | Robbie | Third week of zero serving. Nothing in Ads can fix it |
| 2 | Florida Sealcoating | Put the $17 target CPA back on the Branded campaign | Dave to brief sheokand003 | Brand spend went up ten times in one week and account CPA rose 47 percent |
| 3 | Filutowski Eye Institute | Turn enhanced conversions for leads OFF | Tom, with Accalia | Compliance. Medical practice, no BAA |
| 4 | Filutowski Eye Institute | Enable the eleven CURRENT GA4 actions, retire the nineteen UA goals, make the mobile tap action secondary | Tom, with Accalia | The account is optimising $18,358 a month on phone calls alone |
| 5 | Filutowski Eye Institute | Cut the LASIK catch-all from $455 to $200 a day | Tom, with Accalia | $12,247 in 30 days at a $188 CPA, and the budget just went up |
| 6 | Patio Style | Make the GA4 get_directions action secondary | paidads | Double count is live, not theoretical |
| 7 | All Phase Pool Remodeling | Re-link the master negative list to the live campaign | Dave | Two clicks. The live campaign has been running on 91 negatives instead of 470 |
| 8 | Aqua Coat | Re-link the master negative list to the live campaign | Dave | Same fault, flagged Sep 14, still open |
| 9 | Quality Paralegal Services | Ask the client whether a directions tap counts as a lead | Tom | Everything else in the account is scored off that answer |
| 10 | Patio Style | Re-add the competitor negatives to the Master Negatives list and pause "patio styles" | paidads | A week of negative work netted one negative |
| 11 | Patio Style | Pause the two non-converting pergola keywords and halve that budget | paidads | $500 for one conversion |
| 12 | Precision GPR | Add the GPRS and directory negatives to the LP NKWs list | Dave | $213 a month to a competitor's name |
| 13 | Rover Veterinary Care | Review In-Home Pet Euthanasia, now at $30 a day with 0 conversions in 30 days | Dave | The budget was raised into a campaign that has not converted |
| 14 | Quality Paralegal Services | Add phrase and exact keywords alongside the all-broad set | Tom | 100 percent broad match with no exact or phrase anywhere |
| 15 | Affordable Critter Solutions | Raise the budget from $10 to $20 a day | Dave | Losing 45 percent of impressions to budget at a $21 CPA. The best return available in the fleet |
| 16 | The Counseling Group | Manual trigger test on the tel-tap action | Dave | 40 days, no data, cannot be called dead without a test |
| 17 | Patio Style | Manual trigger test on the two 11 Sep actions | paidads | Ten days, no data |
| 18 | Patio Style, All Phase, M&S, Progetto | Add a second RSA to every single-ad ad group | Dave | 40 ad groups across four accounts. Third week on the list for Patio Style |
| 19 | Precision GPR | Consolidate four service campaigns into one | Dave | 16 conversions cannot feed seven automated bidding strategies |
| 20 | Quality Paralegal Services | Plan the migration of the two Smart campaigns to standard Search | Tom | $595 a month that cannot be audited |
| 21 | Fleet | Check every account for shared negative lists linked to paused campaigns only | Dave | Two found this week by accident. This should be a standing check |

### Negative keywords proposed this week, by account

All proposals below were deduped against live campaign negatives and shared list criteria. Where a proposal was dropped as already present, it is named.

- **Filutowski Eye Institute:** 44 phrase negatives listed in deep dive 1. None present on the existing 38-criteria lists. Check "contacts" and "glasses" against any optical retail arm first.
- **Quality Paralegal Services:** lawyer, attorney, abogado, legal aid, pro bono, law firm, uscis, immigration office, citizenship, jobs, salary, school, certification, course, degree. Use "free lawyer" and "free legal advice" rather than the standalone token "free". Existing list holds 114 criteria; none of these is on it.
- **Patio Style:** homegoods, home goods, highland dunes, ebel, sunvilla, polywood, room to go, azenco, sunsetter, struxure. Dropped as already present: rooms to go, pergolux, wayfair, amazon, costco, big lots, home depot, lowes, walmart, ikea, palm casual.
- **All Phase Pool Remodeling:** leslie pool, pinch a penny, pool cleaner, pool cleaning, pool service, pool paint, pool chemicals, pool supplies. Add "all phase pools" only after a brand campaign exists.
- **Precision GPR:** gprs, sunshine 811, sunshine811, geoslice, radar de, penetracion, penetración. Avoid the standalone token "811".
- **Aqua Coat:** pentair, hayward, pinch a penny, pool pump, pool liner, repair kit. Reattach the shared list first; these belong on it.
- **Affordable Critter Solutions:** critter control, cassan, allstar animal.
- **The Counseling Group:** pdf, book, supplements, antidepressant, medication, worksheet. Do not add "free"; the practice advertises a free 15-minute consultation.
- **Scootz:** scooterbug, gold mobility, buena vista scooter, apple scooters. Own-brand terms should be split into a brand campaign rather than negated outright.

### Keywords proposed to add

- **Filutowski Eye Institute:** lasik, lasik cost, lasik near me, lasik orlando, lasik lake mary, smile eye surgery, prk surgery, laser eye surgery, as phrase and exact, replacing the single broad catch-all.
- **Quality Paralegal Services:** "paralegal services", "paralegal near me", "document preparation services", "legal document preparer", "divorce paperwork help", "uncontested divorce forms", [paralegal orlando], [paralegal services orlando].
- **All Phase Pool Remodeling:** "pool remodeling", "pool resurfacing", "pool renovation", "pebble tec", "pool refinishing" as phrase, plus an exact-match brand set in a new brand campaign.

### Bid and budget adjustments proposed

| Account | Campaign | From | To | Reason |
|---|---|---|---|---|
| Florida Sealcoating | Branded | no target CPA | $17 target CPA | Restore the control removed Sep 15 |
| Filutowski | S / Brand Awareness / LASIK | $455/day | $200/day | $188 CPA against a fleet-best $11.39 in the same account |
| Filutowski | S / Branded / Dr. F | $50/day | $100/day | 55.8 percent of impressions lost to budget at an $11.39 CPA |
| Filutowski | S / Lead Gen / Eye Surgery | $50/day | $80/day | 58.0 percent lost to budget at a $27.86 CPA |
| Affordable Critter | ACS - Search | $10/day | $20/day | 45.1 percent lost to budget at a $21 CPA |
| Patio Style | Pergolas & Louvered Roofs | $16/day | $8/day | $500 in 30 days for 1 conversion |
| All Phase | All Phase Pool Remodeling - M | keep $30/day | raise ad group bid or move to Target CPA | 87.8 percent rank loss with 0 percent budget loss. Budget is not the constraint |
| Quality Paralegal | both search campaigns | $12 and $13/day | $25/day each | Over 62 percent lost to budget, but only after the conversion definition is settled |
| Rover | In-Home Pet Euthanasia | $30/day | hold or reduce | Raised Sep 16 into a campaign with 0 conversions in 30 days |

## Rotation

Deep-dived this month: Filutowski Eye Institute, Quality Paralegal Services, Patio Style, All Phase Pool Remodeling, Precision GPR (Sep 21); Filutowski, Precision GPR, Scootz, Rover, Florida Sealcoating (Sep 14); The Counseling Group (Sep 4).

Due next: Aqua Coat Pool Plastering, Affordable Critter Solutions, Scootz and Progetto Shades. Color Masters and M&S Asphalt Paving should get their first full deep dive once they have three weeks of spend.

## Data notes

- Every figure in this report comes from a GAQL query run during this session. No number is carried over from a previous report except the score deltas, which are stated as such.
- Auction insight metrics were not queried. The developer token has Basic access and those metrics error. Rank-lost impression share is used as the bid competition proxy throughout.
- Filutowski Eye Institute conversion totals use the Conversions metric segmented by conversion action name, which counts only actions flagged primary and included. The all_conversions totals are materially higher and are not used anywhere in this report.
- The $4,755 Filutowski waste figure reconciles as competitor practices $3,008.42, retail optical $1,408.19, insurers $176.46 and Spanish-language queries $161.81, across 153 terms carrying 18 conversions, out of $11,229.81 of visible search-term cost.
- Straightline Fence And Supply returned zero rows for keywords, search terms and negatives because the account has never served. That is an absence of data, not a failed query.
- No query failed this run. Nothing is reported as unavailable.
