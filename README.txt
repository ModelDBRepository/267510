S1 Coding Analysis
------------------

Simulations were conducted using a modified AdEx model. For details of the the AdEx model please see the Methods.
All simulations were performed in Brian2 with the Euler-Maruyama algorithm with fixed time step of 10 μs.

The files (Fig1,Fig2,Fig6) contain all the codes required to run the simulations shown in Fig1,Fig2 and Fig6. 

"adex_sine.py" includes the AdEx model. 
"Final_Code.ipynb" includes the sinusoidal current and synaptic input models. 



.mat files in each folder are the generated data obtained from running "Final_Code.ipynb". For example. "data0.mat" ... "data9.mat" include spike times of 10 different neuron models. 

In "Fig2" folder, .m files include the codes required to plot rasters, firing rate histogram, spectrum, and SNR. 

In "Fig6" folder, "analysis.py" includes the codes for ROC analysis (Fig6A). The other folders contain data for synaptic conductance model with two different Idc (65 and 90 pA), different frequecnies and different level of noise. The data are used for the analysis shown in  Fig6,B,C,D.  




For any questions about the code please contact: 
nooshin.abdollahi@mail.utoronto.ca  ,  aaronrshifman@gmail.com





