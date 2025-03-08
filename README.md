# Pygame 與 OpenSimplex 專案

## 環境要求

- Python 3.X 以上（建議 3.8 以上）

## 套件安裝

請使用以下指令安裝所有所需的 Python 套件：

```bash
pip install -r requirements.txt
```

## 新增 Python 套件規範

如果需要新增額外的 Python 套件，請遵循以下步驟：

1. 使用 `pip install <套件名稱>` 來安裝新套件。

2. 再將安裝的套件名稱寫到 `requirements.txt` 中，這樣做是讓其他人拿到這個專案時可以安裝到你新增的套件。

3. 確保 `requirements.txt` 更新後，其他開發者可以使用 `pip install -r requirements.txt` 來同步環境。

請確保所有新增的 Python 套件都被記錄在 `requirements.txt` 內，以確保專案的可維護性與一致性。

## **pycache** 作用

**pycache** 是 Python 自動生成的目錄，主要用來 存放已編譯的 Python bytecode 檔案，加速程式執行。當 Python 腳本（.py 檔案）執行時，Python 會將它們編譯成 bytecode（位元組碼），然後存入 **pycache** 資料夾，以 .pyc（或 .pyo）檔案的形式儲存。

這樣，當你下次執行相同的 Python 檔案時，Python 就可以直接載入已編譯的 .pyc 檔案，而不需要重新編譯，提升效能。
