first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = " python "
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
favorite_language.lstrip()
favorite_language.strip()


nostarch_url = "https://nostarch.com"
nostarch_url.removeprefix("https://")
