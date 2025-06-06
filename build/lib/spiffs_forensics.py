import argparse
import struct
import os

BLOCK_SIZE = 4096 
PAGE_SIZE = 256    
LOOKUP_ENTRY_SIZE = 2 
OBJ_ID_DELETED = 0xFFFF

def print_data_structure(self):
    print("\n[DATA STRUCTURE OVERVIEW]")
    print(f"Image Size: {self.size} bytes")
    print(f"Block Size: {self.block_size}")
    print(f"Page Size: {self.page_size}")
    print(f"Number of Blocks: {self.blocks}")
    print(f"Lookup Entry Size: {LOOKUP_ENTRY_SIZE} bytes")

def list_files(self):
    print("\n[FILES AND OBJECTS FOUND IN IMAGE]")
    for block in range(self.blocks):
        block_addr = block * self.block_size
        self.fd.seek(block_addr)
        lookup_entries = self.fd.read(self.page_size)  # First page of block is lookup table
        for page_idx in range(self.page_size // LOOKUP_ENTRY_SIZE):
            entry_offset = page_idx * LOOKUP_ENTRY_SIZE
            obj_id = struct.unpack('<H', lookup_entries[entry_offset:entry_offset+2])[0]
            if obj_id != 0xFFFF and obj_id != 0x0000:
                print(f"Object ID: 0x{obj_id:04X} in Block {block}, Page {page_idx}")
                    
def list_dir(path, levels=2, indent=0):
        print("Listing directory:", path)
        try:
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_dir(follow_symlinks=False):
                        print("  " * indent + f"DIR : {entry.name}")
                        if levels > 0:
                            list_dir(entry.path, levels - 1, indent + 1)
                    elif entry.is_file(follow_symlinks=False):
                        size = entry.stat().st_size
                        print("  " * indent + f"FILE: {entry.name}\tSIZE: {size}")
        except FileNotFoundError:
            print("- failed to open directory")
        except NotADirectoryError:
            print("- not a directory")

def find_deleted_pages(self):
        print("\n[DELETED PAGES FOUND]")
        for block in range(self.blocks):
            block_addr = block * self.block_size
            self.fd.seek(block_addr)
            lookup_entries = self.fd.read(self.page_size)
            for page_idx in range(self.page_size // LOOKUP_ENTRY_SIZE):
                entry_offset = page_idx * LOOKUP_ENTRY_SIZE
                obj_id = struct.unpack('<H', lookup_entries[entry_offset:entry_offset+2])[0]
                if obj_id == OBJ_ID_DELETED:
                    page_offset = block_addr + page_idx * self.page_size
                    self.fd.seek(page_offset)
                    header = self.fd.read(16)
                    print(f"Deleted page at Block {block}, Page {page_idx} (Offset: {page_offset})")

def close(self):
        self.fd.close()


def main():
    parser = argparse.ArgumentParser(description='SPIFFS Forensic Tool')
    parser.add_argument('image_file', help='SPIFFS image file to analyze')
    parser.add_argument('--list-files', action='store_true', help='List existing files in image')
    parser.add_argument('--list-dir', action='store_true', help='List existing directories in image')
    parser.add_argument('--print-structure', action='store_true', help='Print filesystem structure')
    parser.add_argument('--find-deleted', action='store_true', help='Search for deleted files/pages')
    parser.add_argument('--recover-all', action='store_true', help='Attempt recovery of deleted files')
    parser.add_argument('--block-size', type=int, default=BLOCK_SIZE, help='Set block size (default: 4096)')
    parser.add_argument('--page-size', type=int, default=PAGE_SIZE, help='Set page size (default: 256)')
    parser.add_argument('--output', help='Directory to dump recovered files')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()

    if args.print_structure:
        parser.print_data_structure()

    if args.list_files:
        parser.list_files()
    
    if args.list_dir:
        parser.list_dir()

    if args.find_deleted:
        parser.find_deleted_pages()

    parser.close()

if __name__ == '__main__':
    main()
