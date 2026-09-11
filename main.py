import random
from playwright.sync_api import sync_playwright

def main():
    # 実際のURLに書き換えてください
    TARGET_URL = "https://form.qooker.jp/Q/ja/suicanewchar/vote/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(TARGET_URL)

        # 1. 「B」を選択
        page.locator("label", has_text="② B").click()

        # 2. 年齢をランダムに選択
        ages = ["10代以下", "20代", "30代", "40代", "50代", "60代", "70代", "80代以上", "その他・無回答"]
        selected_age = random.choice(ages)
        page.locator("label", has_text=selected_age).click()

        # 3. お住まいの地域を「東京都」に選択
        page.locator("select").select_option(label="東京都")

        # 4. 性別をランダムに選択
        genders = ["男性", "女性", "その他・無回答"]
        selected_gender = random.choice(genders)
        page.locator("label", has_text=selected_gender).click()

        # 5. 確認ボタンをタップ
        page.locator("text=確認").first.click()

        page.wait_for_timeout(3000) 
        print("フォームの操作が完了しました。")
        browser.close()

if __name__ == "__main__":
    main()
