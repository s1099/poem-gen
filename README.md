# Poem generator using generative AI

Streamlit app for poem generaton with customizable parameters

## Running

1. [Install Python](https://www.python.org/downloads/)

2. Clone the repo locally 
    ```
    git clone https://github.com/s1099/poem-gen
    cd poem-gen
    ``` 

3. (optional) create venv
    ```
    python3 -m venv .venv
    # or use uv
    uv venv    

    # On macOS and Linux
    source .venv/bin/activate

    # On Windows
    .venv\Scripts\activate
    ```

4. Install dependencies
    ```
    pip install -r requirements.txt
    # or with uv
    uv pip install -r requirements.txt
    ```

5. Rename `.env.example` to `.env` and put in your gemini api key

6. `streamlit run app.py` to run
