import os
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, wait_for_flutter, SCREENSHOT_DIR,
)

#TC-04: search book by name
def test_search_book_by_name(page, test_config):
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
    wait_for_flutter(page, text="Flutter")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-04(search_by_name).png"))

    assert page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() > 0, \
        "TC-04 FAILED: No book cards found after searching 'Flutter' — expected at least one result."

#TC-05: search book no result
def test_search_book_no_result(page, test_config):
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "xyz_khong_ton_tai_12345")
    wait_for_flutter(page, text="Không tìm thấy", timeout=5000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-05(no_results).png"))

    assert page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0, \
        "TC-05 FAILED: Book cards still shown after searching a non-existent keyword — expected zero results."

#TC-06: filter by category
def test_filter_by_category(page, test_config): 
    login(page, test_config)

    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    wait_for_flutter(page, text="Công nghệ")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-06(filter_by_category).png"))

    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    assert books.count() > 0, \
        "TC-06 FAILED: No book cards found after filtering by 'Công nghệ'."
    for i in range(books.count()):
        aria_label = books.nth(i).get_attribute("aria-label")
        assert "Công nghệ" in aria_label, \
            f"TC-06 FAILED: Book at index {i} does not belong to 'Công nghệ' category (aria-label: {aria_label})"

#TC-07: search by author's name
def test_search_by_author(page, test_config): 
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
    wait_for_flutter(page, text="Nguyễn Minh Đức")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-07(search_by_author).png"))

    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    assert books.count() > 0, \
        "TC-07 FAILED: No book cards found after searching author 'Nguyễn Minh Đức'."
    for i in range(books.count()):
        aria_label = books.nth(i).get_attribute("aria-label")
        assert "Nguyễn Minh Đức" in aria_label, \
            f"TC-07 FAILED: Book at index {i} does not have author 'Nguyễn Minh Đức' in aria-label (got: {aria_label})"
