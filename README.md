建立新的虛擬環境:
python -m venv venv


啟動虛擬環境
.\venv\Scripts\activate
安裝必要套件
pip install django pytest pytest-django pytest-html
pip install robotframework robotframework-requests

建立requirements.txt
pip freeze > requirements.txt

重裝:
pip install -r requirements.txt

架構:
shopping_cart:儲存所有source code
shopping_cart/shopping_cart:main django設定
shopping_cart/accounts: 註冊登入設定
shopping_cart/frontend: 前台APP
shopping_cart/backend: 後台APP
shopping_cart/tests/unit: pytest測試
./unit/reports:pytest 測試報告
shopping_cart/tests/robot: ROBOT FRAMEWORK測試
./robot/reports ROBOT測試報告
shopping_cart/run_tests.bat: 可以一次執行兩個不同框架的測試