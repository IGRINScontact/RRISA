# Raw IGRINS Files

Dates included: 20140707 - 20230507

## Description
The Raw component of RRISA includes all of the frames IGRINS has ever observed before June of 2023 including flats, darks, arcs, targets, and standards. This includes images that are not suitable for science like partial frames, frames with incorrect exposure times, or mislabeled frames. We recommend that before reducing spectra using raw files users check the IGRINS paper logs to ensure all frames are science quality. The paper logs can be found [here](https://utexas.box.com/s/wnkqbgf5atxx1hy1ejiou1r2avdcx4c3).

IGRINS simultaneously reads out both H and K Band spectra (SDCH & SDCK) meaning the file numbers for these files correspond to the same pointing.

_Raw files can only be downloaded by night and not individually like reduced data products._

## Header Description
- OBJNAME: name of object observed (user input)
- CIVIL: the date of observation (YYYYMMDD)
- RA: the right ascention recorded by the telescope for the observation (in decimal degrees)
- DEC: the declination recorded by the telescope for the observation (in decimal degrees)
- FILENAME: name of the file
- OBJTYPE: the frame type; can be DARK, ARC, FLAT, SKY, TAR, or STD
- FRAMETYPE: A/B (nod on the slit) or ON/OFF (for flats describes if the lamp is on or off, otherwise same as the nod positions for A/B) 
- FILENUMBER: the number in the filename (also sometimes called the observation ID)
- JD: the julian date when the observation finished
- OBSTIME: the time the observation began
- EXPTIME: exposure time (in seconds)
- ROTPA: position angle of the slit
- AM: airmass at the end of the observation
- BVC: barycentric velocity correction using [barycorrpy](https://github.com/shbhuk/barycorrpy) (km/s)
- FACILITY: telescope of observation (McDonald, DCT, or Gemini South)
- PI: priciple investigator for the observations (who requested the observations); only avalible for McDonald and DCT Observations
- PROGID: Gemini South program ID
- SDCS: Either a list of slit camera image file numbers taken during the acquisition of the raw .spec file or for earlier civil dates with SDCS frames (20150401-20170310), a -1 flag followed by the number of SCDC images taken for that particular civil date (available to download from Box via the raw data URL)
- RAW_URL: Link to access the raw data from the CIVIL using Box
