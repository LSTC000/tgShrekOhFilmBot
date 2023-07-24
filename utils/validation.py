class Validator:
    def __init__(self):
        pass

    def alert_validation(self, text: str) -> bool:
        """
        :param text: Text for the alert.
        :return: True if alert is valid, else - False
        """

        return True if text else False

    def payment_validation(self, amount: str) -> bool:
        """
        :param amount: Amount of payment.
        :return: True if amount is valid, else - False
        """

        try:
            amount = int(amount)
            if amount <= 0:
                return False
        except ValueError:
            return False

        return True

    def user_review_validation(self, review: str) -> bool:
        """
        :param review: User review.
        :return: True if review is valid, else - False
        """

        return True if review and len(review) <= 2048 else False
