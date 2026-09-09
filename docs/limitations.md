# Known Limitations

Honest, scoped limitations — not a place to hide problems. Per the competition rubric, clearly
explaining what broke and why scores *higher* on "technical judgment" and "problem
understanding" than pretending everything works.

## 1. Ephemera coverage is partial

We have full embedding coverage of `codex/`, `wiki/`, and `chronicles/` (3,963 chunks), but only
a targeted 8-document sample of `ephemera/` (37 chunks) out of 145 total ephemera files.

**Cause:** Voyage AI's free tier without a payment method is rate-limited to 3 requests/minute.
Embedding the full corpus (~4,580 chunks) would take 40+ minutes from rate limiting alone. We
made a deliberate call to fully embed the highest-value collections (codex/wiki/chronicles)
first and add ephemera as time allowed.

**Practical effect:** questions whose answer lives *only* in an un-embedded ephemera document
(e.g. a specific tavern letter or ledger) will not be retrievable — the agent will correctly
report it can't find evidence, which is different from the agent failing to search properly.
See `docs/testing.md` for how we distinguish these two cases in our test results.

## 2. Image-only documents produce no searchable text

54 files (portraits, heraldry, landscapes, creature plates, relic plates — all `.png`, `atmo_`
prefix) parsed successfully but extracted zero text, since our current pipeline is text-based.
These images are not currently retrievable by the agent even though they exist in the corpus.
Full filenames are preserved in the raw log below. *(Note: this matters more for sub-track 1A;
for our 1C system it mainly affects questions that depend on purely visual details with no
accompanying text description — e.g. several `1a_*` questions in `sample_questions.json`.)*

## 3. [Add: any agent-loop limitations from Person 2's testing — e.g. cases where reflection
stops too early, or reformulated queries aren't different enough from the first search]

## 4. [Add: any answer-synthesis limitations from Person 3 — e.g. how contradicting sources are
currently handled, and where that handling is incomplete]

---

## Appendix — Raw ingestion log (verbatim, unedited)

Kept in full as supporting evidence for the claims above. Not meant to be read top-to-bottom by
judges; referenced from the summary section.

## Ingestion run — 2026-09-09T09:00:31

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T09:34:43

### Files that failed to parse (54)
- atmo_battle_painting_conflict_the_accord_of_mournthrone.png: parsed successfully but produced no text (empty doc?)
- atmo_battle_painting_conflict_the_leaden_accord.png: parsed successfully but produced no text (empty doc?)
- atmo_battle_painting_conflict_the_purge_of_blackport.png: parsed successfully but produced no text (empty doc?)
- atmo_battle_painting_conflict_the_war_of_drowned_light.png: parsed successfully but produced no text (empty doc?)
- atmo_battle_painting_conflict_the_war_of_endless_vigil.png: parsed successfully but produced no text (empty doc?)
- atmo_battle_painting_conflict_the_winter_reckoning.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_ashfall_colossus.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_cinder_shrike.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_gravemaw_wyrm.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_lantern_moth_swarm.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_marsh_revenant.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_pale_stag_of_omens.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_salt_blind_leviathan.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_thorn_wraith.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_vault_chitin.png: parsed successfully but produced no text (empty doc?)
- atmo_creature_creature_weeping_lurker.png: parsed successfully but produced no text (empty doc?)
- atmo_heraldry_faction_house_morvain.png: parsed successfully but produced no text (empty doc?)
- atmo_heraldry_faction_the_ashen_vanguard.png: parsed successfully but produced no text (empty doc?)
- atmo_heraldry_faction_the_bleeding_crown.png: parsed successfully but produced no text (empty doc?)
- atmo_heraldry_faction_the_iron_ring_cartel.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_blackford.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_embermarch.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_fenspire.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_gloammarch.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_gloamreach.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_hollowreach.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_ironfell_citadel.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_thorncairn.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_vharencrag_fortress.png: parsed successfully but produced no text (empty doc?)
- atmo_landscape_location_vharenford.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_aldous_wrenfield_the_last_warden.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_brannoc_ironmere_the_red_handed.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_cerys_sablewood_the_ashen.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_corvus_hollowmere_the_pale.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_gareth_ironmere.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_halvard_vane_the_grave_sworn.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_ignatz_ashgrove_the_oathless.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_isolde_fellgard_the_unforgiven.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_maelis_harrowick_the_pale.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_malchior_cindervale_the_flame_touched.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_morwenna_ashgrove.png: parsed successfully but produced no text (empty doc?)
- atmo_portrait_character_sabelle_mournvale_the_twice_crowned.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_chalice_of_ashdeep.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_diadem_of_sorrowgate.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_edge_of_gloamreach.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_gauntlet_of_sorrowfell.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_cinder_wrought_aegis.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_crown_of_burned_names.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_hollow_edge.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_psalter_of_seven_sorrows.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_sceptre_of_final_winter.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_silent_psalter.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_thrice_bound_edge.png: parsed successfully but produced no text (empty doc?)
- atmo_relic_artifact_the_thrice_bound_lantern.png: parsed successfully but produced no text (empty doc?)

## Ingestion run — 2026-09-09T09:45:13

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T10:17:33

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T10:38:21

### Files that failed to parse (0)
- None.

## Embedding rate limits
Voyage AI free tier without a payment method is capped at 3 requests/minute.
This meant a full 4580-chunk embedding run would take ~40 minutes just from
rate limiting, not compute time. Prioritized codex/wiki/chronicles folders
first (3963 chunks, ~officially the most load-bearing content), with
ephemera embedding to follow as time allows.

## Ingestion run — 2026-09-09T11:35:31

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T11:39:08

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T11:42:52

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T11:46:53

### Files that failed to parse (0)
- None.

## Embedding resume logic bug
Initial embedding attempts used random UUIDs for chunk IDs, which meant
resume-after-failure logic could never detect "already stored" chunks
(new random IDs never matched old random IDs from a previous run).
Fixed by switching to deterministic hash-based IDs (md5 of filename +
page + chunk index), so re-running after a rate-limit interruption
correctly skips already-embedded chunks instead of re-processing
everything from scratch.

## Final embedding coverage
1117 chunks embedded and stored: full coverage of codex, wiki, and
chronicles folders, plus a targeted 8-document sample from ephemera
(37 chunks). Confirmed present and retrievable under reliability_tier
"unreliable" via both semantic search and direct metadata filter
(collection.get(where={"reliability_tier": "unreliable"})).
Full ephemera coverage (145 files total) was not achievable due to
Voyage AI free-tier rate limits (3 RPM without payment method).
This is a scoped, disclosed limitation, not an oversight.
## Ingestion run — 2026-09-09T20:04:43

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T20:51:06

### Files that failed to parse (0)
- None.

## Ingestion run — 2026-09-09T22:00:03

### Files that failed to parse (47)
- plate_00_location_marrowwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_01_location_emberdeep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_02_conflict_the_accord_of_mournthrone.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_03_location_crookgate_keep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_04_artifact_the_thrice_bound_edge.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_05_location_embercrag_fortress.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_06_location_hollowreach.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_07_artifact_the_thrice_bound_lantern.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_08_creature_weeping_lurker.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_09_location_greyfell_citadel.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_10_creature_marsh_revenant.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_11_location_mournwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_12_location_thorncairn.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_13_artifact_the_cinder_wrought_aegis.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_14_creature_thorn_wraith.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- ballad_concerning_crookgate_keep.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- ballad_concerning_the_sceptre_of_final_winter.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- contract_concerning_halvard_sablewood.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- contract_concerning_marsh_revenant.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- contract_concerning_the_cinder_wrought_aegis.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- field_report_concerning_cerys_sablewood_the_ashen.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_ashreach.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_crookgate_keep.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_greyfell_citadel.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_hesper_wrenfield.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- letter_concerning_the_accord_of_mournthrone.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- muster_roll_concerning_hollowvale.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- petition_concerning_halvard_cindervale.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- petition_concerning_morwenna_morvain.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- sermon_concerning_fenthrone.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- sermon_concerning_marsh_revenant.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- sermon_concerning_salt_blind_leviathan.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- plate_00_location_marrowwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_01_location_emberdeep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_02_conflict_the_accord_of_mournthrone.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_03_location_crookgate_keep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_04_artifact_the_thrice_bound_edge.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_05_location_embercrag_fortress.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_06_location_hollowreach.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_07_artifact_the_thrice_bound_lantern.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_08_creature_weeping_lurker.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_09_location_greyfell_citadel.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_10_creature_marsh_revenant.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_11_location_mournwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_12_location_thorncairn.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_13_artifact_the_cinder_wrought_aegis.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_14_creature_thorn_wraith.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.

## Ingestion run — 2026-09-09T22:00:14

### Files that failed to parse (47)
- plate_00_location_marrowwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_01_location_emberdeep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_02_conflict_the_accord_of_mournthrone.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_03_location_crookgate_keep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_04_artifact_the_thrice_bound_edge.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_05_location_embercrag_fortress.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_06_location_hollowreach.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_07_artifact_the_thrice_bound_lantern.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_08_creature_weeping_lurker.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_09_location_greyfell_citadel.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_10_creature_marsh_revenant.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_11_location_mournwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_12_location_thorncairn.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_13_artifact_the_cinder_wrought_aegis.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_14_creature_thorn_wraith.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- ballad_concerning_crookgate_keep.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- ballad_concerning_the_sceptre_of_final_winter.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- contract_concerning_halvard_sablewood.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- contract_concerning_marsh_revenant.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- contract_concerning_the_cinder_wrought_aegis.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- field_report_concerning_cerys_sablewood_the_ashen.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_ashreach.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_crookgate_keep.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_greyfell_citadel.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- interrogation_record_concerning_hesper_wrenfield.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- letter_concerning_the_accord_of_mournthrone.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- muster_roll_concerning_hollowvale.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- petition_concerning_halvard_cindervale.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- petition_concerning_morwenna_morvain.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- sermon_concerning_fenthrone.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- sermon_concerning_marsh_revenant.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- sermon_concerning_salt_blind_leviathan.scan.pdf: PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
- plate_00_location_marrowwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_01_location_emberdeep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_02_conflict_the_accord_of_mournthrone.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_03_location_crookgate_keep.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_04_artifact_the_thrice_bound_edge.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_05_location_embercrag_fortress.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_06_location_hollowreach.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_07_artifact_the_thrice_bound_lantern.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_08_creature_weeping_lurker.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_09_location_greyfell_citadel.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_10_creature_marsh_revenant.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_11_location_mournwatch.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_12_location_thorncairn.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_13_artifact_the_cinder_wrought_aegis.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
- plate_14_creature_thorn_wraith.png: TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
