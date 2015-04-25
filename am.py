#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Am
# Generated: Sat Apr 25 14:27:54 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx

class am(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Am")

        ##################################################
        # Variables
        ##################################################
        self.decim = decim = 2
        self.adc_rate = adc_rate = 2000000
        self.xlate_offset_fine = xlate_offset_fine = 0
        self.xlate_offset = xlate_offset = 0
        self.xlate_decim = xlate_decim = 4
        self.xlate_bandwidth = xlate_bandwidth = 10000
        self.volume = volume = 10
        self.squelch = squelch = 22
        self.samp_rate = samp_rate = adc_rate/decim
        self.main_freq = main_freq = 118.568e6
        self.audio_rate = audio_rate = 48000
        self.audio_interp = audio_interp = 4

        ##################################################
        # Blocks
        ##################################################
        self.main_notebook = self.main_notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "Baseband")
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "Scope")
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "Waterfall")
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "Quad demod")
        self.Add(self.main_notebook)
        _xlate_offset_fine_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_offset_fine_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(0).GetWin(),
        	sizer=_xlate_offset_fine_sizer,
        	value=self.xlate_offset_fine,
        	callback=self.set_xlate_offset_fine,
        	label="Fine Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_offset_fine_slider = forms.slider(
        	parent=self.main_notebook.GetPage(0).GetWin(),
        	sizer=_xlate_offset_fine_sizer,
        	value=self.xlate_offset_fine,
        	callback=self.set_xlate_offset_fine,
        	minimum=-10000,
        	maximum=10000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.main_notebook.GetPage(0).Add(_xlate_offset_fine_sizer)
        self._xlate_offset_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(0).GetWin(),
        	value=self.xlate_offset,
        	callback=self.set_xlate_offset,
        	label="Xlate Offset",
        	converter=forms.float_converter(),
        )
        self.main_notebook.GetPage(0).Add(self._xlate_offset_text_box)
        _xlate_bandwidth_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_bandwidth_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(0).GetWin(),
        	sizer=_xlate_bandwidth_sizer,
        	value=self.xlate_bandwidth,
        	callback=self.set_xlate_bandwidth,
        	label="Xlate Bandwidth",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_bandwidth_slider = forms.slider(
        	parent=self.main_notebook.GetPage(0).GetWin(),
        	sizer=_xlate_bandwidth_sizer,
        	value=self.xlate_bandwidth,
        	callback=self.set_xlate_bandwidth,
        	minimum=2500,
        	maximum=250000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.main_notebook.GetPage(0).Add(_xlate_bandwidth_sizer)
        _squelch_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_squelch_sizer,
        	value=self.squelch,
        	callback=self.set_squelch,
        	label='squelch',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelch_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_squelch_sizer,
        	value=self.squelch,
        	callback=self.set_squelch,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_squelch_sizer)
        self._main_freq_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(0).GetWin(),
        	value=self.main_freq,
        	callback=self.set_main_freq,
        	label="Main Freq",
        	converter=forms.float_converter(),
        )
        self.main_notebook.GetPage(0).Add(self._main_freq_text_box)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.main_notebook.GetPage(2).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.main_notebook.GetPage(2).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.main_notebook.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/xlate_decim,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.main_notebook.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=20,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_sizer)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(main_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=16000,
                decimation=48000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=audio_rate*audio_interp,
                decimation=samp_rate/xlate_decim,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/xlate_decim, 5000, 1500, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(xlate_decim, (firdes.low_pass(1, samp_rate, xlate_bandwidth/2, 1000)), xlate_offset + xlate_offset_fine, samp_rate)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/Users/ross/Desktop/GRC/testam.wav", 1, 16000, 16)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_ff(squelch*-1, 0.001, 0, True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=48000,
        	audio_decim=4,
        	audio_pass=5000,
        	audio_stop=5500,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-5, 0.9, 10)
        self.analog_agc2_xx_0.set_max_gain(10)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_am_demod_cf_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.low_pass_filter, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.low_pass_filter, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_am_demod_cf_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    


    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samp_rate(self.adc_rate/self.decim)

    def get_adc_rate(self):
        return self.adc_rate

    def set_adc_rate(self, adc_rate):
        self.adc_rate = adc_rate
        self.set_samp_rate(self.adc_rate/self.decim)

    def get_xlate_offset_fine(self):
        return self.xlate_offset_fine

    def set_xlate_offset_fine(self, xlate_offset_fine):
        self.xlate_offset_fine = xlate_offset_fine
        self._xlate_offset_fine_slider.set_value(self.xlate_offset_fine)
        self._xlate_offset_fine_text_box.set_value(self.xlate_offset_fine)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset + self.xlate_offset_fine)

    def get_xlate_offset(self):
        return self.xlate_offset

    def set_xlate_offset(self, xlate_offset):
        self.xlate_offset = xlate_offset
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset + self.xlate_offset_fine)
        self._xlate_offset_text_box.set_value(self.xlate_offset)

    def get_xlate_decim(self):
        return self.xlate_decim

    def set_xlate_decim(self, xlate_decim):
        self.xlate_decim = xlate_decim
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/self.xlate_decim)
        self.low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate/self.xlate_decim, 5000, 1500, firdes.WIN_HAMMING, 6.76))

    def get_xlate_bandwidth(self):
        return self.xlate_bandwidth

    def set_xlate_bandwidth(self, xlate_bandwidth):
        self.xlate_bandwidth = xlate_bandwidth
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth/2, 1000)))
        self._xlate_bandwidth_slider.set_value(self.xlate_bandwidth)
        self._xlate_bandwidth_text_box.set_value(self.xlate_bandwidth)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch
        self._squelch_slider.set_value(self.squelch)
        self._squelch_text_box.set_value(self.squelch)
        self.analog_pwr_squelch_xx_0.set_threshold(self.squelch*-1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/self.xlate_decim)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth/2, 1000)))
        self.low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate/self.xlate_decim, 5000, 1500, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_main_freq(self):
        return self.main_freq

    def set_main_freq(self, main_freq):
        self.main_freq = main_freq
        self._main_freq_text_box.set_value(self.main_freq)
        self.rtlsdr_source_0.set_center_freq(self.main_freq, 0)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = am()
    tb.Start(True)
    tb.Wait()
