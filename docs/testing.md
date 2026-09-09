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
| 1c_000 | State the precise year in the Age of Shadows that marks the true founding of Gloamreach. | Likely 2+ (find Gloamreach's history, resolve which "founding" is the true one — sources may disagree) | Fail | Real archive chunks were retrieved, but the agent could not complete reflection or answer generation because OpenRouter returned HTTP 401. |
| 1c_003 | In which year was the 'Gauntlet of Sorrowfell' actually forged? | Likely 2+ (the word "actually" hints multiple sources give different years — good contradiction test) | Fail | Real chunks were retrieved, but final answer generation was blocked by the OpenRouter authentication failure. |

## Priority 2 — Track 1B (multi-hop, great stress test for your search loop)

| QID | Question | Hops needed | Result | Why |
|---|---|---|---|---|
| 1b_007 | Which accord was ultimately won by the faction of which Ederon Fellgard is a member? | 2 (find Ederon's faction → find what that faction won) | Fail | Retrieval began and returned real chunks, but the full agent test was blocked by OpenRouter HTTP 401; later Voyage requests were rate-limited. |
| 1b_006 | Which individual was a member of the faction that ultimately won the War of Drowned Light? | 2 (find who won the war → find a member of that faction) | Fail | Voyage AI rate limit stopped retrieval before the agent could produce an answer. |
| 1b_022 | Which war did Ravena Stormwell's own faction ultimately win? | 2 (find her faction → find what it won) | Fail | Retrieval returned real chunks, but the full agent answer was blocked by OpenRouter HTTP 401. |
| 1b_013 | Whose dominion encompasses the lair of the Gravemaw Wyrm? | 2 (find where the creature lairs → find who rules that place) | Fail | Retrieval returned real chunks, but the full agent answer was blocked by OpenRouter HTTP 401. |
| 1b_005 | Which war was won by the organization that included Isolde Mournvale as one of its members? | 2 (find her organization → find what it won) | Fail | Retrieval returned real chunks, but the full agent answer was blocked by OpenRouter HTTP 401. |
| 1b_009 | In what way is Halvard Crowhurst connected to the victors of the Purge of Blackport? | 2+ (find who won the Purge → find the connection to this person) | Fail | Voyage AI rate limit stopped retrieval before the agent could produce an answer. |
| 1b_003 | To which shadowed redoubt must one journey to examine the relic long borne by Cerys Sablewood the Ashen since 356 AS? | 2 (find the relic she's carried → find where it currently is) | Fail | Retrieval returned real chunks, but the full agent answer was blocked by OpenRouter HTTP 401. |

## Priority 3 — Track 1A (image/figure-plate questions — try if time allows)

| QID | Question | Hops needed | Result | Why |
|---|---|---|---|---|
| 1a_v12 | What is the central emblem on the banner of House Morvain? | 1 (single lookup) | Fail | The real text index returned chunks, but image-only evidence is not reliably available and final answer generation was blocked by OpenRouter HTTP 401. |
| 1a_v06 | In the portrait of Ignatz Ashgrove the Oathless, what object are they holding? | 1 | Fail | Portrait evidence is image-based; OCR/text retrieval did not establish the answer, and OpenRouter authentication failed. |
| 1a_008 | According to the official threat-classification plate, what numerical rating is assigned to the Weeping Lurker? | 1 | Fail | Figure-plate evidence was not established in text retrieval, and OpenRouter authentication failed. |
| 1a_004 | According to the figure plate detailing weapon binding, how many shards of will are required to attune The Thrice-Bound Edge? | 1 | Fail | A real text chunk was retrieved, but the full agent answer was blocked by OpenRouter HTTP 401. |
| 1a_013 | On the figure plate depicting 'The Cinder-Wrought Aegis', what attunement cost is listed? | 1 | Fail | Figure-plate evidence was not established in text retrieval, and OpenRouter authentication failed. |
| 1a_v11 | What is the central emblem on the banner of The Ashen Vanguard? | 1 | Fail | The real text index returned chunks, but image-only evidence is not reliably available and OpenRouter authentication failed. |
| 1a_v07 | In the portrait of Aldous Wrenfield the Last Warden, what object are they holding? | 1 | Fail | Portrait evidence was not established in text retrieval; Voyage AI rate limiting also interrupted the test. |
| 1a_009 | According to the figure plate, what is the recorded garrison strength of Greyfell Citadel? | 1 | Fail | A real catalogue chunk was retrieved, but the full agent answer was blocked by OpenRouter HTTP 401. |
| 1a_007 | According to the figure plate, what is the attunement cost listed for the Thrice-Bound Lantern? | 1 | Fail | The real text index returned chunks, but the final answer was blocked by OpenRouter HTTP 401. |
| 1a_v21 | What motif is engraved on Gauntlet of Sorrowfell in its official illustration? | 1 | Fail | Illustration evidence was not established in text retrieval, and OpenRouter authentication failed. |
| 1a_001 | According to the figure plate illustrating Emberdeep's forces, what is the recorded total of its garrison strength? | 1 | Fail | Voyage AI rate limiting stopped retrieval before the agent could produce an answer. |

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
| Which archive entries contradict each other about the Gauntlet of Sorrowfell's forging date? | Fail | Retrieval found real archive material, but OpenRouter HTTP 401 prevented the agent from comparing sources. |
| Which faction controlled Gloamreach during the Age of Shadows? | Fail | The question was not completed through the agent because OpenRouter authentication failed. |
| What evidence links the Edge of Gloamreach to the history of the region? | Fail | The real index is available, but final answer generation was unavailable because of OpenRouter HTTP 401. |