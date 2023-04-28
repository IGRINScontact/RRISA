# Reduced IGRINS Files

Dates included: 20140707 - 20211231

## Description
All of the existing IGRINS data has been hand reduced using the ([IGRINS plp](https://github.com/igrins/plp)). The Reduced version of RRISA includes different names for targets than the Raw component. The names come from the recipe files that are used to reduce the raw data. Often these names have been corrected by hand for mistakes in the raw data object names. The original names for all of the targets remain for reference to the Raw component. If users find anything that appears to be a misidentification we ask that they report it by raising a GitHub issue. Additional information about data reduction is outlined on our [website](https://RRISA.github.io/).

_Note: The output files from the IGRINS PLP are an in vacuum wavelength solution. Fit models are offset from expected line positions by 80-120 km/s the models are likely in air and not vacuum. The IAU standard conversion for air to vacuum wavelengths is given by [Morton 1991](https://ui.adsabs.harvard.edu/abs/1991ApJS...77..119M/abstract). For vacuum wavelengths (VAC) in Angstroms and convert to air wavelength (AIR) via: AIR = VAC / (1.0 + 2.735182E-4 + (131.4182 / VAC^2) + (2.76249E8 / VAC^4))_


## Header Description
- NAME: the manually corrected name of the observed object ()
- OBJNAME_super: name of object observed (user input) from the RRISA raw file
- OBJNAME_recipe: name of object observed (user input) from the recipe file
- RA.2000: right ascension from the telescope converted into J2000 (+- deg)
- DEC.2000: declination from the telescope converted into J2000 (+- deg)
- FILENAME: the name of the file that corresponds to the information in the rest of the row
- FILES: file numbers used to create the reduced spectra
- SNRH: signal to noise ratio for the H band spectra
- SNRK: signal to noise ratio for the K band spectra
- URLS_H: the download URLs for the .variance and .spec_a0v H band files
- URLS_K: the download URLs for the .variance and .spec_a0v K band files
- CIVIL: the date of observation (YYYYMMDD)
- FILENUMBER: number of the file
- JD: the julian date when the observation finished
- OBJTYPE: the frame type, can be STD or TAR
- EXPTIME: exposure time (in seconds)
- ROTPA: rotation position angle (+- deg)
- AM: airmass at the end of the observation
- BVC: barycentric velocity correction using [barycorrpy](https://github.com/shbhuk/barycorrpy) (km/s)
- FACILITY: telescope of observation
- PI: requester of observations, either name[s], program ID (for Gemini South), or "Unknown"
- NIGHT_URLS: the download URLs for the files that are generated once a night and used for the spectra reduction
- OTHER_URLS: the download URLS for any other files used to reduce a specific file number or that are a product of the IGRINS PLP reduction
- PAPER_LOGS: the download URLs for any of the IGRINS paper logs that encompass the observation civil date.
