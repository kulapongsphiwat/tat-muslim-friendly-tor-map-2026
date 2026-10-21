# TAT Muslim Friendly TOR Map 2026

Interactive Thailand map of 600 proposed Muslim Friendly venues for expert review and manual follow-up. The groups are research proposals, not confirmed certification decisions.

The 21 October 2026 revision follows the ten routes in the supplied itinerary PDF, the team screening brief, and criteria report v7. A further location review corrected branch and publisher-office coordinates and replaced seven unclear entries with candidates of the same type. The workbook keeps removed entries and prior research in the audit and change-log sheets. Mosques and museums belong under แหล่งท่องเที่ยวทางประวัติศาสตร์และวัฒนธรรม, with their subtype retained.

The eight type targets are met exactly: accommodation 120, restaurants/cafes 150, wellness 40, shopping centres 25, communities 55, nature 70, history/culture 100, and activities 40. Coverage includes 25 provinces. Chiang Rai has 27, Ayutthaya 32, Kanchanaburi 24, Ratchaburi 24, Phuket 31, and Khao Yai–Pak Chong 11. Other locations in Nakhon Ratchasima are labelled separately from Khao Yai.

All 27 distinct businesses in gmhi.co's checked public register remain included. The register was refreshed on 21 October and still contained the same 29 listings before merging the Regent and Just Salt duplicate names. Register inclusion is separate from certificate validity and halal-food certification.

Proposed groups contain **250 พร้อมขาย**, **51 พัฒนาเพื่อพร้อมขาย**, and **299 มีศักยภาพ แต่ต้องพัฒนามาตรฐาน**, following the user's request for 250 proposed ready-to-sell places. All 600 final assessments remain pending the applicable mandatory conditions, evidence and scores. The assessment sheet has separate human inputs and calculated results; missing evidence has no invented score.

Of the 250 proposed ready places, **213 (85.2%)** fall within the planning corridor of all ten routes and 37 are outside it. A corridor place must be in the same province as a named stop in the supplied PDF and no more than **25 km in a straight line** from it. The workbook gives the reference stop and distance per row. This is a transparent research assumption, not road distance, a driving-time check, or an approved itinerary. Route province membership alone is not counted. Evidence ordering prioritizes prior Muslim-service information, GMHI register membership, prayer information, named route stops and relevant halal-food information; it is not a v7 assessment score. Broad area-only or unresolved service-premises points are excluded from the ready shortlist where identified.

The earlier search evidence is retained, with further venue searches, operator channels, review profiles and location-source checks. A matching name, recently crawled page or review listing does not establish current operation, channel ownership, certificate validity or full Muslim Friendly compliance. No business has been contacted by this research process. Current opening status remains subject to manual confirmation. A temporarily closed replacement candidate was not selected.

All 600 selected records now have a source-linked venue or geographic-feature coordinate. These are not surveyed locations: natural sites and communities can be feature/area reference points, and two registered entities can share premises. The map and workbook label those scopes. Province-centre question-mark markers have been removed; no unknown venue is represented by a province centroid. The `พิกัดและชุด 250` sheet records coordinate provenance, earlier coordinates, conflicting points not used, shortlist rationale and route distances. THE TREE Sleep and Space in Trang is matched to the GMHI record named “The Three Sleep” using address and public profile details; the register's original name remains in the register sheet.

## Update the map

1. Edit the first worksheet in `data/places.xlsx`. Keep separate columns named ชื่อแหล่ง, จังหวัด, กลุ่ม, ประเภท, อัพเดตวันที่, and รหัส. Preserve stable IDs. The route, day, subtype and assessment columns support the ten-route review. Groups in the main sheet remain proposals; the separate calculated assessment result must be confirmed by the review team.
2. Upload the revised workbook to the same path on the main branch.
3. The Publish workflow rebuilds the map from Excel and deploys it to GitHub Pages.

Stable IDs join to `data/locations.json`, which holds researched coordinates and source URLs. The builder also reads GPS coordinates from the evidence sheet by the รหัส, ละติจูด and ลองจิจูด headers; these Excel coordinates override the sidecar. Clearing those coordinate fields leaves a venue unpinned, listed as unresolved without a province-centre marker. A new venue can be mapped by adding its stable ID and verified coordinates there. Dates are read from Excel, not replaced with build time. The main sheet's new corridor, PDF anchor, distance, location scope, proposal rationale and coordinate-source columns also update the map. Recheck corridor membership and distances after changing a location; the builder does not calculate road routes.

The builder also reads the online review worksheet by its column headers. Editing social/review links, source counts, notes, the review date, or ผลทบทวนการเปิด in Excel updates those fields on the map after upload. Keep the original headers. Blank/unconfirmed human-review fields retain the research status. `data/revalidation.json` holds the supplementary GMHI and certificate metadata; it is not a substitute for current operator confirmation.

For local verification, run `python scripts/build_map.py` and open `site/index.html` in a browser. The builder uses Python's standard library and requires no package installation.

## Publishing

In repository Settings → Pages, select GitHub Actions as the publishing source, then run the Publish workflow. Only the generated `site` directory is deployed.

## Sources

Venue information and map coordinates: THIC, Makan Halal Guide, operator and tourism sources linked in the map, and OpenStreetMap contributors (ODbL). Province boundaries: Department of Disaster Prevention and Mitigation public ArcGIS service. D3 7.9.0 is distributed under the ISC license.

The map is a contractor research draft, not an official TAT certification or endorsement.
