#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Wbfm2
# Generated: Sat Apr 25 14:38:12 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx

class wbfm2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Wbfm2")

        ##################################################
        # Variables
        ##################################################
        self.decim = decim = 1
        self.adc_rate = adc_rate = 2000000
        self.xlate_offset_fine_0 = xlate_offset_fine_0 = 0
        self.xlate_offset_fine = xlate_offset_fine = 0
        self.xlate_offset_0 = xlate_offset_0 = 0
        self.xlate_offset = xlate_offset = 0
        self.xlate_decim = xlate_decim = 8
        self.xlate_bandwidth_0 = xlate_bandwidth_0 = 250000
        self.xlate_bandwidth = xlate_bandwidth = 250000
        self.samp_rate = samp_rate = adc_rate/decim
        self.freq_slider_2 = freq_slider_2 = 98.9e6
        self.audio_rate = audio_rate = 48000
        self.audio_interp = audio_interp = 4

        ##################################################
        # Blocks
        ##################################################
        self.main_notebook = self.main_notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "Baseband")
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "FIR 1")
        self.main_notebook.AddPage(grc_wxgui.Panel(self.main_notebook), "FIR 2")
        self.Add(self.main_notebook)
        _xlate_offset_fine_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_offset_fine_0_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	sizer=_xlate_offset_fine_0_sizer,
        	value=self.xlate_offset_fine_0,
        	callback=self.set_xlate_offset_fine_0,
        	label="Fine Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_offset_fine_0_slider = forms.slider(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	sizer=_xlate_offset_fine_0_sizer,
        	value=self.xlate_offset_fine_0,
        	callback=self.set_xlate_offset_fine_0,
        	minimum=-10000,
        	maximum=10000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.main_notebook.GetPage(2).Add(_xlate_offset_fine_0_sizer)
        _xlate_offset_fine_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_offset_fine_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(1).GetWin(),
        	sizer=_xlate_offset_fine_sizer,
        	value=self.xlate_offset_fine,
        	callback=self.set_xlate_offset_fine,
        	label="Fine Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_offset_fine_slider = forms.slider(
        	parent=self.main_notebook.GetPage(1).GetWin(),
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
        self.main_notebook.GetPage(1).Add(_xlate_offset_fine_sizer)
        self._xlate_offset_0_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	value=self.xlate_offset_0,
        	callback=self.set_xlate_offset_0,
        	label="Xlate Offset",
        	converter=forms.float_converter(),
        )
        self.main_notebook.GetPage(2).Add(self._xlate_offset_0_text_box)
        self._xlate_offset_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(1).GetWin(),
        	value=self.xlate_offset,
        	callback=self.set_xlate_offset,
        	label="Xlate Offset",
        	converter=forms.float_converter(),
        )
        self.main_notebook.GetPage(1).Add(self._xlate_offset_text_box)
        _xlate_bandwidth_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_bandwidth_0_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	sizer=_xlate_bandwidth_0_sizer,
        	value=self.xlate_bandwidth_0,
        	callback=self.set_xlate_bandwidth_0,
        	label="Xlate Bandwidth",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_bandwidth_0_slider = forms.slider(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	sizer=_xlate_bandwidth_0_sizer,
        	value=self.xlate_bandwidth_0,
        	callback=self.set_xlate_bandwidth_0,
        	minimum=12500,
        	maximum=500000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.main_notebook.GetPage(2).Add(_xlate_bandwidth_0_sizer)
        _xlate_bandwidth_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_bandwidth_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(1).GetWin(),
        	sizer=_xlate_bandwidth_sizer,
        	value=self.xlate_bandwidth,
        	callback=self.set_xlate_bandwidth,
        	label="Xlate Bandwidth",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_bandwidth_slider = forms.slider(
        	parent=self.main_notebook.GetPage(1).GetWin(),
        	sizer=_xlate_bandwidth_sizer,
        	value=self.xlate_bandwidth,
        	callback=self.set_xlate_bandwidth,
        	minimum=12500,
        	maximum=500000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.main_notebook.GetPage(1).Add(_xlate_bandwidth_sizer)
        _freq_slider_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_slider_2_text_box = forms.text_box(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	sizer=_freq_slider_2_sizer,
        	value=self.freq_slider_2,
        	callback=self.set_freq_slider_2,
        	label='freq_slider_2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider_2_slider = forms.slider(
        	parent=self.main_notebook.GetPage(2).GetWin(),
        	sizer=_freq_slider_2_sizer,
        	value=self.freq_slider_2,
        	callback=self.set_freq_slider_2,
        	minimum=0,
        	maximum=100e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.main_notebook.GetPage(2).Add(_freq_slider_2_sizer)
        self.wxgui_waterfallsink2_0_1 = waterfallsink2.waterfall_sink_c(
        	self.main_notebook.GetPage(2).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=50,
        	ref_scale=2.0,
        	sample_rate=samp_rate/xlate_decim,
        	fft_size=512,
        	fft_rate=30,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.main_notebook.GetPage(2).Add(self.wxgui_waterfallsink2_0_1.win)
        self.wxgui_waterfallsink2_0_0 = waterfallsink2.waterfall_sink_c(
        	self.main_notebook.GetPage(0).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=50,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=30,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.main_notebook.GetPage(0).Add(self.wxgui_waterfallsink2_0_0.win)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.main_notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=50,
        	ref_scale=2.0,
        	sample_rate=samp_rate/xlate_decim,
        	fft_size=512,
        	fft_rate=30,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.main_notebook.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(98.9e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=audio_rate*audio_interp,
                decimation=samp_rate/xlate_decim,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=audio_rate*audio_interp,
                decimation=samp_rate/xlate_decim,
                taps=None,
                fractional_bw=None,
        )
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(xlate_decim, (firdes.low_pass(1, samp_rate, xlate_bandwidth_0/2, 1000)), xlate_offset_0 + xlate_offset_fine_0 + freq_slider_2, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(xlate_decim, (firdes.low_pass(1, samp_rate, xlate_bandwidth/2, 1000)), xlate_offset + xlate_offset_fine, samp_rate)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=audio_rate*audio_interp,
        	audio_decimation=4,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=audio_rate*audio_interp,
        	audio_decimation=4,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.audio_sink_0, 1))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.wxgui_waterfallsink2_0_1, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_waterfallsink2_0_0, 0))    


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

    def get_xlate_offset_fine_0(self):
        return self.xlate_offset_fine_0

    def set_xlate_offset_fine_0(self, xlate_offset_fine_0):
        self.xlate_offset_fine_0 = xlate_offset_fine_0
        self._xlate_offset_fine_0_slider.set_value(self.xlate_offset_fine_0)
        self._xlate_offset_fine_0_text_box.set_value(self.xlate_offset_fine_0)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.xlate_offset_0 + self.xlate_offset_fine_0 + self.freq_slider_2)

    def get_xlate_offset_fine(self):
        return self.xlate_offset_fine

    def set_xlate_offset_fine(self, xlate_offset_fine):
        self.xlate_offset_fine = xlate_offset_fine
        self._xlate_offset_fine_slider.set_value(self.xlate_offset_fine)
        self._xlate_offset_fine_text_box.set_value(self.xlate_offset_fine)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset + self.xlate_offset_fine)

    def get_xlate_offset_0(self):
        return self.xlate_offset_0

    def set_xlate_offset_0(self, xlate_offset_0):
        self.xlate_offset_0 = xlate_offset_0
        self._xlate_offset_0_text_box.set_value(self.xlate_offset_0)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.xlate_offset_0 + self.xlate_offset_fine_0 + self.freq_slider_2)

    def get_xlate_offset(self):
        return self.xlate_offset

    def set_xlate_offset(self, xlate_offset):
        self.xlate_offset = xlate_offset
        self._xlate_offset_text_box.set_value(self.xlate_offset)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset + self.xlate_offset_fine)

    def get_xlate_decim(self):
        return self.xlate_decim

    def set_xlate_decim(self, xlate_decim):
        self.xlate_decim = xlate_decim
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate/self.xlate_decim)
        self.wxgui_waterfallsink2_0_1.set_sample_rate(self.samp_rate/self.xlate_decim)

    def get_xlate_bandwidth_0(self):
        return self.xlate_bandwidth_0

    def set_xlate_bandwidth_0(self, xlate_bandwidth_0):
        self.xlate_bandwidth_0 = xlate_bandwidth_0
        self._xlate_bandwidth_0_slider.set_value(self.xlate_bandwidth_0)
        self._xlate_bandwidth_0_text_box.set_value(self.xlate_bandwidth_0)
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth_0/2, 1000)))

    def get_xlate_bandwidth(self):
        return self.xlate_bandwidth

    def set_xlate_bandwidth(self, xlate_bandwidth):
        self.xlate_bandwidth = xlate_bandwidth
        self._xlate_bandwidth_slider.set_value(self.xlate_bandwidth)
        self._xlate_bandwidth_text_box.set_value(self.xlate_bandwidth)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth/2, 1000)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth/2, 1000)))
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate/self.xlate_decim)
        self.wxgui_waterfallsink2_0_1.set_sample_rate(self.samp_rate/self.xlate_decim)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth_0/2, 1000)))

    def get_freq_slider_2(self):
        return self.freq_slider_2

    def set_freq_slider_2(self, freq_slider_2):
        self.freq_slider_2 = freq_slider_2
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.xlate_offset_0 + self.xlate_offset_fine_0 + self.freq_slider_2)
        self._freq_slider_2_slider.set_value(self.freq_slider_2)
        self._freq_slider_2_text_box.set_value(self.freq_slider_2)

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
    tb = wbfm2()
    tb.Start(True)
    tb.Wait()
