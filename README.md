# Django Inquiry API

## 概要
問い合わせ管理APIです。
JWT認証付きでユーザーごとにデータを管理できます。

---

## 技術スタック
- Python
- Django
- Django REST Framework
- JWT認証（SimpleJWT）

---

## 機能一覧

### 認証
- POST /api/token/
- JWT認証

### 問い合わせAPI

| メソッド | URL |
|--------|-----|
| GET | /api/inquiries/ |
| POST | /api/inquiries/ |
| GET | /api/inquiries/{id}/ |
| PUT | /api/inquiries/{id}/ |
| DELETE | /api/inquiries/{id}/ |

---

## フィルタ機能

### ステータス

### 優先度

---

## 動作確認（Windows PowerShell）

### トークン取得

```powershell
$body = @{
    username = "xilong"
    password = "xilong"
} | ConvertTo-Json

$response = Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/token/" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body

$token = $response.access