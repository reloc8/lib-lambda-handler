from abc import ABC, abstractmethod
from logging import getLogger, INFO, Logger
from typing import Any


class LambdaHandler(ABC):

    def __init__(self, logger: Logger = getLogger()):

        self.logger = logger
        self.logger.setLevel(INFO)

    @abstractmethod
    def run(self, event: Any, context: Any) -> Any:
        """Handles a Lambda event

        :param event:   Event information passed by AWS Lambda
        :param context: Invocation, function, and environment information
        :return:        May return some serializable data
        """

        pass

    def walk(self, event: Any, context: Any) -> Any:
        """Handles a Lambda event, but silently

        All exceptions are caught and logged.

        :param event:   Event information passed by AWS Lambda
        :param context: Invocation, function, and environment information
        :return:        May return some serializable data
        """

        try:
            return self.run(event=event, context=context)
        except Exception as logged:
            self.logger.exception(logged)
