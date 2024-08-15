# Reduced IGRINS Files

Dates included: 20140707 - 20230507

## Description
All of the existing IGRINS data has been hand reduced using the [IGRINS plp v3](https://github.com/igrins/plp/releases/tag/v3.0.0) [(Kaplan+ 2024)](https://zenodo.org/records/11080095). The Reduced version of RRISA includes three names for each of the targets: the hand corrected name, the superlog name which can be used to link individual files from the Raw component of RRISA its reduced counterpart and the recipe name which is the name associated with the reduced file, usually manually input often given by the observer. The hand-corrected names were identified by manually searching through the IGRINS paper logs, through SIMBAD for nomenclature corrections, and by correcting telescope coordinate offsets. Targets that are subcomponents of systems or extended sources keep their identifier, and if not SIMBAD searchable, do not have any additional information added in the XMatch component of RRISA. If users find anything that appears to be a misidentification we ask that they report it by raising a [GitHub issue](https://github.com/IGRINScontact/RRISA/issues). Additional information about data reduction is outlined on our [website](https://igrinscontact.github.io/RRISA_reduced/).

_Note: The output files from the IGRINS PLP are an in vacuum wavelength solution. Fit models are offset from expected line positions by 80-120 km/s the models are likely in air and not vacuum. The IAU standard conversion for air to vacuum wavelengths is given by [Morton 1991](https://ui.adsabs.harvard.edu/abs/1991ApJS...77..119M/abstract). For vacuum wavelengths (VAC) in Angstroms and convert to air wavelength (AIR) via: AIR = VAC / (1.0 + 2.735182E-4 + (131.4182 / VAC^2) + (2.76249E8 / VAC^4))_


## Header Description
- NAME: the manually corrected name of the observed object (usually found through coordinate searches)
- OBJNAME_super: name of object observed (observer input) from the RRISA raw file
- OBJNAME_recipe: name of object observed (observer input) from the recipe file used to reduce the data
- CIVIL: the date of observation (YYYYMMDD)
- RA: the right ascention recorded by the telescope for the observation (in decimal degrees)
- DEC: the declination recorded by the telescope for the observation (in decimal degrees)
- FILENAME: name of the reduced file
- FILES: the target file numbers used in the reduction
- SNRH_pix: the signal-to-noise ratio in H-band per pixel
- SNRH_res: the signal-to-noise ratio in H-band per resolution element
- SNRK_pix: the signal-to-noise ratio in K-band per pixel
- SNRK_res: the signal-to-noise ratio in K-band per resolution element
- FILENUMBER: the reduced file number
- STANDARD: the file number of the standard used in the reduction
- JD: the julian date when the observation finished
- OBJTYPE: the frame type; can be STD or TAR
- EXPTIME: the exposure time of the frames (in seconds)
- ROTPA: the position angle of the slit
- AM: airmass at the end of the observation
- BVC: barycentric velocity correction using [barycorrpy](https://github.com/shbhuk/barycorrpy) (km/s)
- FACILITY: telescope of observation (McDonald, DCT, or Gemini South)
- PI: priciple investigator for the observations (who requested the observations); only avalible for McDonald and DCT Observations
- PROGID: Gemini South program ID
- FILE_URL: Link to download the H- and K-band files for a particular file number
- CAL_URL: Link to download the associated H- and K-band files used for file reduction
- RAW_URL: Link to access the raw data from the CIVIL using Box
