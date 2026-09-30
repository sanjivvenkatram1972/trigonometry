import os
import shutil

print("Preparing PWA deployment assets...")
# Simple verification script to ensure all required assets exist
required_files = [
    'manifest.webmanifest',
    'sw.js',
    'pwa_snippets.html',
    'icons/icon-192x192.png',
    'icons/icon-512x512.png',
    'icons/icon-maskable-192x192.png',
    'icons/icon-maskable-512x512.png'
]

missing = 0
for f in required_files:
    if os.path.exists(f):
        print(f"[OK] Found {f}")
    else:
        print(f"[MISSING] {f}")
        missing += 1

if missing == 0:
    print("All PWA assets verified successfully!")
else:
    print(f"Warning: {missing} files are missing.")
