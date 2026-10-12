# PPC Weekly Audit - 2026-10-12 (Google Ads fleet)

Run: Monday Oct 12, 2026, scheduled cloud session through tools/gaql.py (API v24) against MCC 656-695-7229. Windows: 30 days Sep 12 to Oct 11; this week Oct 5 to Oct 11; last week Sep 28 to Oct 4. Score deltas are against the Sep 14 report, the last run with Google Ads data. Auction insight metrics skipped (Basic access token). Nothing in any account was changed.

Protocol followed: docs/weekly-google-ads-audit-protocol.md. Every search account was sweep-scored. Deep dives: Quality Paralegal Services (new, worst score), Color Masters (new), Progetto Shades (first full scoring after the relaunch), Filutowski Eye Institute (worst spend-weighted score, short update) and All Phase Pool Remodeling (biggest regression, on rotation). One-liners for the rest.

The google-ads.yaml in the Drive folder dave-ads-setup authenticated on the first try. It was copied with mode 600, read only by the client library, and deleted before this report was written. No value from it appears in the session output. The installed client no longer ships API v22; tools/gaql.py was run with GOOGLE_ADS_API_VERSION=v24 and needs that default going forward.

## Attention items (read first)

1. **No account vanished.** All 26 accounts from the Sep 14 list are still under the MCC. Five accounts are new since Sep 14: Color Masters (426-092-9847, REK-built search campaigns live since Sep 18), Quality Paralegal Services (447-153-2607, Tom editing since Sep 16), an unnamed account 163-445-9282 (Color Masters' Local Services account, edited by colormasters88 and Tom), MB Skin Care (179-731-0831, LSA built by Tom Oct 5) and All Phase Pool Remodeling (Orlando LSA) (355-287-7099). Two manager link requests are still PENDING on the MCC: customers 116-301-0558 and 325-901-5827. Nobody has accepted them.
2. **Critical, Tom: Filutowski Eye Institute scope is still undecided and a third agency is editing it.** catie@accaliamarketing.com raised the Brand Awareness budget to $455 a day and paused the Performance Max campaign on Sep 14. The account spent $19,812 in 30 days, $13,926 of it on one broad keyword, "lasik treatment cost", whose visible search terms show $6,043 on 2,145 zero-conversion queries (other clinics, optical chains, named doctors, street addresses, insurers). Enhanced conversions for leads is ON in a healthcare account. If REK is not engaged, say so and the routine will stop scoring it.
3. **Critical, Tom: Quality Paralegal Services (447-153-2607), new, 48 F provisional.** $1,365 in 30 days. The 70 reported conversions are mostly Local actions - Directions (28) and Clicks to call (9) counted as primary; 30 are real calls from ads. 93 percent of spend is broad match on lawyer terms ("family law attorney near me" QS 1, "divorce lawyers near me" QS 1) for a non-lawyer document service, three ads are disapproved (DESTINATION_NOT_WORKING, ONE_WEBSITE_PER_AD_GROUP, GOVERNMENT_DOCUMENTS_AND_OFFICIAL_SERVICES) and a Smart campaign is still running. Confirm this is a REK engagement and what the client's primary conversion is before next week's score.
4. **High, REK: All Phase Pool Remodeling's 379-member master negative list is detached from the live campaign** (campaign_shared_set status REMOVED on "All Phase Pool Remodeling - M"). Conversions fell from 30 at $26 (Sep 14 window) to 13 at $58, and sheokand003 removed the $25 target CPA on Sep 25. Reattach the list today.
5. **High, REK: Aqua Coat's 248-member master list is still attached only to the paused campaign.** Third report in a row. Same fix, five minutes.
6. **Medium, REK: Scootz has Recommendations Auto-Apply enabled.** It removed the exact keyword "scooter rental near me" on Oct 8 with a $1.75 bid. Turn auto-apply off and re-add the keyword if it was wanted.
7. **Good news.** Precision GPR's cleanup landed (29 conversions at $87, up from 9 at $268). The Counseling Group's tel-tap action fired for the first time on Oct 5, so the tag is live. Patio Style's GA4 directions import is now secondary, so the directions double count is gone. Straightline Fence's compromised "vinyl fence" search campaign was removed on Sep 22, so the account is LSA-only now and leaves the weekly scope.

## Coverage

| Platform | Accounts visible | Scored | Notes |
|---|---|---|---|
| Google Ads | 31 client accounts, 1 manager | 14 | 5 new since Sep 14, 0 vanished. Excluded: Byers Fence x2, 11 LSA-only accounts (the 8 on Tom's Sep 4 list plus Straightline Fence, MB Skin Care, All Phase Orlando LSA, Color Masters LSA 163-445-9282). Not scorable: Jupiter Boat Supply and REK Marketing (paused), All Phase Jacksonville (no search spend). |

Search, Display and Performance Max spend in the 30-day window: $17,244 across the 13 REK-managed scored accounts, plus $19,812 at Filutowski Eye Institute. Local Services campaigns are excluded from every figure in this report. For the record only: Herrell Plumbing spent $1,702 on two Smart campaigns in the window, which are not LSA; it stays out of scope until Tom says otherwise.

## Fleet table (worst first)

REK Health Score (A 90+, B 80 to 89, C 70 to 79, D 60 to 69, F below 60). Delta is against Sep 14. Waste is confirmed irrelevant spend from visible search terms in 30 days, a floor. Status: Critical, Needs attention, On target.

| Rank | Account | ID | 30d spend | Primary conv | CPA | Score | Grade | Delta | Status | Top finding | Waste/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Filutowski Eye Institute | 192-870-7876 | $19,812 | 258 | $77 | 40 | F | -2 | Critical (scope) | "lasik treatment cost" broad spent $13,896; $6,043 visible on 2,145 zero-conversion terms; Accalia Marketing editing; EC for leads ON in a healthcare account | $6,043 |
| 2 | Quality Paralegal Services | 447-153-2607 | $1,365 | 70 (30 real calls) | $19 ($46 on calls) | 48 | F | new | Critical (scope) | Directions and map taps counted as primary; broad lawyer keywords at QS 1; three disapproved ads; Smart campaign live | $65 |
| 3 | Color Masters | 426-092-9847 | $1,010 | 3 | $337 | 52 | F | new | Critical | $10 CPC on Maximize Clicks with an $11 ceiling; ten keywords at QS 1 to 3 (landing page below average); terms are cost, color and DIY research; every ad group has one RSA | $280 |
| 4 | Progetto Shades | 416-010-8247 | $1,791 | 9 | $199 | 55 | F | first score | Critical | 33 keywords at QS 1 to 3; $917 on zero-conversion keywords; nine single-RSA ad groups; rank-lost share 57 to 85 percent at a $7 CPC ceiling | none confirmed |
| 5 | Rover Veterinary Care | 750-667-5721 | $1,415 | 19 | $74 | 60 | D | -1 | Needs attention | This week $527 for 3 conversions ($176); Pet Cremation $669 for 4 at $167 with competitor-crematory terms; Competitors back to $20/day and 0 conversions this week; "lap of love" exact QS 3 | $310 |
| 6 | Florida Sealcoating | 168-852-7101 | $3,095 | 28 | $111 | 62 | D | -1 | Needs attention | Branded campaign pays $11 to $18 a click for its own name ($775, 5 conversions, $155 CPA) on uncapped Maximize Conversions; $705 on zero-conversion keywords; "m&s asphalt paving" (a REK client) matched $51 | $286 |
| 7 | Scootz | 185-574-5478 | $1,505 | 39 | $39 | 64 | D | +6 | Needs attention | Auto-apply removed a keyword Oct 8; GA4 form_submit still silent (secondary, 0 in 30 days); one 34-keyword ad group; Oct 6 ad schedule cut clicks 483 to 209 and raised CPC $0.70 to $1.69 | $16 |
| 8 | All Phase Pool Remodeling | 103-111-7688 | $756 | 13 | $58 | 64 | D | -8 | Needs attention | Master negative list detached from the live campaign; target CPA removed Sep 25; 100 percent broad; brand term is $297 of $756 inside non-brand groups | $46 |
| 9 | Aqua Coat Pool Plastering | 285-714-0527 | $506 | 17 | $30 | 65 | D | +1 | Needs attention | Master list still only on the paused campaign; Pool Equipment group still live ($164, pump and tech-support queries); 94 percent broad | $70 |
| 10 | Patio Style | 596-555-8707 | $2,005 | 37 | $54 | 66 | D | 0 | Needs attention | Pergolas campaign $479 for 0 conversions at $9 CPC, 77 percent budget-lost this week; 12 of 13 ad groups have one RSA; eight keywords at QS 2 to 3 | $110 |
| 11 | Precision GPR | 554-113-4760 | $2,537 | 29 | $87 | 66 | D | +16 | Needs attention | Cleanup landed; Location campaign is dead ($0, 9 impressions), DSA $331 for 2 at $165; five keywords at QS 2 to 3 with below-average landing page | $290 |
| 12 | The Counseling Group | 657-069-3617 | $553 | 3 (+1 tel tap) | $184 | 68 | D | +2 | On target (small numbers) | Tel-tap fired Oct 5, tag confirmed; Sep 21 negatives landed; Couples, Anxiety and Depression groups $250 for 0 conversions in 30 days; budget-lost 51 percent on plan | $90 |
| 13 | M&S Asphalt Paving | 827-724-4095 | $400 | 7 | $57 | 70 | C | reactivated | On target | Paving - Volusia re-enabled Sep 15, budget $27/day since Sep 24; one RSA per ad group; "christian brothers asphalt" $17 | $47 |
| 14 | Affordable Critter Solutions | 227-108-4521 | $306 | 16 | $19 | 78 | C | +2 | On target | Clean; $10/day losing 26 percent to budget and 62 percent to rank at a $19 CPA | $30 |
| none | All Phase Pool Remodeling - Jacksonville | 918-824-8896 | $0 search | 0 | n/a | n/a | no search spend | n/a | Paused (search) | "Orlando" campaign still ENABLED but NOT_ELIGIBLE, spent nothing | n/a |
| none | Straightline Fence And Supply | 550-094-8786 | $0 search | 0 | n/a | n/a | LSA only | was Critical | Out of scope | "vinyl fence" search campaign REMOVED Sep 22 with its COMPROMISED_SITE ads; LSA spent $3,482 for 25 leads | n/a |
| none | Jupiter Boat Supply, REK Marketing | | $0 | 0 | n/a | n/a | paused | n/a | Paused | Fully paused, no changes | n/a |

## Week over week (Oct 5 to 11 against Sep 28 to Oct 4, search, display and PMax only)

| Account | Spend | Clicks | CTR | CPC | Conv | CPA | Read |
|---|---|---|---|---|---|---|---|
| Filutowski Eye Institute | $4,212 to $5,171 (+23%) | 422 to 389 | 5.7% to 6.1% | $9.98 to $13.29 | 57 to 52 | $73 to $100 | Brand Awareness $2,832 to $3,619, CPC $17.16 to $26.61, budget-lost 86% at $455/day |
| Precision GPR | $571 to $606 (+6%) | 45 to 50 | 5.9% to 6.4% | $12.69 to $12.12 | 9 to 7 | $63 to $87 | Holding after the cleanup; DSA $104 for 0 this week |
| Florida Sealcoating | $922 to $702 (-24%) | 106 to 113 | 5.5% to 7.5% | $8.70 to $6.21 | 6 to 9 | $154 to $78 | Branded cut to $20/day Oct 6; Commercial CPC $22 to $12 |
| Rover Veterinary Care | $241 to $527 (+118%) | 62 to 67 | 12.1% to 10.1% | $3.89 to $7.86 | 4 to 3 | $60 to $176 | Off target. In-Home budget $30 to $50 (Tom, Oct 2) and Competitors $5 to $20 (Oct 6); In-Home CPC $3.77 to $13.65 |
| Patio Style | $396 to $489 (+24%) | 184 to 200 | 6.4% to 7.3% | $2.15 to $2.45 | 4 to 4 | $99 to $122 | Outdoor Kitchens budget $12 to $18 Oct 7; Pergolas 0 for 0 both weeks |
| Scootz | $337 to $354 (+5%) | 483 to 209 | 5.9% to 7.3% | $0.70 to $1.69 | 4 to 10 | $84 to $35 | Ad schedule added Oct 6; fewer, dearer clicks and more Booqable purchases (2 to 7) |
| Progetto Shades | $418 to $406 (-3%) | 95 to 100 | 4.0% to 5.1% | $4.40 to $4.06 | 2 to 0 | $209 to none | Off target; zero conversions this week across six campaigns |
| Color Masters | $387 to $230 (-41%) | 40 to 23 | 8.2% to 4.5% | $9.67 to $9.98 | 1 to 2 | $387 to $115 | Residential $382 to $202; the two conversions are calls |
| Quality Paralegal Services | $310 to $288 (-7%) | 108 to 113 | 1.9% to 2.6% | $2.87 to $2.55 | 10 to 15 | $31 to $19 | Calls from ads 7 to 9; the rest is directions and map taps |
| All Phase Pool Remodeling | $256 to $220 (-14%) | 31 to 29 | 5.1% to 4.5% | $8.26 to $7.59 | 5 to 2 | $51 to $110 | Rank-lost 30% to 44% after the target CPA came off |
| Aqua Coat | $90 to $95 (+5%) | 16 to 18 | 3.2% to 2.9% | $5.61 to $5.25 | 4 to 3 | $22 to $32 | Flat, rank-lost 70% |
| The Counseling Group | $118 to $183 (+55%) | 26 to 44 | 2.9% to 5.4% | $4.55 to $4.16 | 0 to 1 | none to $183 | Plus one tel tap Oct 5; Oct 5 to 9 ran five serving days against four the week before |
| Affordable Critter Solutions | $63 to $77 (+22%) | 20 to 25 | 12.7% to 14.9% | $3.17 to $3.09 | 2 to 6 | $32 to $13 | Best week in the window |
| M&S Asphalt Paving | $106 to $62 (-42%) | 9 to 6 | 4.9% to 4.2% | $11.80 to $10.33 | 3 to 2 | $35 to $31 | Only two serving days this week (Oct 5 and Oct 10); check the schedule or budget pacing |

Bid competition: auction insights are unavailable on this token. Rank-lost impression share is the proxy. Highest rank loss this week: Drapery & Curtains (Progetto) 85 percent, Affordable Critter 70 percent, Aqua Coat 70 percent, Patio Style Outdoor Furniture 63 percent, Shades & Blinds (Progetto) 62 percent, Color Masters Commercial 67 percent. Highest CPC jumps: Rover In-Home Pet Euthanasia ($3.77 to $13.65), Filutowski Brand Awareness ($17.16 to $26.61), Florida Sealcoating Residential ($12.95 to $21.36), Scootz ($0.70 to $1.69).

## Changes made in the past four weeks (Sep 13 to Oct 12) and their impact

| Account | When | Who | What | Impact so far |
|---|---|---|---|---|
| Filutowski | Sep 14 | catie@accaliamarketing.com | Brand Awareness budget $430 to $455; Performance Max paused | Brand Awareness is 70 percent of account spend and 70 of its 77.5 conversions are LASIK CallRail calls; CPA there is $180 against $14 on Branded and $28 on Eye Surgery |
| Precision GPR | Sep 22, Oct 10 | sheokand003@gmail.com | 12 phrase keywords added and 5 broad removed in GPR Scanning; 2 RSAs rewritten; "gpr scanning services near me" and "slab survey" added; $14 target CPA removed from Location | 29 conversions at $87 in the window against 9 at $268 on Sep 14. Working. Location still has no traffic |
| Rover | Sep 16, Sep 22, Oct 2, Oct 3, Oct 6, Oct 10 | sheokand003 (Tom on Oct 2) | Manual bids set ($3 to $7.60), Competitors cut to $5 then raised back to $20, Brand cut to $10, In-Home raised $20 to $30 to $50, Pet Cremation $20 to $30, enhanced CPC toggled, 5 keywords paused, "pet cremation services near me" added | 30-day CPA improved to $74, but this week spent $527 for 3 conversions. Competitors $131 for 0 since the budget went back up |
| Florida Sealcoating | Sep 15, Sep 22, Oct 6, Oct 10 | sheokand003 (Tom renamed a group Oct 8) | Commercial budget $38 to $45; Branded target CPA $17 removed; Residential $30 to $40; Branded $30 to $35 then $35 to $20; 31 keywords added and 16 removed Sep 22; 9 keywords paused and 2 added Oct 10 | Window spend $3,095 against the $3,000 plan, on plan. Removing the Branded target CPA preceded $11 to $18 brand CPCs; the Oct 6 cut to $20 halved Branded CPC this week ($14.15 to $6.15) |
| Patio Style | Sep 15 to Oct 9 | paidads@rekmarketing.com | 197 changes: Pergolas ceiling removed and moved to Manual CPC; AI Max toggled on Brand; 20 exact negatives added Sep 16; 12 sitelinks Sep 23; 17 ads Sep 25; "New Pergolas 07 Oct" ad group with 25 keywords; Pergolas budget $16 to $10 and Outdoor Kitchens $12 to $18 Oct 7; three Pergolas ad groups toggled Oct 9 | GA4 directions import demoted to secondary (37 primary conversions in the window instead of 166, the double count is gone). Pergolas has 0 conversions on $479 |
| Aqua Coat | Sep 16, Oct 1, Oct 10 | sheokand003 | Geo target type changed, four radius targets set, 11 keywords paused, brand keywords added, "hayward pool products" added Oct 1, "pool plaster repair company" added Oct 10 | 17 conversions at $30. "hayward pool products" spent $17 on one "hayward pool pump tech support" click |
| The Counseling Group | Sep 21 | tom@rekmarketing.com | 34 phrase negatives (medication set, names, teen/kids, grounding techniques) | Landed. This week's terms are cleaner; the tel-tap fired for the first time Oct 5 |
| Scootz | Oct 6, Oct 8 | tom@rekmarketing.com; Recommendations Auto-Apply | Seven ad-schedule rows added; auto-apply removed exact "scooter rental near me" | Clicks halved, CPC more than doubled, Booqable purchases 2 to 7. Auto-apply is on and editing keywords |
| All Phase | Sep 18, Sep 25 | tom (pause and re-enable), sheokand003 | Campaign paused and re-enabled the same day; $25 target CPA removed; two ads rewritten | Conversions 5 to 2 this week; master list attachment shows REMOVED |
| Progetto | Sep 14, Sep 18, Sep 25, Oct 6 | tom@rekmarketing.com | CPC ceilings $4 on five campaigns, raised to $7 on three Sep 18; 12 keywords added Sep 25 | 9 conversions at $199 in 30 days, 0 this week |
| Color Masters | Sep 14 to Oct 2 | colormasters88@gmail.com, tom | Client built "Painting Leads" Sep 16; Tom removed the ten legacy campaigns Sep 18 and enabled three REK campaigns; Brand ceiling $3 to $6 to $8 and budget $5 to $8; 18 ad-schedule rows removed Oct 2 | $1,010 for 3 conversions. See deep dive 2 |
| Quality Paralegal | Sep 16 to Oct 7 | tom (robbie Oct 6, ines@qualitylegalservices Oct 5) | 139 keywords auto-paused by Google's low-activity bulk change; networks changed; budgets rebalanced four times; 13 keywords added Sep 23; Smart campaign "Experienced Paralegal Services Provider" paused Sep 25; two ad groups paused Oct 7 | See deep dive 1 |
| M&S Asphalt | Sep 15, Sep 21, Sep 24 | Bulk Actions, tom | Three campaigns re-enabled; 9 assets; Paving - Volusia budget $15 to $27; Orlando Metro paused | 7 conversions at $57 on $400 |
| Affordable Critter | Sep 25, Oct 10 | sheokand003 | 2 keywords added; 10 keyword status changes; 1 RSA rewritten | 16 conversions at $19 |
| Straightline Fence | Sep 14, Sep 22, Sep 23, Sep 25 | robbie@rekmarketing.com, joe611904@yahoo.com | Campaign toggled, "vinyl fence" campaign removed Sep 22, 23 assets, 11 campaign criteria | Search side is gone. LSA only |

### Worklist reconciliation (reports/ppc-worklist-2026-09-08.md and the Sep 14 plan)

Landed since Sep 14: Precision GPR negatives and keyword restructure (Sep 14 item 5, partly: Location and DSA are still enabled), Counseling Group medication negatives and name negatives (item 9), Patio Style directions double count (item 10, GA4 import now secondary), Florida Sealcoating competitor negatives (item 7, the 252-member master list now carries them; Branded is still phrase and not capped), Rover "humane pet euthanasia" still live in Competitors (item 6 not done), Aqua Coat master list attachment (item 8 not done), Scootz form_submit test (item 4 not done, still 0), All Phase Jacksonville Orlando campaign pause (item 11 not done). Filutowski scope (item 2) and Premium Walk-In Clinic (item 1) remain open questions for Tom. Straightline (item 3) resolved by removal.

## Deep dive 1: Quality Paralegal Services (447-153-2607), score 48 F, provisional

Scores: Conversion Tracking 10/25, Wasted Spend 10/20, Structure 8/15, Keywords 5/15, Ads 7/15, Bidding 8/10.

Context: new under the MCC since Sep 14. Campaign names ("Looking for an experienced yet affordable Paralegal?", "Experienced yet affordable Paralegal/Paralegal con 25 anos de experiencia") are the client's, not REK's. Tom has made 226 changes since Sep 16, so REK is working it. Enhanced conversions for leads is ON (not healthcare, fine). 27 serving days, $1,365.

Findings:
1. **Primary conversions are mostly map actions.** 30-day primary conversions by action: Calls from ads 30, Local actions - Directions 28, Clicks to call 9, Calls from Smart Campaign Ads 2, Business profile tracked call 1. Directions and Clicks to call are Google-hosted local actions set primary and included. A paralegal office is not a showroom; unless the client says walk-ins are the goal, these inflate the $19 CPA. On calls alone the CPA is $46 ($1,365 over 30). "Contact form (ads page)" is primary but recorded 0 in 30 days; find out when it was created before calling it dead. Ask what the client counts as a lead.
2. **Keywords are lawyer intent on broad match.** 93 percent of keyword spend is broad. Top spenders: "family mediation" broad (paused, $190, 6 conv), "family law attorney near me" broad QS 1 ($171, 4 conv), "paralegal" broad QS 5 ($156, 3), "divorce lawyers near me" broad QS 1 ($58, 1), "family attorney" ($56, 2). Landing page experience is BELOW_AVERAGE on both QS 1 terms. Search terms include "pro bono divorce lawyers near me", "the number to legal aid", "legal aid orlando", "legal aid polk county", "fathers rights legal aid", "clerk of the court seminole county", "visa center near me", "speak to a lawyer online". Legal aid and pro bono queries are $65 of visible zero-conversion spend and will not become paying document clients.
3. **Three disapproved ads and a government-documents policy limit.** Two ads in "Paralegals Services" are DISAPPROVED for DESTINATION_NOT_WORKING and ONE_WEBSITE_PER_AD_GROUP, one in "Affordable and experienced" for UNCLEAR_RELEVANCE and GOVERNMENT_DOCUMENTS_AND_OFFICIAL_SERVICES (fully limited). All three are in paused ad groups, but the policy flag will return on any new ad that mentions government forms.
4. **Smart campaign still live.** "QPS Non-Lawyer Services Orlando" spent $273 for 267 clicks at $1.02 and 38 "conversions" that are mostly local actions (0.9 percent CTR on 29,555 impressions). No search terms are visible for it. Tom paused the other Smart campaign Sep 25; this one should follow once the search campaigns carry the volume.
5. **Ads.** The live "Ad group 1" RSA is POOR; "Paralegals Services #2" and "Help in all types of divorces" each have one RSA. Budget-lost share is 44 to 50 percent on both search campaigns at $23 and $17 a day.

Prepared change list (suggestions only):
- Decide the primary set: Calls from ads, Contact form (ads page), and Clicks to call if the client wants map calls. Set Local actions - Directions, Website visits, Other engagements and Menu views to secondary.
- Negatives (phrase, deduped against the 146-member Tier 1 list and 1,010 campaign negatives, none of these present): legal aid, pro bono, free lawyer, free consultation, clerk of court, clerk of the court, visa center, immigration (check: "abogado de inmigracion" variants exist, the English token does not), speak to a lawyer, lawyer online.
- Move "family law attorney near me", "divorce lawyers near me", "support attorney" ($47, 0), "custody lawyer" ($14, 0) to paused; replace with phrase "paralegal services orlando", "divorce paperwork help", "legal document preparation" (converted twice at $13 and $15), "notary near me" (converted at $2 to $4, if the client offers it), "temporary custody agreement" (converted at $11).
- Fix or remove the three disapproved ads so the policy history is clean, then write a second RSA for each live ad group with "non-lawyer document preparation" wording rather than "legal services".
- Pause the Smart campaign and move its $5 a day to "Looking for an experienced yet affordable Paralegal?", which is at 44 percent budget-lost.

## Deep dive 2: Color Masters (426-092-9847), score 52 F, new

Scores: Conversion Tracking 17/25, Wasted Spend 8/20, Structure 10/15, Keywords 4/15, Ads 7/15, Bidding 6/10.

Context: REK rebuilt the account Sep 18 (ten legacy campaigns removed, three "REK | Search" campaigns enabled). 20 serving days in the window, $1,010, 3 conversions (2 website calls, 1 lead form) at $337. Residential Painting is 96 percent of spend. Enhanced conversions ON, not healthcare, fine. Tracking is sound: calls from ads, website call, lead form, all primary, GA4 generate_lead secondary.

Findings:
1. **$10 clicks on Maximize Clicks with an $11 ceiling.** Residential and Commercial run Target Spend with an $11 CPC ceiling; average CPC is $10.06 and 96 clicks bought 3 conversions. Both campaigns are flagged BIDDING_STRATEGY_LIMITED. The ceiling is the market price, so the strategy is paying whatever it is allowed to.
2. **Quality Score floor.** Ten enabled keywords at QS 1 to 3 with landing page BELOW_AVERAGE on nine of them: "house painters near me" exact QS 1, "painters near me" exact and phrase QS 2, "exterior painters near me" QS 2, "interior painters near me" QS 2, "exterior painting company" QS 2, "painters daytona beach" QS 3 ($77, 0 conv), "exterior house painters" QS 3 ($40, 0), "painters ormond beach" QS 3 ($29, 0). The landing page is the common factor.
3. **Search terms are research, not hiring.** Visible zero-conversion terms: "how much does it cost to repaint your kitchen cabinets" $21, "front door color idea" $21, "glidden premium interior" $20, "house exterior colors" $11, "florida home colors" $11, "colors to paint my kitchen cabinets" $11, "how much does it cost to paint a door" $11, "cost to paint house exterior" $11, "how much to paint exterior of house" $11, "how much does it cost to paint a mobile home exterior" $11, "kitchen cabinet refacing cost" $11, "equipment painters" $11, "faux painter near me" $10, and two competitor names "j&b painting plus" $21 and "jesus gil painting" $10. That is $280 of $397 visible. The 1,484 campaign negatives and 92-member list already carry "how to", "diy" and many competitor names, but not "how much", "cost", "idea", "ideas", "colors", "color idea", "glidden", "refacing", "equipment", "faux".
4. **Zero-conversion keywords.** $915 of keyword spend converted nothing: "residential painters" phrase $228, "exterior house painting" $132 (paused), "painting contractor" $88 (paused), "cabinet painting" $85 (paused), "painters daytona beach" $77, "cabinet refinishing" $54 (paused), "interior house painting" $41 (paused), "exterior house painters" $40, "kitchen cabinet painters" $39. The one lead-form conversion came from "pool cage painting near me" ($10) and the two calls from "painting companies" ($53).
5. **One RSA per ad group** in all six groups (five EXCELLENT, one GOOD). Commercial Painting had 3 impressions in 30 days.

Prepared change list (suggestions only):
- Negatives (phrase, none present in the live lists): how much, cost, costs, idea, ideas, colors, color, glidden, sherwin, behr, refacing, equipment, faux, mobile home, j&b painting, jesus gil.
- Lower the Residential CPC ceiling to $7 for two weeks and watch impression share (51 percent now, 2 percent budget-lost, so the ceiling is the only lever) or move to Manual CPC at $6 to $7 on the exact "near me" terms once the landing page is fixed.
- Landing page: nine QS 1 to 3 keywords share a BELOW_AVERAGE page. Send "painters near me" and city terms to a page that leads with the service area and a quote form above the fold.
- Add a second RSA to each of the six ad groups.
- Pause "residential painters" phrase until the page is fixed; it is $228 for 0.

## Deep dive 3: Progetto Shades (416-010-8247), score 55 F, first full scoring

Scores: Conversion Tracking 18/25, Wasted Spend 10/20, Structure 11/15, Keywords 4/15, Ads 7/15, Bidding 5/10.

Context: relaunched Sep 10 with six themed campaigns, San Diego market. Tom put all six on Maximize Clicks with $4 ceilings Sep 14 and raised three to $7 Sep 18 (the Sep 14 report suggested $4). 29 serving days, $1,791, 9 primary conversions at $199 (8 Contact, 1 call from ads). Enhanced conversions ON, not healthcare, fine. Tracking is sound: Contact and calls primary, lead form and financing secondary.

Findings:
1. **Quality Score.** 33 enabled keywords at QS 1 to 3 (7 at QS 1, 6 at QS 2, 20 at QS 3). Landing page is BELOW_AVERAGE on most: "outdoor patio shades" phrase QS 2 ($147, 0 conv), "window shutters" exact QS 3 ($131, 0), "interior shutters" exact QS 3 ($62, 0), "window shades" exact QS 3 ($51, 0), "automated shades" QS 3 ($48, 0), "roller shades" QS 2 ($42, 0), "hunter douglas" phrase QS 3 ($48, 1). Rank-lost share is 57 to 85 percent in every campaign, which with 4 to 27 percent budget-lost means the account is being outranked, not outspent.
2. **Zero-conversion keyword spend is $917** of $1,791. The converting keywords: "plantation shutters" exact ($76, 1), "window coverings near me" ($58, 1), "window covering company" ($330, 1), "smart home shades" ($222, 1), "hunter douglas" ($48, 1), "blinds installation near me" and "woven shades" terms. "window treatments san diego" spent $54 for 0.
3. **Single RSA in all nine ad groups**; four are AVERAGE strength (Drapery, Shades, Window Treatments, Plantation Shutters).
4. **Drapery & Curtains** spent $70 for 0 at 85 percent rank-lost and a $4 ceiling. **Brand** served 16 impressions in 30 days; the client's brand has no search volume yet.
5. **Shades & Blinds** carries 46 percent of spend ($842) for 4 conversions at $210; its "Shades" ad group ($162) and "Designer Brands" ($130) are the weak halves.

Prepared change list (suggestions only):
- Landing pages first: the 33 low-QS keywords are the account. Shutters, shades and motorized terms should land on product pages with San Diego in the headline and a consultation form, not the home page.
- Pause the QS 1 to 3 keywords with $40 or more and 0 conversions ("outdoor patio shades", "window shutters", "interior shutters", "window shades", "automated shades", "roller shades") until the pages change; keep "plantation shutters", "window coverings near me", "smart home shades", "window covering company".
- Second RSA in every ad group, written to the ad group theme (the AVERAGE ones first).
- Pause Drapery & Curtains and move its $6 to Shutters, which has the best CPA ($157) and 7 percent budget-lost.
- Keep Maximize Clicks with the $7 ceiling until the account has 15 conversions in 30 days; then test Maximize Conversions on Shutters only.

## Deep dive 4: Filutowski Eye Institute (192-870-7876), score 40 F, update

Scores: Conversion Tracking 12/25, Wasted Spend 4/20, Structure 8/15, Keywords 5/15, Ads 6/15, Bidding 5/10.

What changed since Sep 14: Accalia Marketing raised Brand Awareness to $455 a day and paused Performance Max. Nothing from the Sep 14 change list was applied. Spend rose from $17,496 to $19,812 in the window; this week $5,171.

Evidence:
- "lasik treatment cost" broad: $13,896, 709 clicks at $19.60, 77.5 conversions, CPA $180. Its visible search terms ($9,029 of the $13,896) break down as: other clinics and optical chains 570 terms, $4,927, 19 conversions; generic eye doctor queries 560 terms, $1,517, 13.5; named doctors 281 terms, $1,108, 3; street addresses 31 terms, $455, 3; insurance queries 83 terms, $250, 0; LASIK intent 164 terms, $90, 0. Zero-conversion terms in the campaign: 2,145 terms, $6,043. The 70 conversions the campaign records are CallRail LASIK calls; a call from someone searching "florida eye clinic kissimmee" or "155 cranes roost blvd" is a misdial, not a LASIK lead.
- Branded ($1,435, 106 conversions, $14 CPA) and Eye Surgery ($1,421, 50.5, $28) are budget-constrained at $50 a day with 59 and 55 percent budget-lost share.
- Ten keywords at QS 3 in Eye Surgery and Cataracts, all with BELOW_AVERAGE expected CTR and ad relevance.
- All five live ad groups have one RSA.
- Conversion setup: 57 non-removed actions, 22 of them hidden Universal Analytics imports, two YouTube actions set primary, and Enhanced conversions for leads ON. Eye surgery is healthcare; REK's rule is off without a BAA.

Change list (unchanged from Sep 14, suggestions only): move "lasik treatment cost" to phrase and exact with "lasik cost", "lasik price", "how much is lasik" variants; add the competitor and optical chain names, "dr", "md", "od", insurer names and address patterns to the Brand Awareness shared list; Brand Awareness budget to $200 and Branded and Eye Surgery to $100 each; second RSA in every group; turn Enhanced conversions off; set YouTube actions secondary. Tom decides whether any of this is REK's to do.

## Deep dive 5: All Phase Pool Remodeling (103-111-7688), score 64 D, down 8

Scores: Conversion Tracking 18/25, Wasted Spend 12/20, Structure 9/15, Keywords 7/15, Ads 12/15, Bidding 6/10.

Context: one live campaign, "All Phase Pool Remodeling - M", Maximize Conversions, $30 a day. Jacksonville (918-824-8896) holds the LSA by design and is not a duplicate. Enhanced conversions ON; pool remodeling, not healthcare, fine.

Findings:
1. **The master negative list is off the live campaign.** campaign_shared_set shows "All Phase Master Negatives" (379 members) ENABLED on the paused "All Phase - Pool Remodeling | Search" and REMOVED on the live "- M" campaign. The live campaign runs on 91 campaign negatives and 11 ad-group negatives. Change history does not show who removed it (shared-set attachments are not in change_event), so it predates Sep 13 or is invisible.
2. **Target CPA removed Sep 25** (sheokand003, $25 off Maximize Conversions). Since then rank-lost share rose from 30 to 44 percent and conversions this week were 2 at $110. Thirteen conversions in 30 days is thin for Maximize Conversions in any case.
3. **Brand inside non-brand.** "all phase pool remodeling" broad sits in Pool Renovations ($241, 9 conv) and Pool Resurfacing ($56, 2). Brand terms are $297 of $756 and 11 of 13 conversions. The non-brand keywords, "swimming pool renovations" ($222, 0) and "pool resurfacing companies near me" ($121, 0), bought nothing.
4. **100 percent broad match.** Terms this window: "pebble tec installers near me" $20, "pool deck resurfacing of central florida" $11 (a competitor), "thompson pools and spas" $7, "pool service deland" $5, "pool builders in orlando florida" $3.
5. Ads are fine: two RSAs per group, GOOD to EXCELLENT. "Phone Calls 60s+" recorded 0 in 30 days again while "Calls From Ads" recorded 6; the 60-second threshold may be the only difference, test one call.

Prepared change list (suggestions only):
- Reattach "All Phase Master Negatives" to "All Phase Pool Remodeling - M".
- Split brand out: new "Brand" campaign with exact and phrase "all phase pool remodeling", "all phase pools", "all phase pool", $8 a day; leave the non-brand campaign to earn its own conversions.
- Non-brand: "swimming pool renovations" and "pool resurfacing companies near me" to phrase; add negatives pebble tec installers, thompson, pool deck resurfacing of central florida, pool service, pool builders, deland (if not served).
- Put the $25 target CPA back, or move to Maximize Clicks with a $6 ceiling until the non-brand side has 15 conversions a month on its own.

## No action needed this week beyond the listed items (one-liners)

- **Rover Veterinary Care (60 D):** 30-day CPA improved to $74 on sheokand003's manual bids, but this week is off target: $527 for 3 conversions. Three things moved at once: Tom raised In-Home Pet Euthanasia to $50 a day Oct 2, enhanced CPC was toggled Oct 3, and Competitors went back from $5 to $20 Oct 6. In-Home CPC went $3.77 to $13.65 with the same 10 or 11 clicks; Competitors spent $131 for 0. Pet Cremation Services ($669, 4 conversions, $167) is leaking to crematories: pet angel $61, lap of love and variants $160 across campaigns, peggy adams $13, haisley, paws and cherish, taps, safe passages, gentle pet crossing, pet cemetery $39, cat urns $8. Add those as phrase negatives (none present except lap of love in the Competitors keyword list, where it is a QS 3 exact keyword with $87 and 0 conversions; pause it). Two single-RSA groups (Cat Euthanasia, In-Home Pet Euthanasia) and the POOR Competitors RSA are unchanged from Sep 14. "Event|Contact|Calls From Website" last fired Sep 15 and "Form Submit" Sep 17; both are primary and included, test them.
- **Florida Sealcoating (62 D):** $3,095 in the window is the $3,000 plan, not an overspend. The Branded campaign is the finding: $775 for 5 conversions at $155, CPC $11.07, "florida sealcoating" phrase at $18.47 a click, after the $17 target CPA came off Sep 15. Put Branded on Manual CPC at $3 or Target Impression Share with a $4 ceiling; the Oct 6 budget cut to $20 already halved its CPC. "m&s asphalt paving" matched through broad "asphalt paving services" for $51 (now EXCLUDED); M&S is a REK client, add it as exact negative in every campaign. Other visible competitor and supplier leaks: father and son paving $46, concrete contractor $29, asphalt tack $25, hot mix asphalt $23, american sealcoating $18, striping machine $16, hot shot sealcoating $16, watson paving $15, dmi paving $14 (already in the list; check match type), landmark paving $8, finish line $8. Five QS 1 to 3 keywords remain; sheokand003 paused "driveway repair near me" broad QS 1 on Sep 22. Two Asphalt Patching groups spent $171 for 0.
- **Scootz (64 D):** 39 conversions at $39 (29 Booqable purchases, 10 calls), the best window since July. Three items: Recommendations Auto-Apply removed exact "scooter rental near me" Oct 8, turn it off; GA4 form_submit is still secondary and silent (0 in 30 days), the manual test from Sep 14 is still the ask; the Oct 6 ad schedule cut clicks 483 to 209 and raised CPC to $1.69 while budget-lost share went 17 to 63 percent, so the campaign is now capped by hours rather than budget. Watch one more week before judging. Scooterbug competitor terms $16; "scooterbug orlando photos" is already excluded, add phrase "scooterbug".
- **Aqua Coat (65 D):** 17 conversions at $30 on $506. The 248-member "Master Negative Lisst" is still attached only to the paused campaign (third report). Pool Equipment ($164, 2 conv) matched "pentair pool pump" $19, "hayward pool pump tech support" $17 (through the new "hayward pool products" keyword), "pinch a penny" $20 across three terms, "leslie's" $5. "pinch a penny" is in the master list, which is why attaching it matters. Rank-lost 70 percent this week at $15 a day.
- **Patio Style (66 D):** the directions double count is fixed (GA4 get_directions now secondary; GTM directions 18 is the primary signal, calls 11, forms 2). Pergolas & Louvered Roofs is the problem: $479 for 0 conversions, Manual CPC averaging $9, 77 percent budget-lost this week at $10 a day, and "patio cover orlando" QS 3 ($123, 0), "insulated patio cover" ($121, 0), "orlando pergola" ($94, 0). Panel and roof queries still leak ($48). 12 of 13 ad groups have one RSA. Outdoor Furniture remains the engine (31 conversions at $29).
- **Precision GPR (66 D, up 16):** 29 conversions at $87, five converting actions. Remaining: pause "**LP Search - Location" (9 impressions, $0, Maximize Conversions with no data) and cap or pause DSA ($331, 2 conv, $165); five keywords at QS 2 to 3 with BELOW_AVERAGE landing page ("Underground Utility Survey" $333, "Ground Penetrating Radar" $319 and $69); visible leaks: gprs orlando and tampa $121 (GPRS is a competitor), julie wire locator $28, miss utility $23, sunshine811 $19, 1800 dig $9, who to call before digging $13, s&n locating $12, rebar finder $18. "811" and "before you dig" are in the list; add phrase "julie", "miss utility", "sunshine811", "1800 dig", "s&n", "rebar finder", "gprs orlando", "gprs tampa".
- **The Counseling Group (68 D):** 20 serving days (Mon to Fri), $553, on plan at $25 a day. 2 form leads, 1 call from ads, and the first ever "Website Phone Click (tel tap)" on Oct 5, so the manual test is no longer needed. Tom's 34 negatives on Sep 21 landed. Couples ($114), Anxiety ($80) and Depression ($55) groups converted nothing in 30 days; Therapist Near Me carries all three conversions. "therapist near me" exact is QS 2 ($31, 0). Visible name and info leaks this window were $90, most of them now blocked. Enhanced conversions confirmed OFF.
- **M&S Asphalt Paving (70 C):** back on since Sep 15; $400 for 7 conversions at $57 on 16 serving days. Paving - Volusia only serves some days (two days this week); check whether the $27 budget or an ad schedule is pacing it. One RSA per ad group; "christian brothers asphalt" $17 ("christian brothers" is in the list, check match type); "cost to resurface driveway" $19 and "driveway installation cost" $10 want a "cost" phrase negative (not present).
- **Affordable Critter Solutions (78 C):** 16 conversions at $19, two Attic RSAs PENDING review after sheokand003's Oct 10 rewrite. "orlando animal control phone number" $10 and "animal control orange county number" $3 are county-agency queries; "animal control" phrase would block the converting "24 hour animal control orange county", so add exact "orlando animal control phone number" and phrase "county number", "phone number" instead. $10 a day is still the constraint.
- **All Phase Jacksonville:** "Orlando" search campaign still ENABLED, NOT_ELIGIBLE, $0. Pause it when convenient. LSA paused Sep 24.
- **Jupiter Boat Supply, REK Marketing:** paused, zero spend, nothing to do.

Out of scope, for the record only: Citrus Landscape Solutions Sanford LSA $9,470 and St. Pete $5,330 in the window; Straightline Fence LSA $3,482 for 25 leads; Herrell Plumbing $1,572 LSA plus $1,702 on two Smart campaigns; Byers Fence search campaign "Leads-Search-7/24" spent $1,262 (not REK-managed); Spectrum Electric LSA paused.

## Optimization opportunities (fleet)

New negatives, deduped against live lists, by account: Quality Paralegal (legal aid, pro bono, free lawyer, free consultation, clerk of court, visa center, speak to a lawyer, lawyer online), Color Masters (how much, cost, idea, ideas, colors, glidden, refacing, equipment, faux, mobile home, j&b painting, jesus gil), Rover (pet angel, peggy adams, haisley, paws and cherish, taps animal, safe passage, gentle pet crossing, pet cemetery, urn, urns, free), Florida Sealcoating (m&s asphalt exact in all campaigns, father and son, concrete contractor, asphalt tack, hot mix, american sealcoating, striping machine, hot shot, watson paving, landmark paving, finish line), Precision GPR (julie, miss utility, sunshine811, 1800 dig, s&n, rebar finder, gprs orlando, gprs tampa), All Phase (pebble tec installers, thompson, pool deck resurfacing of central florida, pool service, pool builders), Aqua Coat (attach the master list; then pentair, tech support, pump), Patio Style (carport, show me, screen enclosures), Affordable Critter (exact "orlando animal control phone number", phrase "county number"), Scootz (scooterbug), M&S (cost, christian brothers check), Counseling Group (none new this week).

New keywords to add: Quality Paralegal phrase "legal document preparation" (2 conversions at $13 to $15), "temporary custody agreement" (1 at $11), "paralegal orlando" exact (1 at $6); Color Masters exact "pool cage painting" (1 at $10) and "painting companies near me" (2 calls on "painting companies"); Rover exact "in home pet euthanasia near me" is already there and converting at $7, add phrase "put dog down at home" (1 at $9) and "home euthanasia service for dogs" (1 at $5); Florida Sealcoating exact "asphalt company near me" (1 at $38) and "driveway companies near me" (1 at $46); Aqua Coat phrase "pool refinishing companies near me" (1 at $9); Progetto exact "blinds installation near me" (1 at $4) and "woven shades" (1 at $7); Precision GPR exact "gpr services near me" (1 at $31).

Bid and budget adjustments: Color Masters Residential ceiling $11 to $7; Florida Sealcoating Branded to Manual CPC $3 or Target IS with a $4 cap; Rover Competitors back to $5 until it converts and In-Home capped (enhanced CPC off or a $6 max); All Phase restore the $25 target CPA or Maximize Clicks $6; Patio Style Pergolas to Maximize Clicks with a $5 ceiling and the Oct 7 keywords on phrase only; Progetto pause Drapery and move $6 to Shutters; Precision GPR pause Location, DSA to $5 a day; Quality Paralegal pause the Smart campaign and move $5 to the budget-limited search campaign; Filutowski Brand Awareness $455 to $200, Branded and Eye Surgery $50 to $100 (Tom's call on scope).

Competitive read (rank-lost share as the proxy): Progetto (57 to 85 percent rank-lost on $4 to $7 ceilings) and Color Masters Commercial (67 percent) are being outranked by Quality Score, not outbid; both need landing pages before bids. Rover holds 54 percent absolute top on In-Home at a $13 CPC this week, which is paying for position it already had. Affordable Critter, Aqua Coat and All Phase lose 62 to 70 percent to rank on $10 to $30 budgets; that is a budget and Quality Score story. Filutowski Brand Awareness is at 10 percent impression share with 86 percent budget-lost at $455 a day, which means the keyword's auction is effectively unlimited and more budget would buy more of the same terms.

## Prioritized weekly action plan

1. **Critical, Tom: Filutowski scope.** Accalia Marketing is editing the account and the Sep 14 change list is untouched. Decide whether REK acts; if not, the routine will report it as excluded from next week.
2. **Critical, Tom: Quality Paralegal Services.** Confirm the engagement and the primary conversion, then deep dive 1: directions and map taps to secondary, legal-aid negatives, pause the lawyer-intent broad keywords, pause the Smart campaign, fix the three disapproved ads.
3. **Critical, REK: Color Masters.** Deep dive 2: research-term negatives, Residential ceiling to $7, second RSAs, landing page for the "near me" and city terms, pause "residential painters" phrase.
4. **High, REK: All Phase.** Reattach the master negative list, restore the target CPA or switch to Maximize Clicks, brand split, two phrase conversions.
5. **High, REK: Aqua Coat.** Attach the master list to "Aqua Coat Pool Plastering - M". Third ask.
6. **High, REK: Rover.** Competitors back to $5, pause "lap of love" exact, crematory negatives, cap In-Home, test the two silent website actions, second RSAs in the two single-ad groups.
7. **High, REK: Florida Sealcoating.** Branded to a capped strategy, "m&s asphalt paving" exact negative everywhere, the supplier and competitor negatives above.
8. **High, REK: Progetto Shades.** Deep dive 3: landing pages, pause the six QS 1 to 3 zero-conversion keywords, second RSAs, pause Drapery.
9. **Medium, REK: Scootz.** Turn off Recommendations Auto-Apply, re-add "scooter rental near me" exact if wanted, form_submit manual test, review the ad schedule next Monday.
10. **Medium, REK: Patio Style.** Pergolas to a capped strategy and phrase match, second RSAs in Outdoor Kitchens and Brand (both PENDING single ads), panel negatives.
11. **Medium, REK: Precision GPR.** Pause Location, cap DSA, the eight utility-locator negatives, landing page for the Utility Mapping and GPR groups.
12. **Low: Counseling Group** no action (tel-tap confirmed; watch Couples and Anxiety groups one more month), **Affordable Critter** county-agency negatives and the $15 a day ask, **M&S** pacing check and "cost" negative, **All Phase Jacksonville** pause the Orlando campaign.

## Rotation

Deep-dived this run: Quality Paralegal Services, Color Masters, Progetto Shades, Filutowski Eye Institute (update), All Phase Pool Remodeling. Due next Monday: Rover Veterinary Care (to measure the Oct 2 to 6 budget changes), Florida Sealcoating (to measure the Branded cut), Scootz (ad schedule and auto-apply). The week after: Patio Style, Aqua Coat, Affordable Critter, The Counseling Group (October deep dive per the Sep 4 note), M&S Asphalt.

## Data notes

- Account discovery returned 31 client accounts; the Sep 14 list had 26 and all 26 are still present. Compare next week against this run's list.
- Two PENDING manager links (116-301-0558 and 325-901-5827) are visible in customer_client_link and not yet accepted by the client side. They do not appear in customer_client and could not be queried.
- The installed google-ads client (33.0.0) ships API v23 to v25 only; v22 fails. Set GOOGLE_ADS_API_VERSION=v24 or change the default in tools/gaql.py. Three field names were dropped in v24 (campaign.start_date, campaign.end_date, campaign.maximize_clicks.cpc_bid_ceiling_micros) and the recommendation impact and keyword fields are gone; the queries were adjusted.
- Search-term tables use Google's visible terms only. Confirmed waste is a floor. Filutowski's Brand Awareness campaign shows $9,029 of its $13,926 as visible terms.
- Quality Score is reported only for keywords with enough recent impressions; "n/a" was treated as unknown.
- Change history was pulled from Sep 13 (the API allows 30 days). Shared-set attachments and conversion action edits are not in change history, which is why the All Phase list detachment and the Patio Style directions demotion cannot be dated or attributed.
- Primary conversions are metrics.conversions (primary and included actions). Where an account counts local actions as primary (Quality Paralegal, Patio Style), the table says so.
- Known account context suggested for the protocol: Color Masters (426-092-9847, REK search since Sep 18; 163-445-9282 is its LSA account), Quality Paralegal Services (447-153-2607, engagement and primary conversion to confirm), MB Skin Care (LSA only, built Oct 5), Straightline Fence (LSA only since the Sep 22 removal), M&S Asphalt (active again since Sep 15).
- The credential file was written with mode 600, read only by the google-ads client, and deleted before this report was committed.
