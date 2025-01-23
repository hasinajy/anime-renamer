import os
import argparse

def rename_anime_files(directory, start_episode):
    """
    Rename anime files with configurable starting episode number
    
    Args:
        directory (str): Path to directory containing files to rename
        start_episode (int): Starting episode number for the first file
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if not os.path.isfile(file_path) or not filename.startswith('Watch '):
            continue

        base, ext = os.path.splitext(filename)
        
        try:
            rest = base[len('Watch '):]
            title_part, episode_part = rest.split(' Episode ', 1)
            
            original_episode = int(episode_part.split()[0])
            calculated_episode = original_episode + (start_episode - 1)
            
            new_base = f"{title_part} - E{calculated_episode:02d}"
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
        description="Anime File Renamer with Episode Offset",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  %(prog)s --path "/anime" --start 10  # Start numbering from 10
  %(prog)s -p ~/anime -s 5             # Start numbering from 5
  %(prog)s                             # Use current dir with default numbering"""
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
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        print(f"Error: Directory does not exist - {args.path}")
        exit(1)
        
    if args.start_episode < 1:
        print("Error: Starting episode must be ≥1")
        exit(1)
        
    rename_anime_files(args.path, args.start_episode)