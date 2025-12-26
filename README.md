# 🎮 Pokédex CLI ASCII

A fun command-line Pokédex that displays Pokémon information with colorful ASCII art sprites!

## ✨ Features

- Search any Pokémon by name
- View Pokémon stats (height, weight, abilities, types)
- Beautiful ASCII art sprites with colors
- Smart name suggestions using fuzzy matching
- User-friendly CLI interface

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Fanfulla/pokedex_CLI_ASCII.git
cd pokedex_CLI_ASCII
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the program:
```bash
python main.py
```

Enter a Pokémon name when prompted. Type `exit` to quit.

## 📦 Dependencies

- requests
- ascii-magic
- rapidfuzz

## 🎯 Example
```
Enter a pokemon Name (or type exit to close): pikachu
----------------------------------------------------------------
[ASCII art sprite appears here]
----------------------------------------------------------------
Name: pikachu
Height: 0.4 m
Weight: 6.0 kg
Ability 1: static
Ability 2: lightning-rod
Type 1: electric
```

## 🛠️ Technologies

- Python 3.x
- PokéAPI
- ASCII Magic for sprite rendering
- RapidFuzz for name matching

## 📝 License

MIT

## 🙏 Acknowledgments

- [PokéAPI](https://pokeapi.co/) for the Pokémon data
