#!/usr/bin/env python3
"""Validate source records and ensure committed KML matches generated output."""
import datetime
import json
import math
from pathlib import Path
import tempfile
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import generate_kml as generator

ROOT = Path(__file__).resolve().parent
NS = {'k': 'http://www.opengis.net/kml/2.2'}


def validate():
    venues = json.loads((ROOT / 'venues.json').read_text())
    assert isinstance(venues, list) and venues, 'Expected a nonempty venue array'
    seen = set()
    for venue in venues:
        for field in ('market', 'name', 'address', 'type', 'note', 'url'):
            assert isinstance(venue.get(field), str) and venue[field].strip(), f'Missing {field}: {venue}'
        assert venue['market'] in generator.MARKETS, f'Unknown market: {venue}'
        assert venue['type'] in generator.STYLES, f'Unknown type: {venue}'
        key = (venue['market'], venue['name'].casefold(), venue['address'].casefold())
        assert key not in seen, f'Duplicate venue: {key}'
        seen.add(key)
        for axis, bound in [('lon', 180), ('lat', 90)]:
            value = venue.get(axis)
            assert type(value) in (int, float) and math.isfinite(value) and -bound <= value <= bound, f'Invalid {axis}: {venue}'
        parsed = urlparse(venue['url'])
        assert parsed.scheme in ('http', 'https') and parsed.netloc, f'Invalid source URL: {venue}'
        datetime.date.fromisoformat(venue.get('reviewed', '2026-08-18'))
        assert bool(venue.get('coordinate_source')) == bool(venue.get('coordinate_note')), f'Incomplete coordinate provenance: {venue}'
    with tempfile.TemporaryDirectory() as temporary:
        generator.OUT = Path(temporary)
        generator.main()
        generated = sorted(generator.OUT.glob('*.kml'))
        assert {p.name for p in generated} == {p.name for p in (ROOT / 'maps').glob('*.kml')}, 'Missing or obsolete map files'
        for output in generated:
            committed = ROOT / 'maps' / output.name
            assert output.read_bytes() == committed.read_bytes(), f'Stale export: {output.name}; run python3 generate_kml.py'
            tree = ET.parse(committed)
            marks = tree.findall('.//k:Placemark', NS)
            expected = venues if output.name.startswith('all-destinations') else [v for v in venues if v['market'] == output.name.removesuffix('-pool-venues.kml')]
            assert len(marks) == len(expected), f'Wrong placemark count: {output.name}'
            for mark in marks:
                assert mark.find('k:name', NS).text
                assert mark.find('k:description', NS).text
                assert mark.find('k:styleUrl', NS).text[1:] in generator.STYLES
    print(f'Validated {len(venues)} venues, {len(generator.MARKETS)} markets and {len(generated)} KML files.')


if __name__ == '__main__':
    validate()
