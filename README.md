**#Multimodal Dataset Investigation for Hopeless Speech Detection in English**
This repository contains the dataset and code for the paper **"**Multimodal Dataset Investigation for Hopeless Speech Detection in English"**. In AI and Machine Learning for Social Forensics – Innovations in Intelligent Evidence Analysis. Springer Nature, 2026. (Forthcoming, Accepted, In-press).

Dillon Gatlin, Julian Lares-Ibarra, and Thejas G.S., _Multimodal Dataset Investigation for Hopeless Speech Detection in English_. In _AI and Machine Learning for Social Forensics – Innovations in Intelligent Evidence Analysis_. Springer Nature, 2026. (Forthcoming, Accepted, In-press).
## Textual Data Selection  

### 1. HopeEDI Preprocessing  

- **Utilizing the English portion of HopeEDI**, we processed the data:  
  - Removed usernames  
  - Removed punctuation  
  - Replaced emojis with text descriptions  
  - Normalized Unicode  
  - Removed single-character words  
  - Removed extra whitespaces  

- **Ensured row classification**:  
  - Removed empty or incorrect classifications  
  - Remaining data: **20,700 Non_Hope** and **1,945 Hope**  

- **Finalized textual portion of data**:  
  - Randomly chose **1,945 Non_Hope rows** to obtain a balanced dataset  
  - Split both datasets (Hope + Non_Hope) into **3 subsets**  
  - Due to uneven splitting, we standardized to **647 samples per class**  
  - Combined **647 Hope** + **647 Non_Hope** and matched them with image splits  
  - Final dataset: **3 CSV files**, each containing **1,294 rows** with an even split between Hope and Non_Hope

## MultiModal Creation  

### 2. image Sourcing  
- Collected 1,294 copyright-free images online, generated 1,294 Stable Diffusion images, and generated 1,294 Dall-E 3 images.  
- Images correlated with the textual context and classification.
- Stored the images in 3 folders, segmenting by their type.
- added file link paths to create CSV files for the 3 splits
- Handpicked images in folder "Images", Stable Diffusion in folder "Images_SD", DALLE 3 in folder "Images_DE"

### 3. Dataset Concatenation  
- Combined multiple image sources into one unified dataset  
- Verified no duplicate or corrupted files  
- Final dataset stored in "Complete_img"

## Model Training & Testing  

### 4. Model Training  
- Framework used: **[PyTorch / TensorFlow]**  
- Pretrained backbones/models tested:  
  - **CLIP** (Contrastive Language-Image Pretraining)  
  - **MobileNetV2** (lightweight CNN architecture)  
  - **FLIP** (Fast Language-Image Pretraining)  
  - **FLAVA** (Facebook’s multimodal transformer for vision + language tasks)
 
### 5. Testing & Evaluation  
-Evaluated Image classification
-Evaluated MultiModal classification
-Classifiers used after tokenization
  -LR (Logistic Regression)
  -RF (RandomForest)
  -XGB (XGBoost)
- Split the dataset into:  
  - **Training:** [70]%  
  - **Validation:** [15]%  
  - **Testing:** [15]%  
- Evaluation metrics:  
  - Precision / Recall / F1-score: **[values]**  

---
## This dataset falls under a Creative Commons Attribution 4.0 International license
For more information about this license, please visit: https://creativecommons.org/licenses/by/4.0/
Proper credit must be given to the creators of the original HopeEDI text dataset when using this multimodal version. This acknowledgment should be included in any derivative publications or shared works. Please cite the following references.
## Multimodal Hope dataset Citation
Dillon Gatlin, Julian Lares-Ibarra, and Thejas G.S., _Multimodal Dataset Investigation for Hopeless Speech Detection in English_. In _AI and Machine Learning for Social Forensics – Innovations in Intelligent Evidence Analysis_. Springer Nature, 2026. (Forthcoming, Accepted, In-press).
## HopeEDI Citation
Chakravarthi, B. R. (2020). HopeEDI: A Multilingual Hope Speech Detection Dataset for Equality, Diversity, and Inclusion. 
In *Proceedings of the Third Workshop on Computational Modeling of People’s Opinions, Personality, and Emotion’s in Social Media* (pp. 41–53). 
Association for Computational Linguistics. https://aclanthology.org/2020.peoples-1.5/
