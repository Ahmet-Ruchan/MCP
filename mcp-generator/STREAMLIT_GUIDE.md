# 🤖 MCP Generator - AI-Powered Streamlit (Yeni Versiyon!)

## 🌟 Yeni Özellikler

### ✨ Claude AI Entegrasyonu
- **Akıllı Kod Üretimi**: Artık Claude API ile profesyonel MCP sunucuları otomatik oluşturuluyor!
- **Best Practices**: Claude, en iyi uygulamaları ve error handling'i otomatik ekliyor
- **Production-Ready**: Oluşturulan kod direkt kullanıma hazır

### 🎨 Yeni Modern Arayüz
- **Tek sayfa**: Wizard yok, her şey aynı sayfada
- **Kullanıcı dostu**: Daha temiz ve anlaşılır input alanları
- **Pop-up yok**: Her şey site içinde, inline preview
- **Real-time**: Anlık önizleme ve güncelleme

### ✅ Avantajlar:
- **Claude AI ile akıllı üretim** - Şablon değil, gerçek AI! 🤖
- **Tek komutla çalışır** - Port sorunları yok!
- **Otomatik açılır** - Tarayıcı otomatik başlar
- **Modern arayüz** - Çok daha güzel ve profesyonel
- **Inline kod gösterimi** - Pop-up yok, her şey sayfada

---

## 📦 Kurulum

### 1. Gerekli paketleri yükle

```bash
pip install streamlit anthropic
```

Veya tüm bağımlılıkları yükle:

```bash
pip install -r requirements.txt
```

### 2. Claude API Key Al

Claude API kullanmak için bir API key'e ihtiyacın var:

1. **https://console.anthropic.com** adresine git
2. Hesap oluştur veya giriş yap
3. API key oluştur
4. Key'i kopyala (örn: `sk-ant-...`)

**İki yöntemle kullanabilirsin:**

**A) Sidebar'da gir** (Önerilen)
- Uygulamayı aç
- Sol sidebar'da API Key input alanına yapıştır

**B) Environment variable olarak ayarla**
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
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

## 🎯 Kullanım (Yeni Tek Sayfa Arayüz!)

### Adım 1: Uygulamayı Başlat
```bash
./start_web.sh          # Mac/Linux
start_web.bat           # Windows
```

Tarayıcın otomatik açılır: `http://localhost:8501`

### Adım 2: Claude API Key'ini Gir

Sol sidebar'da:
- **Claude API Key** alanına key'ini yapıştır
- Veya environment variable'dan otomatik alır

### Adım 3: Server Bilgilerini Doldur (Tek Sayfada!)

**📝 Basic Information** (Sol kolon):
- **Server Name**: `my-calculator-server`
- **Server Type**: `tool`, `resource`, veya `full` seç
- **Description**: Ne yaptığını açıkla

**🔧 Components** (Sağ kolon):
- **➕ Add Tool**: Tool ekle (name, description, parameters)
- **➕ Add Resource**: Resource ekle (URI, name, MIME type)
- **➕ Add Prompt**: Prompt ekle (sadece full server için)

### Adım 4: Componentleri Ekle

**Tool Örneği:**
```
Name: calculate
Description: Performs mathematical operations
Parameters (her satır):
  x:number:First number
  y:number:Second number
  operation:string:Operation to perform (+, -, *, /)
```

**Resource Örneği:**
```
URI: data://weather
Name: Weather Data
Description: Current weather information
MIME Type: application/json
```

### Adım 5: Claude ile Oluştur! 🤖

- Tüm bilgileri girdikten sonra
- **🤖 Generate with Claude AI** butonuna bas
- Claude akıllıca MCP server kodunu yazacak
- **Production-ready** kod oluşturulacak!

### Adım 6: Kodu İncele ve İndir

Kod oluşturulunca:
- **📄 server.py** sekmesinde tam kodu gör
- **📋 Preview** sekmesinde kurulum talimatlarını gör
- **⬇️ Download ZIP** ile indir
- İçinde `server.py`, `requirements.txt`, `README.md` var!

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
