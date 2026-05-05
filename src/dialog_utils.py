"""Helpers for safe Playwright dialog handling across downloaders."""

_REGISTERED_PAGE_IDS = set()


async def _auto_accept_dialog(dialog):
    """Auto-accept browser dialogs and ignore already-handled cases."""
    try:
        await dialog.accept()
    except Exception:
        # Dialog can already be handled by another flow; ignore safely.
        pass


def ensure_dialog_auto_accept(page):
    """Register one dialog auto-accept listener per Playwright page."""
    page_id = id(page)
    if page_id in _REGISTERED_PAGE_IDS:
        return

    page.on("dialog", _auto_accept_dialog)
    _REGISTERED_PAGE_IDS.add(page_id)
