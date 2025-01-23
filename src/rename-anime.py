import os
import argparse

def rename_anime_files(directory, start_episode, season, delimiter):
    """
    Rename anime files with custom delimiters and advanced formatting
    
    Args:
        directory (str): Path to directory containing files
        start_episode (int): Starting episode number
        season (int|None): Season number (None for no season)
        delimiter (str|None): Custom delimiter to truncate title
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if not os.path.isfile(file_path) or not filename.startswith('Watch '):
            continue

        base, ext = os.path.splitext(filename)
        
        try:
            rest = base[len('Watch '):]
            title_part, episode_part = rest.split(' Episode ', 1)
            
            # Process custom delimiter if specified
            if delimiter:
                title_part = title_part.split(delimiter, 1)[0].strip()
            
            original_episode = int(episode_part.split()[0])
            calculated_episode = original_episode + (start_episode - 1)
            
            # Build filename components
            season_str = f"S{season:02d} - " if season else ""
            new_base = f"{title_part} - {season_str}E{calculated_episode:02d}"
            
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
        description="Anime File Renamer with Custom Delimiters",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  %(prog)s --delimiter "(Dub)"           # Remove dub indicator
  %(prog)s -S 2 -d " [Subbed]"           # Season 2, remove subbed tag
  %(prog)s -s 10 -d " - "                # Start from 10, clean hyphenated titles
  %(prog)s -S 1 -s 1 -d "(Uncensored)"   # Season 1, remove uncensored tag"""
    )
    
    parser.add_argument(
        '-p', '--path',
        type=str,
        default='.',
        help="Directory containing anime files (default: current directory)"
    )
    parser.add_argument(
        '-s', '--start',
        type=int,
        dest='start_episode',
        default=1,
        help="Starting episode number (≥1, default: %(default)s)"
    )
    parser.add_argument(
        '-S', '--season',
        type=int,
        default=None,
        help="Season number (≥1, adds season to filename)"
    )
    parser.add_argument(
        '-d', '--delimiter',
        type=str,
        default=None,
        help="Custom delimiter to truncate title (e.g. '(Dub)')"
    )
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        print(f"Error: Directory does not exist - {args.path}")
        exit(1)
        
    if args.start_episode < 1:
        print("Error: Starting episode must be ≥1")
        exit(1)
        
    if args.season is not None and args.season < 1:
        print("Error: Season number must be ≥1")
        exit(1)
        
    rename_anime_files(args.path, args.start_episode, args.season, args.delimiter)