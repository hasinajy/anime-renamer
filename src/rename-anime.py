import os
import argparse

def rename_anime_files(directory):
    """
    Rename anime files in the specified directory following the pattern:
    "Anime Title - EXX.ext" based on the original "Watch [Title] Episode [XX] ..." format
    
    Args:
        directory (str): Path to directory containing files to rename
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories and non-matching files
        if not os.path.isfile(file_path) or not filename.startswith('Watch '):
            continue

        base, ext = os.path.splitext(filename)
        
        try:
            # Extract title and episode number
            rest = base[len('Watch '):]
            title_part, episode_part = rest.split(' Episode ', 1)
            
            # Format episode number with leading zero
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
    parser = argparse.ArgumentParser(
        description="Anime File Renamer - Rename anime files from 'Watch [Title] Episode [XX]' format to 'Title - EXX' format",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  %(prog)s --path "/anime/my_hero_Academia"
  %(prog)s  # Uses current directory
  %(prog)s --help  # Show this help message"""
    )
    
    parser.add_argument(
        '-p', '--path',
        type=str,
        default='.',
        help="Directory containing anime files (default: current directory)"
    )
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        print(f"Error: Directory does not exist - {args.path}")
        exit(1)
        
    rename_anime_files(args.path)