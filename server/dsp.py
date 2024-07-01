from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
sys.path.append(str(ROOT))

from library.build import eicpp

def generate_features(implementation_version, draw_graphs, raw_data, axes, sampling_freq,
                      average, minimum, maximum):
    features = []
    graphs = []

    if (len(raw_data) < 1):
        raise ConfigurationError('Input data must not be empty')

    # reshape first
    raw_data = raw_data.reshape(int(len(raw_data) / len(axes)), len(axes))

    for ax in range(0, len(axes)):
        data_for_current_axis = raw_data[:, ax]

        if average:
            features.append(eicpp.avg(data_for_current_axis))
        if minimum:
            features.append(eicpp.min(data_for_current_axis))
        if maximum:
            features.append(eicpp.max(data_for_current_axis))

    if (len(features) == 0):
        raise Exception('No output features, enable at least one parameter')

    return {
        'features': features,
        'graphs': graphs,
        # if you use FFTs then set the used FFTs here (this helps with memory optimization on MCUs)
        'fft_used': [],
        'output_config': {
            # type can be 'flat', 'image' or 'spectrogram'
            'type': 'flat',
            'shape': {
                # shape should be { width, height, channels } for image, { width, height } for spectrogram
                'width': len(features)
            }
        }
    }
