# JUSTINSTEPHEN_00000072126_OPTIMASI_MOBILENETV2_FISH_FRESHNESS
# Optimasi MobileNetV2 Menggunakan Strategi Fine-Tuning untuk Klasifikasi Kesegaran Ikan Berbasis Citra Digital
Optimized MobileNetV2 using transfer learning and fine-tuning for fish freshness classification based on fish eye images.

## 📖 Deskripsi Penelitian

Penelitian ini bertujuan untuk mengoptimalkan performa MobileNetV2 dalam melakukan klasifikasi kesegaran ikan berdasarkan citra mata ikan. Permasalahan utama dalam penentuan tingkat kesegaran ikan secara visual adalah kemiripan karakteristik antar kelas serta subjektivitas penilaian manusia. Oleh karena itu, penelitian ini menerapkan pendekatan Transfer Learning dan Fine-Tuning pada arsitektur MobileNetV2 untuk meningkatkan kemampuan ekstraksi fitur visual dan performa klasifikasi. :contentReference[oaicite:0]{index=0}

---

## 🎯 Tujuan Penelitian

- Mengembangkan model klasifikasi kesegaran ikan berbasis citra digital.
- Mengimplementasikan MobileNetV2 dengan strategi Transfer Learning.
- Mengoptimalkan performa model menggunakan Fine-Tuning.
- Menganalisis peningkatan performa setelah proses Fine-Tuning dilakukan.

---

## 📂 Dataset

Dataset yang digunakan adalah **Freshness of Fish Eyes (FFE)** yang terdiri dari citra mata ikan dengan tiga kategori tingkat kesegaran:

- Highly Fresh
- Fresh
- Not Fresh

Jumlah data yang digunakan dalam penelitian sebanyak **4.404 citra** setelah proses seleksi dan pembersihan data dilakukan.

---

## 🔬 Metodologi

Penelitian dilakukan menggunakan framework **Knowledge Discovery in Databases (KDD)** yang terdiri dari:

1. Data Selection
2. Data Preprocessing
3. Data Transformation
4. Model Development
5. Evaluation

Tahapan preprocessing yang dilakukan:

- Resize image 224×224
- Normalisasi citra
- Data augmentation
  - Rotation
  - Zoom
  - Horizontal Flip

---

## 🧠 Model Architecture

Model utama yang digunakan:

- MobileNetV2
- Transfer Learning
- Fine-Tuning

Konfigurasi:

| Parameter | Nilai |
|------------|---------|
| Input Size | 224 × 224 |
| Optimizer | Adam |
| Batch Size | 32 |
| Transfer Learning LR | 0.0003 |
| Fine-Tuning LR | 0.00001 |
| Output Class | 3 |

---

## 📊 Hasil Penelitian

### Transfer Learning

| Metric | Hasil |
|----------|---------|
| Validation Accuracy | 60.14% |
| Validation Loss | 0.86 |

### Fine-Tuning

| Metric | Hasil |
|----------|---------|
| Validation Accuracy | 69.48% |
| Validation Loss | 0.75 |
| Accuracy | 69.70% |
| Precision | 69.01% |
| Recall | 68.92% |
| F1-Score | 68.87% |

Penerapan Fine-Tuning berhasil meningkatkan validation accuracy dari 60,14% menjadi 69,48% serta meningkatkan performa klasifikasi secara keseluruhan. :contentReference[oaicite:1]{index=1}

---

## 📈 Evaluation Metrics

Evaluasi model dilakukan menggunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Grad-CAM

---

## 📁 Struktur Repository

```
.
├── dataset/
├── notebook/
│   └── skripsi_final.ipynb
├── model/
├── results/
│   ├── confusion_matrix.png
│   ├── training_result.png
│   └── gradcam.png
├── README.md
└── requirements.txt
```

---

## 💻 Requirements

```bash
tensorflow
keras
numpy
pandas
matplotlib
scikit-learn
opencv-python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 👨‍🎓 Author

**Justin Stephen**  
NIM: 00000072126  
Program Studi Sistem Informasi  
Universitas Multimedia Nusantara

---

## 📚 Citation

Justin Stephen. *Optimasi MobileNetV2 Menggunakan Strategi Fine-Tuning untuk Klasifikasi Kesegaran Ikan Berbasis Citra Digital*. Universitas Multimedia Nusantara, 2026.
