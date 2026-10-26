# PPC Weekly Audit - 2026-10-26 (Google Ads fleet)

Run: Monday Oct 26, 2026, scheduled cloud session through tools/gaql.py against MCC 656-695-7229. Windows: 30 days Sep 26 to Oct 25; this week Oct 19 to Oct 25; last week Oct 12 to Oct 18; previous 30 days Aug 27 to Sep 25. Score deltas are against the Sep 14 report, the last run with Google Ads data (six weeks ago, so several deltas are large). Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Patio Style (17-point drop, on rotation), Filutowski Eye Institute (worst score), Progetto Shades (first full score since the relaunch), The Counseling Group (October rotation, 7-point drop) and Aqua Coat (on rotation, to measure the September bidding change). Shorter follow-ups on Precision GPR, Rover, Scootz and Florida Sealcoating, which were deep-dived Sep 14. One-liners for the rest.

Credential: the google-ads.yaml in the Drive folder dave-ads-setup (last modified Sep 8) authenticated on the first try. It was copied with mode 600, read only by the google-ads client library, and deleted before this report was committed. No value from it appears anywhere in the session output. One tooling note: the installed google-ads Python library (34.0.0) no longer carries API v22, which tools/gaql.py used as its default. This run used v24 and the default in gaql.py is updated in this commit.

## Attention items (read first)

1. **Patio Style (596-555-8707) is no longer counting Get Directions as a conversion.** Both directions actions, the GA4 get_directions import and "Get directions (GTM) 11 Sep", are now secondary and excluded. The GTM action stopped counting as primary after Sep 21 and the GA4 import was already secondary by Sep 20. Known account context says directions to the showroom is the client's primary conversion. Reported primary conversions fell from 124 in the previous 30 days to 12 in this window (CPA $16 to $160), and the Brand campaign was moved to Maximize Conversions on Oct 23, so it is now learning on 3 conversions. Conversion action edits do not appear in change history, so the API cannot say who demoted them. If this was not intended, restore one directions action to primary (the GTM one, which does not double count the import) before the Brand campaign learns the wrong thing. Deep dive 1.
2. **Filutowski Eye Institute (192-870-7876) has a new website going live, and its conversion tracking depends on old thank-you URLs.** Tom's sheet "FEI New Website URL Changes (for Google Ads)" (Oct 19) says every old thank-you URL will 301 to a fallback page that fires no event, and that any conversion triggered on those URLs stops at launch. The three website form actions (More Info Form Submit, Vision In-Office Appointment, Contact Page Form Submit) were still recording through Oct 24, which means the launch had not yet broken them as of the data pull. The Cataracts ad final URL (/cataract-surgery/) will redirect, the blog sitelink will be broken, and one sitelink already 404s. The site itself could not be fetched from this session (proxy policy), so launch status is unavailable. The account is otherwise unchanged in shape: one broad keyword is 68 percent of spend. Deep dive 2.
3. **The Counseling Group (657-069-3617) has had zero primary conversions since Oct 9**, 16 days, on about $255 of spend. Two in the 30-day window against six in the previous 30. The tel-tap action built Aug 12 finally recorded its first four conversions (Oct 5 to Oct 20) but they show only in All conversions, not in the Conversions column, even though the action is primary and included. That is worth a look in the UI before any bid change. Deep dive 4.
4. **Five accounts are new under the MCC since Sep 14, none vanished.** Quality Paralegal Services (447-153-2607, Tom-managed search, scored below), Color Masters (426-092-9847, Tom-managed search, paused Oct 22 after $1,240 and 3 conversions), Color Masters LSA, MB Skin Care (LSA only, created Oct 5) and All Phase Pool Remodeling (Orlando LSA). M&S Asphalt Paving (827-724-4095), reported as paused on Sep 14, is live again: Tom re-enabled the Sealcoating campaign Oct 15 and it spent $527 for 7 conversions in 30 days. It is scored below.
5. **Straightline Fence And Supply (550-094-8786) no longer has a search campaign.** The campaign with the COMPROMISED_SITE disapprovals has been removed; only the LSA campaign remains ($3,351 and 24 phone leads in 30 days). The account moves to the LSA-only exclusion list.
6. **Rover Veterinary Care's "lap of love" exact keyword spent $230 across its variants for zero conversions in 30 days.** On Sep 14 the same term had produced 6 conversions on $271. The Competitors campaign budget was raised from $5 to $20 a day on Oct 6 and both of its RSAs are still POOR. Follow-up section.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 31 client accounts, 1 manager | 13 | 5 new since Sep 14, 0 vanished. Excluded: Byers Fence x2, Herrell Plumbing, 10 LSA-only accounts (now including Straightline Fence and MB Skin Care). Not scorable: Color Masters (paused Oct 22), All Phase Jacksonville (no search spend), Jupiter Boat Supply and REK Marketing (no client spend). |

Search, Performance Max and display spend in the 30-day window: $34,921 across the 13 scored accounts, of which $17,525 is Filutowski Eye Institute. Local Services campaigns are excluded from every figure in this report unless marked.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $17,525 | 214 | $82 | 38 | F | -4 | Critical | "lasik treatment cost" broad is $11,859 (68 percent) and still matches competitor clinics, retail optical, insurers and doctor names; website relaunch threatens the form actions | $3,400 |
| 2 | Patio Style | 596-555-8707 | $1,914 | 12 | $160 | 49 | F | -17 | Critical | Both directions actions demoted to secondary; Brand campaign now learning Maximize Conversions on 3 conversions; 12 of 14 ad groups one RSA | $60 |
| 3 | Progetto Shades | 416-010-8247 | $2,112 | 5 | $422 | 53 | F | new | Needs attention | Relaunch under Tom's daily hand: spend tripled to $190 a day since Oct 23 on 5 conversions in 30 days; 38 keywords at QS 1 to 3 with landing page Below average everywhere | $75 |
| 4 | Rover Veterinary Care | 750-667-5721 | $1,904 | 15 | $127 | 57 | F | -4 | Needs attention | "lap of love" $230 for 0 conversions, Competitors budget quadrupled Oct 6, both Competitors RSAs still POOR; website-call action silent since Sep 15 | $420 |
| 5 | Scootz | 185-574-5478 | $1,486 | 28 | $53 | 58 | F | 0 | Needs attention | The GA4 form_submit action is gone from the account, so no form is tracked at all; still one ad group on Maximize Clicks; CPC doubled after the Oct 22 campaign edit | $75 |
| 6 | Precision GPR | 554-113-4760 | $2,603 | 26 | $100 | 59 | F | +9 | Needs attention | Improving (18 to 26 conversions, CPA $155 to $100). "gprs" still not a negative and was added as a keyword Oct 23; Location and DSA campaigns still on | $275 |
| 7 | The Counseling Group | 657-069-3617 | $554 | 2 | $277 | 59 | F | -7 | Needs attention | Zero primary conversions since Oct 9; tel-tap fires but does not count; informational and name queries half of visible spend | $85 |
| 8 | Quality Paralegal Services | 447-153-2607 | $1,333 | 53 | $25 | 62 | D | new | Needs attention | Healthy CPA. "family law attorney near me" broad at QS 1 is $309 of spend for a non-lawyer practice; Spanish campaign RSA is POOR; one ad disapproved | $110 |
| 9 | M&S Asphalt Paving | 827-724-4095 | $527 | 7 | $75 | 62 | D | new | Needs attention | Live again since Oct 15, converting; 4 of 6 ad groups one RSA; cost and DIY queries two-thirds of visible spend | $100 |
| 10 | Florida Sealcoating | 168-852-7101 | $3,312 | 28 | $118 | 63 | D | 0 | Needs attention | Branded campaign pays $10 a click ($727 for 3 conversions) because it still matches generic paving and sealcoating queries; "asphalt patch repair" in both campaigns, $247 for 0 | $240 |
| 11 | Aqua Coat Pool Plastering | 285-714-0527 | $430 | 13 | $33 | 64 | D | 0 | Needs attention | Master negative list still attached only to the paused campaign; Pool Equipment group still live ($110, 1 conversion); target CPA from Sep 9 is gone | $100 |
| 12 | All Phase Pool Remodeling | 103-111-7688 | $927 | 16 | $58 | 64 | D | -8 | Needs attention | CPC up 34 percent and now 54 percent lost to budget at $30 a day; brand term is $415 of $927 inside non-brand groups and 14 of 16 conversions | $70 |
| 13 | Affordable Critter Solutions | 227-108-4521 | $294 | 14 | $21 | 78 | C | +2 | On target | Clean; 1 conversion this week against 5 last week on the same spend, small numbers | $25 |
| none | Color Masters | 426-092-9847 | $1,271 | 3 | $424 | n/a | paused | new | Paused | Tom paused all three campaigns Oct 22 (Commercial Oct 12). Residential Painting spent $1,240 at $10 a click on cost and DIY queries | n/a |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | no search spend | n/a | Paused (search) | "Orlando" campaign still ENABLED and NOT_ELIGIBLE, nothing leaking; LSA campaign paused | n/a |
| none | Jupiter Boat Supply, REK Marketing | | $0 and $55 | 0 | n/a | n/a | n/a | n/a | n/a | Jupiter fully paused. REK Marketing has Tom's "GBP Verification" campaign, $55 this week | n/a |

## Week over week (Oct 19 to 25 against Oct 12 to 18, search, PMax and display only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $4,489 to $3,367 (-25%) | 366 to 205 | 6.9% to 5.6% | $12.26 to $16.43 | 61 to 35 | $74 to $96 | Mon-Fri schedule added Oct 15 cut weekend spend; Eye Surgery 10 to 2 conversions, Branded CPC $4.14 to $7.99 |
| Florida Sealcoating | $847 to $833 (-2%) | 92 to 83 | 6.9% to 7.1% | $9.20 to $10.04 | 4 to 8 | $212 to $104 | Commercial 2 to 4, Residential 0 to 2; display remarketing 2 at $17 |
| Precision GPR | $713 to $625 (-12%) | 48 to 42 | 7.1% to 4.7% | $14.86 to $14.89 | 2.5 to 5.5 | $285 to $114 | Better week; Oct 24 and 25 spent $18 total (weekend) |
| Progetto Shades | $436 to $689 (+58%) | 116 to 132 | 7.0% to 5.3% | $3.76 to $5.22 | 0 to 2 | n/a to $345 | Bid ceilings raised Oct 20 to 23; $190 a day from Oct 23 |
| Rover Veterinary Care | $471 to $597 (+27%) | 63 to 61 | 10.0% to 12.2% | $7.48 to $9.78 | 2 to 4 | $236 to $149 | In-Home CPC $14.85 to $20.51; Competitors 0 conversions two weeks running |
| Patio Style | $461 to $436 (-5%) | 213 to 218 | 6.9% to 7.7% | $2.16 to $2.00 | 2 to 1 | $230 to $436 | 91 all-conversions this week, almost all directions, none counted |
| Scootz | $335 to $357 (+7%) | 134 to 250 | 7.6% to 7.8% | $2.50 to $1.43 | 7 to 3 | $48 to $119 | Campaign re-entered learning after Oct 22 edit; last week's CPC was $2.50 against $0.67 in September |
| Quality Paralegal Services | $357 to $350 (-2%) | 120 to 112 | 3.0% to 5.4% | $2.98 to $3.13 | 13 to 13 | $27 to $27 | Flat; Contact form action recorded its first 4 on Oct 19 to 21 |
| All Phase Pool Remodeling | $211 to $223 (+6%) | 35 to 28 | 5.4% to 7.0% | $6.04 to $7.97 | 3 to 5 | $70 to $45 | 63 percent lost to budget both weeks |
| M&S Asphalt Paving | $155 to $186 (+20%) | 14 to 16 | 8.0% to 7.4% | $11.08 to $11.64 | 0 to 2 | n/a to $93 | Manual CPC, bids $13 to $14 since Oct 15 |
| The Counseling Group | $117 to $136 (+16%) | 28 to 32 | 5.5% to 6.5% | $4.16 to $4.26 | 0 to 0 | n/a | Zero both weeks; 63 percent lost to budget this week |
| Aqua Coat | $121 to $90 (-26%) | 22 to 12 | 4.7% to 2.6% | $5.49 to $7.47 | 3 to 2 | $40 to $45 | Dave rewrote the Equipment and Tile keywords to phrase Oct 22 |
| Affordable Critter Solutions | $69 to $68 (-1%) | 18 to 22 | 7.8% to 11.6% | $3.85 to $3.10 | 5 to 1 | $14 to $68 | Small numbers; Calls From Ads zero two weeks (8 in the previous 30 days) |

Bid competition: auction insights are unavailable on this token; rank-lost impression share is the proxy. Highest rank loss this week: Quality Paralegal 84 percent on its main campaign, Patio Style Outdoor Furniture 67 percent, Affordable Critter 65 percent, Progetto Motorized 66 percent, Aqua Coat 54 percent. Largest CPC rises this week: Rover In-Home Pet Euthanasia ($14.85 to $20.51), Filutowski Branded ($4.14 to $7.99), Filutowski overall ($12.26 to $16.43), Progetto ($3.76 to $5.22), All Phase ($6.04 to $7.97). Scootz went the other way ($2.50 to $1.43) as its campaign came out of learning.

## Changes made in the past week (Oct 19 to Oct 26) and their impact

Change history was read from Sep 27 for every account. The table lists the last seven days; earlier changes are noted in the account sections.

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Patio Style | Oct 23 | paidads@rekmarketing.com | Brand campaign moved from Target Impression Share (90 percent, $4 ceiling) to Maximize Conversions; 9 more exact negatives on Brand | Campaign in LEARNING on 3 primary conversions in 30 days. The Sep 4 Target IS setup was working (78 percent share at $2.38). With directions demoted there is almost nothing for Maximize Conversions to learn from |
| Patio Style | Oct 19 | paidads | One keyword swapped in Brand | None visible |
| Progetto Shades | Oct 19 to 23 | tom@rekmarketing.com | About 40 keywords added, geo and negative edits, Shutters budget $22 to $30, bid ceilings raised in steps (Shades $7 to $12, Shutters $10 to $18, Drapery $4 to $12, Motorized $7 to $12), a two-day Target IS test reverted Oct 23 | Spend $50 to $65 a day through Oct 22, $186 to $197 a day Oct 23 to 25. Two conversions Oct 23 and 24. Too early |
| Quality Paralegal | Oct 19 to 23 | tom | 11 negatives to each English campaign, 18 phrase negatives (fee, fees, how long, how much, valid, expiration, lottery, and more) to Immigration, one ad edit | Contact form action recorded 4 conversions Oct 19 to 21 |
| Precision GPR | Oct 21 | tom | GPR Scanning budget $20 to $15 | Campaign spent $90 this week, 0 conversions |
| Precision GPR | Oct 23 | sheokand003@gmail.com | Phrase keywords "concrete x ray" and "gpr concrete scanning" added, "precision gpr" broad added to Branded, 4 ad edits | "gpr concrete scanning" phrase is the competitor name GPRS plus concrete scanning and matched "gprs concrete scanning" for $35.88, 0 conversions |
| Florida Sealcoating | Oct 23 | sheokand003 | Residential budget $40 to $30, Branded $20 to $15, 6 ad-group negatives in Commercial, desktop bid modifiers on 3 Commercial groups, "sealcoating florida" phrase added to Branded, 3 campaign assets, 2 ad edits | Daily budgets now $95, in line with the $3,000 plan. Desktop converts at $82 against mobile $144, so the modifiers point the right way |
| Aqua Coat | Oct 22 | sheokand003 | 17 broad keywords in Pool Equipment and Tile rebuilt as phrase, 2 keywords paused, "what is pebble sheen" exact negative, 2 keywords added; Oct 24 one asset | Equipment group this week $47 for 0 conversions on phrase match |
| All Phase | Oct 22 | sheokand003 | One exact keyword added to Pool Renovations, one ad edit | None visible |
| Rover | Oct 23 | sheokand003 | 6 phrase keywords added to In-Home Pet Euthanasia, including "putting down a cat" and "when is it time to euthanize a cat"; Spanish price negative; Cremation asset swap; one RSA added | The two question phrases are the intent the Sep 14 report proposed as negatives ("when to", "signs"); watch them |
| Scootz | Oct 22 | tom | Campaign setting edit (field not exposed), [scooter rental near me] re-added after Google's auto-apply removed it Oct 8, one keyword edit | Campaign back in learning; CPC fell from $2.50 to $1.43 this week |
| M&S Asphalt | Oct 21 | tom | [paving near me] added | $0 so far |
| The Counseling Group | Oct 20, 21, 26 | tom | 3 ad edits, [help in marriage] added, budget $25 to $26.50 (today) | No conversions since |
| MB Skin Care | Oct 20, 23 | tom | LSA budget $28.57 to $34.29 to $41.14, service criteria | LSA, out of scope |
| Affordable Critter, Filutowski, Color Masters (paused Oct 22), Straightline | | | No bid, keyword, budget or negative changes Oct 19 to 26 except the Color Masters pause | |

Google's Recommendations auto-apply removed Scootz's exact keyword "scooter rental near me" on Oct 8 (user shown as "Recommendations Auto-Apply"). Check the auto-apply settings on that account; nothing else in the fleet shows auto-applied changes in the window.

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md and the Sep 14 change lists)

Landed since Sep 14: Precision GPR GPR Scanning budget cut and broad match gone (items 3 and 4 in spirit); Aqua Coat Equipment keywords narrowed (not paused as proposed); Florida Sealcoating budgets and desktop modifiers; Patio Style Brand negatives (the generic-query problem, but by exact negatives one at a time); Rover Competitors budget (raised, the opposite of the proposal); Progetto moved to Maximize Clicks during learning (as proposed Sep 14). Not landed: Patio Style second RSAs (item 10) and Outdoor Furniture bidding (13); Scootz form test and ad-group split (4, 17); Precision GPR negative list, Location and DSA pause (5); Rover Brand cleanup, "humane pet euthanasia" move, negatives and POOR RSAs (6, 16); Florida Sealcoating Branded exact-only and generic negatives, QS 3 RSA rewrites (7); Aqua Coat master list attachment (8); Counseling Group greenlit set and name negatives (9); All Phase brand split (11); All Phase Jacksonville Orlando campaign pause (6). Filutowski items 1 to 6 remain unapplied and the scope question (REK manages, audits, or is only linked) is still open; Catie at Accalia Marketing made all the account edits in the window.

## Deep dive 1: Patio Style (596-555-8707), score 49 F, down 17

| Category | Score |
|---|---|
| Conversion Tracking | 35 |
| Wasted Spend | 60 |
| Account Structure | 65 |
| Keywords & Targeting | 50 |
| Ads & Assets | 45 |
| Bidding & Settings | 45 |

Snapshot, 30 days: four search campaigns, $1,914, 882 clicks, $2.17 CPC, 12 primary conversions, 614 all-conversions. Previous 30 days: $2,023 and 124 primary conversions.

| Campaign | Budget/day | Bidding | Spend | Clicks | CPC | Primary conv | All conv | This week |
|---|---|---|---|---|---|---|---|---|
| Outdoor Furniture | $30 | Maximize Clicks | $893 | 647 | $1.38 | 8 | 539 | $203, 1 conv |
| Outdoor Kitchens | $14 | Maximize Clicks | $430 | 120 | $3.58 | 0 | 18 | $107, 0 |
| Pergolas & Louvered Roofs | $10 | Manual CPC | $368 | 41 | $8.98 | 1 | 10 | $71, 0 |
| Brand | $10 | Maximize Conversions (since Oct 23) | $223 | 74 | $3.01 | 3 | 47 | $55, 0 |

### Findings

**Directions are no longer counted.** Daily data by action: "Get directions (GTM) 11 Sep" counted 4 primary on Sep 20 and 4 on Sep 21, then 0 primary with 1 to 5 all-conversions every day since. The GA4 get_directions import shows 0 primary and 1 to 4 all-conversions on every day since Sep 20 (42 in the window, 95 in the previous 30 days). Both actions are primary false, included false today. Primary conversions now come from Calls from ads (7), Thank you page (3) and Website Call Conversions (2). The Sep 14 report flagged that two directions actions were both primary and could double count; the fix that landed removed both instead of keeping one. If Tom or the client chose this, update Known account context; if not, restore the GTM action (one tap, one conversion, no import lag).

**Brand bidding changed on Oct 23 on top of the tracking change.** The Target Impression Share setup from Sep 4 (90 percent, $4 ceiling) had the brand campaign at 78 percent share. On Oct 23 it was moved to Maximize Conversions with 3 primary conversions in 30 days to learn from. Expect erratic CPCs; the campaign reads LEARNING today.

**Brand still matches generic patio queries.** "patio styles" phrase matched "patio roof" ($7.76), "patio cover ideas", "elegant patio ideas", "paver patio ideas", "enclosed patio ideas" and "recommend pergola design ideas for a small backyard" ($3.90). Dave has added about 130 exact negatives to Brand since Oct 14, one query at a time. Phrase negatives "ideas", "roof", "cover", "paver", "design", "decor" would close the class.

**Keywords and ads.** Ten keywords at QS 1 to 3 carry $182: "outdoor kitchen design" QS 2 ($59, 18 clicks, 0), "patio cover orlando" QS 3 ($41), "outdoor grill island" QS 3 ($37), "outdoor fire pit" QS 3 ($25), "outdoor dining set" QS 2. Landing page is Below average on all of them. Twelve of 14 ad groups have one RSA (Sep 14: 11 of 12); the new "New Pergolas 07 Oct" group has a POOR RSA and $9 to $12 CPCs. Pergola keywords spent $368 for one conversion.

**Terms to add as negatives**: "four seasons aluminum patio cover" ($16.88) and "insulated pan roof" ($8.38), pending the client's panel answer from September; "patio screen enclosures orlando" ($8.38), "pergola carport attached to house" ($12.42), "show me a pergola" ($12.09), "pergolas for sale" ($11.47, retail intent), "mont alpi" and "outdoor kitchen pods usa" ($9), "patio furniture villages" ($8.40, outside the service area). Dedupe: none of these exist in the 57-member Master Negatives or the 125 Brand negatives. Azenco and Mirador stay (brands the store carries).

### Prepared change list

1. Decide the directions question today. If directions should count, set "Get directions (GTM) 11 Sep" to primary and included and leave the GA4 import secondary.
2. Put Brand back on Target Impression Share (90 percent, $4 ceiling) until the account has 15 or more counted conversions a month, then revisit Maximize Conversions.
3. Brand negatives, phrase: ideas, roof, cover, paver, design, decor, screen enclosure.
4. Negatives, phrase, master list: carport, for sale, pods, mont alpi, villages, screen enclosures. Exact: the four seasons and insulated pan roof terms once the client answers on panels.
5. Second RSAs for Outdoor Furniture, Outdoor Kitchens and Pergolas groups (the three biggest spenders first). Rebuild the POOR RSA in New Pergolas 07 Oct.
6. Outdoor Furniture bidding (worklist item 13) only after item 1 is resolved, since the switch depends on what counts.

## Deep dive 2: Filutowski Eye Institute (192-870-7876), score 38 F, down 4

Scope note: still no REK user in the change history; Catie at Accalia Marketing made every edit. Tom prepared the website URL sheet on Oct 19, so REK is at least involved in the site. The change list below is for Tom to pass on or apply once scope is settled.

| Category | Score |
|---|---|
| Conversion Tracking | 40 |
| Wasted Spend | 25 |
| Account Structure | 50 |
| Keywords & Targeting | 35 |
| Ads & Assets | 40 |
| Bidding & Settings | 45 |

Snapshot, 30 days: five enabled search campaigns, $17,525, 1,478 clicks, $11.86 CPC, 214 primary conversions at $82. Previous 30 days: $20,399, 319 conversions at $64. Performance Max is now paused. Mobile is $17,038 of the spend.

| Campaign | Budget/day | Bidding | Spend | Clicks | CPC | Conv | CPA | Search IS | Lost to budget |
|---|---|---|---|---|---|---|---|---|---|
| S / Brand Awareness / LASIK | $455 | Target CPA | $11,874 | 569 | $20.87 | 71.5 | $166 | 17% | 69% |
| S / Branded / Dr. F | $50 | Max Conv, tCPA $50 | $1,524 | 402 | $3.79 | 90.0 | $17 | 45% | 48% |
| S / Lead Gen / LASIK | $50 | Target CPA | $1,466 | 90 | $16.29 | 7.0 | $209 | 54% | 19% |
| S / Lead Gen / Cataracts | $50 | Max Conv, tCPA $150 | $1,340 | 166 | $8.07 | 11.0 | $122 | 50% | 22% |
| S / Lead Gen / Eye Surgery | $50 | Max Conv, tCPA $50 | $1,321 | 251 | $5.26 | 34.5 | $38 | 21% | 57% |

### Findings

**What changed since Sep 14.** On Oct 15 Catie added a Monday to Friday ad schedule to the four non-brand campaigns (weekend spend is now about $57 a day against $650 on weekdays), raised the Cataracts target CPA from $75 to $150, Eye Surgery from $30 to $50, Branded from $15 to $50, and paused Performance Max. The Brand Awareness budget went from $430 to $455. Weekly spend fell 25 percent but conversions fell 43 percent, and the Branded CPC doubled this week ($4.14 to $7.99) after its target CPA tripled.

**The catch-all keyword is unchanged.** "lasik treatment cost" broad: $11,859, 559 clicks at $21.22, 71.5 conversions at $166, 69 percent of impressions lost to budget. Of $12,526 in visible search-term cost, the terms naming other practices, retail optical chains, insurers, doctors and street addresses add to about $3,400 and produced 9 conversions: Florida Eye Clinic in five spellings $693, Tomoka Eye $291, My Eye Doctor $252, cornea specialist $215, "eye doctors that take florida blue" $205, two street addresses $316, Eye Physicians of Central Florida $200, Mid Florida Eye $150, Total Vision $158, America's Best $158, Garay $96, AdventHealth $94, the LASIK Vision Institute $96, Samantha Xavier MD $95, "eyephy" $92, Spanish "clinica de la vista cerca de mi" $91, Dr George $82, Target Optical $65, Dr Pal $63. Generic "eye doctor near me" and "optometrist near me" variants add about $800 with a handful of conversions. Only $180 of visible spend on this keyword contains lasik, laser, smile or prk.

**Brand and Eye Surgery remain starved.** Branded converts at $17 and loses 48 percent to budget; Eye Surgery at $38 loses 57 percent. The Sep 14 budget shift (cut Brand Awareness, fund Branded and Eye Surgery) has not happened.

**Lead Gen LASIK is expensive for what it returns.** "lasik eye surgery" exact: $650, 39 clicks, 1 conversion. "lasik eye center near me": $170 for 4 clicks at $42.55 and 0 conversions. Eleven keywords over $10 with zero conversions total $661, eight of them cataract terms.

**Conversion tracking is as it was.** The 18 hidden Universal Analytics goals are still primary and included (none has fired in 60 days). "YouTube follow-on views" is still primary and included. The two call actions (800 line, 407 CallRail LASIK) and "Phone Link Click (From Mobile)" are all primary, so a single call can count up to twice. Enhanced conversions for leads is ON on a medical practice. Sixty conversion actions exist in total.

**Website relaunch.** Per Tom's sheet: old thank-you URLs 301 to /thank-you/ which fires no event; new pages push a dataLayer event form_submit_success with form_type (consultation, contact, job); only the consultation form should count as a lead; the contact form should not (negative feedback routes there). The Cataracts ad final URL /cataract-surgery/ will redirect to /services/cataract/ (gclid carries over, but update the URL); the /blog/ sitelink will be broken at launch; the laser-cataract-surgery.html sitelink already 404s. Form actions recorded through Oct 24, so as of the pull nothing had broken. Launch status: unavailable from this session.

**Keywords and ads.** Ten keywords at QS 1 to 3 carry $1,092, led by "eye specialist near me" phrase ($392, 7 conversions), "ophthalmologist near me" exact ($261, 6), "eye doctor near me" exact QS 1 ($121, 3). Expected CTR and ad relevance are Below average on all of them, which points at the single generic RSA in Eye Surgery. Every enabled ad group still has one RSA; the Branded RSA is POOR. The HEALTH_IN_PERSONALIZED_ADS entries are limitations, not disapprovals; the HAS_ADS_DISAPPROVED flags on Cataracts and Eye Surgery are not explained by the visible policy entries (detail unavailable).

### Prepared change list (once scope is settled)

1. Before launch, or today if it has launched: rebuild the three website form actions on the new thank-you URLs or on the form_submit_success event with form_type = consultation. Do not count form_type = contact. Update the Cataracts final URL and the two sitelinks. Verify with a test submission.
2. Sep 14 items 1 to 3 stand: replace "lasik treatment cost" broad with a phrase and exact LASIK set, cut Brand Awareness to $200 a day, move the money to Branded ($100) and Eye Surgery ($80).
3. Shared negative list, phrase, on all live campaigns (Sep 14 item 2 list plus): florida eye clinic, tomoka, mid florida eye, my eye doctor, eye physicians, total vision, america's best, americas best, garay, adventhealth, lasik vision institute, target optical, eyephy, dr george, dr pal, xavier, cornea, florida blue, cerca de mi, clinica, and the two street addresses as exact. Dedupe: none of these are on the live campaigns today; "Search Terms" (34) and "Brand Awareness" (15) lists do not contain them.
4. Set the 18 UA goals and YouTube follow-on views to secondary; one primary call action per line; turn Enhanced conversions off unless a BAA exists.
5. Put the Branded target CPA back to $15 to $20; at $50 the campaign is paying brand clicks at $7.99.
6. Second RSAs everywhere; rebuild the POOR Branded RSA.

## Deep dive 3: Progetto Shades (416-010-8247), score 53 F, first full score since the relaunch

Context: Tom rebuilt the account Sep 8 to 10 and has been in it daily since Oct 19. Everything below is for Tom's own worklist, not a finding against the team.

| Category | Score |
|---|---|
| Conversion Tracking | 60 |
| Wasted Spend | 45 |
| Account Structure | 70 |
| Keywords & Targeting | 30 |
| Ads & Assets | 55 |
| Bidding & Settings | 60 |

Snapshot, 30 days: six search campaigns, $2,112, 474 clicks, $4.46 CPC, 5 primary conversions (Contact 4, Calls from ads 1) at $422, 32 all-conversions. Daily budgets total $110. Spend was $50 to $65 a day until Oct 22 and $186 to $197 a day Oct 23 to 25 after the bid ceilings were raised.

| Campaign | Budget/day | Ceiling | Spend | Clicks | CPC | Conv | Rank-lost IS |
|---|---|---|---|---|---|---|---|
| Shades & Blinds | $40 | $12 | $848 | 215 | $3.95 | 2 | 61% |
| Shutters | $30 | $18 | $502 | 77 | $6.52 | 0 | 51% |
| Motorized & Smart | $16 | $12 | $319 | 60 | $5.32 | 0 | 56% |
| Exterior & Patio | $7 | n/a | $221 | 69 | $3.20 | 1 | 58% |
| Drapery & Curtains | $12 | $12 | $208 | 45 | $4.61 | 1 | 77% |
| Brand | $5 | n/a | $14 | 8 | $1.78 | 1 | 14% |

### Findings

**Quality Score is the account's problem.** 38 keywords sit at QS 1 to 3 and carry $873 of $2,112. Eleven are QS 1 ("shutters for windows" $46, "blackout curtains" $37, "solar shades", "vertical blinds"). Expected CTR is Below average on nearly all and landing page experience is Below average on most, which says the keywords land on pages that do not match the query (one page for all shutter terms, one for all shade terms). Raising ceilings to $12 to $18 on QS 1 to 3 keywords buys position at a Quality Score penalty; the rank-lost share of 51 to 77 percent is a QS story more than a bid story.

**Zero-conversion keywords**: 37 over $10, $1,669. "smart home shades" phrase $191 (37 clicks), "window covering company" $178 (46 clicks, 14 all-conversions), "window shutters" exact $138, "outdoor patio shades" QS 2 $113 (35 clicks), "shutter store" $93, "hunter douglas blinds" $92, "plantation shutters" exact $80, "interior shutters" exact $73. Shutters as a campaign is $502 for 0 conversions.

**Terms.** Mostly on topic. Add as phrase negatives: "recommend" (two AI-assistant style queries, $15), "curtains for arched windows" and "curtains that attach to blinds" ($18, product questions), "motorized tension blinds" ($14), "outdoor metal window shutters" ($7.83, hurricane shutters), "shutter panel configuration" ($8.48), "where to buy" ($9.83), "blackout blind screen usa" ($6.40), "shutter guys" ($6.95, competitor). Dedupe: none are in the 329-member iLP Global Negatives.

**Ads.** Three of nine ad groups have one RSA (Brand, Exterior, Designer Brands); 11 of 14 RSAs are AVERAGE.

**Tracking.** "Lead form website" (GA4) is secondary with 2 all-conversions; "Web form (start)" fired once Oct 24. Fine for now; make sure the GA4 lead form does not duplicate "Contact" before promoting it.

### Prepared change list

1. Split landing pages by theme (shutters, shades, motorized, drapery, exterior) before spending $190 a day; the QS 1 keywords will not recover on bids alone.
2. Pause the QS 1 keywords with zero conversions until the landing pages exist: shutters for windows, blackout curtains, solar shades, vertical blinds, and the other seven.
3. Shutters campaign: cap at $8 ceiling and $20 a day until it records a conversion; $502 for 0 at $6.52 a click is the worst line in the account.
4. Negatives above.
5. Second RSAs for Brand, Exterior and Designer Brands; rewrite the AVERAGE RSAs in Shutters and Shades with the keyword in headline 1.

## Deep dive 4: The Counseling Group (657-069-3617), score 59 F, down 7

Context applied: one Manual CPC campaign, $25 a day Monday to Friday ($26.50 since this morning), Couples group live since Aug 12, free 15-minute consultation confirmed, tel-tap action created Aug 12, Enhanced conversions must stay off (confirmed: the enhanced_conversions_for_leads flag is not set). Small numbers are normal.

| Category | Score |
|---|---|
| Conversion Tracking | 55 |
| Wasted Spend | 50 |
| Account Structure | 70 |
| Keywords & Targeting | 55 |
| Ads & Assets | 70 |
| Bidding & Settings | 60 |

Snapshot, 30 days: $554, 130 clicks, $4.26 CPC, 2 primary conversions (Form Lead 1, Calls from ads 1) at $277. Previous 30 days: $602 and 6 conversions at $100. Search impression share 19 percent, 39 percent lost to budget (63 percent this week), 43 percent lost to rank.

### Findings

**Zero primary conversions since Oct 9.** The form recorded 1 (Oct 9) against 5 in the previous 30 days. Not declared dead: 130 clicks at 4.8 percent CTR say the ads are fine; the drop is between click and form. A manual form submission on the site, then the GA4 or tag check, is the first step.

**The tel-tap action is live but does not count.** "Website Phone Click (tel tap)" recorded 1 all-conversion on each of Oct 5, 13, 19 and 20, the first since it was built Aug 12. The action is primary and included, yet all four sit in All conversions with 0 in Conversions. The usual causes are a click-through window shorter than the tap-to-click gap, or cross-device attribution without a gclid. Check the action's settings in the UI; if these four were real taps, the account has had 6 leads, not 2.

**Half the visible spend is informational or someone's name.** Visible terms total $169. Informational: "deep breathing for anxiety" $7.60, "pressure points on hands for anxiety" $3.85, "relaxation techniques" $3.27, "things to help with depression at home" $3.91, "strategies for depression and anxiety" $3.98, "treatments for depression" $3.98, "medications for depression" $3.90 ("medication" is a negative; the plural got through), "metacognitive therapy" $4, "ect therapy" $3.99, "how many sessions for marriage counseling" $3.99, "john gottman" $3.95. Names: "dr gorman winter park" $4.93 (proposed as an exact negative on Sep 14, not added), "samantha bickham" $4.44, "john gallagher orlando" $4, "marianne vernacchia" $3.67, "dr cubano lake mary" $3.98. Competitors: "orlando thrive therapy" $4.95, "la amistad behavioral health" $4.90, "livethelife org" $4. Out of area: "marriage counseling titusville fl" and "kissimmee fl" $7.80. Total about $85. Dedupe against the five shared lists (Master 114, Wrong Services 37, Competitor Brands 20, Competitor Names 55, DIY 17): "medication", "psychiatrist", "antidepressant" exist; none of the names, "medications", "breathing", "pressure points", "relaxation", "techniques", "strategies", "treatments", "sessions", "gottman", "ect", "metacognitive", "titusville", "kissimmee" exist. Flag: "treatments" and "techniques" are safe as standalone phrase negatives for this practice; do not add "therapy" or "depression".

**Keywords.** Nine keywords over $10 with zero conversions, $299: "couples counseling" phrase $59, "therapist near me" exact QS 2 $39, "anxiety therapy" $38, "therapist for anxiety" $32, "marriage counseling" $31, "depression therapy" $28. Four keywords at QS 2 ("therapist near me", "therapist orlando", "counseling services winter park" x2), all with landing page Below average. One POOR RSA in the Depression group; the other groups have 2 to 3 RSAs.

### Prepared change list

1. Manual form test and tel-tap settings check today (see findings).
2. Negatives, phrase, Master list: medications, breathing, pressure points, relaxation, techniques, strategies, treatments, sessions, gottman, ect, metacognitive, titusville, kissimmee. Exact: dr gorman winter park, dr patrick gorman winter park, samantha bickham, john gallagher orlando, marianne vernacchia, dr cubano lake mary, orlando thrive therapy, la amistad, livethelife.
3. Rebuild the POOR Depression RSA.
4. The Sep 8 greenlit set remains open; nothing in it has been applied except ad edits.
5. Leave bids and budget alone until the tracking question is answered.

## Deep dive 5: Aqua Coat Pool Plastering (285-714-0527), score 64 D, unchanged

Measuring the Sep 9 target CPA: the campaign no longer carries a target CPA (the field is absent), so it was removed at some point before Sep 27 (change history does not reach further back). Performance is flat: $430 and 13 conversions at $33 in both 30-day windows. The campaign reads LIMITED, BUDGET_CONSTRAINED at $15 a day with 41 percent lost to budget.

| Category | Score |
|---|---|
| Conversion Tracking | 65 |
| Wasted Spend | 60 |
| Account Structure | 60 |
| Keywords & Targeting | 65 |
| Ads & Assets | 70 |
| Bidding & Settings | 60 |

### Findings

- **The 248-member "Master Negative Lisst" is still attached only to the paused "Aqua Coat | Search" campaign** (open since Sep 4). The live "- M" campaign runs on 89 campaign negatives.
- **Pool Equipment is still live.** "swimming pool equipment" $70.63 (13 clicks, 1 conversion from "pool ladder steps replacement"), "swimming pool equipment installation" $13.69, "pool products" $11.95, "hayward pool products" matched "hayward pool pump tech support" $17.19 and "hayward pool heater" $4.51, "aquastrong pool pump" $12.09, "pool handrail installation" $8.10, "pool fountain near me" $3.41. Dave rebuilt the group's broad keywords as phrase on Oct 22; this week it spent $47 for 0 conversions, so phrase match did not change the intent. Leslie's and Pinch A Penny queries cost $18.48 across four terms.
- **Other leaks**: "pool painter near me" $17.90, "paint my pool" $7.07, "diy pool resurfacing" $1.71, "pool cleaning companies" and "pool cleaning near me" $2.49, "blue science pools" $5.43, "pool repair st petersburg fl" $6.47 (outside the Tampa area?). Confirmed waste about $100.
- **Conversions**: Free Estimate 7, Call 813 5, Phone Calls 60+ 1 (5 in the previous 30 days). "Contact Form Submission" has recorded nothing in 60 days; creation date unknown, manual test rather than a finding.
- **Converting terms**: "pool tile repair near me" keyword $109 for 2 conversions; "pool repair tampa" 1 on $21.82; "pool refinishing companies near me", "swimming pool resurfacing near me", "pool resurface" and the two brand terms 1 each.
- Ads: two RSAs in every group, six of ten AVERAGE. Broad match is 89 percent of spend.

### Prepared change list

1. Attach the master negative list to the live campaign (two clicks, open seven weeks).
2. Pause Pool Equipment, or keep only "pool equipment installation" phrase with negatives pump, heater, tech support, products, ladder, handrail, fountain, hayward, aquastrong, leslie, pinch a penny. Dedupe: "equipment" and "supplies" are in the master list, which is not attached; none of the rest exist on the live campaign.
3. Negatives, phrase, live campaign: painter, paint, diy, cleaning, blue science, st petersburg (if out of area).
4. Rewrite the six AVERAGE RSAs with the group's keyword in headline 1.
5. Bidding: with 13 conversions a month Maximize Conversions is thin but workable; do not reintroduce a target CPA until the negatives are in.

## Follow-ups on the Sep 14 deep dives

**Precision GPR (59 F, up 9).** The cleanup is finally moving: 26 primary conversions at $100 against 18 at $155, broad match is gone (phrase 90 percent), GPR Scanning is capped at $15 a day (Tom, Oct 21), the Location target CPA was removed Oct 10, and "Michael Phone Number (305)" now records (8), as does lp_contact_form (9). Still open from Sep 4: Location ($228, 2 conversions, $22.83 CPC) and DSA ($291, 3.5) are enabled; "ground penetrating radar surveys" phrase $175 for 0, "Ground Penetrating Radar" exact QS 3 $72 for 0; "Underground Utility Survey" phrase QS 2 $344 for 4. "gprs" is still not a negative anywhere: "gprs service" $54 (1 conversion), "gprs orlando" $62.55, "gprs scanning" $26.85, "gprs locating" $16.96, and on Oct 23 "gpr concrete scanning" was added as a phrase keyword, which matched "gprs concrete scanning" for $35.88. GPRS is the national competitor; decide once whether to bid on it (then give it its own ad group and ad) or exclude it. Other new negatives: julie, sunshine locate, call before digging, who to call, s&n, price, pipe locator. Dedupe: "811", "equipment", "rental", "low cost" exist in LP NKWs (227 members); the rest are new. Eight keywords at QS 1 to 3 carry $566. Every group has two RSAs.

**Rover Veterinary Care (57 F, down 4).** The Sep 14 conversion scare resolved itself: 15 conversions in 30 days (Book appointment 7, Click to call 7, Form 1), 4 this week. "Event|Contact|Calls From Website" has recorded nothing since Sep 15 (5 in the previous window); test it. The open items got worse, not better: the Competitors campaign budget went from $5 to $20 a day on Oct 6 and the campaign spent $472 for 1 conversion; "lap of love" exact and its variants ("laps of love", "lap of love near me", "lapoflove") cost $230 for 0 conversions at QS 3, after 6 conversions on $271 in September. "humane pet euthanasia" is still in Competitors ($243, 1 conversion). Both Competitors RSAs are still POOR; Cat Euthanasia and In-Home groups still have one RSA. In-Home Pet Euthanasia CPC went from $6.56 to $11.36 (this week $20.51) after Tom raised its budget to $50 a day on Oct 2; "mobile dog put down service" cost $31 a click. New waste: "heaven at home pet hospice reviews" $54.98 for one click, "when to put your dog down quiz" $25.88, "euthanized dogs" $14.88, pet cemetery queries $23, competitor crematories (pet angel x3, gentle pet crossing x2, monarch, pawsetrack, taps, peggy adams) $80, "pet aquamation" $7.60, "dog ashes to diamond" $5.94. Confirmed waste about $420 including the lap of love spend. Dave's Oct 23 additions "putting down a cat" and "when is it time to euthanize a cat" are the question intent Sep 14 proposed as negatives; watch them for a week. The Sep 14 change list stands; add: cut Competitors back to $5 a day or pause "lap of love" until it converts again; negatives phrase: reviews, quiz, cemetery, cemeteries, aquamation, diamond, hospice (already in Core Exclusions), pet angel, gentle pet crossing, monarch, pawsetrack, taps, peggy adams. Dedupe: hospice, oncologist, doula, banfield, palm city animal exist; the rest are new.

**Scootz (58 F, unchanged).** 28 primary conversions at $53 (Booqable Purchases 16, Calls from ads 12); the previous window had 32 at $48. The GA4 form_submit action that went dark on Aug 16 is no longer in the conversion action list at all, so the account tracks no form. Still one ad group with 30 keywords on Maximize Clicks (worklist 17). Tom's Oct 6 ad schedule (6am to midnight) and Oct 22 campaign edit put the campaign back into learning; CPC was $0.67 in September, $2.50 last week, $1.43 this week, and 59 percent of impressions were lost to budget this week at $50 a day. Google's auto-apply removed [scooter rental near me] on Oct 8; Tom re-added it Oct 22. Check the auto-apply toggles. Eleven keywords over $10 with zero primary conversions total $503, led by "scooter rental disney world" exact ($103, 102 clicks) and "disney scooter rental" ($99, 94 clicks); both carry local actions in all-conversions, so the Sep 14 caution stands: do not pause on this data. Competitor and off-service terms: scooterbug and scooter bug in six spellings $33, "buena vista scooter rentals" $10.90, "gateway scooter rentals" $3.47, "deals on wheels" $1.40, "knee scooter rental" $3.06, "ucf scooter rental" $8.76, "st augustine" $2.94, "rent a wheelchair at disney world" $12.38 for one click. Dedupe: 41 campaign negatives and a 10-member shared list; none of these exist. Next: rebuild a form conversion (GA4 generate_lead or a thank-you page), then the split.

**Florida Sealcoating (63 D, unchanged).** 30-day spend $3,312 against $2,534, on the $3,000 plan now that Dave cut Residential to $30 and Branded to $15 on Oct 23 (daily budgets total $95). 28 conversions at $118 (Commercial 13 at $98, Residential 7 at $166, Branded 3, Remarketing 5 at $30). The Branded campaign is the finding: $727 at $10.25 a click for 3 primary conversions, because "florida sealcoating" phrase ($347, 19 clicks at $18.27) and "florida sealcoating llc" phrase ($158) still match generic sealcoating queries ("sealcoating orlando fl" $29.17, "seal master orlando" $26.95) and bid against the service campaigns; the brand query itself ("florida sealcoating llc", 30 clicks) carries 39 all-conversions, so the client's own customers are the ones clicking. Sep 14 item 2 (Branded to exact and phrase with generic negatives) is still the fix, and "florida seal coating services" phrase ($84, 0) should go. "asphalt patch repair" phrase lives in both Residential ($140, QS 3) and Commercial ($107 at $53 a click) for 0 conversions between them; keep one. Three keywords at QS 1 to 3 ("driveway repair near me" is QS 1). Competitor and supplier terms this window: "m&s asphalt paving" $51 (now excluded; note this is also a REK client, Volusia), "tru mark inc" $26, "american sealcoating" $18, "landmark paving" $8, "finish line sealcoating" $8, "the seal coating guys" $5, "sealcoat florida inc" $4, "striping machine" $15.62, "p&p striping" $9.88, "hot mix asphalt near me" $23, "sealers for driveways" $11.49, "cracked driveway repair cost" $18, "angie's list" $6.74, "preferred material" $4.57. About $240. Dedupe against the 252-member master list and 296 campaign negatives: "baker paving" and the Sep 4 names are present now; "tru mark", "american sealcoating", "landmark", "finish line", "seal coating guys", "sealcoat florida", "machine", "hot mix", "sealers", "angie", "preferred material" are not. Converting terms worth exact keywords: "asphalt companies in orlando fl" (4 conversions on $109 across two spellings), "seal coating driveway", "driveway sealing cost near me". Every group has two RSAs; desktop converts at $82 against mobile at $144 and Dave's desktop modifiers are the right direction.

## No action needed this week (one-liners)

- **Quality Paralegal Services (62 D, new):** Tom's account, 53 conversions at $25 in 30 days, flat week over week. Findings for the next pass: "family law attorney near me" broad at QS 1 is $309 of $1,333 and matches Spanish attorney queries ($39, 0 conversions) and "cheap divorce"; a paralegal practice bidding on attorney terms is a relevance and possibly a compliance question for Tom. Notary queries ($43 across five terms, 2 conversions), "legal consultation free" $11, "clerk of the court seminole county" $6, "visa center near me" $5. The Spanish campaign's RSA is POOR; three groups have one RSA; one ad in the main campaign is disapproved (detail unavailable). Enhanced conversions is on (not healthcare). Local directions is counted primary (9).
- **M&S Asphalt Paving (62 D, back from paused):** Volusia only now, Manual CPC with $13 to $14 bids, 7 conversions at $75. "driveway paving companies" ($236, 3) and "asphalt paving" ($161, 4) carry it; "driveway paving" $78 and "driveway replacement" $33 for 0. Cost and DIY queries are most of the visible spend: "cost to resurface driveway" $19, "driveway cost" $10, "ways to pave a driveway" $10, "ecogrid driveway" $10, "chip seal" $5; supplier and competitor: "buds asphalt milling" $25, "all asphalt services inc" $10. Dedupe against the 76-member master list and 73 campaign negatives: "cost" is not present (add phrase: cost, how much, ways to, ecogrid, chip seal, milling, buds, all asphalt services). Four of six groups have one RSA, three AVERAGE. Ten keywords at QS 3 have no spend yet.
- **All Phase Pool Remodeling (64 D, down 8):** $927 against $659, CPC $5.36 to $7.19, 16 conversions in both windows, CPA $41 to $58. The campaign is now budget-capped (54 percent lost to budget, was 3 percent) at $30 a day because the brand term costs $8.74 a click inside the non-brand groups: "all phase pool remodeling" broad in Pool Renovations and Pool Resurfacing is $415 of $927 and 14 of 16 conversions. The non-brand keyword "swimming pool renovations" broad spent $281 for 0 primary conversions (16 local actions in all-conversions). The Sep 4 brand split is the fix and would also let the $30 budget buy non-brand clicks. "Phone Calls 60s+" has still never fired (60 days). Terms: "red rhino jacksonville" $28.52 (now excluded), "pebble tec installers near me" $19.89, "aqua pool us llc" $10.54, "thompson pools and spas" $7.21, "pool deck resurfacing of central florida" $7.29, "tempool" $5.36, "pool service deland" $5.29, "pinch a penny sanford" $4.90, "american pools & spas" $3.90. The 379-member master list is still attached only to the paused campaign. Two RSAs per group.
- **Affordable Critter Solutions (78 C, up 2):** 14 conversions at $21 in 30 days, phrase match 63 percent, two EXCELLENT RSAs per group, both shared lists attached. One conversion this week against five last week on the same $68; Calls From Ads has been zero for two weeks after 8 in the previous 30 days, worth a glance at the call asset. Two broad keywords over $10 with zero conversions: "wildlife animal control" $29.53 and "critter control near me" $23.92 (the latter matches the competitor Critter Control: "critter control orlando reviews" $4.19, "critter control in my area" $6.23). "animal control ocoee/longwood/orange county number" $20 across five terms are municipal-service queries; add phrase: ocoee, longwood, phone number, orange county, reviews. Dedupe: none in the 242 campaign negatives or the two lists (59 and 84 members). Dave paused 10 keywords Oct 10. Eleven paused campaigns still there. $10 a day with 22 percent lost to budget; the $15 a day ask from Sep 14 stands.
- **Color Masters (paused):** Tom's painting account. Residential Painting spent $1,240 at $10 a click for 3 conversions ($413), almost all on cost, DIY and brand-paint queries ("cost of painting house exterior", "labor cost to paint a 12x12 room", "front door color idea", "glidden premium interior"); Tom paused Commercial Oct 12 and the rest Oct 22. Nothing to do until it restarts; if it does, "cost", "how much", "ideas", "diy" and paint brands as phrase negatives first (the 92-member list has none of them).
- **All Phase Jacksonville:** search side spent nothing; the "Orlando" campaign is still ENABLED and NOT_ELIGIBLE. Pause it when convenient (worklist item 6). The LSA campaign is paused; the new "All Phase Pool Remodeling (Orlando LSA)" account spent $173 this week for 3 leads (out of scope).
- **Straightline Fence:** the search campaign is gone; LSA only from here ($3,351, 24 phone leads, $140 a lead in 30 days; this week $237 for 2). Out of scope going forward.
- **Jupiter Boat Supply, REK Marketing:** nothing to do. REK Marketing's "GBP Verification" campaign spent $55 this week (Tom's).

Out of scope, for the record only: Citrus Landscape Solutions Sanford LSA $8,565 and 89 leads in 30 days ($2,080 and 22 this week); St. Pete LSA $4,379 and 37 leads but this week fell to $511 and 4 from $1,582 and 12; Sarasota LSA $1,382 and 12 ($133 and 2 this week, $671 and 5 last week); Roeling Green Lawns LSA $293 and 9; Spectrum Electric LSA $43 and no enabled campaign; ABC Pressure Wash and Statewide Home Remodeling LSA $0; Byers Fence LSA $1,489 and 13; Herrell Plumbing LSA $2,187 and 33 plus the client's two Smart campaigns at $2,400 (excluded); Byers Fence search $1,411 for 1 conversion (excluded); MB Skin Care LSA $0 after Tom's Oct 5 setup.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Patio Style (deep dive 1 items 3 and 4), Filutowski (deep dive 2 item 3), Progetto (deep dive 3 item 4), Counseling Group (deep dive 4 item 2), Aqua Coat (deep dive 5 items 2 and 3), Precision GPR (gprs or a decision on it, julie, sunshine locate, call before digging, who to call, s&n, price, pipe locator), Rover (reviews, quiz, cemetery, cemeteries, aquamation, diamond, pet angel, gentle pet crossing, monarch, pawsetrack, taps, peggy adams), Scootz (scooterbug, scooter bug, buena vista, gateway, deals on wheels, knee, ucf, st augustine, wheelchair at disney), Florida Sealcoating (tru mark, american sealcoating, landmark, finish line, seal coating guys, sealcoat florida, machine, hot mix, sealers, angie, preferred material, plus generic sealcoating and paving negatives on Branded), M&S (cost, how much, ways to, ecogrid, chip seal, milling, buds, all asphalt services), All Phase (pebble tec installers, aqua pool, thompson, tempool, deland, pinch a penny phrase, american pools, pool deck resurfacing of central florida), Affordable Critter (ocoee, longwood, phone number, orange county, reviews), Quality Paralegal (clerk of the court, visa center, consultation free; Tom's call on notary and attorney).

New keywords to add: Florida Sealcoating exact "asphalt companies in orlando fl" (4 conversions on $109), "seal coating driveway" and "driveway sealing cost near me" (3 on $113); Rover exact "at home pet euthanasia services near me" and "home euthanization for pets near me" (2 on $35); Aqua Coat exact "pool refinishing companies near me" and "pool repair tampa" (1 each); Precision GPR exact "underground utility near me" (1 on $35); Quality Paralegal exact "legal document preparation services" (1 on $15, and 71 all-conversions on a second match) and "divorce paralegal"; Scootz exact "scootz mobility scooter rentals orlando" in a brand group; Affordable Critter exact "critter catchers near me" (2 on $1.64), "wildlife trappers in my area".

Bid and budget adjustments: Patio Style Brand back to Target IS; Filutowski Brand Awareness $455 to $200, Branded $50 to $100, Branded target CPA $50 back to $15 to $20; Progetto Shutters ceiling $18 to $8 and $30 to $20 a day until it converts; Rover Competitors $20 back to $5 or pause "lap of love"; Precision GPR pause Location and DSA; Florida Sealcoating keep one "asphalt patch repair"; All Phase brand split so the $30 buys non-brand; Affordable Critter $10 to $15 a day (client decision).

Competitive read (rank-lost share as the proxy): Quality Paralegal loses 84 percent to rank on its main campaign at $3.36 a click, a QS 1 and budget story. Progetto loses 51 to 77 percent with QS 1 to 3 across the board; raising ceilings is buying the wrong fix. Rover holds 91 to 97 percent impression share on In-Home Euthanasia and is paying $20 a click for it this week; it is not being outbid, it is overbidding. Patio Style Outdoor Furniture loses 67 percent at a $1.38 CPC by design. Aqua Coat, All Phase and Affordable Critter lose 54 to 66 percent on tight budgets.

## Prioritized weekly action plan

1. **Critical, Tom today: Patio Style directions.** Decide whether Get Directions counts. If yes, set the GTM action to primary and included and put Brand back on Target Impression Share. Deep dive 1 items 1 and 2.
2. **Critical, Tom: Filutowski website launch and scope.** Confirm the launch date with Accalia and rebuild the three form actions on the new thank-you pages or the form_submit_success event (consultation only); update the Cataracts final URL and the two sitelinks. Then decide scope; the Sep 14 budget and keyword changes would recover an estimated $3,400 a month at the floor.
3. **High, REK: The Counseling Group.** Manual form test and tel-tap counting check; the name and informational negatives in deep dive 4.
4. **High, Tom: Progetto Shades.** Landing pages by theme before the $190 a day continues; pause the eleven QS 1 keywords; cap Shutters. Deep dive 3.
5. **High, REK: Rover.** Competitors back to $5 or pause "lap of love"; rebuild the two POOR RSAs (open seven weeks); test the website-call action; the negatives above.
6. **Medium, REK: Precision GPR.** Decide on GPRS (bid on it properly or exclude it); pause Location and DSA; the remaining negatives. The account is improving, keep going.
7. **Medium, REK: Scootz.** Rebuild a form conversion action, check Recommendations auto-apply, then the ad-group split.
8. **Medium, REK: Aqua Coat.** Attach the master negative list (two clicks); pause or narrow Pool Equipment; deep dive 5.
9. **Medium, REK: Florida Sealcoating.** Branded to exact and phrase with generic negatives (third report in a row); drop one "asphalt patch repair"; add the three converting exact keywords.
10. **Low: All Phase** brand split and master list attachment; **Affordable Critter** municipal and competitor negatives, call asset glance; **M&S Asphalt** cost negatives and second RSAs; **Quality Paralegal** POOR RSA and the attorney-term question; **All Phase Jacksonville** pause the Orlando campaign.

## Rotation

Deep-dived this run: Patio Style, Filutowski Eye Institute, Progetto Shades, The Counseling Group, Aqua Coat. Due next Monday: Rover Veterinary Care (Competitors budget and "lap of love"), Florida Sealcoating (Branded, three reports open), Quality Paralegal Services and M&S Asphalt Paving (first full dives as scored accounts). The week after: Affordable Critter Solutions (carried since Sep 4), All Phase Pool Remodeling, Scootz, Precision GPR.

## Data notes

- Account discovery returned 31 client accounts; the Sep 14 list had 26. The five additions are listed in attention item 4. Compare next week against this run's list.
- Deltas are against Sep 14; there was no run with Google Ads data between Sep 14 and today, so six weeks of change sit inside each delta.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Sep 27 (the API allows 30 days). Conversion action edits are not included in change history, which is why the Patio Style demotion and the Scootz form action removal cannot be attributed.
- The Filutowski website checks (whether the new site is live, whether the Cataracts URL redirects) returned a proxy 403 from this session and are unavailable. The launch date is not in the sheet.
- Florida Sealcoating week-over-week includes the display remarketing campaign (44 clicks at about $0.75 both weeks); search-only CPC was $16.85 last week and $20.51 this week.
- The light pull on excluded and LSA-only accounts covered campaign-level metrics only.
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed. No value from it appears anywhere in the session output.
