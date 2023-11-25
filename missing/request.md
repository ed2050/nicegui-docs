```py
----- request  -----
    app = <nicegui.app.App object at 0x1123a4970>
    auth = error on access
    base_url = http://127.0.0.1:8080/
    body = <bound method Request.body of <starlette.requests.Request object at 0x1298c8b50>>
    client = Address(host='127.0.0.1', port=63297)
    close = <bound method Request.close of <starlette.requests.Request object at 0x1298c8b50>>
    cookies = {}
    form = <bound method Request.form of <starlette.requests.Request object at 0x1298c8b50>>
    get = <bound method Mapping.get of <starlette.requests.Request object at 0x1298c8b50>>
    headers = Headers({
        'host': '127.0.0.1:8080',
        'connection': 'keep-alive',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'referer': 'http://127.0.0.1:8080/foo?bar=raboof',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fr;q=0.8'
    })
    is_disconnected = <bound method Request.is_disconnected of <starlette.requests.Request object at 0x1298c8b50>>
    items = <bound method Mapping.items of <starlette.requests.Request object at 0x1298c8b50>>
    json = <bound method Request.json of <starlette.requests.Request object at 0x1298c8b50>>
    keys = <bound method Mapping.keys of <starlette.requests.Request object at 0x1298c8b50>>
    method = GET
    path_params = {}
    query_params = bar=raboof
    receive = <function BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.receive_or_disconnect at 0x1298575e0>
    scope = {
        'type': 'http',
        'asgi': {'version': '3.0',
        'spec_version': '2.3'},
        'http_version': '1.1',
        'server': ('127.0.0.1', 8080),
        'client': ('127.0.0.1', 63297),
        'scheme': 'http',
        'root_path': '',
        'headers': [(b'host', b'127.0.0.1:8080'), (b'connection', b'keep-alive'), (b'cache-control', b'max-age=0'), (b'sec-ch-ua', b'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"'), (b'sec-ch-ua-mobile', b'?0'), (b'sec-ch-ua-platform', b'"macOS"'), (b'upgrade-insecure-requests', b'1'), (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'), (b'accept', b'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'), (b'sec-fetch-site', b'same-origin'), (b'sec-fetch-mode', b'navigate'), (b'sec-fetch-dest', b'document'), (b'referer', b'http://127.0.0.1:8080/foo?bar=raboof'), (b'accept-encoding', b'gzip, deflate, br'), (b'accept-language', b'en-US,en;q=0.9,fr;q=0.8')],
        'state': {},
        'method': 'GET',
        'path': '/foo',
        'raw_path': b'/foo',
        'query_string': b'bar=raboof',
        'app': <nicegui.app.App object at 0x1123a4970>,
        'fastapi_astack': <contextlib.AsyncExitStack object at 0x1298c8ac0>,
        'router': <fastapi.routing.APIRouter object at 0x128ff28b0>,
        'endpoint': <function page.__call__.<locals>.decorated at 0x12948aa60>,
        'path_params': {},
        'route': APIRoute(path='/foo', name='decorated', methods=['GET'])
    }
    send_push_promise = <bound method Request.send_push_promise of <starlette.requests.Request object at 0x1298c8b50>>
    session = error on access
    state = <starlette.datastructures.State object at 0x12989d3d0>
    stream = <bound method Request.stream of <starlette.requests.Request object at 0x1298c8b50>>
    url = http://127.0.0.1:8080/foo?bar=raboof
    url_for = <bound method HTTPConnection.url_for of <starlette.requests.Request object at 0x1298c8b50>>
    user = error on access
    values = <bound method Mapping.values of <starlette.requests.Request object at 0x1298c8b50>>

```
