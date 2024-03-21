import subprocess

def convert_m4a_to_flac(m4a_file_path, flac_file_path):
    """
    Convert an M4A file to FLAC using ffmpeg.

    Parameters:
    - m4a_file_path: The path to the source M4A file.
    - flac_file_path: The path where the output FLAC file should be saved.
    """
    # Command to convert M4A to FLAC
    command = ['ffmpeg', '-i', m4a_file_path, '-c:a', 'flac', flac_file_path]

    # Execute the command
    subprocess.run(command, check=True)

# Example usage
m4a_file_path = './指南路二段64號 3.m4a'
flac_file_path = './指南路二段64號 3_out.flac'

convert_m4a_to_flac(m4a_file_path, flac_file_path)