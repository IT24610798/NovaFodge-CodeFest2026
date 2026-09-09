# Testing Log — Sample Questions

How to use this: once Person 2 confirms the search is connected to the real database, go
through each row live. Ask the question through the actual system (not by reading the code),
watch what it does, and fill in the columns honestly — including when it fails.

**Priority order:** test all the 1C rows first, then 1B, then 1A. 1C and 1B questions need
multiple search hops (find fact A, then use it to find fact B) — that's exactly what your
sub-track is judged on. 1A questions are mostly about images/figure plates, which is a
different sub-track's focus — still worth trying, but not where your score comes from.

## Column guide (plain language)
- **Hops needed** — my guess at whether this needs 1 lookup or 2+ chained lookups. Confirm or
  correct this once you actually see the search happen.
- **Result** — Pass / Partial / Fail. *Partial* = got an answer but missed something or search
  stopped too early.
- **Why** — one sentence. This is the most valuable column — "why" is what goes in your failure
  log and impresses judges more than the pass/fail count itself.

---

## Priority 1 — Track 1C (your sub-track, test these first)

| QID | Question | Hops needed | Result | Why |
|---|---|---|---|---|
| 1c_000 | State the precise year in the Age of Shadows that marks the true founding of Gloamreach. | Likely 2+ (find Gloamreach's history, resolve which "founding" is the true one — sources may disagree) | | |
| 1c_003 | In which year was the 'Gauntlet of Sorrowfell' actually forged? | Likely 2+ (the word "actually" hints multiple sources give different years — good contradiction test) | | |

## Priority 2 — Track 1B (multi-hop, great stress test for your search loop)

| QID | Question | Hops needed | Result | Why |
|---|---|---|---|---|
| 1b_007 | Which accord was ultimately won by the faction of which Ederon Fellgard is a member? | 2 (find Ederon's faction → find what that faction won) | | |
| 1b_006 | Which individual was a member of the faction that ultimately won the War of Drowned Light? | 2 (find who won the war → find a member of that faction) | | |
| 1b_022 | Which war did Ravena Stormwell's own faction ultimately win? | 2 (find her faction → find what it won) | | |
| 1b_013 | Whose dominion encompasses the lair of the Gravemaw Wyrm? | 2 (find where the creature lairs → find who rules that place) | | |
| 1b_005 | Which war was won by the organization that included Isolde Mournvale as one of its members? | 2 (find her organization → find what it won) | | |
| 1b_009 | In what way is Halvard Crowhurst connected to the victors of the Purge of Blackport? | 2+ (find who won the Purge → find the connection to this person) | | |
| 1b_003 | To which shadowed redoubt must one journey to examine the relic long borne by Cerys Sablewood the Ashen since 356 AS? | 2 (find the relic she's carried → find where it currently is) | | |

## Priority 3 — Track 1A (image/figure-plate questions — try if time allows)

| QID | Question | Hops needed | Result | Why |
|---|---|---|---|---|
| 1a_v12 | What is the central emblem on the banner of House Morvain? | 1 (single lookup) | | |
| 1a_v06 | In the portrait of Ignatz Ashgrove the Oathless, what object are they holding? | 1 | | |
| 1a_008 | According to the official threat-classification plate, what numerical rating is assigned to the Weeping Lurker? | 1 | | |
| 1a_004 | According to the figure plate detailing weapon binding, how many shards of will are required to attune The Thrice-Bound Edge? | 1 | | |
| 1a_013 | On the figure plate depicting 'The Cinder-Wrought Aegis', what attunement cost is listed? | 1 | | |
| 1a_v11 | What is the central emblem on the banner of The Ashen Vanguard? | 1 | | |
| 1a_v07 | In the portrait of Aldous Wrenfield the Last Warden, what object are they holding? | 1 | | |
| 1a_009 | According to the figure plate, what is the recorded garrison strength of Greyfell Citadel? | 1 | | |
| 1a_007 | According to the figure plate, what is the attunement cost listed for the Thrice-Bound Lantern? | 1 | | |
| 1a_v21 | What motif is engraved on Gauntlet of Sorrowfell in its official illustration? | 1 | | |
| 1a_001 | According to the figure plate illustrating Emberdeep's forces, what is the recorded total of its garrison strength? | 1 | | |

**Heads up on the 1A rows:** several of these ask about portraits/plates/banners — the kind of
`.png` files your ingestion log noted as "produced no text." If the answer isn't in any text
document, that's a corpus-coverage limitation, not your agent failing — note that distinction in
the Why column instead of just marking it Fail (see `docs/limitations.md`).

---

## After you finish: write 3–5 fresh questions

Not from this list — make up your own, in your own words, about things you're curious about in
the archive (a faction, an artifact, a character). These are the ones judges most want to see
tried live in the demo. Add them below as you go:

| Your question | Result | Why |
|---|---|---|
| | | |
| | | |