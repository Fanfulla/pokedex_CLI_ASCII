import pokeapi
import ascii_magic as am

while True:

    all_names = pokeapi.get_all_pokemon_names()
    pokemon_name = input("Enter a pokemon Name (or type exit to close): ")

    #names check
    suggested_names = pokeapi.suggest_names(pokemon_name, all_names)

    #print(suggested_names)
    if pokemon_name == "exit":
        print("bye bye")
        break


    pokemon_info = pokeapi.get_pokemon_info(pokemon_name)

    if pokemon_info:
        print("----------------------------------------------------------------")
        #this print the sprite as Ascii
        art = am.from_url(pokemon_info['sprites']['front_default'])
        #monocrome FALSE to see sprite with colors
        art.to_terminal(columns=60, monochrome=False)
        print("----------------------------------------------------------------")
        print(f"Name: {pokemon_info['name']}")
        # /10 to calculate m and kg
        print(f"Height: {pokemon_info['height']/10} m")
        print(f"Weight: {pokemon_info['weight']/10} kg")
        #look and define the abilities and the types, without printing only 1 or both. It work "dynamcly"
        for i, a in enumerate(pokemon_info['abilities'], start=1):
            print(f"Ability {i}: {a['ability']['name']}")
        for i, t in enumerate(pokemon_info['types'], start=1):
            print(f"Type {i}: {t['type']['name']}")


    else:
        print(f"Pokemon {pokemon_name} not found")
        maybe_p = pokeapi.suggest_names(pokemon_name, all_names, limit=5, min_score=70)
        if maybe_p:
            #suggested names list
            print("Maybe you were looking for:", ", ".join(maybe_p))
        else:
            print("Nothing, i can't find your pokemon. Maybe is a new species")



