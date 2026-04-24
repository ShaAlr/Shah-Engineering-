# 📦 FILE STRUCTURE & DESCRIPTION

## Sistem Rekomendasi Game Steam - Kelompok 12

---

## 📁 Daftar File yang Sudah Di-Download

Anda telah men-download **9 file** untuk aplikasi Steam Game Recommender:

---

### 🎯 FILE UTAMA

#### 1. **steam_recommender_app.py** (59 KB)
**Deskripsi:** File aplikasi utama Streamlit  
**Fungsi:** Berisi seluruh kode sistem rekomendasi  
**Status:** ✅ LENGKAP - All Steps 1-7 SELESAI

**Features:**
- ✅ Content-Based Filtering (TF-IDF + Cosine Similarity)
- ✅ Multi-parameter filtering (Genre, Budget, RAM)
- ✅ Dark theme modern UI
- ✅ 5 tabs lengkap:
  1. Rekomendasi Game
  2. Monitoring & Metrics (7 metrics)
  3. Visualisasi Data (7+ charts)
  4. EDA (Exploratory Data Analysis)
  5. Dokumentasi Proyek

**Yang sudah selesai:**
- ✅ Step 1: Define Objectives & Scope
- ✅ Step 2: Data Requirements
- ✅ Step 3: Exploratory Data Analysis
- ✅ Step 4: Data Preprocessing
- ✅ Step 5: Model Development
- ✅ Step 6: Deployment
- ✅ Step 7: Monitoring & Evaluation

---

### 📋 FILE KONFIGURASI

#### 2. **requirements.txt** (81 bytes)
**Deskripsi:** Dependencies Python yang dibutuhkan  
**Isi:**
```
streamlit==1.31.0
pandas==2.1.4
numpy==1.26.3
plotly==5.18.0
scikit-learn==1.4.0
```

**Cara install:**
```bash
pip install -r requirements.txt
```

#### 3. **config.toml** (303 bytes)
**Deskripsi:** Konfigurasi Streamlit  
**Lokasi:** Letakkan di folder `.streamlit/`  
**Fungsi:** Mengatur tema, warna, dan performance

**Struktur folder:**
```
.streamlit/
└── config.toml
```

---

### 📚 FILE DOKUMENTASI

#### 4. **README.md** (6.4 KB)
**Deskripsi:** Dokumentasi utama proyek  
**Isi:**
- Deskripsi proyek
- Features lengkap
- Cara instalasi
- System requirements
- Metodologi (TF-IDF, Cosine Similarity)
- Evaluation metrics
- Troubleshooting
- Referensi akademis

#### 5. **SETUP_GUIDE.md** (7.5 KB)
**Deskripsi:** Panduan setup lengkap step-by-step  
**Isi:**
- Langkah 1: Install Python
- Langkah 2: Download dataset (PENTING!)
- Langkah 3: Install dependencies
- Langkah 4: Jalankan aplikasi
- Langkah 5: Gunakan aplikasi
- Troubleshooting detail
- Tips penggunaan
- Checklist setup

#### 6. **QUICK_START.md** (1.1 KB)
**Deskripsi:** Panduan cepat mulai dalam 5 menit  
**Isi:**
- Quick steps
- Command-command penting
- Link dataset

---

### 🚀 FILE RUNNER

#### 7. **run.bat** (755 bytes)
**Deskripsi:** Script untuk menjalankan aplikasi di Windows  
**Cara pakai:** Double-click atau jalankan di Command Prompt  
**Fungsi:**
- Check apakah games.csv ada
- Install dependencies otomatis
- Jalankan aplikasi Streamlit

#### 8. **run.sh** (790 bytes)
**Deskripsi:** Script untuk menjalankan aplikasi di Mac/Linux  
**Cara pakai:**
```bash
chmod +x run.sh
./run.sh
```
**Fungsi:**
- Check apakah games.csv ada
- Install dependencies otomatis
- Jalankan aplikasi Streamlit

---

### 🧪 FILE TESTING

#### 9. **create_sample_dataset.py** (5.2 KB)
**Deskripsi:** Script untuk generate sample dataset (testing only)  
**WARNING:** Hanya untuk testing! Tidak untuk produksi!  
**Cara pakai:**
```bash
python create_sample_dataset.py
```
**Output:** `games_sample.csv` (50 games sample)

**Note:**
- Sample dataset tidak akurat untuk rekomendasi
- Gunakan hanya untuk memastikan aplikasi berjalan
- Untuk aplikasi sebenarnya, download dataset lengkap dari Kaggle

---

## ⚠️ FILE YANG MASIH DIBUTUHKAN

### **games.csv** (300+ MB) - BELUM ADA!

**STATUS:** ❌ HARUS DI-DOWNLOAD MANUAL

**Kenapa tidak disertakan?**
- File terlalu besar (300+ MB)
- Tidak bisa diupload ke sistem
- Harus download langsung dari Kaggle

**Cara Download:**

1. **Buka:** https://www.kaggle.com/datasets/fronkongames/steam-games-dataset
2. **Login** ke Kaggle (buat akun jika belum punya)
3. **Klik** tombol "Download"
4. **Extract** file `games.csv` dari zip
5. **Letakkan** di folder yang sama dengan `steam_recommender_app.py`

**Struktur folder akhir:**
```
steam-recommender/
├── steam_recommender_app.py
├── requirements.txt
├── README.md
├── SETUP_GUIDE.md
├── QUICK_START.md
├── run.bat
├── run.sh
├── create_sample_dataset.py
├── .streamlit/
│   └── config.toml
└── games.csv                    ← DOWNLOAD INI!
```

---

## 🎯 CARA MENGGUNAKAN

### Option 1: QUICK START (Recommended)

1. **Download dataset:**
   - https://www.kaggle.com/datasets/fronkongames/steam-games-dataset
   - Extract `games.csv`
   - Letakkan di folder ini

2. **Buat folder `.streamlit`:**
   ```bash
   mkdir .streamlit
   ```

3. **Copy `config.toml` ke `.streamlit/`:**
   ```bash
   # Windows
   move config.toml .streamlit\
   
   # Mac/Linux
   mv config.toml .streamlit/
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan:**
   ```bash
   # Windows
   run.bat
   
   # Mac/Linux
   chmod +x run.sh
   ./run.sh
   
   # Atau manual
   streamlit run steam_recommender_app.py
   ```

### Option 2: TESTING MODE (Tanpa Dataset Lengkap)

**WARNING:** Rekomendasi tidak akurat! Hanya untuk testing!

1. **Generate sample dataset:**
   ```bash
   python create_sample_dataset.py
   ```

2. **Rename sample:**
   ```bash
   # Windows
   rename games_sample.csv games.csv
   
   # Mac/Linux
   mv games_sample.csv games.csv
   ```

3. **Jalankan aplikasi:**
   ```bash
   streamlit run steam_recommender_app.py
   ```

---

## 📊 FITUR LENGKAP APLIKASI

### ✅ STEP 1-7 SEMUA SUDAH SELESAI!

**Step 1: Define Objectives & Scope**
- ✅ Problem definition
- ✅ Objectives
- ✅ Scope
- ✅ Key deliverables

**Step 2: Data Requirements**
- ✅ Dataset Kaggle Steam Games
- ✅ 50,000+ games
- ✅ Input/Output features identified

**Step 3: EDA**
- ✅ Dataset overview
- ✅ Statistical summary
- ✅ Missing values analysis
- ✅ Data quality insights

**Step 4: Preprocessing**
- ✅ Handling missing values
- ✅ Feature extraction (RAM, Price)
- ✅ Feature engineering
- ✅ Text processing

**Step 5: Model Development**
- ✅ TF-IDF Vectorization
- ✅ Cosine Similarity
- ✅ Filtering logic
- ✅ Ranking algorithm

**Step 6: Deployment**
- ✅ Streamlit application
- ✅ Interactive UI
- ✅ Dark modern theme
- ✅ Real-time recommendations

**Step 7: Monitoring & Evaluation**
- ✅ Precision@10 (Target: ≥70%)
- ✅ Recall@20 (Target: ≥50%)
- ✅ NDCG@10 (Target: ≥75%)
- ✅ Coverage (Target: ≥40%)
- ✅ Diversity (Target: ≥60%)
- ✅ MAP (Target: ≥65%)
- ✅ User Satisfaction (Target: ≥4.0/5.0)

---

## 🎨 UI FEATURES

### Dark Theme Modern
- Background gradient (navy, charcoal)
- Neon blue accents (#00d4ff)
- Poppins font
- Hover effects
- Interactive charts

### 5 Tabs Lengkap
1. **REKOMENDASI** - Game cards & filtering
2. **MONITORING** - 7 metrics dashboard
3. **VISUALISASI** - 7+ interactive charts
4. **EDA** - Data analysis
5. **DOKUMENTASI** - Complete guide

### Interactive Elements
- Multi-select genre
- Budget slider (USD/IDR)
- RAM selector
- Real-time filtering
- Responsive design

---

## 📈 METRICS & VISUALIZATIONS

### Metrics (Tab 2)
- Precision@10 dengan target indicator
- Recall@20 dengan visual comparison
- NDCG@10 dengan color coding
- Coverage measurement
- Diversity score
- MAP score
- User satisfaction gauge

### Visualizations (Tab 3)
1. Genre distribution (bar chart)
2. Price distribution (pie chart)
3. Rating distribution (histogram)
4. RAM requirements (bar chart)
5. Similarity score scatter plot
6. Top games by similarity
7. Price vs Rating correlation

---

## 💡 TIPS PENTING

### 1. Dataset adalah WAJIB!
- Tanpa `games.csv`, aplikasi tidak bisa jalan
- Download dari Kaggle: https://www.kaggle.com/datasets/fronkongames/steam-games-dataset
- File harus bernama `games.csv` (case-sensitive)

### 2. First Load Lambat
- Pertama kali load 1-2 menit (normal)
- Dataset 300+ MB perlu preprocessing
- Setelah itu cepat karena caching

### 3. RAM Requirement
- Minimal 4GB RAM
- Recommended 8GB+
- Close aplikasi berat lainnya

### 4. Browser Modern
- Chrome, Firefox, Safari, Edge
- Versi terbaru
- JavaScript enabled

---

## 🔧 TROUBLESHOOTING

**Error: games.csv not found**
→ Download dataset dari Kaggle dan letakkan di folder ini

**Error: Module not found**
→ `pip install -r requirements.txt`

**Aplikasi lambat**
→ Tunggu caching selesai, close aplikasi lain

**Port already in use**
→ `streamlit run steam_recommender_app.py --server.port 8502`

**Visual tidak muncul**
→ Refresh browser, check JavaScript enabled

---

## 📞 SUPPORT

**Kelompok 12 - ITS**
- Ghalib Ibrahim Zardy (5052231028)
- M Shah Aquilla Febryano (5052231043)

**Dokumentasi:**
- `QUICK_START.md` - Panduan cepat
- `SETUP_GUIDE.md` - Panduan lengkap
- `README.md` - Dokumentasi utama

---

## ✅ CHECKLIST FINAL

Sebelum menjalankan aplikasi, pastikan:

- [ ] Python 3.8+ terinstall
- [ ] File `games.csv` sudah ada (download dari Kaggle)
- [ ] Dependencies terinstall (`pip install -r requirements.txt`)
- [ ] Folder `.streamlit` dibuat
- [ ] File `config.toml` ada di `.streamlit/`
- [ ] RAM minimal 4GB available
- [ ] Browser modern tersedia

Jika semua ✅, siap untuk dijalankan! 🚀

---

**Developed with ❤️ by Kelompok 12 - ITS**  
**Proyek Sains Data 2024**
