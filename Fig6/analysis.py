import pickle
from pathlib import Path

import numpy as np
from brian2 import Hz, second, ms
from scipy.signal import find_peaks
from sklearn import metrics
from tqdm import tqdm


def gaussian(x, mu, sig):
    """Create gaussian waveform on domain x

    :param x: Values to compute over
    :param mu: Gaussian center
    :param sig: Gaussian variance
    :return: gaussian(x)
    """

    return 1. / (np.sqrt(2. * np.pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.) / 2)


def infer_frequency(spike_times, t1=0.6, t2=0.3, res=0.1, prom=0.5, time_step=0.01):
    """Try to infer the frequency from the superposition method.

    :param spike_times: Spike times
    :param t1: Variance of the isi gaussian
    :param t2: Variance of the diff gaussian
    :param res: Width of the ISI bins
    :param prom: Minimum prominence
    :param time_step: Width of the frequency bins
    :return: Inferred frequency
    """
    try:
        isi_bin = np.arange(0, 350, res)
        isi = np.diff(spike_times)

        # replace ISI with sum of gaussians at each ISI value
        isi_hist_g = np.sum(np.vstack([gaussian(isi_bin, i, t1) for i in isi]), axis=0)
        isi_hist_g /= isi_hist_g.sum() # normalize gaussian

        pks, _ = find_peaks(isi_hist_g, prominence=prom)
        pk_location_diffs = np.diff(isi_bin[pks]) # find difference between peaks (ix+n skipping value)

        peak_loc_bins = np.arange(0, 15, time_step)
        peak_hist_g = np.sum(np.vstack([gaussian(peak_loc_bins, pk, t2) for pk in pk_location_diffs]), axis=0)

        return 1000 / (peak_loc_bins[np.argmax(peak_hist_g)])
    except:
        return np.nan  # lots can go wrong but in all cases assume nan


def infer_amplitude(spike_times):
    """Infer a proxy for the amplitude

    :param spike_times: Times of the spikes
    :return: Number of spikes (proxy for amplitude)
    """

    return len(spike_times)


def discriminate(d1, d2, a, b):
    """ Discriminate between 2 sets of measures

    :param d1: Measure 1
    :param d2: Measure 2
    :param a: True value of d1
    :param b: True value of d2
    :return: Roc of discrimination
    """

    if a > b:
        d1, d2 = d2, d1

    # clean values from d1 and d2
    # if there's any funny business both are set to 0 i.e. 50/50 disc.
    d1 = np.array(d1)
    d1[~np.isfinite(d1)] = 0
    d1 = d1[np.isfinite(d1)].tolist()

    d2 = np.array(d2)
    d2[~np.isfinite(d2)] = 0
    d2 = d2[np.isfinite(d2)].tolist()

    score = d1 + d2 # concatenate
    true_value = [0] * len(d1) + [1] * len(d2)

    try:
        false_positive_rate, true_positive_rate, threshold = metrics.roc_curve(list(map(int, true_value)), score,
                                                                               pos_label=int(1))
        auc = metrics.auc(false_positive_rate, true_positive_rate)
        return auc
    except:
        Warning('Something went wrong')
        return 0


def create_param_range(x0, x1, res):
    """ Create a set of parameters.

    :param x0: Lower bound
    :param x1: Upper bound
    :param res: Step size
    :return: Parameter set
    """

    return np.arange(x0, x1 + res, res)


def evaluate_amplitude_discrimination(model, *, a0, a1, res, unit, f0=100, f1=600, t_max=10 * second):
    """ Test a model for amplitude discrimination

    :param model: Model to run
    :param a0: Min amplitude
    :param a1: Max amplitude
    :param res: Amplitude resolution
    :param unit: Amplitude unit (amp or siemens)
    :param f0: Min frequency
    :param f1: Max frequency
    :param t_max: Sim length
    :return: Spike time, inferred amp. measure
    """
    trial_amplitude = create_param_range(a0, a1, res)
    model.store('initial') # set initial state

    # create placeholders
    spike_times = {}
    infered_amplitude = {}

    for amp in tqdm(trial_amplitude):
        model.restore('initial') # reset initial conditions
        model.set_stimulus_current(amp * unit)

        model.f = np.random.uniform(f0, f1, model.neurons.N) * Hz # set a random frequency

        model.run(t_max, report=None)
        spike_times[amp] = model.spike_train
        infered_amplitude[amp] = list(map(infer_amplitude, model.spike_train.values()))

    return spike_times, infered_amplitude


def evaluate_frequency_discrimination(model, *, f0, f1, res, unit, a0=50, a1=100, t_max=10 * second,
                                      t1=None, t2=None, prom=None, infer_res=0.25, time_step=0.05):
    """ Test a model for frequency discrimination

    :param model: Model to run
    :param f0: Min frequency
    :param f1: Max frequency
    :param res: Frequency resolution
    :param unit: Amplitude unit (amp or siemens)
    :param a0: Min amplitude
    :param a1: Max amplitude
    :param t_max: Sim length
    :param t1: Disc parameter t1
    :param t2: Disc parameter t2
    :param prom: Min prominence
    :param infer_res: Disc parameter infer_res
    :param time_step: Disc parameter time_Step
    :return: Spike time, inferred freq. measure
    """

    trial_frequency = create_param_range(f0, f1, res)
    model.store('initial') # set initial state

    # create placeholders
    spike_times = {}
    infered_frequency = {}

    for freq in tqdm(trial_frequency):
        model.restore('initial') # reset initial conditions

        model.f = freq * Hz
        model.set_stimulus_current(np.random.uniform(a0, a1, model.neurons.N) * unit)

        model.run(t_max, report=None)
        spike_times[freq] = model.spike_train

        if t1 is not None:
            infered_frequency[freq] = list(map(lambda x:
                                               infer_frequency(x / ms, t1=t1, t2=t2, prom=prom,
                                                               res=infer_res, time_step=time_step),
                                               model.spike_train.values()))
    return spike_times, infered_frequency


def save(sim_name, sim_type, spike_times, infered_values):
    """ Save a set of results

    :param sim_name: Name of simulation
    :param sim_type: amplitude or frequency
    :param spike_times: Dict of spike times
    :param infered_values: Measure for each experiment
    """

    with open(Path('save_data') / f'{sim_name}_{sim_type}.pkl', 'wb') as f:
        pickle.dump((spike_times, infered_values), f, protocol=pickle.HIGHEST_PROTOCOL)


def load(sim_name, sim_type):
    """ Load a given sim_name and class

    :param sim_name: Name of a simulation
    :param sim_type: amplitude or frequency
    :return: Data
    """

    with open(Path('save_data') / f'{sim_name}_{sim_type}.pkl', 'rb') as f:
        return pickle.load(f)


def load_amplitude(sim_name):
    """ Helper function to load an amplitude sim

    :param sim_name: Name of the simulatiion
    :return: Data
    """

    return load(sim_name, 'A')


def load_frequency(sim_name):
    """ Helper function to load a frequency sim

    :param sim_name: Name of the simulatiion
    :return: Data
    """

    return load(sim_name, 'f')


def save_amplitude(sim_name, spike_times, infered_amplitude):
    """ Helper function to save an amplitude sim

    :param sim_name: Name of the simulatiion
    :param spike_times: Dict of spike times
    :param infered_amplitude: Infered amplitude
    """

    save(sim_name, 'A', spike_times, infered_amplitude)


def save_frequency(sim_name, spike_times, infered_frequency):
    """ Helper function to save a frequency sim

    :param sim_name: Name of the simulatiion
    :param spike_times: Dict of spike times
    :param infered_frequency: Infered freq
    """
    save(sim_name, 'f', spike_times, infered_frequency)


def discrimination_combinations(infered_values):
    """ Compute discrimination for all combinations.

    :param infered_values: param:measure dict of inferred values
    :return: Meshgrid for x, y (param_x, param_x) and z (discriminability)
    """

    levels = list(infered_values.keys())
    x = y = levels

    xx, yy = np.meshgrid(x, y)
    z = np.array(
        [discriminate(infered_values[x], infered_values[y], x, y) for (x, y) in zip(np.ravel(xx), np.ravel(yy))])
    zz = z.reshape(xx.shape)

    return xx, yy, zz
