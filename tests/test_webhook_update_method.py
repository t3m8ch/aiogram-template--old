from aiogram_template.config import WebhookUpdateMethod


def test_url_property_if_host_is_localhost_1():
    method = WebhookUpdateMethod(
        host="localhost/",
        path="/path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "localhost/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_localhost_2():
    method = WebhookUpdateMethod(
        host="localhost",
        path="path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "localhost/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_localhost_3():
    method = WebhookUpdateMethod(
        host="localhost/",
        path="path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "localhost/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_localhost_4():
    method = WebhookUpdateMethod(
        host="localhost",
        path="/path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "localhost/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_1():
    method = WebhookUpdateMethod(
        host="https://some.thing/",
        path="/path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_2():
    method = WebhookUpdateMethod(
        host="https://some.thing",
        path="path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_3():
    method = WebhookUpdateMethod(
        host="https://some.thing/",
        path="path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected


def test_url_property_if_host_is_https_4():
    method = WebhookUpdateMethod(
        host="https://some.thing",
        path="/path/to/bot",
        webapp_host="",
        webapp_port=3000
    )

    actual = method.url
    expected = "https://some.thing/path/to/bot"
    assert actual == expected
