# tinyserver

**tinyserver** is a **minimal, production-ready web server** designed for simplicity, speed, and an extremely small footprint. It provides only the essential features needed to serve HTTP requests with no unnecessary abstraction or framework overhead.

Perfect for:

* Embedded systems
* Tiny microservices
* Command‑line tools
* Educational purposes (learn how HTTP works internally)
* Any project that needs *just enough* server functionality

---

## ✨ Features

* 🚀 **Ultra-lightweight** — tiny codebase, minimal dependencies
* 🧱 **Bare‑bones HTTP implementation** — transparent, predictable behavior
* 📦 **Production‑ready** — stable request parsing and response handling
* 🔒 **Secure by default** — sensible defaults and safety‑oriented design
* 📁 **Optional static file serving**
* 🔌 **Extensible architecture** — easy to add small custom features
* 🧪 **Testing‑friendly** — clean, modular structure

---

## 📦 Installation

````bash
```bash
working on how to make it a pip package
# pip install tinyserver
````


---

## 🚀 Quick Start

```python
from tinyserver import TinyServer, Response

server = TinyServer()

@server.route("/")
def index(req):
    return Response(text="Hello from tinyserver!")

server.listen(3000)
print("tinyserver running on http://localhost:3000")
```

---

## 🧩 API Overview

### `createServer(handler)`

Creates a new tinyserver instance.

**Parameters:**

* `handler(req, res)` — function called for every HTTP request.

**Returns:**

* A `server` object with `.listen(port, callback)`.

---

## 📁 Serving Static Files (Optional)

If static file support is enabled:

````python
from tinyserver import TinyServer, serve_static

server = TinyServer()
serve = serve_static("./public")

@server.route("/")
def index(req):
    if serve(req):
        return  # static file was served
    return "Fallback handler"
```
import { createServer, serveStatic } from 'tinyserver';

const serve = serveStatic('./public');

const server = createServer((req, res) => {
  if (serve(req, res)) return; // static file was served

  res.end('Fallback handler');
});

server.listen(3000);
````

---

## 🏗️ Project Structure (Example)

```
tinyserver-py/
├── src/
│   ├── server.js
│   ├── parser.js
│   ├── response.js
│   └── utils.js
├── examples/
├── tests/
└── README.md
```

---

## 🛠️ Development

```bash
git clone https://github.com/sannegash/tinyserver
cd tinyserver
python3 tinyserver
```

---

## 📄 License

MIT License

---

## ❤️ Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

