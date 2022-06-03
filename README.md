# Classification-of-plants-of-Southeast-Asia
This is the 3rd International Competition in Data Science & Artificial Intelligence, organized by The International Society of Data Scientists ([ISODS](https://www.isods.org/about-the-society)).
## Overview
#### About ISODS
The International Society of Data Scientists (or The ISODS), registered as a Massachusetts non-profit, is a professional organization for Data Science and AI practitioners and researchers, which may include Data Scientists, Machine Learning Scientists, AI Scientists, Data Analysts, Data Engineers, Software Engineers, Risk Analysts, Actuaries, Business Analysts, and more, who apply Data Science and AI at work. ISODS promotes Data Science and AI domestically in the United States as well as internationally via activities such as competitions, conferences, training, professional exams, and publications.
#### About track
Classification of plants of Southeast Asia is a track in the competition with Bali26 dataset. Bali26 is an image dataset dedicated to ethnobotany, the study of the interaction between people and plants. Bali26 is the first machine-vision ready image collection of ethnobotanically significant flora of south-east Asia, collected on the island of Bali in 2020 (and amended in 2021) together with Balinese residents with intimate local knowledge in coordination with expertise from the Indonesia National Research and Innovation Agency.

## Results
### Before balancing data
Models  | Score | Params
------------- | ------------- | ------------
Fine-tuned VGG16 (from layer 15)  | 0.93339 | 13,589,402 
Fine-tuned VGG16 (all layers)   | 0.91695 | 21,223,898
Fine-tuned Resnet50 (all layers)   | 0.92387 | 24,065,818
Fine-tuned InceptionResNetV2 (from layer 618)   | 0.94809 | 24,342,298
Fine-tuned InceptionResNetV2 (all layers)   | 0.80968 | 55,076,474
Fine-tuned InceptionV3 (all layers)   | 0.72923 | 22,830,778
Fine-tuned DenseNet201 (all layers)   | 0.76211 | 19,089,818

### After balancing data

Models  | Score | Params
------------- | ------------- | ------------
Fine-tuned VGG16 (from layer 15)  | 0.99826 | 13,589,402 
Fine-tuned VGG16 (all layers)   | 0.99913 | 21,223,898
Fine-tuned Resnet50 (all layers)   | 0.99826 | 24,065,818
Retrain Resnet50 (Don't use pretrain) | 0.99134 |23,587,866
Fine-tuned InceptionResNetV2 (from layer 618)   | 0.99913 | 24,342,298
Retrain InceptionResNetV2  (Don't use pretrain)  | 1.00000 | 54,316,154
Fine-tuned InceptionV3 (all layers)   |  |
Fine-tuned DenseNet201 (all layers)   |  | 
EfficientNet | |
