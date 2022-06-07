# Raw IGRINS Files

Dates included: 20140707 - 20210530

## Description
The Raw component of RRISA includes all of the frames IGRINS has ever observed before May 2021 including Flats, Darks, Arcs, Targets, and Standards. This includes images that are not suitable for science like partial frames, frames with incorrect exposure times, or mislabeled frames. We recommend that before reducing spectra using raw files users check the IGRINS paper logs to ensure all frames are science quality. The paper logs can be downloaded using this [link](https://utexas.box.com/s/xinbky19f5t584l1ky3xq3wffig684zi).

IGRINS simultaneously reads out both H and K Band spectra (SDCH & SDCK) meaning the file numbers for these files correspond to the same pointing. However, this is not true for the slit-viewer images (SDCS) which are instead saved during target acquisition and guiding.

_Raw files can only be downloaded by night and not individually like reduced data products._

## Header Description
- OBJNAME: name of object observed (user input)
- RA_2000: telescope right ascension from the telescope converted into J2000 (+- deg)
- DEC_2000: telescope declination from the telescope converted into J2000 (+- deg)
- FILENAME: the name of the file that corresponds to the information in the rest of the row
- OBJTYPE: the frame type, can be DARK, ARC, FLAT, SKY, TAR, STD and more
- FRAMETYPE: ON or OFF
- CIVIL: the date of observation (YYYYMMDD)
- FILENUMBER: number of the file
- JD: the julian date when the observation finished
- OBSTIME: time of observation
- EXPTIME: exposure time (in seconds)
- ROTPA: rotation position angle
- AM: airmass at the end of the observation
- BVC: barycentric velocity correction using [barycorrpy](https://github.com/shbhuk/barycorrpy) (km/s)
- FACILITY: telescope of observation
- PI: requester of observations, either name[s], program ID (for Gemini South), or "Unknown"
