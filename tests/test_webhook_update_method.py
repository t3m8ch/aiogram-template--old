from aiogram_template.config import WebhookUpdateMethod


def test_url_property_if_host_is_https_1():
    method = WebhookUpdateMethod(
        webhook_host="https://some.thing/",
        webhook_path="/path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_2():
    method = WebhookUpdateMethod(
        webhook_host="https://some.thing",
        webhook_path="path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_3():
    method = WebhookUpdateMethod(
        webhook_host="https://some.thing/",
        webhook_path="path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_4():
    method = WebhookUpdateMethod(
        webhook_host="https://some.thing",
        webhook_path="/path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected
