import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button, wait_for_flutter,
    login, SCREENSHOT_DIR,
)

#TC-08: borrow book
def test_borrow_book(page, test_config):
    login(page, test_config)
    enable_flutter_semantics(page)
    book = page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]')
    assert book.count() > 0
    book.nth(0).locator('flt-semantics[role="button"]:has-text("Mượn sách này")').click()
    page.get_by_role("button", name="Mượn", exact=True).click()
    enable_flutter_semantics(page)
    wait_for_flutter(page, text="Mượn sách thành công!")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-08(borrow).png"))
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Mượn sách thành công!" in sem_text, \
        f"Borrowing failed."


#TC-09: view borrowed books
def test_view_borrowed_books(page, test_config):
    login(page, test_config)
    enable_flutter_semantics(page)
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, text="Phiếu mượn của tôi")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-09(view_borrowed_books).png"))
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đang mượn" in sem_text or "Trả sách" in sem_text, \
        f"Navigation failed."


#TC-10: return book
def test_return_book(page, test_config):
    login(page, test_config)
    enable_flutter_semantics(page)
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, text="Phiếu mượn của tôi")
    page.locator('flt-semantics[role="button"]:has-text("Trả sách")').click()
    wait_for_flutter(page, text="Trả sách thành công.")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-10(return).png"))
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Trả sách thành công." in sem_text, \
        f"Returning failed."
