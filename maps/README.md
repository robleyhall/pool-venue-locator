# Pool Venue KML Maps

Generated from `../venues.json` by `../generate_kml.py`. Austin added October
24, 2026; other markets retain August 18, 2026 evidence dates. Review dates
are shown per placemark. All nine files use the same legend:

- **green:** verified serious room / anchor;
- **orange:** league or supporting room;
- **magenta:** regional tournament or major-event access;
- **gray:** lead requiring field verification; and
- **purple:** planned, not open.

Every placemark contains an address, evidence note, source link, and reminder to
reverify time-sensitive schedules. A coordinate locates the venue; it does not
verify that the venue is currently open.

## Files

- `austin-pool-venues.kml` — 12 venues; see [Austin evidence and coordinate notes](../docs/DATA.md)
- `las-vegas-pool-venues.kml`
- `phoenix-pool-venues.kml`
- `tucson-pool-venues.kml`
- `dallas-fort-worth-pool-venues.kml`
- `southern-new-hampshire-pool-venues.kml`
- `orlando-pool-venues.kml`
- `knoxville-east-tennessee-pool-venues.kml`
- `all-destinations-pool-venues.kml`

Google My Maps imports KML through **Create a new map → Add layer → Import**.
The composite is organized into one folder per market. Google Maps/My Maps may
re-style icons during import; the status is also preserved in each placemark's
`evidence_type` field and description.


Austin: ten pins are approximate Census street-address matches, two use venue-linked Google Maps coordinates. These are not verified entrances or driving-time boundaries.
