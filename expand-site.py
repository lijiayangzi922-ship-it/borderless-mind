from pathlib import Path
import hashlib, io, json, zipfile

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'source-manifest.json').read_text(encoding='utf-8-sig'))
archive = bytearray()
for part in manifest['parts']:
    data = (root / part['name']).read_bytes()
    assert len(data) == part['bytes'], 'Unexpected part length'
    assert hashlib.sha256(data).hexdigest() == part['sha256'], 'Part checksum failed'
    archive.extend(data)
assert hashlib.sha256(archive).hexdigest() == manifest['archiveSha256'], 'Archive checksum failed'
destination = root / '_site'
destination.mkdir(exist_ok=True)
with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
    for member in bundle.infolist():
        name = member.filename.replace(chr(92), '/')
        target = (destination / name).resolve()
        assert target.is_relative_to(destination.resolve()), 'Invalid archive path'
        if member.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(bundle.read(member))
assert (destination / 'index.html').is_file(), 'Missing homepage'
(destination / '.nojekyll').touch()
print('Verified and extracted complete website.')
