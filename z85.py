import base64


def compress_hex_z85(hex_string):
    bytes_data = bytes.fromhex(hex_string)
    compressed = base64.z85encode(bytes_data).decode()
    return compressed

def decompress_hex_z85(z85_string):
    bytes_data = base64.z85decode(z85_string)
    return bytes_data.hex()



def convert_raw_to_z85(raw_file_path, z85_file_path):
    with open(raw_file_path, mode='r') as raw_file, open(z85_file_path, mode='w') as z85_file:
        for raw_line in raw_file:
            raw_line_stripped = raw_line.strip()
            raw_line_evened = raw_line_stripped + 'a'
            z85_line = compress_hex_z85(raw_line_evened)
            print(z85_line, file=z85_file)

def convert_z85_to_raw(raw_file_path, z85_file_path):
    with open(raw_file_path, mode='w') as raw_file, open(z85_file_path, mode='r') as z85_file:
        for z85_line in z85_file:
            z85_line_stripped = z85_line.strip()
            raw_line_evened = decompress_hex_z85(z85_line_stripped)
            raw_line = raw_line_evened[:-1]
            print(raw_line, file=raw_file)


RAW_FILE_PATH='...'
Z85_FILE_PATH='...'

if __name__ == '__main__':
    convert_raw_to_z85(
        RAW_FILE_PATH,
        Z85_FILE_PATH
    )
