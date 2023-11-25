# Client

to get client ip without await client.connected () :
```
@ui.page("/")
async def index(request: Request):
   connect_ip = request.client.host
```

All client fields :
   
```py
----- client  -----
    body_html =
    build_response = <bound method Client.build_response of <nicegui.client.Client object at 0x1298c8d60>>
    connect_handlers = []
    connected = <bound method Client.connected of <nicegui.client.Client object at 0x1298c8d60>>
    content = <nicegui.element.Element object at 0x1298d40a0>
    created = 1700937639.964743
    disconnect_handlers = []
    disconnected = <bound method Client.disconnected of <nicegui.client.Client object at 0x1298c8d60>>
    download = <bound method Client.download of <nicegui.client.Client object at 0x1298c8d60>>
    elements = {0: <nicegui.element.Element object at 0x1298c8e20>, 1: <nicegui.element.Element object at 0x1298c8ee0>, 2: <nicegui.element.Element object at 0x1298c8fd0>, 3: <nicegui.element.Element object at 0x1298d40a0>}
    environ = {
        'wsgi.input': <engineio.async_drivers.asgi.translate_request.<locals>.AwaitablePayload object at 0x1298e1b50>,
        'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>,
        'wsgi.version': (1, 0),
        'wsgi.async': True,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
        'SERVER_SOFTWARE': 'asgi',
        'REQUEST_METHOD': 'GET',
        'PATH_INFO': '/socket.io/',
        'QUERY_STRING': 'client_id=82920b8e-7ab6-435b-82cb-b536c6cb8f26&EIO=4&transport=websocket',
        'RAW_URI': '/socket.io/?client_id=82920b8e-7ab6-435b-82cb-b536c6cb8f26&EIO=4&transport=websocket',
        'SCRIPT_NAME': '',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'REMOTE_ADDR': '127.0.0.1',
        'REMOTE_PORT': '0',
        'SERVER_NAME': 'asgi',
        'SERVER_PORT': '0',
        'asgi.receive': <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x12989dcd0>>,
        'asgi.send': <function ExceptionMiddleware.__call__.<locals>.sender at 0x129894820>,
        'asgi.scope': {'type': 'websocket',
        'asgi': {'version': '3.0',
        'spec_version': '2.3'},
        'http_version': '1.1',
        'scheme': 'ws',
        'server': ('127.0.0.1', 8080),
        'client': ('127.0.0.1', 63302),
        'client': ('127.0.0.1', 63302),
        'root_path': '/_nicegui_ws',
        'path': '/socket.io/',
        'raw_path': b'/_nicegui_ws/socket.io/',
        'query_string': b'client_id=82920b8e-7ab6-435b-82cb-b536c6cb8f26&EIO=4&transport=websocket',
        'headers': [(b'host', b'127.0.0.1:8080'), (b'connection', b'Upgrade'), (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'), (b'upgrade', b'websocket'), (b'origin', b'http://127.0.0.1:8080'), (b'sec-websocket-version', b'13'), (b'accept-encoding', b'gzip, deflate, br'), (b'accept-language', b'en-US,en;q=0.9,fr;q=0.8'), (b'sec-websocket-key', b'P3sh9240m9RQVtnKZpUi2g=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')],
        'subprotocols': [],
        'state': {},
        'app': <nicegui.app.App object at 0x1123a4970>,
        'fastapi_astack': <contextlib.AsyncExitStack object at 0x1298e1ac0>,
        'router': <fastapi.routing.APIRouter object at 0x128ff28b0>,
        'path_params': {},
        'app_root_path': '',
        'endpoint': <socketio.asgi.ASGIApp object at 0x128ff2fd0>},
        'HTTP_HOST': '127.0.0.1:8080',
        'HTTP_CONNECTION': 'Upgrade',
        'HTTP_PRAGMA': 'no-cache',
        'HTTP_CACHE_CONTROL': 'no-cache',
        'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'HTTP_UPGRADE': 'websocket',
        'HTTP_ORIGIN': 'http://127.0.0.1:8080',
        'HTTP_SEC_WEBSOCKET_VERSION': '13',
        'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
        'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9,fr;q=0.8',
        'HTTP_SEC_WEBSOCKET_KEY': 'P3sh9240m9RQVtnKZpUi2g==',
        'HTTP_SEC_WEBSOCKET_EXTENSIONS': 'permessage-deflate; client_max_window_bits',
        'wsgi.url_scheme': 'http'
    }
    has_socket_connection = True
    head_html =
    id = 82920b8e-7ab6-435b-82cb-b536c6cb8f26
    ip = 127.0.0.1
    is_waiting_for_connection = False
    is_waiting_for_disconnect = False
    layout = <nicegui.element.Element object at 0x1298c8e20>
    next_element_id = 4
    on_air = False
    on_connect = <bound method Client.on_connect of <nicegui.client.Client object at 0x1298c8d60>>
    on_disconnect = <bound method Client.on_disconnect of <nicegui.client.Client object at 0x1298c8d60>>
    open = <bound method Client.open of <nicegui.client.Client object at 0x1298c8d60>>
    page = <nicegui.page.page object at 0x10ed73cd0>
    page_container = <nicegui.element.Element object at 0x1298c8ee0>
    remove_all_elements = <bound method Client.remove_all_elements of <nicegui.client.Client object at 0x1298c8d60>>
    remove_elements = <bound method Client.remove_elements of <nicegui.client.Client object at 0x1298c8d60>>
    run_javascript = <bound method Client.run_javascript of <nicegui.client.Client object at 0x1298c8d60>>
    shared = False
    waiting_javascript_commands = {}
```
