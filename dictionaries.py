capitals = {"Ukraine": "Kyiv", "France": "Paris", "Germany": "Berlin"}

print(capitals["France"])
# --> Paris

capitals["Japan"] = "Tokyo"
capitals["France"] = "Marseille"

print(capitals["France"])
# --> updated value -> Marseille

# methods

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for country, capital in capitals.items():
    print(f'country: {country}, capital: {capital}')