# 🚀 MCP Generator - Streamlit Sürümü (Kolay Kurulum)

## Neden Streamlit Versiyonu?

FastAPI/Uvicorn ile port sorunları yaşıyorsanız, **Streamlit versiyonu çok daha kolay ve güvenilir çalışır!**

### ✅ Avantajlar:
- **Tek komutla çalışır** - Port sorunları yok!
- **Otomatik açılır** - Tarayıcı otomatik başlar
- **Modern arayüz** - Güzel ve kullanıcı dostu
- **Daha az bağımlılık** - Daha stabil

---

## 📦 Kurulum

### 1. Gerekli paketleri yükle

```bash
pip install streamlit
```

Veya tüm bağımlılıkları yükle:

```bash
pip install -r requirements.txt
```

---

## 🚀 Çalıştırma (4 Kolay Yöntem)

### Yöntem 1: İnteraktif Launcher (Önerilen) ⭐

Bu script hem Web Interface hem de MCP Server seçeneği sunar:

**Mac/Linux:**
```bash
./start.sh
```

**Windows:**
```bash
start.bat
```

Menüden seçim yaparsın:
```
1) Web Interface (Streamlit) - Recommended ⭐
2) MCP Server (Python stdio)
```

### Yöntem 2: Direkt Web Interface

Sadece web arayüzü için:

**Mac/Linux:**
```bash
./start_web.sh
```

**Windows:**
```bash
start_web.bat
```

### Yöntem 3: Manuel Streamlit Komutu

```bash
streamlit run streamlit_app.py
```

### Yöntem 4: Belirli Port'ta Çalıştır

```bash
streamlit run streamlit_app.py --server.port 8080
```

### 💡 Hangisini Kullanmalıyım?

- **İlk kez kullanıyorsan:** `./start.sh` (veya `.bat`)
- **Sadece web interface istiyorsan:** `./start_web.sh` (veya `.bat`)
- **MCP Server olarak kullanmak istiyorsan:** `./start_mcp.sh` (veya `.bat`)

---

## 🎯 Kullanım

1. **Script'i çalıştır** - Yukarıdaki yöntemlerden birini kullan
2. **Tarayıcı açılır** - Otomatik olarak `http://localhost:8501` açılır
3. **4 adımlı wizard'ı takip et:**
   - **Adım 1:** Server adı, tip ve açıklama
   - **Adım 2:** Tool, resource ve prompt ekle
   - **Adım 3:** Ayarları gözden geçir
   - **Adım 4:** Server'ı oluştur ve indir

---

## 🎨 Özellikler

### ✨ Kullanıcı Dostu Arayüz
- Modern ve temiz tasarım
- Step-by-step wizard
- Gerçek zamanlı önizleme
- Hata kontrolleri

### 🛠️ Kapsamlı Server Desteği
- **Tool Server:** Claude'un çağırabileceği fonksiyonlar
- **Resource Server:** Claude'un okuyabileceği veri kaynakları
- **Full Server:** Tool + Resource + Prompt hepsi bir arada

### 📦 Hazır Paket
- Server kodu (.py)
- Requirements.txt
- README.md
- Tek ZIP dosyası - hepsi içinde!

---

## 🔧 Sorun Giderme

### Port zaten kullanımda?

Streamlit otomatik olarak farklı port seçer! Veya manuel belirle:

```bash
streamlit run streamlit_app.py --server.port 9000
```

### Tarayıcı açılmıyor?

Manuel olarak aç: http://localhost:8501

### Streamlit yüklü değil?

```bash
pip install streamlit
```

---

## 💡 İpuçları

1. **Wizard'ı sıfırla:** Sol sidebar'da "Reset Wizard" butonu
2. **Code önizleme:** Adım 4'te "Preview Generated Code" ile kodu incele
3. **Birden fazla server:** "Create Another Server" ile yeni server oluştur

---

## 🆚 FastAPI vs Streamlit

| Özellik | FastAPI (web_app.py) | Streamlit (streamlit_app.py) |
|---------|---------------------|------------------------------|
| Kurulum | Daha karmaşık | ✅ Çok kolay |
| Port sorunları | Olabilir | ✅ Yok |
| Başlatma | Manuel | ✅ Otomatik |
| API | REST API | Web UI |
| Kullanım | Programatik | ✅ Kullanıcı dostu |

**Tavsiye:** Sadece web arayüzü için kullanıyorsanız **Streamlit'i seçin!** ✅

---

## 📸 Örnek Kullanım

```bash
# 1. Streamlit'i yükle (ilk seferde)
pip install streamlit

# 2. Uygulamayı başlat
streamlit run streamlit_app.py

# 3. Tarayıcı otomatik açılır
# http://localhost:8501

# 4. Wizard'ı takip et ve server'ını oluştur!
```

---

## 🎓 Örnek: Calculator Server Oluşturma

1. **Adım 1 - Basic Info:**
   - Name: `calculator-server`
   - Type: `tool`
   - Description: `A simple calculator`

2. **Adım 2 - Add Tools:**
   - Tool 1: `add`
     - Parameters: `a:number:First number`, `b:number:Second number`
   - Tool 2: `multiply`
     - Parameters: `x:number:First number`, `y:number:Second number`

3. **Adım 3 - Review:** Ayarları kontrol et

4. **Adım 4 - Generate:** İndir ve kullan!

---

## 🚀 Hızlı Başlangıç (TL;DR)

```bash
# Mac/Linux
./start.sh

# Windows
start.bat

# Veya direkt
streamlit run streamlit_app.py
```

Tarayıcıda açılan sayfayı takip et - hepsi bu kadar! 🎉

---

## 📞 Yardım

Sorun mu yaşıyorsun?

1. `pip install streamlit` komutunu çalıştır
2. `streamlit run streamlit_app.py` ile başlat
3. Tarayıcıda http://localhost:8501 adresini aç

Hala çalışmıyor mu? Port numarasını değiştir:
```bash
streamlit run streamlit_app.py --server.port 9999
```

---

**Not:** FastAPI versiyonu (web_app.py) hala kullanılabilir ama port sorunları varsa Streamlit versiyonu **çok daha kolay ve güvenilir!** ✅
