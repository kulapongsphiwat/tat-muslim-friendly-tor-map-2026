# TAT Muslim Friendly TOR Map 2026

Interactive Thailand map of 600 proposed Muslim Friendly venues for expert review and manual follow-up. The groups are research proposals, not confirmed certification decisions.

The initial data contains 250 พร้อมขาย, 162 พัฒนาเพื่อพร้อมขาย, and 188 มีศักยภาพ แต่ต้องพัฒนามาตรฐาน. There are 584 sourced venue coordinates. The other 16 entries are listed by province, pending coordinate confirmation. Mosques are included in แหล่งท่องเที่ยวทางประวัติศาสตร์และวัฒนธรรม.

## Update the map

1. Edit the first worksheet in `data/places.xlsx`. Keep separate columns named ชื่อแหล่ง, จังหวัด, กลุ่ม, ประเภท, and อัพเดตวันที่.
2. Upload the revised workbook to the same path on the main branch.
3. The Publish workflow rebuilds the map from Excel and deploys it to GitHub Pages.

Names and provinces join to `data/locations.json`, which holds the researched coordinates and source URLs. A new or renamed venue without a matching coordinate record remains unpinned until its coordinates are added. Never invent coordinates for an unmatched venue. Dates are read from Excel, not replaced with the website build time.

For local verification, run `python scripts/build_map.py` and open `site/index.html` in a browser. The builder uses Python's standard library and requires no package installation.

## Publishing

In repository Settings → Pages, select GitHub Actions as the publishing source, then run the Publish workflow. Only the generated `site` directory is deployed.

## Sources

Venue information and map coordinates: THIC, Makan Halal Guide, operator and tourism sources linked in the map, and OpenStreetMap contributors (ODbL). Province boundaries: Department of Disaster Prevention and Mitigation public ArcGIS service. D3 7.9.0 is distributed under the ISC license.

The map is a contractor research draft, not an official TAT certification or endorsement.
