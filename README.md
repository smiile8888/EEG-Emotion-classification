# Emotion Classification using DEAP Dataset

It is difficult to classify human emotions based on the electroencephalogram (EEG). 
In this project, the Support Vector Machine (SVM) is used to classify emotions trained on the DEAP dataset to 
predict emotions based on arousal-valence dimension.
The DEAP dataset is a multimodal dataset for the analysis of human affective states [\[1\]](#references). 
The electroencephalogram (EEG) and peripheral physiological signals of 32 participants were 
recorded as each watched 40 one-minute-long excerpts of music videos. 
Each participant was asked for doing self-assessment to rate each video in terms of 
the levels of arousal, valence, like/dislike, dominance and familiarity. 
For 22 of the 32 participants, frontal face video was also recorded [\[1\]](#references). 

## Methodology
### 1. Data Preprocessing
The data of each participant has 32 EEG channels with four labels (valence, arousal, dominance, liking) (see details on 
[DEAP Dataset](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/)). These values is decomposed to five features by using 
Wavelet Transform [\[2\]]()
These five features are based on the frequency of the signals: 
1) Delta (< 4 Hz)
2) Theta (4-7 Hz)
3) Alpha (8-15 Hz)
4) Beta (16-31 Hz)
5) Gamma (> 32 Hz)

Two ranges of frequencies are removed (0-0.5 Hz to avoid the artifacts, and near 50 Hz to reduce the effect of power line on signals).

### 2. Modeling
The traditional SVM with default parameters as a classifier is used to be a model. However, other classifiers, 
such as neural networks and deep learning models should be applied in comparison in future work.

## Dependencies
To install dependencies of this project:

```python setup.py```

## Running Program
To start the program:
1. Download [DEAP Dataset](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/) (you need to sign disclosure). We will use `data_preprocessed_python`, make sure you download the right one.
2. Put the entire folder in the same working directory
3. Make sure you edit the path, `DATASET_PATH` variable in `load_deap.py` regarding the path of data
4. Run `load_deap.py` to get the data ready for training
5. Run `svm_clas.py` to train the model

## References
1. Koelstra, S., Muhl, C., Soleymani, M., Lee, J.S., Yazdani, A., Ebrahimi, T., Pun, T., Nijholt, A. and Patras, I., 2011. 
Deap: A database for emotion analysis; using physiological signals. _IEEE transactions on affective computing_, 3(1), pp.18-31.

#
**Disclaimer:** This project originally published by [Raghav714](https://github.com/Raghav714/EEG-Emotion-classification). 
I modified the code to be compatible with **Python3**, updated the libraries, and refactored the code and document accordingly. 
This project is just-for-fun.