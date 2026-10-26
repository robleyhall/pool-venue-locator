# Pool Venue Locator

An evidence-backed pool venue directory with Google Earth and Google My Maps
KML exports. Includes 75 venues across ten US markets, with room roles,
table-size notes, addresses, source links and review dates.

## Use the maps

Download [all destinations](maps/all-destinations-pool-venues.kml), or choose a market:

| Market | Venues | Date refreshed | KML |
|---|---:|---|---|
| Austin / Round Rock / Cedar Park | 12 | 2026-10-24 | [Austin](maps/austin-pool-venues.kml) |
| Las Vegas | 7 | 2026-10-26 | [Las Vegas](maps/las-vegas-pool-venues.kml) |
| Phoenix | 8 | 2026-08-18 | [Phoenix](maps/phoenix-pool-venues.kml) |
| Tucson | 4 | 2026-08-18 | [Tucson](maps/tucson-pool-venues.kml) |
| Dallas–Fort Worth | 8 | 2026-08-18 | [DFW](maps/dallas-fort-worth-pool-venues.kml) |
| Southern New Hampshire / regional reach (including Portland, ME) | 9 | 2026-10-26 | [Southern NH](maps/southern-new-hampshire-pool-venues.kml) |
| Orlando | 6 | 2026-08-18 | [Orlando](maps/orlando-pool-venues.kml) |
| Knoxville / East Tennessee | 10 | 2026-08-18 | [Knoxville](maps/knoxville-east-tennessee-pool-venues.kml) |
| Colorado (Front Range trip) | 9 | 2026-10-26 | [Colorado](maps/colorado-pool-venues.kml) |
| Taos, New Mexico | 2 | 2026-10-26 | [Taos](maps/taos-pool-venues.kml) |

Follow [How to load the maps into Google Earth](docs/GOOGLE_EARTH.md) for
step-by-step browser and desktop instructions, saving maps and troubleshooting.
In Google My Maps, create a map, add a layer and import it.
The combined file groups venues by market. This project produces map files;
it does not require a hosted web application or API key.

Each market's latest refresh date is listed above. Venue popups include source
links, review dates and equipment notes. Confirm schedules and availability
before travel.

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
