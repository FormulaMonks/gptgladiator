## Quick start guide

### Prerequisites
- An [OpenAI](https://platform.openai.com/) API Key
  - Ensure an environment variable named `OPENAI_API_KEY` is set containing a valid key to call the OpenAI REST API, OR
  - Instead of setting the environment variable manually, you can create a .env file at the root of the repository with 
  the following content (replace the placeholder values between <> with your own keys):
    ```ini
    OPENAI_API_KEY=<YOUR_OPENAI_API_KEY_HERE>
    ```
  - If you already have an existing environment variable you can also use its handler in the .env file:
    ```ini
    OPENAI_API_KEY=${OPENAI_API_KEY}
    ```

### Configurable settings
Other settings you can set via the .env file / environment variables:
```ini
# When set to On or a truthy value (1, True), the OpenAI API is mocked and a sample response is used.
# Useful while the API key is available or while developing other app features)
# Default: Off
MOCK_API=<Off|On> 

# When set to On or a truthy value (1, True) log messages are printed to the python console / terminal from where
# the app is running with information about the requests and responses while interacting with the OpenAI API.
 # Default: Off   
DEBUG=<On|Off>
```

### How to run it locally?

Clone this repo:
```shell
$ git clone https://github.com/TheoremOne/gladiator.git
```
Navigate to the directory where the sources where cloned to:
```shell
$ cd gladiator
````

Create and activate a python virtual environment:
```shell
Windows:
$ python -m venv venv
$ .\venv\Scripts\activate

Linux:
$ python3 -m venv venv
$. venv/bin/activate
```

Upgrade pip if needed and install requirements:
```shell
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

Run the app:
_Remove the optional <--debug> to run in production mode_
```shell
$ flask --app gladiator run <--debug>

```

Type a prompt and click **Go**

Enjoy!








