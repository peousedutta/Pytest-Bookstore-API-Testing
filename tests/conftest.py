import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import httpx
from utilities.ReadConfigurations import ReadConfig

configs = ReadConfig()

SLACK_WEBHOOK = configs.getSlackWebHook()

def send_slack_message(message: str):
    payload = {"text": message}
    try:
        response = httpx.post(SLACK_WEBHOOK, json=payload, timeout=5)
        response.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Slack notification failed: {e}")

# Hook for individual test result
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call' and result.failed:
        test_name = item.name  # Only "test_login"
        message = f":x: *{test_name} failed*"
        send_slack_message(message)