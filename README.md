# plat sse-with-fastapi

- `src/stream_client_example.py`

or

```
curl -N -X POST  \
-H "Content-Type: application/json" \
-d '{"query":"大谷翔平はどこに所属していますか？"}' \
http://localhost:8080/streaming/ask

```

## Run Container

To start development, you are supposed to run the following command:
```bash 
make setup   
```

## Development Commands

### Enter into container
```bash
make enter_container
```

### Lint

```bash 
make lint
```
### Format

```bash 
make format
```

## References
- https://gist.github.com/oneryalcin/2921408da70266aa61f9c40cb2973865