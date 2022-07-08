import tabula

# firstMethod
tables = tabula.read_pdf("NORTHERN JUPITER LOAD SEQ SHEET.pdf", pages="all")

#tabula.convert_into("NORTHERN JUPITER LOAD SEQ SHEET.pdf", "SecondPage.csv", format="csv", pages="all")

tables
