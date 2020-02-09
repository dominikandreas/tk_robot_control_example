from logging import warning

supported = "EN", "DE"


class Entry:
    def __init__(self, en, de):
        # set english as the default
        self.value = en
        self.translations = dict(en=en, de=de)

    def set_language(self, lang_str):
        # reset the value of this string
        self.value = self.translations[lang_str]

    def __call__(self, *args, **kwargs):
        return self.value

    def __str__(self):
        return self.value


# noinspection SpellCheckingInspection
class Translations:
    accept_pos = Entry("Accept Position", "Position Übernehmen")
    current_pos = Entry("Current Position", "Aktuelle Position")
    steps = Entry("Steps", "Schritte")


def set_language(lang_str):
    if lang_str not in supported:
        warning("language %s not supported, ignoring request")
    else:
        for var in dir(Translations):
            if isinstance(var, Entry):
                var.set_language(lang_str)
