# TAT Muslim Friendly TOR Map 2026

Interactive Thailand map of 600 proposed Muslim Friendly venues for expert review and manual follow-up. The groups are research proposals, not confirmed certification decisions.

The proposed groups contain 250 พร้อมขาย, 162 พัฒนาเพื่อพร้อมขาย, and 188 มีศักยภาพ แต่ต้องพัฒนามาตรฐาน. The dashboard shows counts by group, type and province, with Phuket and Khao Yai–Pak Chong shortcuts. Unresolved coordinates remain unpinned. Mosques are included in แหล่งท่องเที่ยวทางประวัติศาสตร์และวัฒนธรรม.

The 20 October 2026 research revision includes all 27 distinct businesses in gmhi.co's public register (29 names before merging the Regent and Just Salt duplicates). It adds 24 businesses, merges four duplicate physical premises, and moves 20 lower-priority or unresolved entries to the reserve list. Phuket has 17 entries. The workbook preserves all original 600 entries plus the 24 additions in the online review tab, with a separate change log.

Searches were run for every original entry and every addition. Matching names and locations were screened conservatively; social and review links remain candidates for branch and owner confirmation. A recently crawled page does not establish recent business activity or current operation. Missing search results do not establish closure or absence of social media. GMHI ratings, certificate labels, certificate images and halal-food certificates are separate evidence. The workbook flags certificate-name and star discrepancies instead of silently treating them as confirmed.

## Update the map

1. Edit the first worksheet in `data/places.xlsx`. Keep separate columns named ชื่อแหล่ง, จังหวัด, กลุ่ม, ประเภท, อัพเดตวันที่, and รหัส. Preserve existing stable IDs; assign unique IDs to new venues.
2. Upload the revised workbook to the same path on the main branch.
3. The Publish workflow rebuilds the map from Excel and deploys it to GitHub Pages.

Stable IDs join to `data/locations.json`, which holds researched coordinates and source URLs. Workbooks without IDs can still join by exact name and province. A new venue without a matching coordinate record remains unpinned until its coordinates are added. Never invent coordinates for an unmatched venue. Dates are read from Excel, not replaced with the website build time.

The builder also reads the online review worksheet by its column headers. Editing social/review links, source counts, notes, the review date, or ผลทบทวนการเปิด in Excel updates those fields on the map after upload. Keep the original headers. Blank/unconfirmed human-review fields retain the research status. `data/revalidation.json` holds the supplementary GMHI and certificate metadata; it is not a substitute for current operator confirmation.

For local verification, run `python scripts/build_map.py` and open `site/index.html` in a browser. The builder uses Python's standard library and requires no package installation.

## Publishing

In repository Settings → Pages, select GitHub Actions as the publishing source, then run the Publish workflow. Only the generated `site` directory is deployed.

## Sources

Venue information and map coordinates: THIC, Makan Halal Guide, operator and tourism sources linked in the map, and OpenStreetMap contributors (ODbL). Province boundaries: Department of Disaster Prevention and Mitigation public ArcGIS service. D3 7.9.0 is distributed under the ISC license.

The map is a contractor research draft, not an official TAT certification or endorsement.
