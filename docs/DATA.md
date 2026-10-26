# Data and evidence conventions

`venues.json` is a JSON array. Each venue requires:

| Field | Meaning |
|---|---|
| `market` | Key in `MARKETS` in the generator |
| `name`, `address` | Venue identity and street address |
| `lon`, `lat` | WGS84 decimal degrees; KML uses longitude first |
| `type` | `serious`, `support`, `event`, `lead`, or `planned` |
| `note` | Published inventory/activity and explicit uncertainties |
| `url` | Primary evidence or clearly identified lead |
| `reviewed` | ISO review date; legacy records default to 2026-08-18 |
| `coordinate_source`, `coordinate_note` | Optional coordinate provenance and limits; supply together |

`serious` identifies an anchor, `support` a secondary or league room, `event`
a regional/event campus, `lead` a venue needing verification and `planned`
a room not yet open. These classifications are editorial research labels,
not guarantees or confidence scores. Venue availability and league availability
are separate claims. A nine-foot inventory does not prove a nine-foot league.

Austin's October 24 review uses official venue/league sources linked in records.
Ten Austin coordinates came from successful Census Geocoder Public_AR_Current
street-address matches; these locate an approximate road address, not a building
entrance. Suite numbers are retained in addresses but omitted from geocoding.
Shooters' two coordinates come from official venue directions links.
Mayfield's and Stardust addresses carry forward September research and are
explicitly marked as not independently reverified in the October review.

Other markets were not refreshed during the Austin update. Keep historical review
dates when changing formatting or regenerating exports. Record closure evidence
and uncertainty rather than silently treating a removed room as never researched.
