# PPC Weekly Audit - 2026-09-04 (scoped run: The Counseling Group only)

Scope: single-account deep dive on The Counseling Group (657-069-3617) at Tom's request. Not a fleet sweep. Data pulled live through the read-only google-ads-mcp on the Mac, MCC 656-695-7229. Window: last 30 days (Aug 5 to Sep 3, 2026). Auction insights skipped (Basic access token). Nothing was changed in the account.

Revised Sep 4 after Tom's review. The first draft ran without the context of REK's Aug 12 hand-work on this account, which changed three findings. See "Aug 12 context" below.

Account context applied: one Manual CPC search campaign, small counts are normal, and no finding below is based on a single conversion swing.

## Aug 12 context (from REK's hand-work, not visible in the API)

- Budget was raised from $18/day to $25/day on Aug 12 when the Couples Counseling group launched (Option A). $25/day on a Mon to Fri schedule is about $650/mo, so the $652.58 below is on plan. Clark may not have been looped in on the roughly $150/mo increase.
- Clark confirmed on Aug 12 that the practice offers a free 15-minute online or telehealth consultation. The ad copy promising it is correct.
- The "Website Phone Click (tel tap)" conversion action was created on Aug 12. Zeros before that date mean no tag existed, not a broken tag.
- The Master Negatives list had six couples and marriage negatives removed on Aug 12 (120 down to 114). The current count of 114 confirms that change held.
- The Depression RSA 801870651961 had an "epression" typo fixed on Aug 12. It is clean now but still the weakest of the three ads in that group.

## Health Score

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Conversion Tracking | 25% | 80 | 20.0 |
| Wasted Spend | 20% | 65 | 13.0 |
| Account Structure | 15% | 78 | 11.7 |
| Keywords & Targeting | 15% | 62 | 9.3 |
| Ads & Assets | 15% | 72 | 10.8 |
| Bidding & Settings | 10% | 78 | 7.8 |
| **Total** | | | **73 (C)** |

Week-over-week delta: unavailable. Last week's run (Sep 3) had no Google Ads data because the cloud refresh token failed, so there is no prior score to compare.

Estimated recoverable waste: $71.42 confirmed from visible search terms in the last 30 days, plus an unconfirmed share of the $468 that Google reports only as "other search terms".

## 30-day snapshot

| Metric | Value |
|---|---|
| Campaign | TCG - Search - Winter Park (Manual CPC, no eCPC) |
| Daily budget | $25.00 |
| Spend | $652.58 |
| Impressions | 3,633 |
| Clicks | 153 |
| CTR | 4.21% |
| Avg CPC | $4.27 |
| Conversions (primary) | 6 (4 form leads, 2 calls from ads) |
| Cost per conversion | $108.76 |
| Search impression share | 19.4% |
| Lost to budget | 36.5% |
| Lost to rank | 44.1% |
| Campaign primary status | LIMITED, reason BUDGET_CONSTRAINED |

Weekly trend (Mon to Fri serving only):

| Week of | Spend | Clicks | Conv | Search IS | Lost to budget |
|---|---|---|---|---|---|
| Aug 10 | $166.87 | 39 | 2 | 22.8% | 26.3% |
| Aug 17 | $164.63 | 38 | 0 | 16.7% | 42.8% |
| Aug 24 | $121.90 | 29 | 1 | 16.5% | 48.0% |
| Aug 31 (4 days) | $141.68 | 34 | 3 | 20.3% | 34.4% |

Note on spend: $652.58 in 30 days is exactly what a $25/day budget on a Mon to Fri schedule produces. It is on plan since the Aug 12 increase from $18/day. The only open item is making sure Clark knows the account scaled to $25/day.

## Findings with evidence

### 1. Conversion tracking (80)

What is right: two real lead types are tracked as primary and both fire. Form Lead (webpage, one per click) and Calls from ads (call asset, many per click). The four GA4 imports (qualify_lead, close_convert_lead, purchase, form_submission) are hidden and excluded from the conversions column, so there is no double counting. Conversions and all_conversions match (6 and 6). Auto-tagging is on. Tracking is owned by this account, not the MCC.

Finding: the third primary action, Website Phone Click (tel tap), was created on Aug 12 and has recorded zero conversions since. That is about three weeks of live data, not the four months the first draft implied (June and July zeros predate the tag). In that window the campaign sent 122 of its 153 clicks, and mobile was 69% of clicks across the full 30 days. Zero tel taps on that much mobile traffic is a real flag. Per the house rule it is not declared dead. It needs a manual trigger test: tap the phone number on the mobile site and confirm a conversion appears in Google Ads within a day. If the tag is broken, mobile lead attribution is undercounted and the true cost per lead is lower than $108.76.

Minor: 90-day click lookback on the tel tap action vs 30 days on the other two. Align to 30 once the tag is confirmed working.

Privacy: this is a mental health practice. Google will not sign a BAA, so Enhanced Conversions must stay off. The API confirms enhanced conversions for leads is disabled at the account level, but the account has accepted Google's customer data terms, which is the prerequisite for turning it on. Web-level Enhanced Conversions is a per-action setting the API does not expose, so confirm in the UI that it is off on Form Lead, Website Phone Click, and all four GA4 imports (purchase, qualify_lead, close_convert_lead, form_submission). Reference: TRACKING-privacy-checklist.md on the audit branch. This check belongs in every audit of a healthcare client.

Monthly primary conversions for context: June 2 (calls), July 2 (forms), Aug 4 (1 call, 3 forms), Sep 1 to 3: 2 (1 call, 1 form). The tel tap action did not exist before Aug 12, so it is absent from June and July by construction.

### 2. Wasted spend (65)

Search-term visibility: Google reports only $184.90 of the $652.58 (28%) at the search-term level. The rest sits in the privacy-thresholded "other" bucket. Every figure below is from the visible 28% only, so the true waste is likely higher but cannot be confirmed.

Irrelevant search terms that cost money (30 days):

| Group | Search term | Cost | Why irrelevant |
|---|---|---|---|
| Names | new leaf center winter park | $4.96 | competitor practice |
| Names | dr patrick gorman winter park | $4.95 | named practitioner |
| Names | center peace therapy | $4.94 | competitor practice |
| Names | teresa kovach | $4.92 | named practitioner |
| Names | camden huber | $4.92 | named practitioner |
| Names | retrouvaille | $3.94 | church marriage program |
| Names | dr david bloodgood | $3.75 | named practitioner |
| Names | net therapy near me | $3.94 | different modality (NET) |
| Medication / DIY | how do i get rid of depression naturally | $7.58 | self-help intent |
| Medication / DIY | supplement for depression and anxiety | $4.00 | supplements |
| Medication / DIY | curing depression | $3.95 | info intent |
| Medication / DIY | depression med list | $3.94 | medication |
| Medication / DIY | depression screening | $3.92 | info intent |
| Medication / DIY | what helps depression | $3.91 | info intent |
| Medication / DIY | older antidepressants | $3.82 | medication |
| Wrong population | treating anxiety in teenage girl | $3.98 | ads say adults |

Total confirmed irrelevant: $71.42 (names $36.32, medication and self-help $31.12, teen $3.98), which is 38.6% of the $184.90 visible search-term spend.

Zero-click impressions that show where the next waste will come from: antidepressants (23 impressions), ssri (5), spravato treatment near me (5), 54321 method (6), 5 4 3 2 1 grounding (5), gottman method (11), the mindful practice winter park (7). The account already has exact-match negatives for "5 4 3 2 1 method for anxiety" and "exercises for anxiety". Exact-match negatives do not block variants, which is why the grounding searches keep appearing.

Zero-conversion keywords with cost over $10 (30 days):

| Keyword | Match | Cost | Clicks | QS | Note |
|---|---|---|---|---|---|
| help with depression | phrase | $58.19 | 15 | n/a | 7 of its visible terms are medication or self-help |
| stress therapy | phrase | $43.18 | 11 | 2 | matched "net therapy near me" |
| anxiety therapy | phrase | $39.34 | 10 | 5 | matched the teen search |
| depression therapy | phrase | $35.45 | 9 | n/a | matched "curing depression", "treating depression in the elderly" |
| marriage counseling | phrase | $27.60 | 7 | n/a | |
| therapist for anxiety | phrase | $27.54 | 7 | n/a | |
| therapist winter park | phrase | $22.13 | 5 | 5 | |

Total: $253.43, or 39% of spend. At 6 conversions a month, a $30 keyword with zero conversions is not proof it cannot convert. The two that stand out are "help with depression" (intent is informational by construction) and "stress therapy" (QS 2, below-average landing page and expected CTR).

### 3. Account structure (78)

One campaign, four ad groups with clean themes: Therapist Near Me, Anxiety & Stress, Depression, Couples Counseling. Five shared negative lists attached (Master Negatives 114, Competitor Names 55, Wrong Services 37, Competitor Brands 20, DIY 17). No dead or duplicate campaigns.

Confirmation: Master Negatives shows 114 members, which matches the Aug 12 removal of six couples and marriage negatives (from 120). The unblock held.

Finding: cross-group keyword overlap. Therapist Near Me holds phrase-match "marriage counseling winter park", "couples counseling winter park", and "anxiety counseling winter park". The Couples and Anxiety groups hold the exact-match versions. A search like "couples counseling winter park fl" can be served from Therapist Near Me with the generic homepage ad instead of the couples ad and couples landing page. Low spend so far (14 impressions on those three), but it is a structural leak.

Finding: about 25 enabled keywords had 0 or 1 impressions in 30 days. Harmless, but they clutter the account and hide the ones that matter.

### 4. Keywords and targeting (62)

Quality Score is only available on 12 keywords. Four are at the floor:

| Keyword | Match | QS | Expected CTR | Landing page | Ad relevance | 30d cost | Conv |
|---|---|---|---|---|---|---|---|
| stress therapy | phrase | 2 | below avg | below avg | avg | $43.18 | 0 |
| therapist near me | exact | 2 | below avg | below avg | avg | $41.04 | 1 |
| therapist orlando | exact | 3 | below avg | below avg | above avg | $31.22 | 1 |
| couples therapy | phrase | 3 | below avg | below avg | above avg | $15.50 | 1 |

The common thread is landing page experience. The Therapist Near Me group sends every click to the homepage. The two "near me" keywords that convert are paying a rank penalty for it. Rank-lost impression share is 44%, the largest single reason this campaign does not show.

Broad match share of spend: 0%. Good. Everything is phrase or exact.

Missing negatives: see the wasted spend list. The gaps are medication and pharmacology terms, self-help and grounding techniques as phrase match, teen and child terms, and eight practitioner and practice names.

Targeting: 15-mile radius around Winter Park, presence-only. Search partners and Display off. Language set. All sensible.

### 5. Ads and assets (72)

Responsive search ads per group and ad strength:

| Ad group | RSAs | Strengths | 30d spend | Conv |
|---|---|---|---|---|
| Therapist Near Me | 3 | POOR, AVERAGE, AVERAGE | $339.24 | 4 |
| Anxiety & Stress | 3 | AVERAGE, AVERAGE, GOOD | $110.06 | 0 |
| Depression | 3 | POOR, GOOD, GOOD | $93.64 | 0 |
| Couples Counseling | 1 | GOOD | $109.64 | 2 |

Finding: Couples Counseling has one RSA. The protocol floor is two.

Finding: the POOR ad in Therapist Near Me (ad 801828725034) is the biggest spender in the account at $151.15 and produced 2 of the group's 4 conversions, so it should be improved rather than paused. Its problems are visible in the copy: a typo in description 1 ("progress.Insurance" with no space), and five short filler headlines that carry no keyword ("Real Progress", "Small Practice", "Personal Attention", "Positive People & Change", "Men's & Women's Specialists").

Finding: the POOR ad in Depression (ad 801870651961) got 33 impressions and 0 clicks in 30 days. Its typo was fixed on Aug 12 and the copy is clean now, but Google still barely serves it because two GOOD ads sit beside it. Pausing it is fine and nearly free at 33 impressions.

Finding: the callout "Free 15-Min Consultation" is paused, while eight of the ten live RSAs promise a free 15-minute consultation. Clark confirmed the offer on Aug 12, so the ad copy is right and the callout was simply never re-enabled. No client question needed.

Assets in place: 4 sitelinks, 9 live callouts, structured snippet, call asset (407) 647-4902, business name. No image assets. Google's open recommendation for dynamic image extensions is safe to ignore for a counseling practice.

### 6. Bidding and settings (78)

Manual CPC with $4.00 bids on most keywords, $5.00 and $7.00 on two Winter Park terms. Enhanced CPC off. This is the correct choice at 6 conversions a month. Google's open recommendation to switch to Maximize Conversions should be declined; the campaign is well under the 15 per month where that strategy has enough signal. Same for the Search Partners opt-in recommendation.

Budget vs delivery: primary status is LIMITED by budget, budget-lost impression share is 36.5%, and daily spend hits or exceeds $25 on most serving days. Those three agree with each other, so there is no pacing contradiction. The campaign is simply capped. Raising the budget would buy more impressions at the current waste rate, so fix the negatives first.

Device split (30 days):

| Device | Spend | Clicks | Conv | Cost per conv |
|---|---|---|---|---|
| Mobile | $457.92 | 106 | 3 | $152.64 |
| Desktop | $190.68 | 46 | 3 | $63.56 |
| Tablet | $3.98 | 1 | 0 | n/a |

Three conversions each is too few to act on with confidence, and the missing tel-tap tag (finding 1) would understate mobile if it is broken. Re-check after the tag test before touching device bids.

Ad schedule: Mon to Thu 8am to 8pm, Fri 8am to 2pm, no weekends. Deliberate, but it means no ads on Saturday and Sunday when people often search for a therapist. A client decision, not a defect.

Change history (30 days): one batch of 9 ad-group keyword removals on Aug 10 applied through Google Ads recommendations by tom@rekmarketing.com. Nothing else. The account is stable.

## Prepared change list (suggestions only, nothing applied)

### A. Negative keywords

Checked against the live shared lists (Master Negatives 114, Wrong Services 37, Competitor Brands 20, Competitor Names 55, DIY 17) so nothing below is a re-add. Already present and therefore dropped from the list: "medication" and "adolescent" (Wrong Services, phrase), "child therapist" and "teen therapist" (Wrong Services), "teen therapy", "kids therapy", "child psychologist", and "grounding techniques" (Master Negatives, broad). The standalone tokens below still add coverage because negative keywords do not match plurals or partial phrases. "child" is deliberately left out: as a phrase negative it would also block "childhood trauma", which is adult-relevant for this practice.

Add to the "Wrong Services" or "DIY" shared list as phrase match unless noted:

- antidepressant
- antidepressants
- ssri
- spravato
- med list
- supplement
- supplements
- naturally
- get rid of
- curing
- screening
- what helps
- grounding
- 54321
- 5 4 3 2 1
- teen
- teenage
- teenager
- kids

Add to the "Competitor Names" shared list as phrase match:

- new leaf center
- patrick gorman
- center peace
- teresa kovach
- camden huber
- david bloodgood
- retrouvaille
- mindful practice
- net therapy

Ask the client before adding: "gottman" (11 impressions on "gottman method" plus a $3.95 click). If the therapists use or are trained in the Gottman method, keep it and consider an ad headline. If not, add it as a phrase negative.

Convert existing exact-match campaign negatives to phrase match so variants stop leaking: "breathing exercises for anxiety", "exercises for anxiety", "5 4 3 2 1 method for anxiety", "5 things anxiety trick", "how to meditate for stress relief", "somatic exercises for nervous system regulation", "vagus nerve exercises for anxiety", "tapping for anxiety".

### B. Keywords

- Pause "help with depression" (phrase) in Depression. $58.19 with zero conversions and informational intent by construction. "depression therapy", "depression counseling", and "therapist for depression" already cover the commercial searches.
- Pause "stress therapy" (phrase) in Anxiety & Stress. QS 2, $43.18, zero conversions, and it pulled in a NET therapy search. "anxiety therapy" and "therapist for anxiety" stay.
- Remove the three phrase-match keywords from Therapist Near Me that belong elsewhere: "marriage counseling winter park", "couples counseling winter park", "anxiety counseling winter park". Add phrase-match versions of the first two to Couples Counseling and the third to Anxiety & Stress, so the search lands on the matching ad and page.
- Leave the two QS 2 to 3 "near me" and "orlando" exact keywords alone. They convert. Their fix is the landing page in section D.

### C. Ads and assets

- Add a second RSA to Couples Counseling. Reuse the GOOD ad's structure with a different angle: lead with "Marriage Counseling Winter Park" and "Couples Therapist Near You". The free consultation line is confirmed and can stay.
- Edit ad 801828725034 in Therapist Near Me. Fix the "progress.Insurance" typo. Replace "Real Progress", "Small Practice", "Personal Attention", and "Positive People & Change" with keyword-bearing headlines such as "Counseling in Winter Park", "Therapist Near Winter Park", "Licensed Therapist, Orlando", and "Therapy Near Me, Winter Park". Keep the pinned "Therapist in Winter Park, FL" headline.
- Pause ad 801870651961 in Depression (POOR, 33 impressions, 0 clicks). The group keeps two GOOD ads.
- Re-enable the paused "Free 15-Min Consultation" callout. The offer is confirmed (Clark, Aug 12) and the ad copy is correct.

### D. Landing page (REK web task)

Build a dedicated "Therapist in Winter Park" page for the Therapist Near Me group instead of the homepage. All four QS 2 to 3 keywords are marked below average on landing page experience, and that group carries 52% of spend. This is the single change most likely to move rank-lost impression share, which is currently 44%.

### E. Tracking

- Manual trigger test of "Website Phone Click (tel tap)": tap the number on the mobile site, then confirm the conversion registers. Zero in the three weeks since the tag was built on Aug 12 is a signal, not a verdict.
- After the test, set its click lookback to 30 days to match the other two primary actions.
- Confirm in the UI that Enhanced Conversions is off on every conversion action. No BAA, so it must stay off.

### F. Settings

- Decline Google's Maximize Conversions and Search Partners recommendations.
- Hold the budget at $25/day until the negatives in A are in and two weeks of data confirm the waste is gone. Make sure Clark is aware the account has been at $25/day (about $650/mo) since Aug 12, since that increase was a REK call at the time.
- Revisit a mobile bid adjustment only after the tel-tap tag is verified. Current data (3 vs 3 conversions) is too thin.

## Execution triage (Tom, Sep 4)

Greenlight now: re-enable the free-consult callout, the deduped negative additions above, converting the exact-match technique negatives to phrase, pausing "help with depression" and "stress therapy", fixing the typo and filler headlines in ad 801828725034, and adding a second Couples RSA.

Confirm first: whether the therapists use the Gottman method (decides the "gottman" negative), and loop Clark on the $25/day spend.

The needle-mover: the dedicated Winter Park landing page in section D. Everything else trims waste. That one addresses the 44% rank-lost impression share.

## Rotation note

This account was deep-dived on Sep 4 and does not need another until early October unless its score moves 10 points. The rest of the fleet is still due for the Monday sweep once the cloud token is replaced or the audit runs from the Mac MCP.
