# Configurações para subir ambinete de demonstração

## Iniciar - Passos

1) Acessar a pasta ``config/demo``

2) Executar o comando:

    ```bash
    docker compose up
    ```

3) Após o sistema subir, executar:

    ```bash
    docker run --rm --network host --pull always ghcr.io/larc-logs-transparentes/bu-utils:gh-73
    ```


## Finalizar - Passos

1) Acessar a pasta ``config/demo``

2) Executar o comando:

    ```bash
    docker compose down
    ```
