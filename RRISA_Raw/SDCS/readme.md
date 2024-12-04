# Slit Camera Images from IGRINS

Dates included: 20140707 - 20230507

## Description
IGRINS uses a K-band engineering-grade slit-viewing camera for target acquisition (and guiding at McDonald Observatory and LDT). Slit-viewing camera images were not saved reliably until September of 2016 and not linked to raw .spec file numbers until March 2017. Any images taken before March 2017 can only be linked to raw IGRINS data by comparing the observation time in the headers of the .spec files and the SDCS files. The slit-viewing camera field-of-view changes depending on the telescope IGRINS is observing on: ~187 x 112 arcseconds at McDonald Observatory, ~117 x 70 arcseconds at LDT, ~70 x 40 arcseconds at Gemini South.

IGRINS simultaneously reads out both H and K Band spectra (SDCH & SDCK) meaning the file numbers for these files correspond to the same pointing.

_SDCS images can only be downloaded by night via link and not individually like reduced data products._

## Header Description
- FILENAME: name of the SDCS file (the filename does NOT correspond to H- and K-band .spec files)
- CIVIL: the date of observation (YYYYMMDD)
- FILENUMBER: the number in the filename
- ASSOC: the file number of the raw .spec file (in H- and K-band) that the slit camera image is associated with
- OBSTIME: the time the observation began
- EXPTIME: exposure time (in seconds)
- RA: the right ascention recorded by the telescope for the observation
- DEC: the declination recorded by the telescope for the observation
- AM: airmass at the end of the observation
- FACILITY: telescope of observation (McDonald, DCT, or Gemini South)
- RAW_URL: Link to access the raw data from the CIVIL using Box (the only place the slit camera images can be downloaded from)
