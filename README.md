# inf332-pratica4-flask

An API based on Flask and Flask-APISpec for VagaGO application.


## How to use:

1. Clone the repo:

    ```bash
    git clone https://github.com/ex188929/inf332-pratica4-flask.git
    cd inf332-pratica4-flask

2. Create a virtual environment and install dependencies:

    - With venv:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - With conda:

        ```bash
        conda create -n vagago_api_env python=3.11 -y
        conda activate vagago_api_env
        pip install -r requirements.txt

3. Install package locally:

    ```bash
    pip install -e .

4. Execute the app:

    ```bash
    python -m vagago_api.main

5. Access Swagger UI: http://127.0.0.1:5000/swagger/

6. Test the API:

    ```bash
    curl http://127.0.0.1:5000/hello

Expected response:

    ```json
    {
        "message": "Hello, World!"
    }
