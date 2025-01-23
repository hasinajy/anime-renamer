import os

def rename_anime_files(directory='.'):
    for filename in os.listdir(directory):
        # Skip non-files and files that don't start with 'Watch '
        if not os.path.isfile(os.path.join(directory, filename)) or not filename.startswith('Watch '):
            continue

        # Split filename and extension
        base, ext = os.path.splitext(filename)
        
        try:
            # Remove 'Watch ' and split into title/episode parts
            rest = base[len('Watch '):]
            title_part, episode_part = rest.split(' Episode ', 1)
            
            # Extract episode number and format
            episode_number = int(episode_part.split()[0])
            new_base = f"{title_part} - E{episode_number:02d}"
            
            # Create new filename and rename
            new_filename = new_base + ext
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_filename)
            )
            print(f"Renamed: {filename} -> {new_filename}")
            
        except (ValueError, IndexError) as e:
            print(f"Skipping {filename}: {str(e)}")

if __name__ == '__main__':
    rename_anime_files()