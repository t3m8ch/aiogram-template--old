from aiogram_template.errors import PortMustBeNumberError

from aiogram_template.config import _compute_update_method, \
    LongPollingUpdateMethod, WebhookUpdateMethod


def test_returns_long_polling_if_envs_is_none():
    actual = type(_compute_update_method(None, None, None, None))
    expected = LongPollingUpdateMethod
    assert actual == expected


def test_returns_long_polling_if_webapp_host_is_none():
    actual = type(_compute_update_method("", "", None, "1234"))
    expected = LongPollingUpdateMethod
    assert actual == expected


def test_error_if_webapp_port_is_not_numeric():
    try:
        _compute_update_method("", "", "", "I'm number XD")
        assert False
    except PortMustBeNumberError:
        assert True


def test_returns_webhook_if_all_right():
    actual = _compute_update_method(
        webhook_host="localhost",
        webhook_path="/path/to/bot",
        webapp_host="localhost",
        webapp_port="3000"
    )
    expected = WebhookUpdateMethod(
        webhook_host="localhost",
        webhook_path="/path/to/bot",
        webapp_host="localhost",
        webapp_port=3000
    )
    assert actual == expected
