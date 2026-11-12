# Xmas-Adventure: Little Elf's Xmas Adventures

Xmas Adventures in the South Bay: an interactive map for a toddler.

A storybook, toddler-friendly Christmas map of the South Bay (Mountain View to Gilroy) for the 2026 holiday season. It shows 10 kid-appropriate events on a snowy red, white and green map.

**Live map:** https://kamilkolacek.github.io/Xmas-Adventure/

## Features

- 10 holiday events with dates, cost, address, toddler tips, directions and links to the official event pages
- Chunky 3D storybook pins that wiggle and jingle when tapped
- Santa's sleigh and reindeer that fly across the map when you tap an event
- "X sleeps until Christmas" countdown (Pacific time)
- Sticker book: tap "We went!" to collect a sticker for each event (saved in your browser)
- Chiptune versions of public-domain carols (Jingle Bells, Deck the Halls, We Wish You a Merry Christmas) made with the Web Audio API
- Falling snow, a free-events filter and a hide-past-events filter
- Works on phones: the event list becomes a bottom sheet

## The 10 events (2026)

| City | Event | When |
|---|---|---|
| Mountain View | Community Tree Lighting | Mon, Dec 7, 5:30–8 pm |
| Santa Clara | Holiday Tree Lighting | Fri, Dec 4, 5:30–8 pm |
| San Jose | Christmas in the Park | Nov 27 – Jan 1, daily noon–10 pm |
| San Jose | San Jose Holiday Lights | Nov 13 – Jan 1, daily 4:30–10:30 pm |
| San Jose | My Very First Nutcracker | Dec 20, 22, 23 & 27, 11 am |
| Campbell | Carol of Lights | Sat, Dec 5 |
| Los Gatos | Children's Christmas/Holidays Parade | Sat, Dec 5, 11 am |
| Los Gatos | Fantasy of Lights Walk-thru | Dec 5–6 & 12–13, 4–9 pm |
| Los Gatos | Billy Jones Holiday Train | Dec 14–23 & 26–27, 6–9 pm |
| Gilroy | North Pole Nights at Gilroy Gardens | Select dates, Nov 21 – Dec 31 |

Dates were checked against each event's official page on November 12, 2026. Events change, so check the official page before you go.

## Project layout

```
index.html            The finished, self-contained page (open it directly or via GitHub Pages)
src/template.html     Editable page: layout, styles, icons, music, sleigh animation
src/data.js           Packed map data: events, roads, water, highway labels, decorations
src/leaflet.css       Leaflet 1.9.4 stylesheet (inlined into index.html at build time)
src/build.py          Rebuilds index.html from the three files above
data/events.json      The 10 events (human-editable)
data/events_geo.json  The same events with map coordinates
```

To change something, edit `src/template.html`, then run `python3 src/build.py`.

To change an event, edit `data/events_geo.json`, copy it into the `EVENTS=` line of `src/data.js`, then rebuild.

## Credits

- Map library: [Leaflet](https://leafletjs.com/) 1.9.4 (BSD 2-Clause), loaded from cdnjs
- Roads and water: U.S. Census Bureau TIGER/Line via TIGERweb (public domain)
- Geocoding: U.S. Census Geocoder and OpenStreetMap Nominatim (© OpenStreetMap contributors)
- Fonts: Mountains of Christmas and Baloo 2 via Google Fonts (SIL Open Font License)
- Carols: traditional and public-domain melodies, arranged as chiptune
- Icons, pins, sleigh and logo: original SVG artwork drawn for this project

Event information comes from the organizers' official pages, which are linked in each event card.

## License

MIT. See [LICENSE](LICENSE).
