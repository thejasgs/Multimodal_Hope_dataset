## 📂 Data Selection  

### 1. HopeEDI Preprocessing  
-Utilizing the English portion of HopeEDI, we processed the data
  -remove usernames
  -removes punctuation
  -replace emojis with description
  -normalize unicode
  -remove single-character words
  -removes the whitespaces
-Ensured row classification
  -removed any empty or incorrect classifications
  -20,700 Non_hope and 1945 Hope remained
-Finalized textual portion of data
  -randomly chose 1945 Non_hope rows to obtain a balanced dataset
  -Split both 1945 data sets into 3
  -because of the uneven split, we went down to 647 per classification
  -647 Non_hope and 647 Hope were combined and labeled per image split.
  -The final textual data was 3 CSV files containing 1294 rows, with an even split between hope and Non_hope 

## 📂 MultiModal Creation  

### 2. image Sourcing  
- Collected 1,294 copyright-free images online, generated 1,294 Stable Diffusion images, and generated 1,294 Dall-E 3 images.  
- Images correlated with the textual context and classification.
- Stored the images in 3 folders, segmenting by their type.
- added file link paths to create CSV files for the 3 splits

### 3. Dataset Concatenation  
- Combined multiple image sources into one unified dataset  
- Verified no duplicate or corrupted files  
- Final dataset stored in "Complete_img"

## 🧪 Model Training & Testing  

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

Chakravarthi, B. R. (2020). HopeEDI: A Multilingual Hope Speech Detection Dataset for Equality, Diversity, and Inclusion. 
In *Proceedings of the Third Workshop on Computational Modeling of People’s Opinions, Personality, and Emotion’s in Social Media* (pp. 41–53). 
Association for Computational Linguistics. https://aclanthology.org/2020.peoples-1.5/
