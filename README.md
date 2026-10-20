# TAT Muslim Friendly TOR Map 2026

Interactive Thailand map of 600 proposed Muslim Friendly venues for expert review and manual follow-up. The groups are research proposals, not confirmed certification decisions.

The 21 October 2026 revision follows the ten routes in the supplied itinerary PDF, the team screening brief, and criteria report v7. It retains 284 of the previous candidates and adds 316 candidates. The workbook keeps removed entries and prior research in the audit and change-log sheets. Mosques and museums belong under แหล่งท่องเที่ยวทางประวัติศาสตร์และวัฒนธรรม, with their subtype retained.

The eight type targets are met exactly: accommodation 120, restaurants/cafes 150, wellness 40, shopping centres 25, communities 55, nature 70, history/culture 100, and activities 40. Coverage includes 25 provinces: 330 entries in the brief's main provinces, 86 in its secondary provinces, 120 in its potential provinces, 63 in additional route provinces/Khao Yai, and one retained GMHI listing in Udon Thani. Chiang Rai has 27, Ayutthaya 30, Kanchanaburi 24, Ratchaburi 24, and Phuket 31.

All 27 distinct businesses in gmhi.co's checked public register remain included. The register was refreshed on 21 October and still contained the same 29 listings before merging the Regent and Just Salt duplicate names. Register inclusion is separate from certificate validity and halal-food certification.

Proposed groups contain 130 พร้อมขาย, 108 พัฒนาเพื่อพร้อมขาย, and 362 มีศักยภาพ แต่ต้องพัฒนามาตรฐาน. These are research proposals. All final assessments remain pending the applicable mandatory conditions, evidence and scores. The brief's 250 is the number for TAT to select subsequently; it is not a forced number of confirmed ready-to-sell venues. The assessment sheet has separate human inputs and calculated results. It does not invent scores for missing evidence.

The earlier search evidence is retained. This revision searched 388 route and supplementary candidates, refreshed weaker matches, and consulted public tourism, operator and review pages. A matching name, recently crawled page or review listing does not establish current operation, channel ownership, certificate validity or full Muslim Friendly compliance. The route-source sheet records unresolved names and itinerary corrections, including the Al Meroz location, Khun Anan's restaurant classification and dates requiring confirmation. Unresolved coordinates stay unpinned; province-level indicators are labelled as unresolved, not exact venue locations.

## Update the map

1. Edit the first worksheet in `data/places.xlsx`. Keep separate columns named ชื่อแหล่ง, จังหวัด, กลุ่ม, ประเภท, อัพเดตวันที่, and รหัส. Preserve stable IDs. The route, day, subtype and assessment columns support the ten-route review. Groups in the main sheet remain proposals; the separate calculated assessment result must be confirmed by the review team.
2. Upload the revised workbook to the same path on the main branch.
3. The Publish workflow rebuilds the map from Excel and deploys it to GitHub Pages.

Stable IDs join to `data/locations.json`, which holds researched coordinates and source URLs. The builder also reads GPS coordinates from the evidence sheet by the รหัส, ละติจูด and ลองจิจูด headers; these Excel coordinates override the sidecar. Clearing those coordinate fields leaves a venue unpinned. A new venue can be mapped by adding its stable ID and verified coordinates there. Dates are read from Excel, not replaced with build time.

The builder also reads the online review worksheet by its column headers. Editing social/review links, source counts, notes, the review date, or ผลทบทวนการเปิด in Excel updates those fields on the map after upload. Keep the original headers. Blank/unconfirmed human-review fields retain the research status. `data/revalidation.json` holds the supplementary GMHI and certificate metadata; it is not a substitute for current operator confirmation.

For local verification, run `python scripts/build_map.py` and open `site/index.html` in a browser. The builder uses Python's standard library and requires no package installation.

## Publishing

In repository Settings → Pages, select GitHub Actions as the publishing source, then run the Publish workflow. Only the generated `site` directory is deployed.

## Sources

Venue information and map coordinates: THIC, Makan Halal Guide, operator and tourism sources linked in the map, and OpenStreetMap contributors (ODbL). Province boundaries: Department of Disaster Prevention and Mitigation public ArcGIS service. D3 7.9.0 is distributed under the ISC license.

The map is a contractor research draft, not an official TAT certification or endorsement.
