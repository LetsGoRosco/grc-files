#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Multiple Rtlsdr
# Generated: Sat Apr 25 14:31:27 2015
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx

class multiple_rtlsdr(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Multiple Rtlsdr")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2400000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_waterfallsink2_0_0_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
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
        self.Add(self.wxgui_waterfallsink2_0_0_0.win)
        self.wxgui_waterfallsink2_0_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
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
        self.Add(self.wxgui_waterfallsink2_0_0.win)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
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
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(3) + " " + "rtl=0 rtl=1 rtl=2" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(98.9e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self.rtlsdr_source_0.set_center_freq(100e6, 1)
        self.rtlsdr_source_0.set_freq_corr(0, 1)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 1)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 1)
        self.rtlsdr_source_0.set_gain_mode(False, 1)
        self.rtlsdr_source_0.set_gain(10, 1)
        self.rtlsdr_source_0.set_if_gain(20, 1)
        self.rtlsdr_source_0.set_bb_gain(20, 1)
        self.rtlsdr_source_0.set_antenna("", 1)
        self.rtlsdr_source_0.set_bandwidth(0, 1)
        self.rtlsdr_source_0.set_center_freq(102e6, 2)
        self.rtlsdr_source_0.set_freq_corr(0, 2)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 2)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 2)
        self.rtlsdr_source_0.set_gain_mode(False, 2)
        self.rtlsdr_source_0.set_gain(10, 2)
        self.rtlsdr_source_0.set_if_gain(20, 2)
        self.rtlsdr_source_0.set_bb_gain(20, 2)
        self.rtlsdr_source_0.set_antenna("", 2)
        self.rtlsdr_source_0.set_bandwidth(0, 2)
          

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.rtlsdr_source_0, 1), (self.wxgui_waterfallsink2_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 2), (self.wxgui_waterfallsink2_0_0_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_waterfallsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_waterfallsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

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
    tb = multiple_rtlsdr()
    tb.Start(True)
    tb.Wait()
