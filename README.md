# 神易數兵占 | Shenyishu Military Divination System

**講武全書兵佔卷之十六 · 明州玄谷蔡時宜撰**

---

[中文](#中文說明) | [English](#english)

---

## 中文說明

### 簡介

**神易數**是一套基於《講武全書》卷十六的古代兵佔推演系統。本系統運用天干地支、八卦、五行、神煞等傳統易學理論，對指定時間進行軍事吉凶推演，為研究中國古代兵學與易學的交叉領域提供工具。

《講武全書》為明代重要兵書，其中兵佔卷由明州玄谷蔡時宜所撰，融合易學與軍事決策，將八卦、五行、干支等術數體系應用於行軍佈陣的吉凶判斷。本程式即以此為藍本，忠實還原其推演邏輯，並以現代計算方式呈現。

### 功能特色

- 🔮 **干支推演** — 自動計算年、月、日、時四柱干支
- ☯️ **八卦與五行** — 連山卦、歸藏卦、八卦及五行分析
- ⚔️ **行軍佔** — 總數分析（主將、我兵、賊寇三方對比）
- 🏯 **主客判斷** — 陰陽數理判定主客形勢
- 🌟 **神煞系統** — 貴人、驛馬、天財、魁元、羊刃、正祿、白虎、血光、破碎、劫殺等
- 📊 **吉凶評分** — 綜合評分與等級（大吉、吉、平、凶、大凶）
- 🖥️ **多種介面** — 命令列（CLI）、JSON 輸出、Web 伺服器、Streamlit 互動網頁

### 系統架構

```
┌──────────────────────────────────────┐
│      神易數兵占系統 (Shenyishu)       │
│  基於《講武全書》卷十六 · 蔡時宜撰   │
└──────────────┬───────────────────────┘
               │
    ┌──────────┴──────────┐
    │  shenyishu.py 核心  │
    │  (干支·八卦·五行·   │
    │   神煞·評分演算)    │
    └──┬──────┬────────┬──┘
       │      │        │
  ┌────▼──┐ ┌─▼─────┐ ┌▼──────────┐
  │CLI/   │ │HTTP   │ │Streamlit  │
  │JSON   │ │Server │ │Web App    │
  │輸出   │ │+ API  │ │(app.py)   │
  └───────┘ └──┬────┘ └───────────┘
               │
          ┌────▼─────┐
          │index.html│
          │靜態網頁  │
          └──────────┘
```

### 推演算法

系統的核心推演流程如下：

```
陽曆日期（年月日時）
    ↓
透過 sxtwl 壽星天文曆轉換為農曆
    ↓
計算四柱干支（年柱·月柱·日柱·時柱）
    ↓
查甲子碼表取得各柱數碼
    ↓
四柱數碼相加 → 總數
    ↓
拆解百位·十位·個位 → 主將·我兵·賊寇
    ↓
對應八卦與陰陽屬性
    ↓
計算神煞（貴人·驛馬·天財 等 12 種）
    ↓
綜合評分 → 判定等級：大吉/吉/平/凶/大凶
```

#### 甲子碼表

系統內建六十甲子碼表，將每一組干支組合對應到一個特定數值（10–289）。四柱干支分別查表後相加即為**總數**。

#### 總數分析（行軍佔）

總數的各位數分別代表不同的軍事角色：

| 位數 | 代表 | 說明 |
|------|------|------|
| 百位 | 主將 | 統帥的氣勢與能力 |
| 十位 | 我兵 | 己方兵力的強弱 |
| 個位 | 賊寇 | 敵方的氣勢與威脅 |

- **奇數**（1、3、5、7、9）為**陽數**，代表剛強有力
- **偶數**（0、2、4、6、8）為**陰數**，代表柔弱不利

#### 五行生剋

系統運用五行理論分析四柱干支之間的關係：

| 關係 | 循環 |
|------|------|
| 相生 | 金 → 水 → 木 → 火 → 土 → 金 |
| 相剋 | 金 → 木 → 土 → 水 → 火 → 金 |

並依據時令判斷五行的**旺相休囚死**狀態：

| 季節 | 旺 | 相 | 休 | 囚 | 死 |
|------|----|----|----|----|-----|
| 春   | 木 | 火 | 水 | 金 | 土  |
| 夏   | 火 | 土 | 木 | 水 | 金  |
| 秋   | 金 | 水 | 土 | 火 | 木  |
| 冬   | 水 | 木 | 金 | 土 | 火  |

### 神煞系統

系統根據年柱干支計算以下 12 種神煞，並據此進行吉凶評分：

| 神煞 | 性質 | 評分影響 | 說明 |
|------|------|---------|------|
| 貴人 | 吉 | +30 | 遇貴人相助，大利行軍 |
| 天財 | 吉 | +20 | 財運亨通，軍糧充足 |
| 魁元 | 吉 | +15 | 將星高照，領導有方 |
| 驛馬 | 吉/凶 | +15 / −40 | 利於行動；若「馬帶刀」則大凶 |
| 寶馬 | 吉 | +30 | 良駒在側，行軍迅捷 |
| 飲泉食谷 | 吉 | +15 | 糧草充足，軍心穩定 |
| 白虎 | 凶 | −25 | 主殺伐，有血光之災 |
| 血光 | 凶 | −30 | 傷亡之象，不宜輕進 |
| 破碎 | 凶 | −20 | 器物損壞，陣形散亂 |
| 劫殺 | 凶 | −15 | 遭遇劫掠，損兵折將 |
| 羊刃 | 參考 | — | 剛烈之象，需配合其他神煞判斷 |
| 正祿 | 參考 | — | 祿位所在，關乎官運 |

### 吉凶評分等級

| 等級 | 分數範圍 | 含義 | 建議 |
|------|---------|------|------|
| 🟢 大吉 | ≥ 40 | 出征大吉，諸事順利 | 宜出兵、宜進攻 |
| 🟢 吉 | 20 ~ 39 | 出兵有利，可行軍事 | 宜行動、宜部署 |
| 🟡 平 | 0 ~ 19 | 吉凶參半，謹慎行事 | 宜觀望、宜防守 |
| 🔴 凶 | −20 ~ −1 | 不宜出兵，另擇吉日 | 宜退守、宜避戰 |
| 🔴 大凶 | ≤ −21 | 兵佔大凶，切勿妄動 | 宜固守、宜撤退 |

### 安裝

```bash
pip install -r requirements.txt
```

**依賴套件：**

| 套件 | 版本 | 用途 |
|------|------|------|
| [sxtwl](https://pypi.org/project/sxtwl/) | ≥ 1.0.0 | 壽星天文曆 — 農曆與干支計算 |
| [streamlit](https://streamlit.io/) | ≥ 1.24.0 | 互動式網頁介面框架 |
| [pendulum](https://pendulum.eustace.io/) | ≥ 3.0.0 | 日期時間處理與時區支援 |

### 使用方式

#### 命令列模式

```bash
# 基本使用（預設時間）
python shenyishu.py

# 指定時間
python shenyishu.py --year 2024 --month 3 --day 15 --hour 10

# 簡寫參數
python shenyishu.py -y 2024 -m 3 -d 15 -t 10
```

#### JSON 輸出

```bash
python shenyishu.py --year 2024 --month 3 --day 15 --hour 10 --json
```

<details>
<summary>📋 JSON 輸出範例（點擊展開）</summary>

```json
{
  "生辰": "2024年3月15日10時",
  "干支": {
    "年": "甲辰",
    "月": "丁卯",
    "日": "庚午",
    "時": "辛巳"
  },
  "總數": 539,
  "總數分析": {
    "百位": { "數": 5, "卦": "中", "陰陽": "陽" },
    "十位": { "數": 3, "卦": "坤", "陰陽": "陽" },
    "個位": { "數": 9, "卦": "離", "陰陽": "陽" }
  },
  "主客判斷": {
    "結論": "主將強於我兵 - 陽數吉利",
    "分析": ["主將強於我兵", "陽數賊寇衰弱"]
  },
  "連山卦": "巽",
  "歸藏卦": "乾",
  "神煞": {
    "貴人": "艮",
    "驛馬": "巽",
    "天財": "離",
    "魁元": "坎",
    "白虎": "離",
    "血光": "巽",
    "破碎": "巽",
    "劫殺": "艮"
  },
  "吉凶": {
    "level": "吉",
    "score": 25,
    "detail": "出兵有利，可行軍事",
    "reasons": [
      "天財加持(+20)",
      "魁元照臨(+15)",
      "破碎殺伐(-20)",
      "劫殺顯現(-15)"
    ]
  }
}
```

</details>

#### Web 伺服器模式

```bash
# 啟動伺服器（預設埠 8080）
python shenyishu.py --server

# 指定埠
python shenyishu.py --server --port 9090
```

啟動後可訪問：
- 網頁介面：`http://localhost:8080`
- API 端點：`http://localhost:8080/api/bingzhan?year=2024&month=3&day=15&hour=10`

#### Streamlit 互動網頁

```bash
streamlit run app.py
```

啟動後瀏覽器自動開啟 `http://localhost:8501`，提供：
- 📅 日期時間選擇器（支援「現在」快捷按鈕，自動取用香港時區）
- 🧮 **排盤**分頁 — 干支資訊、神卦、總數分析、主客判斷、神煞、吉凶判斷，以彩色卡片呈現
- 📄 **排盤文字**分頁 — 純文字格式輸出，方便複製存檔
- 📖 **說明**分頁 — 系統介紹與使用指南

### API 參數

| 參數   | 說明   | 類型  | 預設值 |
|--------|--------|-------|--------|
| `year` | 年份   | int   | 2023   |
| `month`| 月份   | int   | 7      |
| `day`  | 日期   | int   | 4      |
| `hour` | 時辰（24小時制） | int | 22 |

### CLI 參數一覽

| 參數 | 簡寫 | 說明 | 預設值 |
|------|------|------|--------|
| `--year` | `-y` | 年份 | 2023 |
| `--month` | `-m` | 月份 | 7 |
| `--day` | `-d` | 日期 | 4 |
| `--hour` | `-t` | 時辰 | 22 |
| `--json` | `-j` | 以 JSON 格式輸出 | — |
| `--server` | `-s` | 啟動 Web 伺服器 | — |
| `--port` | `-p` | 伺服器埠號 | 8080 |

### 系統依賴

- Python 3.6+
- [sxtwl](https://pypi.org/project/sxtwl/) — 壽星天文曆（中國農曆計算庫）
- [Streamlit](https://streamlit.io/) — 互動式網頁應用框架
- [Pendulum](https://pendulum.eustace.io/) — 日期時間與時區處理

### 檔案結構

```
shenyishu/
├── shenyishu.py       # 核心推演引擎（干支、八卦、五行、神煞、評分、CLI、HTTP 伺服器）
├── app.py             # Streamlit 互動網頁應用
├── templates/
│   └── index.html     # 靜態 HTML 網頁介面（配合 HTTP 伺服器使用）
├── .streamlit/
│   └── config.toml    # Streamlit 主題配置（暗色底 + 金色主調）
├── requirements.txt   # Python 依賴套件
└── README.md          # 本說明文件
```

---

## English

### Introduction

**Shenyishu** (神易數) is an ancient Chinese military divination system based on Volume 16 of *"The Complete Book of Military Arts"* (講武全書). The system uses traditional Chinese metaphysics — Heavenly Stems and Earthly Branches (天干地支), Eight Trigrams (八卦), Five Elements (五行), and Spirit Stars (神煞) — to perform auspiciousness analysis for military affairs based on a given date and time.

*"The Complete Book of Military Arts"* is an important Ming Dynasty military treatise. The divination volume was authored by Cai Shiyi (蔡時宜) of Mingzhou Xuangu, who integrated Yi Jing (Book of Changes) theory with military decision-making. This program faithfully reproduces the original computational logic using modern tools.

### Features

- 🔮 **Stem-Branch Calculation** — Automatic computation of the Four Pillars (year, month, day, hour)
- ☯️ **Trigrams & Five Elements** — Lianshan, Guicang, Bagua, and Wuxing analysis
- ⚔️ **Military Analysis** — Numerical analysis of commander, troops, and enemy forces
- 🏯 **Host-Guest Judgment** — Yin-Yang determination of strategic positions
- 🌟 **Spirit Stars System** — Noble Person, Post Horse, Heavenly Wealth, Star Chief, Blade, Official Salary, White Tiger, Blood Light, Broken, Robbery Star, and more
- 📊 **Auspiciousness Score** — Comprehensive scoring with five levels (Great Fortune, Fortune, Neutral, Misfortune, Great Misfortune)
- 🖥️ **Multiple Interfaces** — CLI, JSON output, HTTP server, and Streamlit interactive web app

### System Architecture

```
┌──────────────────────────────────────┐
│     Shenyishu Divination System      │
│  Based on "Complete Book of          │
│  Military Arts" Vol. 16              │
└──────────────┬───────────────────────┘
               │
    ┌──────────┴──────────┐
    │  shenyishu.py Core  │
    │  (Stems · Trigrams · │
    │   Elements · Stars · │
    │   Scoring Engine)    │
    └──┬──────┬────────┬──┘
       │      │        │
  ┌────▼──┐ ┌─▼─────┐ ┌▼──────────┐
  │CLI /  │ │HTTP   │ │Streamlit  │
  │JSON   │ │Server │ │Web App    │
  │Output │ │+ API  │ │(app.py)   │
  └───────┘ └──┬────┘ └───────────┘
               │
          ┌────▼─────┐
          │index.html│
          │Static UI │
          └──────────┘
```

### Calculation Algorithm

The core divination flow works as follows:

```
Solar Date (Year / Month / Day / Hour)
    ↓
Convert to Lunar Calendar via sxtwl library
    ↓
Compute Four Pillars (Year · Month · Day · Hour Stem-Branch pairs)
    ↓
Look up each pillar in the Jiazi Code Table (60 entries, values 10–289)
    ↓
Sum the four codes → Total Number
    ↓
Decompose into Hundreds · Tens · Units → Commander · Troops · Enemy
    ↓
Map each digit to a Trigram and Yin/Yang polarity
    ↓
Calculate Spirit Stars (12 types based on year pillar)
    ↓
Aggregate score → Determine level: Great Fortune / Fortune / Neutral / Misfortune / Great Misfortune
```

#### Total Number Analysis (Military Divination)

Each digit of the total represents a different military role:

| Digit | Represents | Meaning |
|-------|-----------|---------|
| Hundreds | Commander (主將) | Leadership strength and ability |
| Tens | Our Troops (我兵) | Strength of allied forces |
| Units | Enemy (賊寇) | Enemy threat and momentum |

- **Odd digits** (1, 3, 5, 7, 9) = **Yang** — strong, auspicious
- **Even digits** (0, 2, 4, 6, 8) = **Yin** — weak, inauspicious

#### Five Elements (五行)

The system uses Five Elements theory to analyze relationships between the Four Pillars:

| Relationship | Cycle |
|-------------|-------|
| Generation (相生) | Metal → Water → Wood → Fire → Earth → Metal |
| Suppression (相剋) | Metal → Wood → Earth → Water → Fire → Metal |

Seasonal strength is also assessed (Prosperous · Prime · Resting · Imprisoned · Dead).

### Spirit Stars System

The system computes 12 Spirit Stars from the year pillar and scores them:

| Spirit Star | Nature | Score | Description |
|------------|--------|-------|-------------|
| Noble Person (貴人) | Auspicious | +30 | Assistance from influential allies |
| Heavenly Wealth (天財) | Auspicious | +20 | Abundant supplies and resources |
| Star Chief (魁元) | Auspicious | +15 | Strong leadership qualities |
| Post Horse (驛馬) | Mixed | +15 / −40 | Mobility advantage; "Horse with Blade" is very inauspicious |
| Treasure Horse (寶馬) | Auspicious | +30 | Swift movement and fine steeds |
| Spring & Grain (飲泉食谷) | Auspicious | +15 | Ample provisions, stable morale |
| White Tiger (白虎) | Inauspicious | −25 | Conflict and bloodshed |
| Blood Light (血光) | Inauspicious | −30 | Casualties and injuries |
| Broken (破碎) | Inauspicious | −20 | Equipment loss and disarray |
| Robbery Star (劫殺) | Inauspicious | −15 | Raiding and losses |
| Blade (羊刃) | Reference | — | Fierce energy; interpretation depends on context |
| Official Salary (正祿) | Reference | — | Position of official fortune |

### Auspiciousness Levels

| Level | Score Range | Meaning | Recommendation |
|-------|-----------|---------|----------------|
| 🟢 Great Fortune (大吉) | ≥ 40 | All signs favorable | Advance and attack |
| 🟢 Fortune (吉) | 20 – 39 | Conditions are favorable | Proceed with plans |
| 🟡 Neutral (平) | 0 – 19 | Mixed signs | Proceed with caution |
| 🔴 Misfortune (凶) | −20 – −1 | Conditions unfavorable | Defend and wait |
| 🔴 Great Misfortune (大凶) | ≤ −21 | All signs unfavorable | Retreat and fortify |

### Installation

```bash
pip install -r requirements.txt
```

**Dependencies:**

| Package | Version | Purpose |
|---------|---------|---------|
| [sxtwl](https://pypi.org/project/sxtwl/) | ≥ 1.0.0 | Chinese Astronomical Calendar — lunar date & stem-branch computation |
| [Streamlit](https://streamlit.io/) | ≥ 1.24.0 | Interactive web application framework |
| [Pendulum](https://pendulum.eustace.io/) | ≥ 3.0.0 | Date/time handling with timezone support |

### Usage

#### Command Line

```bash
# Basic usage (default date/time)
python shenyishu.py

# Specify date and time
python shenyishu.py --year 2024 --month 3 --day 15 --hour 10

# Short flags
python shenyishu.py -y 2024 -m 3 -d 15 -t 10
```

#### JSON Output

```bash
python shenyishu.py --year 2024 --month 3 --day 15 --hour 10 --json
```

<details>
<summary>📋 JSON Output Example (click to expand)</summary>

```json
{
  "生辰": "2024年3月15日10時",
  "干支": {
    "年": "甲辰",
    "月": "丁卯",
    "日": "庚午",
    "時": "辛巳"
  },
  "總數": 539,
  "總數分析": {
    "百位": { "數": 5, "卦": "中", "陰陽": "陽" },
    "十位": { "數": 3, "卦": "坤", "陰陽": "陽" },
    "個位": { "數": 9, "卦": "離", "陰陽": "陽" }
  },
  "主客判斷": {
    "結論": "主將強於我兵 - 陽數吉利",
    "分析": ["主將強於我兵", "陽數賊寇衰弱"]
  },
  "連山卦": "巽",
  "歸藏卦": "乾",
  "神煞": {
    "貴人": "艮",
    "驛馬": "巽",
    "天財": "離",
    "魁元": "坎",
    "白虎": "離",
    "血光": "巽",
    "破碎": "巽",
    "劫殺": "艮"
  },
  "吉凶": {
    "level": "吉",
    "score": 25,
    "detail": "出兵有利，可行軍事",
    "reasons": [
      "天財加持(+20)",
      "魁元照臨(+15)",
      "破碎殺伐(-20)",
      "劫殺顯現(-15)"
    ]
  }
}
```

</details>

#### Web Server

```bash
# Start server (default port 8080)
python shenyishu.py --server

# Custom port
python shenyishu.py --server --port 9090
```

Once running, access:
- Web UI: `http://localhost:8080`
- API endpoint: `http://localhost:8080/api/bingzhan?year=2024&month=3&day=15&hour=10`

#### Streamlit Interactive Web App

```bash
streamlit run app.py
```

Opens automatically at `http://localhost:8501`, featuring:
- 📅 Date & time selectors (with a "Now" shortcut button using Hong Kong timezone)
- 🧮 **Chart** tab — Stem-branch info, trigrams, total analysis, host-guest judgment, spirit stars, and auspiciousness displayed as colorful cards
- 📄 **Text** tab — Plain text output for easy copying
- 📖 **Instructions** tab — System guide and references

### API Parameters

| Parameter | Description | Type | Default |
|-----------|-------------|------|---------|
| `year`    | Year        | int  | 2023    |
| `month`   | Month       | int  | 7       |
| `day`     | Day         | int  | 4       |
| `hour`    | Hour (24h)  | int  | 22      |

### CLI Flags

| Flag | Short | Description | Default |
|------|-------|-------------|---------|
| `--year` | `-y` | Year | 2023 |
| `--month` | `-m` | Month | 7 |
| `--day` | `-d` | Day | 4 |
| `--hour` | `-t` | Hour | 22 |
| `--json` | `-j` | Output in JSON format | — |
| `--server` | `-s` | Start HTTP server | — |
| `--port` | `-p` | Server port number | 8080 |

### Requirements

- Python 3.6+
- [sxtwl](https://pypi.org/project/sxtwl/) — Chinese Astronomical Calendar library
- [Streamlit](https://streamlit.io/) — Interactive web application framework
- [Pendulum](https://pendulum.eustace.io/) — Date/time and timezone library

### Project Structure

```
shenyishu/
├── shenyishu.py       # Core engine (stems, trigrams, elements, stars, scoring, CLI, HTTP server)
├── app.py             # Streamlit interactive web application
├── templates/
│   └── index.html     # Static HTML interface (served by the HTTP server)
├── .streamlit/
│   └── config.toml    # Streamlit theme config (dark background + gold accents)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## 參考文獻 | References

- 《講武全書》兵佔卷之十六，明州玄谷蔡時宜撰
- [壽星天文曆 sxtwl](https://pypi.org/project/sxtwl/) — 中國農曆計算庫
- 中國傳統術數：天干地支、八卦、五行、神煞理論

## 致謝 | Acknowledgments

- **蔡時宜**（明代）— 原書《講武全書》兵佔卷作者
- **sxtwl 壽星天文曆** — 提供精確的農曆與干支計算
- **Streamlit** — 提供簡潔高效的 Python 網頁框架
- 排盤介面設計參考 [kentang2017/kinliuren](https://github.com/kentang2017/kinliuren)

## 授權 | License

此項目僅供學術研究與文化傳承之用。

This project is for academic research and cultural heritage purposes.
