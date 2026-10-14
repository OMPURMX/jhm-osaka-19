# 第19回 日本医療マネジメント学会 大阪府支部学術集会

ChatGPT Sitesから独立して公開するための静的サイト一式です。

## 最初に

1. `GUIDE_JA.md`（日本語手順書）をお読みください。
2. GitHubリポジトリの直下に `dist` とこのREADMEが並ぶよう保存してください。
3. Cloudflare PagesでGitHubリポジトリを接続し、公開ディレクトリを `dist` に設定します。

| 設定 | 値 |
|---|---|
| Framework preset | None |
| Production branch | main |
| Build command | exit 0 |
| Build output directory | dist |
| Root directory | 空欄（リポジトリ直下） |
| 環境変数 | 不要 |

## 構成

- `dist/`：公開するHTML13ページ・画像1点。原本とバイト単位で同一です。
- `GUIDE_JA.md`：GitHub保存・Cloudflare Pages公開・更新の手順。
- `CHECKSUMS.sha256`：公開用ファイルのSHA-256。
- `verify.py`：標準ライブラリだけでリンク・画像・チェックサムを検査。
- `EXPORT_INFO.json`：書き出し日・原本コミット等の記録。

React / Next.js / npm / データベース / ChatGPT APIは不要です。CSSは各HTMLに含まれます。JavaScriptはありません。
登録・決済・マイページは未実装です。公開しても受付が開始されるわけではありません。

## 任意のローカル確認

Python 3がある場合：

```sh
python3 verify.py
python3 -m http.server 8000 --directory dist
```

ブラウザで http://localhost:8000/ を開きます。終了はControl+Cです。

## 権利

この書き出しは、サイトの文章・画像等に新たな再配布ライセンスを付与するものではありません。
管理者による運営・移行のための一式です。第三者素材やマスコットの利用条件は引き継いでください。
