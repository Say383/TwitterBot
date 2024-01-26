import gettext

def setup_localization(locale_path, language):
    try:
        lang_translations = gettext.translation('base', localedir=locale_path, languages=[language])
        lang_translations.install()
        _ = lang_translations.gettext
        print(_("Localization set to {language}.").format(language=language))
    except FileNotFoundError:
        print("Locale not found. Falling back to default language.")
        _ = gettext.gettext

setup_localization('locales', 'es')  # Example usage with 'es' for Spanish
