import unicodedata


def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


class FuzzyString(str):
    def __eq__(self, other):
        return normalize_caseless(self) == normalize_caseless(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.lower() < other.lower()

    def __le__(self, other):
        return self.lower() <= other.lower()

    def __gt__(self, other):
        return self.lower() > other.lower()

    def __ge__(self, other):
        return self.lower() >= other.lower()

    def __add__(self, other):
        return FuzzyString(str(self) + other)

    def __contains__(self, key):
        return key.lower() in normalize_caseless(self)
