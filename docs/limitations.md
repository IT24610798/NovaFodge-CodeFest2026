#Limitations

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