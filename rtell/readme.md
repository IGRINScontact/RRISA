# IGRINS rtell Code

Created by Dr. Kim Sokal in 2017, adapted by Erica Sawczynec for RRISA in 2022.

## Purpose
Refine the telluric corrected IGRINS PLP output so the standard and target spectra are pixel aligned before division.
Achieved by fitting the telluric sky line between 16452 and 16458 Angstroms for H-Band and 21740 and 21752 Angstroms for K-Band.

## Input
The code is for specific use with the RRISA .csv files as pandas DataFrame objects (in Python) since the code iterates by row for each observation (each row contains all the information about each observation).
Optimized for use on subsamples, may come back to making a single use version of this code in the future.

## Variables to Change
For local use, change the following paths/names to your local data paths/desired names:
- Line 185: obsdir; the file path to the data (must contain .spec_a0v, .sn, and .spec files in the directory)
- Line 194: file_target; the filename of the target spectra
- Line 195: obsdir_out; the desired output file path
- Line 196: base_filename_out; desired output filename extension
- Line 218: recipedir; the file path to the corresponding recipe logs directory
