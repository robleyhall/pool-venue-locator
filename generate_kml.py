#!/usr/bin/env python3
"""Generate market and composite KML files from venues.json."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENUES = json.loads((ROOT / "venues.json").read_text(encoding="utf-8"))
OUT = ROOT / "maps"

MARKETS = {
    "austin": "Austin / Round Rock / Cedar Park",
    "las-vegas": "Las Vegas",
    "phoenix": "Phoenix",
    "tucson": "Tucson",
    "dallas-fort-worth": "Dallas–Fort Worth",
    "southern-new-hampshire": "Southern New Hampshire / Regional Reach",
    "orlando": "Orlando",
    "knoxville-east-tennessee": "Knoxville / East Tennessee",
}

STYLES = {
    "serious": ("Serious room / anchor", "ff2e8b57", "1.15"),
    "support": ("League or supporting room", "ffffa500", "1.05"),
    "event": ("Regional or major-event access", "ffff00ff", "1.05"),
    "lead": ("Lead — field verification required", "ff999999", "1.0"),
    "planned": ("Planned — not open", "ff800080", "1.05"),
}


def style_xml() -> str:
    chunks = []
    for key, (_, color, scale) in STYLES.items():
        chunks.append(
            f"""  <Style id="{key}">
    <IconStyle><color>{color}</color><scale>{scale}</scale>
      <Icon><href>https://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href></Icon>
    </IconStyle>
    <LabelStyle><scale>0.85</scale></LabelStyle>
  </Style>"""
        )
    return "\n".join(chunks)


def placemark(v: dict) -> str:
    label = STYLES[v["type"]][0]
    description = (
        f"<b>Status:</b> {html.escape(label)}<br/>"
        f"<b>Address:</b> {html.escape(v['address'])}<br/><br/>"
        f"{html.escape(v['note'])}<br/><br/>"
        f"<a href=\"{html.escape(v['url'], quote=True)}\">Website/Source</a><br/>"
        f"Reviewed {html.escape(v.get('reviewed', '2026-08-18'))}."
        + (f"<br/><b>Coordinates:</b> {html.escape(v['coordinate_source'])}. {html.escape(v['coordinate_note'])}" if v.get("coordinate_source") else "")
    )
    return f"""    <Placemark>
      <name>{html.escape(v['name'])}</name>
      <styleUrl>#{v['type']}</styleUrl>
      <description><![CDATA[{description}]]></description>
      <ExtendedData>
        <Data name="market"><value>{html.escape(MARKETS[v['market']])}</value></Data>
        <Data name="evidence_type"><value>{html.escape(v['type'])}</value></Data>
        <Data name="address"><value>{html.escape(v['address'])}</value></Data>
      </ExtendedData>
      <Point><coordinates>{v['lon']},{v['lat']},0</coordinates></Point>
    </Placemark>"""


def market_refreshed(key: str) -> str:
    """Latest evidence update in a market, not a full-market recheck."""
    return max(v.get("reviewed", "2026-08-18") for v in VENUES if v["market"] == key)


def document(name: str, folders: list[str]) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
  <name>{html.escape(name)}</name>
  <description>Pool venues, league hosts, event campuses, and verification leads. Date refreshed is shown in each market folder; venue popups include sources, review dates and equipment notes.</description>
{style_xml()}
{''.join(folders)}
</Document>
</kml>
"""


def folder(key: str, venues: list[dict]) -> str:
    body = "\n".join(placemark(v) for v in venues)
    return f"""  <Folder>
    <name>{html.escape(MARKETS[key])}</name>
    <description>Date refreshed: {market_refreshed(key)}. Individual venue review dates are shown in popups.</description>
{body}
  </Folder>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    composite_folders = []
    for key, title in MARKETS.items():
        market_venues = [v for v in VENUES if v["market"] == key]
        market_folder = folder(key, market_venues)
        (OUT / f"{key}-pool-venues.kml").write_text(
            document(f"{title} Pool Venues", [market_folder]), encoding="utf-8"
        )
        composite_folders.append(market_folder)
    (OUT / "all-destinations-pool-venues.kml").write_text(
        document("All Destination Pool Venues", composite_folders), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
