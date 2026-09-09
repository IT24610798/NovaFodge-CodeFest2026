SAMPLE_CHUNKS = [
    {
        "id": "novel_ashfall_0012",
        "text": "Ashvael raised the Cindered Accord above his head, and the ash-lit "
                "sky answered with a single peal of thunder. The soldiers of Veyr Hold "
                "knelt, not from loyalty, but from fear of what he had become.",
        "source_doc": "Novel: The Ashfall Cycle, Book II",
        "doc_type": "novel",
    },
    {
        "id": "wiki_ashvael_003",
        "text": "Ashvael, also known as the Cinder King, was the last confirmed bearer "
                "of the Cindered Accord before its disappearance in 214 AE. Wiki editors "
                "note his birth year is disputed between sources.",
        "source_doc": "Wiki: Ashvael (character page)",
        "doc_type": "wiki",
    },
    {
        "id": "codex_artifacts_0045",
        "text": "Cindered Accord: a bonded pair of obsidian gauntlets, forged during the "
                "War of Embers. Codex records list its last verified owner as Ashvael, "
                "circa 214 AE, matching wiki records exactly.",
        "source_doc": "Codex III: Artifacts and Relics, Plate 45",
        "doc_type": "codex",
    },
    {
        "id": "ephemera_tavernballad_009",
        "text": "Oh Ashvael, born of ember and salt, they say you were crowned before "
                "you could walk, and that the Accord chose you in your cradle.",
        "source_doc": "Ephemera: Tavern Ballad, 'The Cinder-Born'",
        "doc_type": "ephemera",
    },
    {
        "id": "novel_ashfall_0034",
        "text": "The northern trade routes through the Veyr provinces had been cut off "
                "for three winters, ever since the fall of Veyr Hold. Grain shortages "
                "spread as far south as the Salt Coast.",
        "source_doc": "Novel: The Ashfall Cycle, Book II",
        "doc_type": "novel",
    },
    {
        "id": "wiki_veyrhold_001",
        "text": "Veyr Hold was a fortified city on the northern border, destroyed during "
                "the War of Embers. Its fall triggered widespread trade disruption across "
                "the northern provinces.",
        "source_doc": "Wiki: Veyr Hold (location page)",
        "doc_type": "wiki",
    },
    {
        "id": "ephemera_trialtranscript_022",
        "text": "WITNESS: I saw the gauntlets myself, at the trial of Marrow Kest. They "
                "did not belong to Ashvael by then — they had passed to his squire, "
                "a woman named Deira Thorne.",
        "source_doc": "Ephemera: Trial Transcript, Marrow Kest Hearing",
        "doc_type": "ephemera",
    },
    {
        "id": "codex_factions_0011",
        "text": "The Ember Concord was a military alliance formed after the War of Embers "
                "to prevent any single bearer of an ember-forged artifact from holding "
                "unchecked power again.",
        "source_doc": "Codex II: Factions and Alliances, Plate 11",
        "doc_type": "codex",
    },
    {
        "id": "wiki_deirathorne_002",
        "text": "Deira Thorne served as squire to Ashvael before his disappearance. "
                "Some wiki contributors argue she inherited the Cindered Accord "
                "afterward, though this conflicts with codex records.",
        "source_doc": "Wiki: Deira Thorne (character page)",
        "doc_type": "wiki",
    },
    {
        "id": "novel_ashfall_0090",
        "text": "Deira did not want the gauntlets. She had watched what they did to "
                "Ashvael, watched the ash creep into his veins until his own men no "
                "longer recognized his voice.",
        "source_doc": "Novel: The Ashfall Cycle, Book III",
        "doc_type": "novel",
    },
    {
        "id": "codex_geography_0007",
        "text": "The Salt Coast lies south of the Veyr provinces and was historically "
                "dependent on northern grain shipments, making it vulnerable to any "
                "disruption of the Veyr trade routes.",
        "source_doc": "Codex I: Geography and Provinces, Plate 7",
        "doc_type": "codex",
    },
    {
        "id": "ephemera_ledger_014",
        "text": "Grain shipment record, third winter post-Embers: Salt Coast granaries "
                "at less than one quarter capacity. Northern route unusable. "
                "Recommend rationing effective immediately.",
        "source_doc": "Ephemera: Merchant Ledger, Salt Coast Trading House",
        "doc_type": "ephemera",
    },
    {
        "id": "wiki_warofembers_004",
        "text": "The War of Embers was fought primarily over control of ember-forged "
                "artifacts, of which the Cindered Accord was the most powerful known "
                "example.",
        "source_doc": "Wiki: War of Embers (event page)",
        "doc_type": "wiki",
    },
    {
        "id": "novel_ashfall_0101",
        "text": "\"The Accord does not choose kindly,\" Marrow Kest said at his trial. "
                "\"Ask Ashvael, if you can find what is left of him to ask.\"",
        "source_doc": "Novel: The Ashfall Cycle, Book III",
        "doc_type": "novel",
    },
    {
        "id": "codex_artifacts_0046",
        "text": "No verified sighting of the Cindered Accord has been recorded since "
                "214 AE. Its current status is listed as 'lost' in official codex records.",
        "source_doc": "Codex III: Artifacts and Relics, Plate 46",
        "doc_type": "codex",
    },
]

if __name__ == "__main__":
    print(f"Loaded {len(SAMPLE_CHUNKS)} sample chunks")
    for c in SAMPLE_CHUNKS[:3]:
        print(f"- {c['id']} ({c['doc_type']}): {c['text'][:60]}...")