import argparse
import time
import brainflow.board_shim

from brainflow.board_shim import BoardShim, BrainFlowInputParams,BoardIds,LogLevels
from brainflow.data_filter import DataFilter, WindowOperations, WaveletTypes


params = BrainFlowInputParams()
params.serial_port = 'COM5' # Cambie esto al puerto serial correcto
board = BoardShim(2, params)
board.prepare_session()
sample_rate=BoardShim.get_sampling_rate(2)
board.start_stream()
time.sleep(90)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
data = board.get_board_data()  # get all data and remove it from internal buffer
board.stop_stream()
board.release_session()




eeg_channels = BoardShim.get_eeg_channels(2)
    # demo for transforms
for count, channel in enumerate(eeg_channels):
        print('Original data for channel %d:' % channel)
        print(data[channel])
        # demo for wavelet transforms
        # wavelet_coeffs format is[A(J) D(J) D(J-1) ..... D(1)] where J is decomposition level, A - app coeffs, D - detailed coeffs
        # lengths array stores lengths for each block
        wavelet_coeffs, lengths = DataFilter.perform_wavelet_transform(data[channel], WaveletTypes.DB5, 3)
        app_coefs = wavelet_coeffs[0: lengths[0]]
        detailed_coeffs_first_block = wavelet_coeffs[lengths[0]: lengths[1]]
        # you can do smth with wavelet coeffs here, for example denoising works via thresholds 
        # for wavelets coefficients
        restored_data = DataFilter.perform_inverse_wavelet_transform((wavelet_coeffs, lengths), data[channel].shape[0],
                                                                     WaveletTypes.DB5, 1)
        #print('Restored data after wavelet transform for channel %d:' % channel)
        #print(restored_data)

        # demo for fft, len of data must be a power of 2
        #fft_data = DataFilter.perform_fft(data[channel], WindowOperations.NO_WINDOW.value)
        # len of fft_data is N / 2 + 1
        #restored_fft_data = DataFilter.perform_ifft(fft_data)
        #print('Restored data after fft for channel %d:' % channel)
        #rint(restored_fft_data)



#print(data)
print(sample_rate)