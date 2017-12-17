import numpy as np
import math

#There are 8 neurons which spike for each of the 8 notes respectively
#snn is the spiking neural net which is the 8 bit state of the system showing which neurons are spiking based on the given musical note
#if a bit is 1 it means that neuron is firing at maximum rate for the given musical note, else it is 0
def main(currentArg, totalTimeArg, musicalNote):
    snn = []
    snn.append(LIFforC(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforD(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforE(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforF(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforG(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforA(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforB(currentArg, totalTimeArg, musicalNote))
    snn.append(LIFforHighC(currentArg, totalTimeArg, musicalNote))
    return snn


#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforC(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "C":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforD(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "D":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforE(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "E":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforF(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "F":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforG(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "G":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforA(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "A":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforB(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "B":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	
#function for LIF neuron, given the stimulus current in nA, total time to inject the current in msec, and the musical note
def LIFforHighC(currentArg, totalTimeArg, musicalNote):
	#initializing properties of the cell membrane
	R_m = 10 #resistance of the cell membrane [MOhm]
	C_m = 1 #capacitance of the cell membrane [nF]
	tau_m = R_m * C_m #time constant [msec]

	#time values
	totalTime = totalTimeArg #total time to inject current [msec]
	t_startCurrent = 0 #time to start injecting current [msec]
	t_stopCurrent = totalTime #time to stop injecting current [msec] 
	dt = 1 #steps of time [msec] ... in order to differentiate membrane potential with respect to time, we need to move in steps of dt
	timeArray =  np.arange(0, totalTime+dt, dt) #time intervals in array [msec] ... note: totalTime+dt makes totalTime inclusive
	
	ARP = 2 #absolute refractory period [msec] The neuron cannot spike during this time. Note: For the sake of convenience, we ignore the relative refractory period
	#Note: Value assigned to ARP has been taken from http://www.physiologyweb.com/lecture_notes/neuronal_action_potential/neuronal_action_potential_refractory_periods.html

	#membrane potential values
	Vrest = -70 #resting membrane potential [mV]
	V_m = np.zeros(len(timeArray)) * Vrest # membrane potential array [mV] i.e membrane potential will be calculated for each time step, for now it is initialized to Vrest because there is no spike yet.
	Vthresh = -55 #threshold potential [mV] ... Note: For the sake of convenience, we assume Vthresh remains constant i.e. threshold does not get higher and higher after consecutive spikes.
	Vspike = 20 #spike value for membrane potential [mV]
	Vdip = -75 #dip the membrane potential after a spike [mV] i.e. hyperpolarization
	#Note: Values assigned to Vrest and Vthresh have been taken from https://teaching.ncl.ac.uk/bms/wiki/index.php/Action_potential

	I = currentArg #the current to inject [nA]

	firingRate = 0 #for each input current stimulus, calculate firingRate [Hz]

	numSpikes = 0 #counter for the number of spikes
		
	beginNoCurrent = np.zeros(int(t_startCurrent/dt)) #no current until the time to start current
	injectCurrent = np.ones(int((t_stopCurrent - t_startCurrent + 1)/dt)) * I #duration for which we inject the current
	endNoCurrent = np.zeros(int((totalTime - t_stopCurrent)/dt)) #no current after the time to stop current

	#append all arrays into one array called current
	current = beginNoCurrent
	current = np.append(current, injectCurrent)
	current = np.append(current, endNoCurrent) 
		
	ARPOver = 0 #the neuron can now be allowed to spike [msec]. This value is initialized to zero, but it will be calculated after spike time.
	
	
	#set the bias so that this neuron will only spike for this note
	if musicalNote == "^C":
		bias = 1
	
	else:
		bias = 0
		
	U = 0 #the threshold for hopfield network which says if this neuron is on or off
	#run a loop through timeArray with counter t
	for t, time in enumerate(timeArray):
		
		if time>ARPOver: #absolute refractory period is over
			Vinf = Vrest + current[t] * R_m #V at infinity, i.e. membrane potential exponentially decays towards Vinf
			V_m[t] = Vinf + ((V_m[t-1] - Vinf) * math.exp(-dt/tau_m)) #calculate membrane potential (explanation given in theory note above)
			
			if V_m[t] > Vthresh and bias==1: #membrane potential is over the threshold and it is the required note
				V_m[t] = Vspike #neuron spikes
				numSpikes += 1 #incrememnt number of spikes
				ARPOver = time+ARP #neuron goes into refractory period
				
		else: #still in absolute refractory period
			V_m[t] = Vdip #hyperpolarization after spike		

	firingRate = numSpikes/((t_stopCurrent - t_startCurrent + 1)/1000) #time is converted from msec to sec, so that firingRate can be in Hz. numSpikes depends on input current so firing rate is a function of input current.
	
	
	#if firing rate crosses the threshold the neuron is on
	if firingRate > U:
		return 1 #neuron is on
	else:
		return 0 #neuron is off
	