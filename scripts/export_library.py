#!/usr/bin/env python3
"""Export all design library pages via MCP export-page tool.
Saves full Elementor JSON for each page, plus a manifest for re-import.
"""
import json, time, os, subprocess, sys

SID = open('/tmp/mcp_sid.txt').read().strip()
ENDPOINT = 'https://willinstructions-new.affinitydns.uk/wp-json/mcp/elementor-mcp-server'
OUTPUT_DIR = '/tmp/design-library-export'

def mcp_call(method, params, timeout=30):
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": method, "arguments": params},
        "id": 1
    }
    cmd = [
        'curl', '-s', '-X', 'POST', ENDPOINT,
        '-H', 'Content-Type: application/json',
        '-H', f'Mcp-Session-Id: {SID}',
        '-d', json.dumps(payload),
        '--max-time', str(timeout)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
    if result.returncode != 0:
        return None
    try:
        resp = json.loads(result.stdout)
        if 'result' in resp:
            content = resp['result'].get('content', [])
            for item in content:
                if item.get('type') == 'text':
                    try:
                        return json.loads(item['text'])
                    except:
                        return item['text']
        if 'error' in resp:
            print(f"  MCP error: {resp['error']}")
            return None
        return resp
    except:
        return None

# Page ranges by category
categories = {
    'archetypes': list(range(314, 367)) + list(range(438, 555)),
    'philosophy': list(range(1253, 1454, 2)) + list(range(1495, 1696, 2)),
    'brands-batch1': list(range(1741, 2216, 2)),
    'brands-batch2': list(range(2225, 2700, 2)),
    'brands-batch3': list(range(2705, 3360, 2)),
    'index-pages': [737, 1737, 2221]
}

# Create output dirs
for cat in categories:
    os.makedirs(f'{OUTPUT_DIR}/{cat}', exist_ok=True)

results = {'exported': 0, 'failed': 0, 'errors': [], 'pages': {}}

for category, pids in categories.items():
    print(f"\n{'='*50}")
    print(f"Exporting {category} ({len(pids)} pages)")
    print(f"{'='*50}")
    
    for i, pid in enumerate(pids):
        try:
            data = mcp_call('elementor-mcp-export-page', {"post_id": pid})
            
            if data and isinstance(data, (dict, list)):
                filepath = f'{OUTPUT_DIR}/{category}/page-{pid}.json'
                export_obj = {
                    'source': 'willinstructions-new.affinitydns.uk',
                    'page_id': pid,
                    'category': category,
                    'exported_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    'elementor_data': data
                }
                with open(filepath, 'w') as f:
                    json.dump(export_obj, f, indent=2)
                
                # Track file size
                fsize = os.path.getsize(filepath)
                results['pages'][str(pid)] = {
                    'category': category,
                    'file': filepath,
                    'size_bytes': fsize
                }
                results['exported'] += 1
                
                if results['exported'] % 10 == 0:
                    print(f"  [{i+1}/{len(pids)}] Exported {results['exported']} total ({fsize//1024}KB)")
            else:
                results['failed'] += 1
                results['errors'].append(f'pid={pid}: no data')
                print(f"  [{i+1}/{len(pids)}] FAILED pid={pid}")
        except Exception as e:
            results['failed'] += 1
            results['errors'].append(f'pid={pid}: {str(e)[:100]}')
            print(f"  [{i+1}/{len(pids)}] ERROR pid={pid}: {str(e)[:80]}")
        
        time.sleep(0.3)  # Rate limit

# Save manifest
manifest = {
    'version': '1.0',
    'library_name': 'Elementor Design Library',
    'total_exported': results['exported'],
    'total_failed': results['failed'],
    'exported_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'source_site': 'https://willinstructions-new.affinitydns.uk',
    'categories': {cat: {'count': len(pids), 'range': f"{min(pids)}-{max(pids)}"} for cat, pids in categories.items() if pids},
    'pages': results['pages'],
    'errors': results['errors'][:50]
}

with open(f'{OUTPUT_DIR}/manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

# Summary
total_size = sum(p['size_bytes'] for p in results['pages'].values())
print(f"\n{'='*50}")
print(f"EXPORT COMPLETE")
print(f"  Exported: {results['exported']}")
print(f"  Failed: {results['failed']}")
print(f"  Total size: {total_size//1024}KB ({total_size//1024//1024}MB)")
print(f"  Output: {OUTPUT_DIR}")
print(f"{'='*50}")
