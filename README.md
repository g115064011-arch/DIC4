# DIC4: Overleaf Draft for IEEE Conference using MCP and OpenSpec

> **專案名稱**：AI SOC Analyst Agent — IEEE Conference Draft & Spec-Driven Development (DIC4)  
> **關聯專案 (DIC3)**：[DIC3-AI-SOC-Agent (GitHub)](https://github.com/g115064011-arch/DIC3-AI-SOC-Agent.git)  
> **交付儲存庫 (DIC4)**：[DIC4 (GitHub)](https://github.com/g115064011-arch/DIC4.git)  
> **組別名單**：第 16 組（蘇恩平、周妤、袁靖淇、蕭宥瑄）  
> **更新日期**：2026 年 11 月  

---

## 📌 執行摘要（Executive Summary）

本專案為 **DIC4** 核心成果交付，包含：
1. **IEEE Conference 論文草稿重構**：以 DIC3 核心成果（AI SOC Analyst Agent）為基礎，修正過往草稿之重大錯誤，依循標準 IEEEtran 雙欄會議論文規範建立完整模組化 LaTeX 專案。
2. **學術 A–F Checkpoint 嚴格驗證**：在 Abstract 與各章節中落實 Attention Getter (A)、But (B)、Cure (C)、Development (D)、Experiments (E)、Expected Outcomes (F) 六段標準學術標籤與實證數據。
3. **OpenSpec 規格驅動開發（SDD）結構**：在 GitHub 上完整建置 `openspec/` 規格樹狀結構，涵蓋核心 Capabilities 形式化規格（RFC 2119 規範詞彙）與 `000-abstract` 至 `006-reference` 變更提案。
4. **Agent 核心模組實作**：以 Python 實作八大架構模組（GBDT 機率校準、TreeSHAP 特徵解釋、MITRE ATT&CK STIX 2.1 知識檢索、SQL 日誌工具、證據融合與人機協同升級閘門）。
5. **雙版本 PDF 交付（一好一壞）**：
   - 🔴 **壞的草稿 PDF**（`DIC4_Bad_Draft_Erroneous.pdf`）：標註診斷出的五大致命問題，含主題錯置、Checkpoints 缺乏實證、Overleaf 引用警告等。
   - 🟢 **好的正式 PDF**（`DIC4_Good_Final_IEEE_Conference.pdf`）：修正完畢的標準 IEEE 雙欄會議論文，具備完整八大模組架構圖、演算法虛擬碼、實證對照表與 16 篇已驗證文獻。
6. **Overleaf 專案同步與 MCP 指引**：提供 Overleaf 專案 (`6afafb3ef4ed8b43cc1d222`) 之完整模組化原始碼與 MCP 串接操作指引。

---

## 🔍 草稿錯誤診斷與修正對照（Bad vs. Good Comparison）

| 檢核維度 | 🔴 壞的草稿版本（Erroneous Draft） | 🟢 修正好的正式版本（Corrected Final Draft） |
|---|---|---|
| **專題研究主題** | **致命錯置**：誤植為「台灣房地產實價登錄分析代理人」(Taiwan Housing Intelligence Agent)，完全偏離第 16 組之資安研究主體。 | **對齊專題**：嚴格回歸 DIC3 專題主體 **AI SOC Analyst Agent**（結合機器學習分級、MITRE ATT&CK 領域知識與有界 LLM 推理之資安告警分級代理人）。 |
| **Checkpoints A–F** | 僅形式標籤，缺乏 2026 最新官方與產業實證數據支撐；未清楚界定 TP/BP/FP 分級價值。 | 完整引用 2026 實證數據：國安局 2.63M 次外部侵擾（嚴格區隔內部 SOC 告警）、IBM 499 萬美元外洩代價、Mandiant 14 天潛伏期、40.4% LLM 漏判率、ExCyTIn-Bench 0.606 基準分數。 |
| **系統架構與規格** | 概念模糊，未定義 RFC 2119 規範詞彙（SHALL/MUST），無人因自滿防護設計。 | 形式化定義八大功能模組（①–⑧）、具備 RFC 2119 規範詞彙、Tool Contracts（表 II）與非對稱錯誤成本安全升級邏輯。 |
| **核心控制演算法** | 無演算法虛擬碼；遇查詢日誌為空時直接誤判結案（落入 premature closure 陷阱）。 | 提供 **Algorithm 1: Bounded ReAct+RAG with Evidence Gate**，設計 Evidence Gate 主動防止空日誌偽陰性結案並觸發人工複核。 |
| **文獻格式與編譯狀態** | 在 Overleaf 中以裸網址 `\bibitem` 塞入，產生 3 處 `citation undefined` 與 `empty bibentry` 編譯警告（如 Overleaf 截圖所示）。 | 模組化 `references.bib`，收錄 16 篇 Peer-reviewed 頂級文獻（AI 與 Domain 各 50%），含合法 DOI/URL，Overleaf 編譯 **0 警告、0 錯誤**。 |
| **LaTeX 檔案架構** | 單一混雜的 `main.tex`（超過 400 行），難以由 MCP 多代理人分工協同維護。 | 模組化結構：`preamble.tex`、`authors.tex`、`references.bib`、`sections/00_abstract.tex` 至 `07_conclusion.tex`。 |

---

## 📂 專案目錄結構（Repository Layout）

```text
DIC4/
├── .agents/                      # Agent 技能與工作流
│   ├── skills/                   # OpenSpec 專屬 skills (apply, propose, explore...)
│   └── workflows/                # opsx 任務標準流程 (apply, archive, sync...)
├── openspec/                     # 規格驅動開發 (SDD) 核心結構
│   ├── config.yaml               # OpenSpec 設定檔
│   ├── project.md                # 專案背景與 RFC 2119 關鍵字規範
│   ├── specs/                    # 形式化 Capabilities 規格 (incident-triage 等)
│   └── changes/                  # Active 與分章變更提案
│       ├── 000-abstract/         # A–F Checkpoint 規格與任務清單
│       ├── 001-introduction/     # Introduction 與背景脈絡任務清單
│       ├── 002-related-work/     # 文獻回顧與 Table I 任務清單
│       ├── 003-proposed-design/  # 八大架構與 Algorithm 1 任務清單
│       ├── 004-experiment/       # GUIDE 與 ExCyTIn 雙評測任務清單
│       ├── 005-conclusion/       # 結論與人機協同任務清單
│       ├── 006-reference/        # BibTeX 查證與規範化任務清單
│       └── refactor-ai-soc-agent-proposal/
├── paper/                        # IEEE Conference LaTeX 完整模組套件
│   ├── IEEEtran.cls              # IEEE 官方 Conference 樣式類別檔
│   ├── main.tex                  # 論文主編譯入口檔
│   ├── preamble.tex              # 數學符號與巨集設定
│   ├── authors.tex               # 第 16 組作者與機構資訊
│   ├── references.bib            # 16 篇已查證真實文獻庫
│   ├── README.md                 # 論文專用說明檔
│   └── sections/                 # 獨立論文章節檔
│       ├── 00_abstract.tex       # 標註 Checkpoints A–F 之摘要
│       ├── 01_introduction.tex   # Section I (A–D 貢獻)
│       ├── 02_related_work.tex   # Section II (50% AI / 50% Domain & Table I)
│       ├── 03_domain_analysis.tex# Section III (5 大思維與 3 大爭論)
│       ├── 04_system_architecture.tex # Section IV (8 大模組、Table II、Algorithm 1)
│       ├── 05_experimental_design.tex # Section V (GUIDE 1M 筆評測設計)
│       ├── 06_expected_outcomes.tex   # Section VI (Pareto 取捨與效度威脅)
│       └── 07_conclusion.tex     # Section VII (總結與展望)
├── src/                          # 可執行的 AI SOC Analyst Agent 原始碼
│   └── soc_agent/
│       ├── __init__.py
│       ├── models.py             # 核心資料結構與 RFC 2119 Schema
│       ├── analytics.py          # GBDT 機率校準與 TreeSHAP 解釋
│       ├── knowledge.py          # MITRE ATT&CK STIX 2.1 RAG & NIST Playbooks
│       ├── evidence.py           # SQL 日誌查詢工具與防提早結案檢查
│       ├── fusion.py             # 證據融合與升級決策引擎
│       ├── agent.py              # Bounded ReAct 規劃器
│       └── cli.py                # 互動式告警分級展示 CLI
├── deliverables/                 # 交付成果 PDF
│   ├── DIC4_Bad_Draft_Erroneous.pdf        # 🔴 壞的草稿 PDF（含 5 大錯誤審查標註）
│   └── DIC4_Good_Final_IEEE_Conference.pdf # 🟢 好的正式 PDF（標準 IEEE 雙欄排版）
├── DIC4_Bad_Draft_Erroneous.pdf            # 根目錄便民副本
├── DIC4_Good_Final_IEEE_Conference.pdf     # 根目錄便民副本
├── DESIGN.md                     # 系統架構詳細設計規格書
└── README.md                     # 本檔案
```

---

## 🚀 快速上手與驗證指引

### 1. 驗證 OpenSpec SDD 規格
在終端機中執行 OpenSpec 規格校驗：
```bash
npx @fission-ai/openspec validate refactor-ai-soc-agent-proposal
```

### 2. 執行 AI SOC Analyst Agent CLI
執行展示腳本，模擬對真實資安事件進行自動化證據蒐集、MITRE ATT&CK 對應、NIST SP 800-61r3 處置與人機協同升級決策：
```bash
python -m src.soc_agent.cli
```

### 3. 同步至 Overleaf
- **Overleaf 專案網址**：`https://www.overleaf.com/project/6afafb3ef4ed8b43cc1d222`
- **同步步驟**：
  1. 將本儲存庫 `paper/` 資料夾下的所有檔案直接上傳至 Overleaf。
  2. 在 Overleaf 左上方確認編譯引擎為 **pdfLaTeX**，主文件設定為 `main.tex`。
  3. 點選 **Recompile** 即可獲得零警告、零錯誤的標準 IEEE 雙欄會議論文 PDF。
