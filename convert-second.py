# Import Module
import pdftables_api

# API KEY VERIFICATION
conversion = pdftables_api.Client('ttqcmxp9i0ch')

# PDf to Excel
# (Hello.pdf, Hello)
conversion.csv("NORTHERN JUPITER LOAD SEQ SHEET.pdf", "first sheet.csv")
