# odoo-addons
Odoo addons developped by TransformaTek team


## Regenerate assets using RPC calls

```bash
curl 'http://localhost:8069/jsonrpc' -X POST  -H 'Content-Type: application/json' --data-raw '{"jsonrpc": "2.0","method": "call","params": {"service": "object","method": "execute","args": ["<dbname>",2,"<password>","ir.attachment","search",["&",["res_model","=","ir.ui.view"], "|","|","|",["name","=like","%.assets_%.css"],["name","=like","%.assets_%.js"],["name","=","web_editor.summernote.css"],["name","=","web_editor.summernote.js"]]]},"id":14996920}'

curl 'http://localhost:8069/jsonrpc' -X POST  -H 'Content-Type: application/json' --data-raw '{"jsonrpc": "2.0","method": "call","params": {"service": "object","method": "execute","args": ["<dbname>",2,"<password>","ir.attachment","unlink",[<returned list from first command>]]},"id":14996920}'
```

Force assets regenaration by coionnecting to : [http://localhost:8069/web?debug=asset](http://localhost:8069/web?debug=asset)
