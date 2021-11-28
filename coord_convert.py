import sys
import csv
from pyproj import Proj, transform
import sys

vstupni_soubor = sys.argv[1] # načtu si vstupní soubor - argument je jméno souboru
lines = list()

with open(vstupni_soubor, 'r', encoding='utf-8') as csv_file_in:
  lines_reader = csv.reader(csv_file_in, delimiter=',')
  header = next(lines_reader) # do proměnné header mi uloží hlavičku a přeskočí ji, abych mohla pracovat se zbytkem souboru
  for line in lines_reader:
    lines.append(line)
vystupni_soubor = f"new_{sys.argv[1]}"
print(vystupni_soubor)

inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')

with open(vystupni_soubor, 'w', encoding='utf-8', newline='') as csv_file_out:
   lines_writer = csv.writer(csv_file_out, delimiter=',')
   header[0], header [1] = 'lon', 'lat'
   lines_writer.writerow (header)
   for line in lines:
       line[0], line[1]= transform(inProj,outProj,line[0],line[1])
       lines_writer.writerow(line)
