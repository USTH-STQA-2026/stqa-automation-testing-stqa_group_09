import os
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    wait_for_flutter, login, SCREENSHOT_DIR,
)


#TC-11: logout
def test_logout(page, test_config):
    login(page, test_config)
    flutter_click_button(page, "Đăng xuất")
    wait_for_flutter(page, text="Đăng nhập")
    enable_flutter_semantics(page)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-11(logout).png"))
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đăng nhập" in sem_text, \
        "TC-11 FAILED: Logout did not return to login page — 'Đăng nhập' button not found."


#TC-12: switch language to English
def test_switch_language_to_english(page, test_config):
    login(page, test_config)
    flutter_click_button(page, "EN")
    wait_for_flutter(page, text="Library")
    enable_flutter_semantics(page)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-12(switch_language).png"))
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Logout" in sem_text or "Borrow" in sem_text or "Library" in sem_text, \
        "TC-12 FAILED: Language did not switch to English — none of 'Logout', 'Borrow', 'Library' found in page."
