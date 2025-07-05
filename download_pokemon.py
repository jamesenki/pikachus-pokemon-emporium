#!/usr/bin/env python3
"""
Download original files from Internet Archive Pokemon collections.
"""

import internetarchive as ia
import os

# =======================
COLLECTIONS = [
    'RusBTPokemonTCGCards',
    'RusPCPokemonTCGCards',
    'animecollection_pokemon',
    'TwitchPlaysPokemon'
]
DEST_ROOT = './downloads'
# =======================

def download_collection(collection_id, dest_root, max_items=5):
    """Download items from a specific Internet Archive collection."""
    print(f'\n🎯 Starting collection: {collection_id}')
    os.makedirs(dest_root, exist_ok=True)
    
    search = ia.search_items(f'collection:{collection_id}')
    count = 0
    
    for result in search:
        count += 1
        if count > max_items:
            print(f'⚠️  Stopping after {max_items} items from {collection_id}')
            break
            
        item_id = result['identifier']
        print(f'\n➡️ Processing item: {item_id}')
        dest = os.path.join(dest_root, item_id)
        os.makedirs(dest, exist_ok=True)
        
        item = ia.get_item(item_id)
        
        # Filter for 'original' files only
        originals = [f['name'] for f in item.files if f.get('source') == 'original']
        
        if not originals:
            # Download image files if no originals found
            image_files = [f['name'] for f in item.files 
                          if f['name'].endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            if image_files:
                print(f'   📁 Downloading {len(image_files)} image files...')
                originals = image_files
            else:
                print('   ⚠️ No image files found.')
                continue
        else:
            print(f'   🔍 Found {len(originals)} original files, downloading...')
        
        try:
            ia.download(item_id, files=originals, destdir=dest, verbose=False)
            print(f'   ✅ Downloaded {len(originals)} files')
        except Exception as e:
            print(f'   ❌ Error downloading {item_id}: {e}')

def search_pokemon_collections():
    """Search for Pokemon-related collections in Internet Archive."""
    print('🔍 Searching for Pokemon collections...')
    search = ia.search_items('pokemon AND mediatype:collection')
    
    collections = []
    for i, result in enumerate(search):
        if i >= 20:
            break
        collections.append(result['identifier'])
        print(f'{i+1}. {result["identifier"]}')
    
    return collections

if __name__ == '__main__':
    print("🎮 Pikachu's Pokemon Emporium - Internet Archive Downloader")
    print("=" * 60)
    
    # Download from known collections
    for collection in COLLECTIONS:
        download_collection(collection, DEST_ROOT, max_items=5)
    
    print(f"\n🎉 Download complete! Check the '{DEST_ROOT}' directory for files.")