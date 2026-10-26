# Pool Venue Locator

An evidence-backed pool venue directory with Google Earth and Google My Maps
KML exports. Includes 60 venues across eight US markets, with room roles,
table-size notes, addresses, source links and review dates.

## Use the maps

Download [all destinations](maps/all-destinations-pool-venues.kml), or choose a market:

| Market | Venues | KML |
|---|---:|---|
| Austin / Round Rock / Cedar Park | 12 | [Austin](maps/austin-pool-venues.kml) |
| Las Vegas | 5 | [Las Vegas](maps/las-vegas-pool-venues.kml) |
| Phoenix | 8 | [Phoenix](maps/phoenix-pool-venues.kml) |
| Tucson | 4 | [Tucson](maps/tucson-pool-venues.kml) |
| Dallas–Fort Worth | 8 | [DFW](maps/dallas-fort-worth-pool-venues.kml) |
| Southern New Hampshire / regional reach | 7 | [Southern NH](maps/southern-new-hampshire-pool-venues.kml) |
| Orlando | 6 | [Orlando](maps/orlando-pool-venues.kml) |
| Knoxville / East Tennessee | 10 | [Knoxville](maps/knoxville-east-tennessee-pool-venues.kml) |

Use the file's **Raw / Download** control on GitHub, then open/import the KML
in Google Earth. In Google My Maps, create a map, add a layer and import it.
The combined file groups venues by market. This project produces map files;
it does not require a hosted web application or API key.

Popups carry evidence and limitations. A pin is not proof that a room remains
open or that a league is running. Confirm schedules, equipment and availability
before travel. Austin was reviewed October 24, 2026; other markets retain
August 18, 2026 review dates. Ten Austin pins are approximate Census street-address
matches, while the two Shooters pins come from venue-linked map coordinates.

## Develop

Python 3.10 or newer; standard library only.

```sh
cd pool-venue-locator
python3 generate_kml.py
python3 validate.py
```

Edit `venues.json`, regenerate the KML files and commit data plus exports together.
GitHub Actions validates the dataset and checks that committed exports match the
generator. See [contributing](CONTRIBUTING.md), [data conventions](docs/DATA.md)
and [source provenance](docs/PROVENANCE.md).

## Layout

- `venues.json` — canonical venue records
- `generate_kml.py` — market definitions, marker styles and KML generator
- `maps/` — committed KML exports
- `validate.py` — schema, coordinates, uniqueness and export consistency checks
- `docs/` — evidence conventions and provenance
