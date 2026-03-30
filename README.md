# Django Inquiry API 

問い合わせ管理を行うためのREST APIです。
JWT認証・CRUD・フィルタ機能を備えた実務想定のAPIとして構築しています。

---

## 🚀 概要 本APIは、ユーザーごとに問い合わせ（Inquiry）を管理するシステムです。 
- JWT認証によるユーザー管理 - 問い合わせのCRUD操作
- ステータス・優先度による絞り込み
- Django REST Framework の Generic Views を使用
 
---

## 🛠 技術スタック
- Python 
- Django 
- Django REST Framework 
- Simple JWT
- SQLite（開発環境）

---

## 🔐 認証
### トークン取得

``` POST /api/token/ ```

---

## 📡 API一覧
| メソッド | URL | 
|--------|-----|
| GET | /api/inquiries/ |
| POST | /api/inquiries/ |
| GET | /api/inquiries/{id}/ |
| PUT | /api/inquiries/{id}/ |
| DELETE | /api/inquiries/{id}/ | 

--- 

## 🔎 フィルタ機能 ### ステータスで絞り込み 

``` GET /api/inquiries/?status=OPEN ``` 

### 優先度で絞り込み 

``` GET /api/inquiries/?priority=HIGH ```

--- 

## 💻 セットアップ（Windows） 

- ```cmd python -m venv venv venv\Scripts\activate ``` 
- ```pip install -r requirements.txt``` 
- ```python manage.py migrate``` 
- ``` python manage.py runserver ``` 

--- 

## ▶ 動作確認（PowerShell） 

### トークン取得 

- ```$body= @{ username = "xilong" password = "xilong" } | ConvertTo-Json```

- ```$response = Invoke-RestMethod ` -Uri "http://127.0.0.1:8000/api/token/" ` -Method Post ` -ContentType "application/json" ` -Body $body```
- ```$token = $response.access ```

---

### ヘッダー設定 

```$headers = @{ Authorization = "Bearer $token" "Content-Type" = "application/json" } ``` 

--- 

### 一覧取得 

```Invoke-RestMethod ` -Uri "http://127.0.0.1:8000/api/inquiries/" ` -Headers $headers ``` 

---

### 作成 

```$body = @{ title = "ログインできない" content = "管理画面にログインできません" status = "OPEN" priority = "HIGH" } | ConvertTo-Json Invoke-RestMethod ` -Uri "http://127.0.0.1:8000/api/inquiries/" ` -Method Post ` -Headers $headers ` -Body $body```

---

### 更新 

```$body = @{ title = "ログインできない（更新）" content = "パスワード再設定も失敗します" status = "IN_PROGRESS" priority = "HIGH" } | ConvertTo-Json Invoke-RestMethod ` -Uri "http://127.0.0.1:8000/api/inquiries/1/" ` -Method Put ` -Headers $headers ` -Body $body ```

---

### 削除

```Invoke-RestMethod ` -Uri "http://127.0.0.1:8000/api/inquiries/1/" ` -Method Delete ` -Headers $headers ```

--- 

## ⚠ 文字化け対策（Windows）

```powershell chcp 65001 $OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 ``` 

---

## 🧠 設計意図 
- JWT認証によりユーザーごとに問い合わせを分離
- Generic Views を使用し、保守性の高い構成に 
- ステータス・優先度で業務管理を想定
- RESTful設計を意識 

--- 

## 📎 関連リポジトリ
- Django Task API（1つ目のポートフォリオ）

---
---
