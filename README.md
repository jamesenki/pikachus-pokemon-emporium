# Pikachu's Pokemon Emporium

A Python script for downloading Pokemon TCG collections from the Internet Archive.

## Features

- Downloads original files from Internet Archive Pokemon collections
- Filters for image files (PNG, JPG, etc.)
- Supports multiple collections simultaneously
- Progress tracking and error handling

## Usage

1. Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install internetarchive
```

2. Run the script:
```bash
python3 download_pokemon.py
```

## Collections Downloaded

Currently downloads from these verified collections:
- `RusBTPokemonTCGCards` - Pokemon TCG booster packs
- `RusPCPokemonTCGCards` - Pokemon TCG cards and packs
- `animecollection_pokemon` - Pokemon anime content
- `TwitchPlaysPokemon` - Twitch Plays Pokemon streams

## Downloaded Content

The script has successfully downloaded 18+ PNG files including:
- High-resolution booster pack images
- Individual Pokemon card artwork
- Various Pokemon TCG promotional materials

Files are organized by collection item in the `downloads/` directory.