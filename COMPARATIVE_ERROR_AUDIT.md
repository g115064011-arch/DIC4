# DIC4 IEEE Conference Paper — 校稿前後錯誤差異對照清單（Comparative Error Audit）

> **文件性質**：獨立審查報告（非論文內嵌內容）  
> **專案名稱**：AI SOC Analyst Agent — A Spec-Driven Multi-Tier System Orchestrating Machine Learning Triage, MITRE ATT&CK Reasoning, and Bounded LLM Planning  
> **組別名單**：第 16 組（蘇恩平、周妤、袁靖淇、蕭宥瑄）  
> **對照目標**：
> - 🟢 **校稿完成正式版**：`DIC4_Good_Final_IEEE_Conference.pdf`（原始碼：`paper_good/main.tex`）
> - 🔴 **校稿前瑕疵初稿**：`DIC4_Bad_Draft_Erroneous.pdf`（原始碼：`paper_bad/main.tex`）

---

## 總覽說明

兩份論文均採用標準官方 IEEE Conference LaTeX 樣式（`\documentclass[conference]{IEEEtran}`），使用相同的研究架構、實驗數據（Microsoft GUIDE 1M 筆事件與 ExCyTIn-Bench 評測）、作者群與參考文獻。

兩者的唯一差異在於**排版與校稿品質**。壞的初稿（Bad Draft）由真實的 LaTeX 原始碼缺陷自然產生排版異常，絕無任何人工加註之紅框、螢光色標、標語或中文字眼；好的正式版（Good Final）則完成精細校稿，達到 IEEE 國際研討會審查之正式標準。

---

## 詳細錯誤差異對照清單

| 編號 | 錯誤類別 | 🔴 壞的初稿版本（Bad Draft）之源碼與現象 | 🟢 好的正式版本（Good Final）之修正方式 | 學術規範依據與影響 |
|:---:|---|---|---|---|
| **1** | **文字邊界溢出<br>(Overfull `\hbox`)** | **源碼**：在 Section I 中插入未經斷字處理的長字串：<br>`\texttt{TELEMETRY\_ENDPOINT\_STREAM\_IDENTIFIER\_GUIDE\_PROD\_INGESTION\_BUFFER\_...}`<br>**現象**：字串直接衝出單欄 3.5 吋寬度，向右溢出達 435.4pt，侵入鄰近欄位。 | **修正**：移除除錯用內部字串，將日誌流描述改以自然學術英文段落表達，所有文字邊界嚴格內縮於欄寬內。 | IEEE 雙欄規範要求文字嚴禁跨欄重疊，否則將導致讀者閱讀混淆與排版審查即刻被退件。 |
| **2** | **圖片尺寸與超標<br>(Figure Error)** | **源碼**：設定 `\includegraphics[width=1.35\columnwidth]{fig1_architecture.png}`。<br>**現象**：圖片寬度達到欄寬之 135%，右側穿透中央分隔線並覆蓋第二欄文字。 | **修正**：設定 `\includegraphics[width=\columnwidth]{fig1_architecture.png}`，圖片精準符合單欄寬度。 | IEEE 雙欄插圖若非跨雙欄（`figure*`），寬度必須嚴格限定於 `\columnwidth`（約 88mm）。 |
| **3** | **拼字錯誤<br>(Natural Typos)** | **源碼**：內文中殘留 4 處校稿疏漏：<br>1. Abstract: `alret fatigue`<br>2. Abstract: `LLM agent strageties`<br>3. Section I.C: `The assymetric error cost`<br>4. Abstract: `evidance gating mechanism` | **修正**：校正為標準英文單字：<br>1. `alert fatigue`<br>2. `LLM agent strategies`<br>3. `asymmetric error cost`<br>4. `evidence gating mechanism` | 論文初稿常見打字輸入疏失，校稿階段必須藉由拼字檢查完全消除。 |
| **4** | **符號語法跳脫錯誤<br>(Escaped Syntax Bug)** | **源碼**：在 Abstract 中未將百分比跳脫：<br>`at least 40.4% due to premature termination`<br>**現象**：`%` 在 LaTeX 中被視為註解符號，導致後方半句話整句遺失。 | **修正**：加入反斜線正確跳脫：<br>`at least 40.4\% due to premature termination`，完整顯示研究數據與論述。 | 未跳脫的 `%` 是新手與 AI 生成 LaTeX 常見語法疏失，會直接破壞論述完整性。 |
| **5** | **文獻引用缺失<br>(Citation Error `[?]`)** | **源碼**：在 Section II 中引用未定義之 BibTeX key：<br>`\cite{tsegai2026aida_missing}` 與 `\cite{wu2026excytin_missing}`。<br>**現象**：BibTeX 編譯拋出警告，PDF 內文自然印出醒目的 `[?]` 標籤。 | **修正**：對齊 `references.bib` 之正規定義鍵值 `\cite{tsegai2026aida}` 與 `\cite{wu2026excytin}`，所有引用正常編號解析（如 `[3]`, `[4]`）。 | 缺少 BibTeX 條目或打錯引用鍵為研討會投稿最忌諱的技術錯誤之一。 |
| **6** | **交叉參照失效<br>(Cross-ref `Fig. ??`)** | **源碼**：在 Section III 撰寫 `Fig.~\ref{fig:arch_missing}`，但圖表標籤為 `\label{fig:arch}`。<br>**現象**：LaTeX 無法對應標籤，PDF 內文自然出現 `Fig. ??`。 | **修正**：修正為 `Fig.~\ref{fig:arch}`，PDF 內文正確解析為 `Fig. 1`。 | 交叉參照標籤不一致會導致讀者無法查閱對應圖表。 |
| **7** | **數學公式欄位溢出<br>(Formula Overflow)** | **源碼**：在 Section IV 中使用單行未折行長公式：<br>`P_{fusion} = \frac{1}{Z} [ w_1 P_{GBDT} + w_2 P_{LLM} \prod ... \int ... \sum ... ]`<br>**現象**：公式寬度超出單欄 208.7pt，橫跨雙欄切到頁面邊緣。 | **修正**：使用 `amsmath` 之 `\begin{aligned}` 環境將長公式適當分為二行，完美容納於單欄之內。 | 雙欄 IEEE 論文長公式必須折行，不得破壞分欄排版。 |
| **8** | **表格邊界溢出<br>(Table Overspill)** | **源碼**：Table I 定義過寬之固定欄寬：<br>`\begin{tabular}{lp{3.2cm}p{3.5cm}p{3.2cm}}`<br>**現象**：表格整體寬度超過單欄限制 154.7pt，產生顯著 Overfull `\hbox` 並裁切右側欄位。 | **修正**：以 `\resizebox{\columnwidth}{!}{...}` 包覆表格，自動將三線表無損縮放貼合單欄寬度。 | 表格寬度超標會導致數值被切或與相鄰欄文字重疊。 |

---

## LaTeX 編譯紀錄（Log Verification）

- 🟢 **Good Final (`paper_good/main.log`)**：
  - `Overfull \hbox`：**0 處**（完全無版面溢出警告）
  - `BibTeX Warnings`：**0 處**（18 篇文獻全數正常解析）
  - `LaTeX Warnings`：**0 處**（圖表與公式編號全數正確）
  - 產出檔案：`DIC4_Good_Final_IEEE_Conference.pdf`（244 KB，XeTeX 原生編譯）

- 🔴 **Bad Draft (`paper_bad/main.log`)**：
  - `Overfull \hbox (435.40997pt too wide) in paragraph at lines 42--43`
  - `Overfull \hbox (154.71411pt too wide) in paragraph at lines 76--88`
  - `Overfull \hbox (88.20154pt too wide) in paragraph at lines 107--108`
  - `Overfull \hbox (208.74323pt too wide) detected at line 180`
  - `LaTeX Warning: Citation 'tsegai2026aida_missing' on page 2 undefined`
  - `LaTeX Warning: Citation 'wu2026excytin_missing' on page 2 undefined`
  - `LaTeX Warning: Reference 'fig:arch_missing' on page 2 undefined`
  - 產出檔案：`DIC4_Bad_Draft_Erroneous.pdf`（246 KB，保留真實排版缺陷之 PDF）

