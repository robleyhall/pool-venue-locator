# How to load the maps into Google Earth

Use Google Earth in a browser or Google Earth Pro on your computer. The KML
exports are ready to use; you do not need Python or an API key.

## 1. Download a map

1. Choose a market from the [project's map list](../README.md#use-the-maps),
   or download [all destinations](../maps/all-destinations-pool-venues.kml).
2. On GitHub's file page, use **Download raw file**. If you open **Raw** instead,
   save that raw content with its original `.kml` filename. Do not save the
   GitHub webpage as HTML.
3. Keep the file somewhere easy to find, such as Downloads. If you already have
   a local copy of this repository, use the files in `maps/` directly.

Start with one market for a closer view. The combined file contains the same
venues, grouped into market folders; loading both can show duplicate pins.

## 2. Open in Google Earth on the web

### Quick viewing without signing in

1. Open [Google Earth](https://earth.google.com/web/).
2. On the home screen, select **Open local KML editor** at the bottom left.
3. Select **Open KML from device**, then choose your downloaded `.kml` file.

Local KML files are device-local, not saved as Google Drive projects. Keep your
download; explicitly save or download any edits you want to retain.

### Save as a Google Drive project

1. Open [Google Earth](https://earth.google.com/web/) and sign in.
2. From the home screen, select **New → Import file to project → Upload from device**.
3. Choose the `.kml` file. If asked for an output type, choose
   **Import as project features**. Earth creates a project saved in Google Drive.

For an existing project, open it first, then use **File → Import file to
{Project name} → Upload from device**.

These web steps follow Google's [import documentation](https://developers.google.com/maps/documentation/earth/import-data),
checked October 26, 2026. Menu labels may change.

## 3. Open in Google Earth Pro on desktop

1. Launch Google Earth Pro on your Mac or Windows computer.
2. Select **File → Open**, choose the downloaded `.kml` file and open it.
3. Find the imported folder under **Temporary Places** in the Places panel.
   Enable its checkbox and expand it to see markets and venues.
4. Double-click a venue in the list to zoom to it; click its pin to read its notes.
5. To retain the imported map, drag its folder from **Temporary Places** into
   **My Places**, then select **File → Save → Save My Places**.

Google documents the desktop import and saving controls in
[Import & change map data](https://support.google.com/earth/answer/176685?hl=en).

## Read the venue information

Expand a market folder and select a venue. Its popup includes the address,
evidence notes, source link and review date. See the [marker color legend](../maps/README.md).
Check the notes even when a marker's color or icon looks different after import.
Pins do not establish current opening hours, league schedules or equipment;
confirm those details with the linked sources before travel.

## Updates and troubleshooting

- **New data is available:** download the latest KML and import it again. These
  exports are snapshots and do not automatically update in Earth. Hide or remove
  the previous imported copy to avoid duplicates; save any personal edits first.
- **Earth rejects the file:** confirm the filename ends in `.kml`, not `.html`
  or `.kml.txt`. Download the raw file again. Renaming an HTML page does not turn
  it into KML.
- **No pins are visible:** enable the imported folder or features, expand the
  market list and select a venue to zoom to its location. The combined map spans
  several states, so pins may be far from your current view.
- **Pins appear twice:** hide or remove the older import, or use either the
  combined file or individual markets without overlapping them.
- **Web styling or popups look incomplete:** try the same file in Earth Pro.
  Google Earth versions support different subsets of KML; Google's
  [import documentation](https://developers.google.com/maps/documentation/earth/import-data)
  links to current compatibility guidance.
