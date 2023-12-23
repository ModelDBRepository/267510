"""
Model specification

Subsequent models are created by overwriting the amplitude units and forms to get desired inputs
"""

ADEX_MODEL = """
dv/dt=(i_l+i_adapt+i_noise_ex+i_noise_in+i_injected+i_input + i_flux + i_m-w)/c : volt
dw/dt=(a*(v-e_l)-w)/tau_w : amp

i_l = -g_l*(v-e_l) : amp
i_adapt = g_l*DeltaT*exp((v-v_T)/DeltaT) : amp
i_noise_ex = -g_noise_ex*(v-e_ex) : amp
i_noise_in = -g_noise_in*(v-e_in) : amp

di_flux/dt = (-i_flux)/(10*ms) + sigma_flux*sqrt(2/(10*ms))*xi_77 : amp

i_m = -g_adapt*z*(v-e_k) : amp
dz/dt = (1/(1+exp((beta_z - v)/gamma_z)) - z)/ tau_z : 1

g_adapt : siemens
e_k : volt
beta_z : volt
gamma_z : volt
tau_z : second

sigma_flux : amp

dnoise_ex/dt = (mu_ex-noise_ex)/tau_noise_ex + sigma_ex*sqrt(2/tau_noise_ex)*xi_1 : siemens
g_noise_ex = noise_ex*int(noise_ex>0*siemens) : siemens

dnoise_in/dt = (mu_in-noise_in)/tau_noise_in +sigma_in*sqrt(2/tau_noise_in)*xi_2: siemens
g_noise_in = noise_in*int(noise_in>0*siemens) : siemens 

v_reset: volt
v_T: volt
v_thresh: volt
a: siemens
b: amp
i_injected : amp
DeltaT : volt

e_ex : volt
e_in : volt

tau_w : second (constant)

e_l : volt (constant)
g_l : siemens (constant)
c : farad (constant)

tau_noise_ex : second (constant)
mu_ex : siemens (constant)
sigma_ex : siemens (constant)

tau_noise_in: second (constant)
sigma_in : siemens (constant)
mu_in : siemens (constant)

f : hertz (constant)
"""

CURRENT_INPUT = """
A : amp (constant)
"""
SINE_INPUT = """
i_input = A*sin(2*pi*f*t)+A: amp
"""

SAW_INPUT = """
i_input = -A*((f*t) % 1)+A: amp
"""

SUMMATION_OFFSET = """
offset = offset_switch*(offset_A*x**4 + offset_B*x**3 + offset_C*x**2 + offset_D*x + offset_E):1
x = f/(1*Hz): 1

offset_A : 1 (constant)
offset_B : 1 (constant)
offset_C : 1 (constant)
offset_D : 1 (constant)
offset_E : 1 (constant)

tau_input_1: second (constant)
tau_input_2: second (constant)

offset_switch: 1 (constant)
"""

EXP2SYN_WAVEFORM = """
dinput/dt = ((tau_input_2 / tau_input_1) ** (tau_input_1 / (tau_input_2 - tau_input_1))*input_aux-input)/tau_input_1 : 1
dinput_aux/dt  = - input/tau_input_2 : 1
"""

SYNAPTIC_INPUT_CURRENT = """
i_input = A*(input-offset)*int(t>10*ms): amp
"""

CONDUCTANCE_INPUT = """
A: siemens (constant)
"""

SYNAPTIC_CONDUCTANCE_FLAT = """
i_input = i_excite + i_inhib: amp
# i_inhib = -offset*g_i*(v-e_in): amp
i_excite = -A*input*(v-e_ex): amp

g_i : siemens (constant)
"""

SYNAPTIC_CONDUCTANCE_STIM = """
dinput_inhib/dt = ((tau_inhibition_2 / tau_inhibition_1) ** (tau_inhibition_1 / (tau_inhibition_2 - tau_inhibition_1))*input_inhib_aux-input_inhib)/tau_inhibition_1 : 1
dinput_inhib_aux/dt  = - input_inhib/tau_inhibition_2 : 1

tau_inhibition_1: second
tau_inhibition_2: second

#i_input = i_excite + i_inhib: amp
#i_inhib  = -g_i*input_inhib*(v-e_in): amp
#i_excite = -A*input*(v-e_ex): amp

f_non = f/(1*Hz): 1
i_input = -(A/f_non)* input * (v-e_ex): amp

g_i : siemens (constant)
"""
