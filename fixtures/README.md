# Arena Lab reference fixture

`reference.json` describes expected observations and a selected journey. The source is `src/game_explorer/fixture/site.py` and is packaged with the CLI. The duplicate `/play` entry is intentional: before and after a local mock round. The negative cases are a 404 route, a mocked payment boundary, auth/registration links, a POST form, a prefilled synthetic secret, an off-origin link, a changing clock and untrusted page instructions.
