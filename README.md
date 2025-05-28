# Shopping Cart System

這是一個使用 Django 架設的購物車網站，具備前台與後台功能，並同時整合了兩種測試框架：`pytest` 與 `Robot Framework`。

---

### 建立新的虛擬環境:
python -m venv venv


### 啟動虛擬環境
.\venv\Scripts\activate  

### 安裝必要套件  
pip install django pytest pytest-django pytest-html  
pip install robotframework robotframework-requests  

### 建立requirements.txt  
pip freeze > requirements.txt  

### 重裝環境:  
pip install -r requirements.txt  

### 啟動Django   
python manage.py runserve   

### 架構:  
shopping_cart/ ← 專案根目錄  
├── accounts/ ← 帳號註冊 / 登入模組  
├── backend/ ← 後台管理模組  
├── frontend/ ← 前台展示模組  
├── shopping_cart/ ← Django 設定檔（settings.py, urls.py）  
├── tests/  
│ ├── unit/ ← pytest 測試  
│ │ ├── test_sample.py  
│ │ └── reports/ ← pytest 測試報告輸出位置  
│ └── robot/ ← Robot Framework 測試  
│ ├── test_sample.robot  
│ └── reports/ ← Robot 測試報告輸出位置  
├── run_tests.bat ← 一鍵執行兩種測試的批次檔  
├── requirements.txt ← 所需套件列表  
└── manage.py ← Django 專案啟動點  

## 測試執行方式  
### 執行 Pytest 並產出 HTML 報告  

```  
pytest tests/unit --html=tests/unit/reports/report.html --self-contained-html  
```  

### 執行 Robot Framework 並產出報告  
```  
robot --outputdir tests/robot/reports tests/robot/test_sample.robot  
```  

### 一鍵執行兩種測試（需啟動 Django server） 
```
./run_tests.bat
```