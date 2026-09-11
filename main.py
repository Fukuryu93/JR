import random
from playwright.sync_api import sync_playwright

def main():
    # ターゲットのURL（実際のURLに変更してください）
    TARGET_URL = "https://form.qooker.jp/Q/ja/suicanewchar/vote/"

    with sync_playwright() as p:
        # GitHub Actions上ではヘッドレスモード（画面なし）で起動
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(TARGET_URL)

        # 1. 「B」を選択 (ラジオボタンのラベルテキストを指定)
        page.locator("text=② B").click()

        # 2. 年齢をランダムに選択
        ages = ["10代以下", "20代", "30代", "40代", "50代", "60代", "70代", "80代以上", "その他・無回答"]
        selected_age = random.choice(ages)
        page.locator(f"text={selected_age}").click()

        # 3. お住まいの地域を「東京都」に選択 (プルダウンメニューの場合)
        # ※ プルダウンの要素が<select>タグであることを想定
        page.locator("select").select_option(label="東京都")

        # 4. 性別をランダムに選択
        genders = ["男性", "女性", "その他・無回答"]
        selected_gender = random.choice(genders)
        page.locator(f"text={selected_gender}").click()

        # 5. 送信（確認）ボタンをタップ
        page.locator("text=確認").click()

        # 画面遷移の待機（必要に応じて）
        page.wait_for_timeout(3000) 
        
        print("フォームの送信が完了しました。")
        browser.close()

if __name__ == "__main__":
    main()
