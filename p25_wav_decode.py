#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: P25 Wav Decode
# Generated: Sat Apr 25 14:53:07 2015
##################################################

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import dsd

class p25_wav_decode(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "P25 Wav Decode")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=8000,
                taps=None,
                fractional_bw=None,
        )
        self.dsd_block_ff_0 = dsd.block_ff(dsd.dsd_FRAME_AUTO_DETECT,dsd.dsd_MOD_AUTO_SELECT,3,True,2)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("p25_raw_unencrypted_edf.wav", True)
        self.audio_sink_0 = audio.sink(48000, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_0, 0), (self.dsd_block_ff_0, 0))    
        self.connect((self.dsd_block_ff_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = p25_wav_decode()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()
