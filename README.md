## What does this do?

I generate multiple drafts for each response. The number of drafts I generate varies depending on the complexity of the request. For simple requests, I may only generate a few drafts. For more complex requests, I may generate dozens of drafts.
I use a variety of factors to determine how many drafts to generate. These factors include the length of the request, the number of possible answers, and the level of detail required. I also consider the quality of the drafts I generate. If I am not satisfied with a draft, I will generate a new one.
I continue to generate drafts until I am satisfied with the quality of the response. I then select the best draft and send it to you.
Generating multiple drafts allows me to provide you with the best possible response. By considering all of the possible answers and the level of detail required, I can ensure that you receive a response that is accurate, comprehensive, and informative.

Content is then evaluated with GPT4 which takes into account:

```
It is accurate and factual.
It is comprehensive and informative.
It is clear and easy to understand.
It is relevant to the request.
It is creative and engaging.
The quality of the language used.
The accuracy of the information.
The relevance of the information to the request.
The clarity and conciseness of the writing.
The creativity and engagement of the writing.
```


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

![image](https://user-images.githubusercontent.com/8228671/236520814-81d8b733-7ec0-4512-9d98-a78982a573e2.png)






