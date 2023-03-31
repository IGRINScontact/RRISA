import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import scipy
import sys
import numpy as np
from matplotlib.pyplot import cm
from scipy.optimize import curve_fit
import astropy.units as u
from astropy.io import fits
import astropy.constants as c

import warnings
from scipy.optimize import OptimizeWarning

warnings.simplefilter("error", OptimizeWarning)

"""
This program rtell.py is to take some of the IGRINS plp products
to refine the telluric correction. It will divide a science spectra by a standard spectra,
in the same fashion as the plp, with the following intended differences:
- don't need to run from the pipeline (just a quick program)
- will find the pixel center of a given sky line and then shift the standard spectra in pixel space
before dividing the target by this (thus possible to use standards from different nights).

author:
	Kim Sokal 2017
	Adapted for RRISA by Erica Sawczynec 2022

input:
	config file with the target and standard spectra names (which are from the plp)
	it has the following entries:
		specfile_target [example:  ='SDCK_20150127_0152.spec.fits']
		specfile_standard	[example: ='SDCK_20150127_0156.spec.fits']
		obsdir	[example: ='/Users/observations/IG_plp_reduced_data/outdata/']
				* note that the program expects plp format. It will pull out the date itself
				  (as plp data are stored as /outdata/20150127/)
				  you only need the directory above that level (i.e. outdata/)
		filename_out	[this will be added before .fits in the target filename. example: ='.spec_a0v.']
		band ['H' or 'K'. example: = 'K']

output:
	telluric corrected target spectra
		specfile_target+filename_out.fits

how to run:
	python refine_igrins_telluric_corr.py refine_igrins_telluric_corr.cfg

	* while it runs you will see 3 plots pop up. The first two are showing the fit to
	the sky lines - if the vertical line doesn't match the center then something is wrong.
	The last is to check the final output.

"""
def new_spec(row, band):
	def read_config(configfile):
		cfg=dict()
		f=open(configfile)
		for row in f:
			if not row.strip() or row.lstrip().startswith('#'):
				continue
			option, value = [r.strip() for r in row.split('=')]
			cfg[option]=value

		return cfg

	def align_by_f_interp(shiftvalue,flux_shifted,uncs_shifted,wvsol):
		#this is where we apply the pixel shift

		length=len(flux_shifted)
		pixs=np.arange(length)
		shifted_pixs=pixs+shiftvalue

		#so by doing it this way, i am assuming the real "value" of the pixels here is the
		#shifted value
		flux_fixed=np.interp(shifted_pixs, pixs,flux_shifted)
		uncs_fixed=np.interp(shifted_pixs, pixs,uncs_shifted)

		return [flux_fixed,uncs_fixed,wvsol]

	def gaussian(x,amp,cen,wid):
		#just defining the gaussian to fit the sky line
		return amp*np.exp(-(x-cen)**2/wid)

	def find_line_center(pixelsin, normed, wls, cutoffs, name, i):
		#this is where we fit a gaussian to a sky line and find the center in pixel space
		blueend_pix,redend_pix=cutoffs

		#using just the specified region of the spectra
		blueend=np.where(pixelsin > blueend_pix)
		fluxes_out=normed[blueend]
		pixels=pixelsin[blueend]
		wls=wls[blueend]

		redend=np.where(pixels < redend_pix)
		fluxes_out=fluxes_out[redend]
		pixels=pixels[redend]
		wls=wls[redend]

		#trying to make it look like a normal gaussian.
		#meaning positive, as the sky lines are in absorption
		fluxes_out=np.array(fluxes_out)
		flipped=1./fluxes_out
		f=flipped-np.nanmedian(flipped)


		#now fit it with a gaussian to find the center!
		n=len(f)
		newpix=np.arange(n)

		init_vals=[np.nanmax(f), np.mean(pixels), np.mean(pixels)/100]
		try:
			best_vals, covar = curve_fit(gaussian, pixels, f, p0=init_vals)
		except RuntimeError:
			print('curve_fit failure, aborting.\n')
			center = np.nan
			return center
		center = best_vals[1]

		#plot to ensure that you are actually measuring the line center
		plotnow='yes'
		if plotnow == 'yes':
			fig, axes = plt.subplots(1, 2, figsize = (14, 5), facecolor = 'white')
			axes[0].plot(pixels, f, color="green")
			axes[0].plot(np.mean(pixels), np.nanmax(f), marker = 'o', color="blue")
			axes[0].plot(pixels, gaussian(pixels, *init_vals), ls = '--', c = 'r')
			axes[0].set_xlim(cutoffs[0]-50, cutoffs[1]+50)

			axes[1].plot(pixels, f, color="green")
			axes[1].plot(center, np.nanmax(f), marker = 'o', color="blue", label = f'{center}', ls = '')
			axes[1].plot(pixels, gaussian(pixels, *best_vals), color="magenta")
			axes[1].axvline(x = cutoffs[0], ls = '--', c = 'k')
			axes[1].axvline(x = cutoffs[1], ls = '--', c = 'k')
			axes[1].set_xlim(cutoffs[0]-50, cutoffs[1]+50)
			axes[1].legend()

			if i == 0:
				axes[0].set_title('Initial Gaussian Center: Target')
				axes[1].set_title('Curvefit Gaussian Center: Target')
			else:
				axes[0].set_title('Initial Gaussian Center: Standard')
				axes[1].set_title('Curvefit Gaussian Center: Standard')

			plt.savefig(name)
			plt.close()

		return center


	def fix_num_orders(wls, fluxes,sns):
		keep = 26#53248 # 26 orders times 2048 pixels per order
		diff=keep-len(wls)
		if diff >0:
			#add in nans for any missing data. it is probably for the early part!
			startwave=np.nanmin(wls)
			if startwave < 1000:
				startwave=startwave*1.e4
			if startwave > 18600:
				#one order
				add=np.array([0.]*2048)
				wls=np.insert(wls,-1,add, axis=0)
				fluxes=np.insert(fluxes,-1,add, axis=0)
				sns=np.insert(sns,-1,add, axis=0)
				if startwave > 18800:
					#two orders
					wls=np.insert(wls,-1,add, axis=0)
					fluxes=np.insert(fluxes,-1,add, axis=0)
					sns=np.insert(sns,-1,add, axis=0)
					if startwave > 19000:
						#three orders
						wls=np.insert(wls,-1,add, axis=0)
						normed=np.insert(normed,-1,add, axis=0)
						sns=np.insert(sns,-1,add, axis=0)
			if len(wls) != keep:
				diff=keep-len(wls)
				add=np.array([0.]*diff)
				wls=np.insert(wls,-1,add, axis=0)
				fluxes=np.insert(fluxes,-1,add, axis=0)
				sns=np.insert(sns,-1,add, axis=0)

		return [wls,fluxes,sns]

	"""
	This is the body of the code.
	"""

	obsdir='/Volumes/ExIGRINS5/igplp/outdata/'

	civil = row['CIVIL']

	if band == 'K':
		filename = row['FILENAME'].split('.')[0].replace('H', 'K')
	else:
		filename = row['FILENAME'].split('.')[0]

	file_target=f'{filename}'
	obsdir_out=f'{obsdir}{civil}/'
	base_filename_out=f'rtell_{band}'

	try:
		hdul = fits.open(f'{obsdir_out}{file_target}.spec_a0v.fits')
		standard_filename = hdul[0].header['HIERARCH IGR_A0V_BASENAME']
	except FileNotFoundError:
		print(f"No file {obsdir_out}{file_target}.spec_a0v.fits\n")
		filename_out_txt = obsdir_out+file_target.split(".fits")[0]+"."+base_filename_out+".spec_a0v.txt"
		f = open(filename_out_txt, 'w')
		f.write(f'Missing {file_target}, correction aborted.')
		f.close()
		return

	file_standard=f'{standard_filename}'

	if np.char.isnumeric(str(row['BVC'])):
		bary_correct='True'
		bvc= float(row['BVC'])
	else:
		bary_correct = 'False'

	recipe_info ='yes'
	recipedir='/Volumes/ExIGRINS5/igplp/recipe_logs/'

	#step 1.a: read in the observed data

	targetfile=file_target.split(".fits")
	find_obsdate_target=targetfile[0].split("_")
	obsdate_target=find_obsdate_target[1]
	filenumber_target=find_obsdate_target[2]

	specfile_target=targetfile[0]+".spec.fits"
	snrfile_target=targetfile[0]+".sn.fits"
	vegafile=targetfile[0]+".spec_a0v.fits"

	specpath_target=obsdir+obsdate_target+'/'+specfile_target
	snrpath_target=obsdir+obsdate_target+'/'+snrfile_target
	vegapath_target=obsdir+obsdate_target+'/'+vegafile

	try:
		spec_target = pyfits.getdata(specpath_target)
		wlsol_target = pyfits.getdata(specpath_target,1)
	except FileNotFoundError:
		print(f'Missing target {specpath_target} file.\n')
		filename_out = obsdir_out+file_target.split(".fits")[0]+"."+base_filename_out+".spec_a0v.txt"
		f = open(filename_out_txt, 'w')
		f.write(f'Missing target file {specpath_target}, correction aborted.')
		f.close()
		return

	try:
		snr_target = pyfits.getdata(snrpath_target)
	except FileNotFoundError:
		print(f'Missing target {snrpath_target} file.\n')
		filename_out = obsdir_out+file_target.split(".fits")[0]+"."+base_filename_out+".spec_a0v.txt"
		f = open(filename_out_txt, 'w')
		f.write(f'Missing target SNR file {snrpath_target}, correction aborted.')
		f.close()
		return

	vega = pyfits.getdata(vegapath_target,4)

	filename_out=obsdir_out+targetfile[0]+"."+base_filename_out+".spec_a0v.fits" #spectra
	filename_out_txt=obsdir_out+targetfile[0]+"."+base_filename_out+".spec_a0v.txt" #text file out on info
	f=open(filename_out_txt, 'w')
	f.write('Performing a telluric correction \n')
	print(specfile_target)

	dataheader_target = pyfits.getheader(specpath_target)

	#step 1.b: learn about the observed data
	object_target=dataheader_target['OBJECT',0]
	date_target=dataheader_target['UTDATE',0]
	amstart=dataheader_target['AMSTART',0]
	amend=dataheader_target['AMEND',0]
	try:
		am_target=0.5*(float(amstart)+float(amend))
	except TypeError:
		am_target = False
	f.write('*** Target ***'+'\n')
	f.write('SPEC FILE: '+ specfile_target+'\n')
	f.write('OBJECT: '+ object_target+'\n')
	f.write('DATE: '+ date_target+'\n')
	f.write('am dets:'+ str(amstart)+'\t'+str(amend)+'\n')
	if am_target:
		f.write('average am: '+ str(am_target)+'\n')
	else:
		f.write('average am: airmass error')

	tel=dataheader_target.get('TELESCOP')
	exptime=dataheader_target.get('EXPTIME')
	acqtime=dataheader_target.get('ACQTIME') #get local date
	obs=dataheader_target.get('OBSERVER')


	f.write('**********************'+'\n')
	f.write('Target observing info from header:'+'\n')
	f.write('Object \t UT Date \t Telescope \t Exp Time \t Airmass \t Observers'+'\n')
	if am_target:
		f.write(str(object_target)+'\t'+str(date_target)+'\t'+str(tel)+'\t'+str(exptime)+'\t'+str(am_target)+'\t'+str(obs)+'\n')
	else:
		f.write(str(object_target)+'\t'+str(date_target)+'\t'+str(tel)+'\t'+str(exptime)+'\t'+str(obs)+'\n')

	if recipe_info =='yes':
		#step 1.c. how many frames are in there?
		recipelog=recipedir+obsdate_target+'.recipes'
		#each line will be 'observed name', 'target type', group1 = file # for some, group 2, exptime, recipe, obsids, frametypes
		filenumber_target=int(filenumber_target)
		f_recipe=open(recipelog, 'r')

		for line in f_recipe.readlines():
			#ignore comment lines in recipe files
			if line[0] != '#':
				split=line.split(",")
				test_sky=split[5]
				test_sky=test_sky.strip(" ")
				if test_sky != 'SKY':
					find_file=split[6].split()
					if find_file[0] == str(filenumber_target):
						f.write('recipe file: \n')
						f.write(line+'\n')


	#step 1.d. make sure the order numbers are the same
	a,vega,b=fix_num_orders(wlsol_target,vega,snr_target)
	wlsol_target,spec_target,snr_target=fix_num_orders(wlsol_target,spec_target,snr_target)


	#step 2.a: read in the standard data

	standardfile=file_standard.split(".fits")
	find_obsdate_standard=standardfile[0].split("_")
	obsdate_standard=find_obsdate_standard[1]

	specfile_standard=standardfile[0]+".spec.fits"
	snrfile_standard=standardfile[0]+".sn.fits"

	specpath_standard=obsdir+obsdate_standard+'/'+specfile_standard
	snrpath_standard=obsdir+obsdate_standard+'/'+snrfile_standard

	try:
		spec_standard = pyfits.getdata(specpath_standard)
		wlsol_standard = pyfits.getdata(specpath_standard,1)
	except FileNotFoundError:
		print(f'Missing A0V {specpath_standard} file.\n')
		f.write(f'Missing standard file {specpath_standard}, correction aborted.')
		f.close()
		return

	try:
		snr_standard = pyfits.getdata(snrpath_standard)
	except FileNotFoundError:
		print(f'Missing A0V {snrpath_standard} file.\n')
		f.write(f'Missing standard SNR file {snrpath_standard}, correction aborted.')
		f.close()
		return

	dataheader_standard = pyfits.getheader(specpath_standard)

	#step 2.b: learn about the standard data
	object_standard=dataheader_standard['OBJECT',0]
	date_standard=dataheader_standard['UTDATE',0]
	amstart=dataheader_standard['AMSTART',0]
	amend=dataheader_standard['AMEND',0]
	try:
		am_standard=0.5*(float(amstart)+float(amend))
	except TypeError:
		am_standard = False

	f.write('*** standard ***'+'\n')
	f.write('SPEC FILE: '+ specfile_standard+'\n')
	f.write('OBJECT: '+ object_standard+'\n')
	f.write('DATE: '+ date_standard+'\n')
	if am_standard:
		f.write('average am: '+ str(am_standard)+'\n')
	else:
		f.write('average am: airmass error')
	f.write('start am: '+str(amstart)+'\n')
	f.write('end am: '+str(amend)+'\n')

	#step 2.d: correct for # of orders
	wlsol_standard,spec_standard,snr_standard=fix_num_orders(wlsol_standard,spec_standard,snr_standard)

	#step 3: need to find any pixel shift between the target and standard spectra, by measuring a sky line.
	#(there is a pixel shift in general, esp. when we move between telescopes). Order of < or a couple of pixels.
	#unfortunately that means that I have to go through the entire spectra

	save_centers=[]
	num=0
	for spec,wlsol,snr in zip([spec_target,spec_standard],[wlsol_target,wlsol_standard],[snr_target,snr_standard]):

		fluxes=[]
		wls=[]
		sns=[]
		for wl, I, sn in zip(wlsol, spec,snr):

			#convert units
			wl=wl*1.e4 #from 1.4 to 1.4e4 as expected (um to Ang i think)

			#combine all the data
			wls.extend(wl)
			fluxes.extend(I)
			sns.extend(sn)

		#lets sort these by wavelength, since the orders are random and have overlap
		sorts=np.argsort(wls)
		wls=np.array(wls)
		fluxes=np.array(fluxes)
		sns=np.array(sns)
		wls=wls[sorts]
		fluxes=fluxes[sorts]
		sns=sns[sorts]

		#lets make sure our 2 spectra are the same length - the pipeline currently produced different
		#numbers of orders depending on the flat fields. so we need to fix this.

		pix=np.arange(len(fluxes))
		#first one first
		if num==0:
			keep=len(fluxes)

			#find the cut offs for the line we will be using
			#choosing some region of the spectra
			if band == 'K':
				region=[21740,21752] #if it has problems, try editing a bit. also [22145,22165]?
				#this is just a line that i found that works well. you can play with it, and just run again!
			elif band == 'H':
				region=[16452,16458] #if it has problems, try [16452,16458]?16429,16431]
			blueend=np.where(wls > region[0])
			findblue=pix[blueend]
			blueend_pix=np.min(findblue)

			redend=np.where(wls < region[1])
			findred=pix[redend]
			redend_pix=np.max(findred)

		#ok lets find the shift!
		try:
			if num == 0:
				figure_name = obsdir_out+targetfile[0]+'.'+base_filename_out+'.center_align_target.png'
			else:
				figure_name = obsdir_out+targetfile[0]+'.'+base_filename_out+'.center_align_standard.png'

			foundcenter=find_line_center(pix, fluxes, wls,[blueend_pix,redend_pix], figure_name, num)
		except OptimizeWarning:
			print('Poor telluric line fit, aborting.\n')
			f.write('Poor telluric line fit, use original spec_a0v file or refine reduction.\n')
			f.close()
			return

		if np.isnan(foundcenter):
			f.write('Poor telluric line fit, use original spec_a0v file or refine reduction.\n')
			f.close()
			return
		save_centers.append(foundcenter)

		#yep, all that work to find the center of that line
		num=+1

	shift = save_centers[1]-save_centers[0]

	f.write('*** shift ***'+'\n')
	f.write('The target and standard are shifted by {0} pixels'.format(shift)+'\n')
	print(f'{object_target}, {date_target}, {object_standard}, {shift:.2f} pix')
	if abs(shift) > 1.0:
		shift = 0.0
		print('Shift Rejected since > 1 pix. Shift = 0.0')
		f.write('Shift Rejected since > 1 pix. Shift = 0.0')

	#step 4: order by order, apply the shift and divide the spectra
	spec_target_a0v=[]
	wlsol=[]
	snr=[]


	for order in range(len(spec)):
		#this assumes that the spectra have the same number of orders and are in the same order

		##ok, so lets shift the standard spectra here. by the amount in pixels.
		pix_order=np.arange(len(wlsol_standard))
		#it will interpolate
		spec_standard[order],snr_standard[order],wlsol_standard[order]=align_by_f_interp(shift,spec_standard[order],snr_standard[order],wlsol_standard[order])

		### when dividing: thinking about if we need to normalize them in any way. but
		## that means just multiplying by some factor - so the answer is no then,
		# it is not mathematically necessary.

		#fyi - keeping the target wavesol so we can just use that vega to get the correct shape
		div=spec_target[order]/spec_standard[order]*vega[order]

		spec_target_a0v.append(div)
		wlsol_order=wlsol_target[order]
		#wlsol_order=wlsol_standard[order] used to use this
		wlsol.append(wlsol_order)
		#adding in quadrature
		unc_order=(snr_standard[order]**-2+snr_target[order]**-2)**0.5
		snr.append(unc_order**-1)


	spec_target_a0v=np.array(spec_target_a0v)

	#step 5: save to a new fits file
	#the extensions are a bit like the plp output
	#except now with uncs (that incorporate the a0v division as well)

	#write the primary data, and fill out the header
	hdu=pyfits.PrimaryHDU()
	hdu.writeto(filename_out, overwrite = True)
	#copy the target header
	header=dataheader_target
	header["EXTNAME"] = 'SPEC_DIVIDE_A0V'
	header["STD"]=(specfile_standard,"Standard spectra used")
	header.add_comment("This spectrum was created by dividing by the standard spectra and multiplying by a generic Vega (as in the plp)")
	header.add_comment("The standard pixels were shifted by an offset of "+str(shift) )
	pyfits.update(filename_out,spec_target_a0v, header)


	#add the rest of the extensions
	header["EXTNAME"]="WAVELENGTH"
	pyfits.append(filename_out,wlsol_target, header)
	header["EXTNAME"]="TGT_SPEC"
	pyfits.append(filename_out,spec_target, header)
	header["EXTNAME"]="A0V_SPEC"
	pyfits.append(filename_out,spec_standard, header)
	header["EXTNAME"]="VEGA_SPEC"
	pyfits.append(filename_out,vega, header)
	###This one is new!
	header["EXTNAME"]="SNR"
	pyfits.append(filename_out,snr, header)

	f.write('*** File out ***'+'\n')
	f.write('The divided spectra is being saved to '+filename_out)
	f.close()
