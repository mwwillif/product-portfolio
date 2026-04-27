from playwright.sync_api import sync_playwright
from config import MAX_JOB_TEXT_CHARS


def clean_text(text):
    return " ".join(text.split())


def score_text_block(text):
    """
    Score how likely this block is a real job description
    """
    text_lower = text.lower()

    keywords = [
        "responsibilities",
        "requirements",
        "qualifications",
        "experience",
        "skills",
        "what you will",
        "what you'll do",
        "preferred",
    ]

    bad_signals = [
        "cookie",
        "accept all cookies",
        "privacy",
        "sign in",
        "language",
    ]

    score = 0

    for k in keywords:
        if k in text_lower:
            score += 2

    for b in bad_signals:
        if b in text_lower:
            score -= 3

    score += len(text) / 1000  # favor longer meaningful blocks

    return score


def fetch_job_description(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="networkidle", timeout=60000)

        # Try to accept cookies
        try:
            page.locator("text=Accept All Cookies").click(timeout=3000)
        except:
            pass

        page.wait_for_timeout(3000)

        candidates = []

        selectors = [
            "main",
            "[role='main']",
            "article",
            "section",
            "div",
        ]

        for selector in selectors:
            elements = page.locator(selector).all()

            for el in elements:
                try:
                    text = el.inner_text()
                    text = clean_text(text)

                    if len(text) > 300:
                        candidates.append(text)
                except:
                    continue

        browser.close()

    # Score all blocks and pick best
    best_text = ""
    best_score = -999

    for c in candidates:
        s = score_text_block(c)
        if s > best_score:
            best_score = s
            best_text = c

    return best_text[:MAX_JOB_TEXT_CHARS]