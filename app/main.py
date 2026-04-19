from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
from starlette.middleware.sessions import SessionMiddleware
import socket
import os

app = FastAPI()

cart = []

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja2 setup (manual)
env = Environment(loader=FileSystemLoader("app/templates"))

SERVER_NAME = socket.gethostname()
CONTAINER_NAME = os.getenv('CONTAINER_NAME', "unknown")


def add_server_header(response):
    response.headers["X-Server-Name"] = CONTAINER_NAME
    return response


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = env.get_template("index.html")

    html = template.render(
        cart=cart,
        count=len(cart),
        server=CONTAINER_NAME
    )

    response = HTMLResponse(content=html)
    return add_server_header(response)


@app.post("/add")
async def add_item(request: Request):
    data = await request.json()
    item = data.get("item")

    cart.append(item)

    response = JSONResponse({
        "cart": cart,
        "server": CONTAINER_NAME
    })

    return add_server_header(response)


@app.get("/cart")
async def get_cart():
    response = JSONResponse({
        "cart": cart,
        "server": CONTAINER_NAME
    })

    return add_server_header(response)


@app.post("/clear")
async def clear_cart():
    cart.clear()
    response = RedirectResponse("/", status_code=303)
    return add_server_header(response)
