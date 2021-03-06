from lddecode.core import RFParams_PAL,RFParams_NTSC,SysParams_PAL,SysParams_NTSC

# We base the parameters off the original laserdisc ones and override the ones
# we need.
# NOTE: (This requires python 3.5+)
RFParams_PAL_VHS = {**RFParams_PAL}
RFParams_NTSC_VHS = {**RFParams_NTSC}

# Tape-specific paramaters that differs from the laserdisc analogues
# Video Y deemphasis
# Not used, generated elsewhere.
# RFParams_PAL_VHS['video_deemp'] = (100*.24, 400*.24)

# Band-pass filter for Video rf.
# TODO: Needs tweaking
RFParams_PAL_VHS['video_bpf_low'] = 3550000
RFParams_PAL_VHS['video_bpf_high'] = 5200000
# Band-pass filter order.
# Order may be fine as is.
RFParams_PAL_VHS['video_bpf_order'] = 1

# Low-pass filter on Y after demodulation
RFParams_PAL_VHS['video_lpf_freq'] = 3600000
# Order may be fine as is.
#RFParams_PAL_VHS['video_lpf_order'] = 9

# PAL color under carrier is 40H + 1953
RFParams_PAL_VHS['color_under_carrier'] = ((625 * 25) * 40) + 1953

# Band-pass filter for Video rf.
# TODO: Needs tweaking
RFParams_NTSC_VHS['video_bpf_low'] = 3300000
RFParams_NTSC_VHS['video_bpf_high'] = 5000000

RFParams_NTSC_VHS['video_bpf_order'] = 2

# Low-pass filter on Y after demodulation
RFParams_NTSC_VHS['video_lpf_freq'] = 3600000
# Order may be fine as is.
#RFParams_PAL_VHS['video_lpf_order'] = 9

# NTSC color under carrier is 40H
RFParams_NTSC_VHS['color_under_carrier'] = (525 * (30 / 1.001)) * 40

SysParams_PAL_VHS = {**SysParams_PAL}
SysParams_NTSC_VHS = {**SysParams_NTSC}

#0 IRE level after demodulation
SysParams_PAL_VHS['ire0'] = 4100000

# frequency/ire IRE change pr frequency (Is this labeled correctly?)
SysParams_PAL_VHS['hz_ire'] = 700000 / 100.0

SysParams_PAL_VHS['max_ire'] = 100 # Top/white point defined by the standard 4.8 MHz

# Mean absolute value of color burst for Automatic Chroma Control.
# The value is eyeballed to give ok chroma level as of now, needs to be tweaked.
SysParams_PAL_VHS['burst_abs_ref'] = 750

#0 IRE level after demodulation
SysParams_NTSC_VHS['ire0'] = 3685000

# frequency/ire IRE change pr frequency (Is this labeled correctly?)
SysParams_NTSC_VHS['hz_ire'] = 715000 / 100.0

SysParams_NTSC_VHS['max_ire'] = 100 # Top/white point defined by the standard 4.8 MHz

# Mean absolute value of color burst for Automatic Chroma Control.
# The value is eyeballed to give ok chroma level as of now, needs to be tweaked.
SysParams_NTSC_VHS['burst_abs_ref'] = 300

#SysParams_PAL['outlinelen'] = calclinelen(SysParams_PAL, 4, 'fsc_mhz')
#SysParams_PAL['outlinelen_pilot'] = calclinelen(SysParams_PAL, 4, 'pilot_mhz')
#SysParams_PAL['vsync_ire'] = -.3 * (100 / .7)

#TODO: SECAM
