# Cross-Matched Reduced IGRINS Files

Dates included: 20140707 - 20230507

## Description

For objects in the IGRINS sample that are searchable via SIMBAD, we can crossmatch with other catalogs to provide additional information. In version 3 of RRISA we support crossmatching with 2MASS, APOGEE-2 DR 17, Gaia DR3, and PASTEL.

The XMatch version of RRISA has the same names as the Reduced component including the hand corrected names. The hand-corrected names were identified by manually searching through the IGRINS paper logs, through SIMBAD for nomenclature corrections, and by correcting telescope coordinate offsets. Targets that are subcomponents of systems or extended sources keep their identifier, and if not SIMBAD searchable, do not have any additional information added in the XMatch component of RRISA. If users find anything that appears to be a misidentification we ask that they report it by raising a [GitHub issue](https://github.com/IGRINScontact/RRISA/issues). Additional information about data reduction is outlined on our [website](https://igrinscontact.github.io/RRISA_reduced/).

A detailed description of object matching can be found on our [website](https://igrinscontact.github.io/RRISA_xmatch/).

_Note: The output files from the IGRINS PLP are an in vacuum wavelength solution. If fit models are offset from expected line positions by 80-120 km/s, the models are likely in air and not vacuum. The IAU standard conversion for air to vacuum wavelengths is given by [Morton 1991](https://ui.adsabs.harvard.edu/abs/1991ApJS...77..119M/abstract). For vacuum wavelengths (VAC) in Angstroms and convert to air wavelength (AIR) via: AIR = VAC / (1.0 + 2.735182E-4 + (131.4182 / VAC^2) + (2.76249E8 / VAC^4))_

## Header Description
- NAME: the manually corrected name of the observed object (usually found through coordinate searches)
- OBJNAME_super: name of object observed (observer input) from the RRISA raw file
- OBJNAME_recipe: name of object observed (observer input) from the recipe file used to reduce the data
- MAIN_ID: the primary SIMBAD identifier
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
- RA_s: right ascension from SIMBAD
- DEC_s: the declination from SIMBAD
- IDS: all of the object names in SIMBAD associated with the object
- OTYPE: SIMBAD [object type](https://simbad.u-strasbg.fr/simbad/sim-display?data=otypes)
- SP_TYPE: SIMBAD spectral type
- SP_BIBCODE: the NASA ADS bibcode for the reference of the spectral type
- PMRA: SIMBAD RA proper motion
- PMDEC: SIMBAD DEC proper motion  
- PM_BIBCODE: the NASA ADS bibcode for the reference of the PM values
- RV_VALUE: the radial velocity value from SIMBAD
- RV_BIBCODE: the NASA ADS bibcode for the reference of the RV value
- PLX_VALUE: the parallax value from SIMBAD
- PLX_BIBCODE: the NASA ADS bibcode for the reference of the parallax value
- U, B, V, R, G, I, J, H, or K: magnitude values for various filters
- 2MASS_ID: the 2MASS identifier
- 2MASS_J: 2MASS J band magnitude
- 2MASS_H: 2MASS H band magnitude
- 2MASS_K: 2MASS K band magnitude
- 2MASS_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
- GaiaDR3_source: the Gaia DR3 identifier
- GaiaDR3_parallax: the Gaia DR3 parallax
- GaiaDR3_pm: the Gaia DR3 total proper motion
- GaiaDR3_bprp: the difference in the filters from Gaia DR3 photometry
- GaiaDR3_ebprp: the bp-rp excess factor from the Gaia DR3 photometry
- GaiaDR3_gmag: the G mean magnitude from the Gaia DR3 photometry
- GaiaDR3_RV: the Gaia DR3 radial velocity
- GaiaDR3_teff: the Gaia DR3 effective temperature from [GSP-Phot Aeneas](https://gea.esac.esa.int/archive/documentation/GDR3/Data_analysis/chap_cu8par/sec_cu8par_apsis/ssec_cu8par_apsis_gspphot.html) best library using BP/RP spectra
- GaiaDR3_logg: the Gaia DR3 surface gravity from [GSP-Phot Aeneas](https://gea.esac.esa.int/archive/documentation/GDR3/Data_analysis/chap_cu8par/sec_cu8par_apsis/ssec_cu8par_apsis_gspphot.html) best library using BP/RP spectra 
- GaiaDR3_FeH: the Gaia DR3 iron abundance from [GSP-Phot Aeneas](https://gea.esac.esa.int/archive/documentation/GDR3/Data_analysis/chap_cu8par/sec_cu8par_apsis/ssec_cu8par_apsis_gspphot.html) best library using BP/RP spectra
- GaiaDR3_dist: the Gaia DR3 distance from [GSP-Phot Aeneas](https://gea.esac.esa.int/archive/documentation/GDR3/Data_analysis/chap_cu8par/sec_cu8par_apsis/ssec_cu8par_apsis_gspphot.html) best library using BP/RP spectra
- GaiaDR3_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
- APOGEE2_HRV: the radial velocity estimate from APOGEE-2 DR17
- APOGEE2_teff: the effective temperature estimate from APOGEE-2 DR17
- APOGEE2_logg: the surface gravity estimate from APOGEE-2 DR17
- APOGEE2_Vsini: the vsini estimate from APOGEE-2 DR17
- APOGEE2_[M/H]: the metals over hydrogen value from APOGEE-2 DR17
- APOGEE2_[a/H]: the alpha elements over hydrogen value from APOGEE-2 DR17
- APOGEE2_[Fe/H]: the metallicity value from APOGEE-2 DR17
- PASTEL_Teff: the effective temperature from PASTEL
- PASTEL_logg: the surface gravity from PASTEL
- PASTEL_[Fe/H]: the metallicity value from PASTEL
- PASTEL_Flag: either 1 or nan, 1 indicates that the cross match should be verified by the user
- FILE_URL: Link to download the H- and K-band files for a particular file number
- CAL_URL: Link to download the associated H- and K-band files used for file reduction
- RAW_URL: Link to access the raw data from the CIVIL using Box
