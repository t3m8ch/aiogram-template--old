from aiogram_template.handlers import common


def register_handlers(dp):
    """A function that registers all handlers
    Example of registration of several handlers:
    .. code-block:: python

       handlers = module1.handlers +
                  module2.handlers +
                  module3.handlers

    Each handler module must contain a list of 'handlers',
    which stores the functions that register the handler.

    Remember that the order of handlers is important!
    """
    handlers = common.handlers
    for handler in handlers:
        handler(dp)
