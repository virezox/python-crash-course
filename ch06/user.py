user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())
