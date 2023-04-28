# Cross-Matched Reduced IGRINS Files

Dates included: 20140707 - 20211231

## Description

For objects in the IGRINS sample that are searchable via SIMBAD, we can crossmatch with other catalogs to provide additional information. In the beta version of RRISA we support crossmatching with 2MASS, APOGEE, Gaia EDR3, Gaia DR2, and PASTEL.

The XMatch version of RRISA includes different names for targets than the Raw and Reduced components. The new names have been painstakingly corrected by manually searching through the IGRINS paper logs, through SIMBAD for nomenclature corrections, and by correcting telescope coordinate offsets. Targets that are subcomponents of systems or extended sources keep their identifier, and if not SIMBAD searchable, do not have any additional information added in the XMatch component of RRISA. The names from the Reduced component of RRISA remain for reference. If users find anything that appears to be a misidentification we ask that they report it by raising a GitHub issue.

A detailed description of object matching can be found on our [website](https://RRISA.github.io/).

_Note: The output files from the IGRINS PLP are an in vacuum wavelength solution. If fit models are offset from expected line positions by 80-120 km/s, the models are likely in air and not vacuum. The IAU standard conversion for air to vacuum wavelengths is given by [Morton 1991](https://ui.adsabs.harvard.edu/abs/1991ApJS...77..119M/abstract). For vacuum wavelengths (VAC) in Angstroms and convert to air wavelength (AIR) via: AIR = VAC / (1.0 + 2.735182E-4 + (131.4182 / VAC^2) + (2.76249E8 / VAC^4))_

## Header Description
- NAME: the manually corrected name of the observed object
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
- BVC: barycentric velocity correction using [barycorrpy](https://github.com/shbhuk/barycorrpy) (km/s)
- FACILITY: telescope of observation
- NIGHT_URLS: the download URLs for the files that are generated once a night and used for the spectra reduction
- OTHER_URLS: the download URLS for any other files used to reduce a specific file number or that are a product of the IGRINS PLP reduction
- PAPER_LOGS: the download URLs for any of the IGRINS paper logs that encompass the observation civil date.
- MAIN_ID: the primary SIMBAD identifier
- RA_s: right ascension from SIMBAD
- DEC_s: the declination from SIMBAD
- IDS: all of the object names in SIMBAD associated with the object
- OTYPE: SIMBAD [object type](https://simbad.u-strasbg.fr/simbad/sim-display?data=otypes)
- SP_TYPE: SIMBAD spectral type
- SP_QUAL: SIMBAD spectral type quality A->E (best->worst)
- PMRA: SIMBAD RA propermotion
- PMDEC: SIMBAD DEC propermotion  
- RV_VALUE: the radial velocity value from SIMBAD
- PLX_VALUE: the parallax value from SIMBAD
- FLUX_ : the SIMBAD magnitude for U, B, V, R, G, I, J, H, or K filters
- Teff: the effective temperature from SIMBAD
- logg: the surface gravity from SIMBAD
- Fe/H: the metallicity from SIMBAD
- 2MASS_ID: the 2MASS identifier
- 2MASS_J: 2MASS J band magnitude
- 2MASS_H: 2MASS H band magnitude
- 2MASS_K: 2MASS K band magnitude
- 2MASS_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
- GaiaDR2_source: the Gaia DR2 identifier
- GaiaDR2_plx: the Gaia DR2 parallax
- GaiaDR2_pmra: the Gaia DR2 RA proper motion
- GaiaDR2_pmdec: the Gaia DR2 DEC proper motion
- GaiaDR2_gmag: the G magnitude from Gaia DR2 photometry
- GaiaDR2_bprp: the difference in the filters from Gaia DR2 photometry
- GaiaDR2_ebprp: the bp-rp excess factor from the Gaia DR2 photometry
- GaiaDR2_rv: the radial velocity estimate from Gaia DR2
- GaiaDR2_teff: the effective temperature estimate from Gaia DR2
- GaiaDR2_ag: the estimate of extinction in the G band from Apsis-Priam
- GaiaDR2_radius: the radius estimate from Gaia DR2
- GaiaDR2_luminosity: the luminosity estimate from Gaia DR2
- GaiaDR2_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
- GaiaEDR3_source: the Gaia EDR3 identifier
- GaiaEDR3_parallax: the Gaia EDR3 parallax
- GaiaEDR3_bprp: the difference in the filters from Gaia EDR3 photometry
- GaiaEDR3_ebprp: the bp-rp excess factor from the Gaia EDR3 photometry
- GaiaEDR3_gmag: the G magnitude from the Gaia EDR3 photometry
- GaiaEDR3_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
- APOGEE2_HRV: the radial velocity estimate from APOGEE
- APOGEE2_teff: the effective temperature estimate from APOGEE
- APOGEE2_logg: the surface gravity estimate from APOGEE
- APOGEE2_Vsini: the vsini estimate from APOGEE
- APOGEE2_[M/H]: the metals over hydrogen value from APOGEE
- APOGEE2_[a/H]: the alpha elements over hydrogen value from APOGEE
- APOGEE2_[Fe/H]: the metallicity value from APOGEE
- PASTEL_Teff: the effective temperature from PASTEL
- PASTEL_logg: the surface gravity from PASTEL
- PASTEL_[Fe/H]: the metallicity value from PASTEL
- PASTEL_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
