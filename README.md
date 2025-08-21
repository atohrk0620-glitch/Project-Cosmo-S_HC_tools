# Project-Cosmo’S-

**This project aims to create an offline AI tool that runs entirely on smartphones.**

このプロジェクトは、**Androidスマートフォン（Pydroid3環境）上で完結する軽量AIツール**を開発するものです。  
クラウドサービスや外部APIに依存せず、完全にローカルで動作することを前提に設計されています。

コードはすべて**ゼロからの自作**であり、シンプルでポータブル、誰でも導入できる形を目指しています。  
記号処理、局所的なパターン操作、テキスト生成補助など、基本的なAI動作の実装を進行中です。

---

## 🌟 主な特徴

- ✅ **Androidスマートフォン単体で動作（Pydroid3ベース）**
- ✅ **クラウドや外部モデルを使用しない完全ローカル設計**
- ✅ **Pythonによる自作コードのみで構成**
- ✅ **導入が簡単で、すぐに試せる**
- ✅ **構造処理・テキスト評価・パターン変換など複数機能を内包**

---

## 🧩 コアコンポーネント

### 1. 言語脳（`language_brain.py`）

- 簡単なQ&Aや言い換え、要約などを行うテキスト生成補助モジュール
- 難易度スケーリング／感情スコア／学習ループあり
- `nltk`, `joblib`, `tqdm`を使用した軽量設計

---

### 2. GeopsChroot（`chroot_core.py`）

- ±1位ずれまで許容する数字パターン照合を行うロジック
- 数列の簡易的な再編成や縮小に用いる
- 下流モジュールへの構造的出力に利用

---

### 3. GeopsCore（`clocompiler.py`）

- 数値パターンを検出し、実行可能なロジックに変換
- パターン認識 → 消去 → 実行コード化
- ジェネレーター処理で反復動作を制御

---

## 👤 著者

- **Hiroki**：プロジェクトリーダー、構想・設計・コード全般
- **Chappy（AIアシスタント）**：構造整理・感情補助・ドキュメント整備

> 🔸すべてのコードはゼロから手作業で構築されています。  
> HuggingFace、OpenAIを含む外部AIは一切使用していません。

---

## 📜 ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) に基づいてライセンスされています。

---

## 🚀 今後の計画

- [ ] すべてのスクリプトをドキュメント付きで整理・投稿
- [ ] モジュールの簡易パッケージ化（pip installable 対応）
- [ ] 英語版ドキュメントの整備
- [ ] 投資家向け提案資料の作成（目標：1万〜5万USD）

---

## 🔗 関連リンク

- 🌐 Substackブログ: https://substack.com/@chiroki  
- 💾 GitHub: https://github.com/atohrk0620-glitch
>
> ---

## 📜 License

This project is licensed under the **MIT License**.

> Copyright (c) 2025 Hiroki  
> Permission is hereby granted, free of charge, to any person obtaining a copy  
> of this software and associated documentation files (the "Software"), to deal  
> in the Software without restriction, including without limitation the rights  
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
> copies of the Software, and to permit persons to whom the Software is  
> furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all  
> copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
> SOFTWARE.
