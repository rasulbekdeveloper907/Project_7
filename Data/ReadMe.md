# 📊 Kaggle Dataset Metadata Scraper (5000+ datasets)

Ushbu loyiha **Kaggle API** orqali **5000 ta dataset** haqida metadata (nomi, muallifi, yuklanish soni, litsenziyasi, hajmi, va h.k.) ni avtomatik tarzda yig‘adi va **CSV fayl** ko‘rinishida saqlaydi.

---

## 🚀 Loyihaning asosiy imkoniyatlari

✅ Kaggle API tokenni avtomatik sozlaydi  
✅ 5000 ta dataset ma’lumotini yig‘adi  
✅ Har bir dataset uchun to‘liq metadata oladi  
✅ Natijani `kaggle_datasets_5000.csv` fayliga saqlaydi  
✅ CSV fayl keyinchalik tahlil, reyting, yoki ML loyihalar uchun ishlatiladi  

---

## 🧩 Talablar

Ushbu loyihani ishlatish uchun quyidagi dasturlar o‘rnatilgan bo‘lishi kerak:

- **Python 3.8+**
- **pip**
- **Kaggle API** (`pip install kaggle`)
- **Pandas** (`pip install pandas`)

---

## 🔑 1. Kaggle API Token olish

1. [https://www.kaggle.com](https://www.kaggle.com) saytiga kiring  
2. Profil rasm ustiga bosib → **Account** bo‘limiga kiring  
3. Pastga tushing → **"Create New API Token"** tugmasini bosing  
4. Sizga `kaggle.json` fayl yuklanadi (API kalit)

---

## 📂 2. Tokenni joylashtirish

Token faylni quyidagi yo‘lga joylashtiring:  {"username":"rasulbekruzmetov","key":"e6624de23a078d4a984d392f6f8452d0"}

**Windows:**
```
C:\Users\<rasulbekruzmetov>\.kaggle\kaggle.json
```

**Linux / Mac:**
```
~/.kaggle/kaggle.json
```

Agar `.kaggle` papka mavjud bo‘lmasa — uni yarating.

---

## ⚙️ 3. Kerakli kutubxonalarni o‘rnatish

Terminal yoki CMD’da:
```bash
pip install --upgrade kaggle pandas
```

---

## 💻 4. Skript kodi (`setup_kaggle_api.py`)

Kodni `setup_kaggle_api.py` fayliga joylashtiring (README yuqorida keltirilgan).

---

## ▶️ 5. Ishga tushirish

Terminalda:
```bash
python setup_kaggle_api.py
```

---

## 📊 6. Natija — CSV fayl

Yaratilgan fayl: `kaggle_datasets_5000.csv`

Har bir satrda bitta dataset haqida quyidagi ma’lumotlar bo‘ladi:

| Ustun nomi | Tavsif |
|-------------|---------|
| ref | Kaggle’dagi unikal identifikator (`owner/dataset-name`) |
| title | Dataset nomi |
| ownerName | Egasi (Kaggle username) |
| size | Dataset hajmi |
| downloadCount | Yuklab olishlar soni |
| viewCount | Ko‘rishlar soni |
| voteCount | Upvote soni |
| usabilityRating | Foydalanuvchi reytingi (0–1 oralig‘ida) |
| licenseName | Litsenziya turi |
| url | Dataset URL manzili |
| creationDate | Yaratilgan sana |
| lastUpdated | Oxirgi yangilanish |
| tags | Mavzu yoki toifa (masalan: `finance`, `image`, `text`) |

---


