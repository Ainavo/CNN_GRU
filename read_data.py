<<<<<<< HEAD
import mne
import scipy.io as scio
import numpy as np

def read_data(data_path,i):
    data_path = data_path
    DATA = scio.loadmat(data_path)
    DATA = DATA["data"][0]
    DATA = DATA[i] #第i次实验，从3到8
    EEG_DATA = DATA["X"][0][0].transpose(1,0)
    EEG_label = DATA['y'][0][0][:,0]

    ch_names = ['Fz','Fp1','Fp2','AF3','AF4','AF7','AF8','C3','POz','Cz','PO3','C4','PO4','PO5','PO6','PO7','PO8','Oz','O1','Pz','P6','P7','EOG-left','EOG-central','EOG-right']
    ch_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg',
                'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg',
                'eeg','eeg','eog','eog','eog']

    info = mne.create_info(ch_names = ch_names,
                            ch_types=ch_types,
                            sfreq=250)
    info.set_montage('standard_1020')
    raw = mne.io.RawArray(EEG_DATA,info)

    n_times = DATA["trial"][0][0][:,0] #时间戳
    event = np.zeros((4,12),int)
    v,b,n,m=0,0,0,0
    for i in range (0,n_times.shape[0]):
        if EEG_label[i]==1:
            event[0,v]=n_times[i]
            v+=1
        if EEG_label[i]==2:
            event[1,b]=n_times[i]
            b+=1
        if EEG_label[i]==3:
            event[2,n]=n_times[i]
            n+=1
        if EEG_label[i]==4:
            event[3,m]=n_times[i]
            m+=1


    events = np.zeros((48,3),int)
    j=0
    for i in range(events.shape[0]):
        if i<12:
            events[i][0]=event[0][j]
            events[i][2]=1
        elif i<24:
            events[i][0]=event[1][j]
            events[i][2]=2
        elif i<36:
            events[i][0]=event[2][j]
            events[i][2]=3
        elif i<48:
            events[i][0]=event[3][j]
            events[i][2]=4
        j+=1
        if j>=12:
            j=0
    events = sorted(events, key = lambda events: events[0])
    event_id = dict(lefthand=1,righthand=2,feet=3,tongue=4)
    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, ecg=False,
                    exclude='bads')
    epochs = mne.Epochs(raw, events, event_id, tmin=3, tmax=6, proj=True,baseline=(None, None), picks=picks,preload=True)


    data = epochs.get_data()
    data =np.array(data).reshape((48*22,751))
    label = EEG_label.repeat(22)
    return data,label
=======
import mne
import scipy.io as scio
import numpy as np

def read_data(data_path,i):
    data_path = data_path
    DATA = scio.loadmat(data_path)
    DATA = DATA["data"][0]
    DATA = DATA[i] #第i次实验，从3到8
    EEG_DATA = DATA["X"][0][0].transpose(1,0)
    EEG_label = DATA['y'][0][0][:,0]

    ch_names = ['Fz','Fp1','Fp2','AF3','AF4','AF7','AF8','C3','POz','Cz','PO3','C4','PO4','PO5','PO6','PO7','PO8','Oz','O1','Pz','P6','P7','EOG-left','EOG-central','EOG-right']
    ch_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg',
                'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg',
                'eeg','eeg','eog','eog','eog']

    info = mne.create_info(ch_names = ch_names,
                            ch_types=ch_types,
                            sfreq=250)
    info.set_montage('standard_1020')
    raw = mne.io.RawArray(EEG_DATA,info)

    n_times = DATA["trial"][0][0][:,0] #时间戳
    event = np.zeros((4,12),int)
    v,b,n,m=0,0,0,0
    for i in range (0,n_times.shape[0]):
        if EEG_label[i]==1:
            event[0,v]=n_times[i]
            v+=1
        if EEG_label[i]==2:
            event[1,b]=n_times[i]
            b+=1
        if EEG_label[i]==3:
            event[2,n]=n_times[i]
            n+=1
        if EEG_label[i]==4:
            event[3,m]=n_times[i]
            m+=1


    events = np.zeros((48,3),int)
    j=0
    for i in range(events.shape[0]):
        if i<12:
            events[i][0]=event[0][j]
            events[i][2]=1
        elif i<24:
            events[i][0]=event[1][j]
            events[i][2]=2
        elif i<36:
            events[i][0]=event[2][j]
            events[i][2]=3
        elif i<48:
            events[i][0]=event[3][j]
            events[i][2]=4
        j+=1
        if j>=12:
            j=0
    events = sorted(events, key = lambda events: events[0])
    event_id = dict(lefthand=1,righthand=2,feet=3,tongue=4)
    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, ecg=False,
                    exclude='bads')
    epochs = mne.Epochs(raw, events, event_id, tmin=3, tmax=6, proj=True,baseline=(None, None), picks=picks,preload=True)


    data = epochs.get_data()
    data =np.array(data).reshape((48*22,751))
    label = EEG_label.repeat(22)
    return data,label
>>>>>>> 01d5a4b6f6a345f8700056939e9080b3b1b1a0e5
