# Maintaining the locator

1. Read current records before editing. Check for an existing venue/address.
2. Prefer venue, league operator and sanctioning-body sources. Label secondary leads.
3. Record table sizes separately from count and league format. Confirm time-sensitive details.
4. Include a review date and coordinate provenance for new/updated records.
5. Add a new market to `MARKETS` when necessary.
6. Run `python3 generate_kml.py` and `python3 validate.py`.
7. Update README market counts when adding/removing records, and commit data and KML together.

Include only public venue information. Do not include private account data,
credentials, personal addresses or individual travel and housing plans.
