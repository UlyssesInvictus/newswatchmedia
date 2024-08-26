# NewsWatchMedia

Sorta scratch repo for handling NWM newsletter output

## How newsletters function

- Ongage pulls HTML directly from relevant pages
- Pages are stored in pages/ folder
- (Not all are used, Ongage will only pull specific ones)

## How to generate pages

- Update input.txt with following format:
  - Name of newsletter on its own line
  - CSV of url, title, summary for each news item below that
  - Repeat for each newsletter (still in input.txt)
- Run newsletter.py -f input.txt (in python 3)
- Upload to github
  - After a few minutes github will finish building new website
  - No other action in Ongage needed
