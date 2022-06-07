# Reduced IGRINS Files

Dates included: 20140707 - 20210530

## Description


## Header Description
- FILENAME: the name of the file that corresponds to the information in the rest of the row
- CIVIL: the date of observation (YYYYMMDD)
- JD: the julian date when the observation finished
- FILENUMBER: number of the file
- OBSTIME: time of observation
- GROUP1: observation ID, file number for the first frame in the ABBA sequence (can be incorrect)
- GROUP2: file number of the A0V star used in reduction (can be incorrect)
- OBJNAME: name of object observed (user input) from the recipe file
- OBJTYPE: the frame type, can be STD or TAR
- FRAMETYPE: A or B
- EXPTIME: exposure time (in seconds)
- ROTPA: rotation position angle (+- deg)
- AM: airmass at the end of the observation
- RA_2000: telescope right ascension converted into J2000 (+- deg)
- DEC_2000: telescope declination converted into J2000 (+- deg)
- BVC: barycentric velocity correction using [barycorrpy](https://github.com/shbhuk/barycorrpy) (km/s)
- FACILITY: telescope of observation
- PI: requester of observations, either name[s], program ID (for Gemini South), or "Unknown"
- SNRH: signal to noise ratio for the H band spectra
- SNRK: signal to noise ratio for the K band spectra
- NUMPAIRS: number of AB pairs that make up the reduced spectra
- FILES: file numbers used to create the reduced spectra
- URLS_H: the download URLs for the .variance and .spec_a0v H band files
- URLS_K: the download URLs for the .variance and .spec_a0v K band files
- NIGHT_URLS: the download URLs for the files that are generated once a night and used for the spectra reduction
  - .flat_off.fits
  - .flat_normed.fits
  - .flat_on.fits
  - a0v.db: a list of all the A0V standards used for spectra reduction
- OTHER_URLS: the download URLS for any other files used to reduce a specific file number or that are a product of the IGRINS PLP reduction
