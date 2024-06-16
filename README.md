<div align="center">

<div align="center">
<br/>
CodeGuard AI Cover Agent aims to help efficiently increasing code coverage, by automatically generating qualified tests to enhance existing test suites
</div>

</div>

## Table of Contents
- [Overview](#overview)
- [Installation and Usage](#installation-and-usage)


## Overview
This tool is part of a broader suite of utilities designed to automate the creation of unit tests for software projects. Utilizing advanced Generative AI models, it aims to simplify and expedite the testing process, ensuring high-quality software development. The system comprises several components:
1. **Test Runner:** Executes the command or scripts to run the test suite and generate code coverage reports.
2. **Coverage Parser:** Validates that code coverage increases as tests are added, ensuring that new tests contribute to the overall test effectiveness.
3. **Prompt Builder:** Gathers necessary data from the codebase and constructs the prompt to be passed to the Large Language Model (LLM).
4. **AI Caller:** Interacts with the LLM to generate tests based on the prompt provided.

## Installation and Usage
### Requirements
Before you begin, make sure you have the following:
- `OPENAI_API_KEY` set in your environment variables, which is required for calling the OpenAI API.
- Code Coverage tool: A Cobertura XML code coverage report is required for the tool to function correctly.
  - For example, in Python one could use `pytest-cov`. Add the `--cov-report=xml` option when running Pytest.

If running directly from the repository you will also need:
- Python installed on your system.
- Poetry installed for managing Python package dependencies. Installation instructions for Poetry can be found at [https://python-poetry.org/docs/](https://python-poetry.org/docs/).

### Standalone Runtime
The Cover Agent can be installed as a Python Pip package or run as a standalone executable.

#### Python Pip
To install the Python Pip package directly via GitHub run the following command:
```
pip install git+[Project .git Location]
```


### Repository Setup
Run the following command to install all the dependencies and run the project from source:
```shell
poetry install
```

### Running the Code
After downloading the executable or installing the Pip package you can run the Cover Agent to generate and validate unit tests. Execute it from the command line by using the following command:
```shell
cover-agent \
  --source-file-path "<path_to_source_file>" \
  --test-file-path "<path_to_test_file>" \
  --code-coverage-report-path "<path_to_coverage_report>" \
  --test-command "<test_command_to_run>" \
  --test-command-dir "<directory_to_run_test_command>" \
  --coverage-type "<type_of_coverage_report>" \
  --desired-coverage <desired_coverage_between_0_and_100> \
  --max-iterations <max_number_of_llm_iterations> \
  --included-files "<optional_list_of_files_to_include>"
```

You can use the example projects within this repository to run this code as a test.

Follow the steps in the README.md file located in the `templated_tests/python_fastapi/` directory, then return to the root of the repository and run the following command to add tests to the **python fastapi** example:
```shell
cover-agent \
  --source-file-path "templated_tests/python_fastapi/app.py" \
  --test-file-path "templated_tests/python_fastapi/test_app.py" \
  --code-coverage-report-path "templated_tests/python_fastapi/coverage.xml" \
  --test-command "pytest --cov=. --cov-report=xml --cov-report=term" \
  --test-command-dir "templated_tests/python_fastapi" \
  --coverage-type "cobertura" \
  --desired-coverage 70 \
  --max-iterations 10
```


Note: If you are using Poetry then use the `poetry run cover-agent` command instead of the `cover-agent` run command.

### Outputs
A few debug files will be outputted locally within the repository (that are part of the `.gitignore`)
* `run.log`: A copy of the logger that gets dumped to your `stdout`
* `test_results.html`: A results table that contains the following for each generated test:
  * Test status
  * Failure reason (if applicable)
  * Exit code, 
  * `stderr`
  * `stdout`
  * Generated test

### Additional logging
If you set an environment variable `WANDB_API_KEY`, the prompts, responses, and additional information will be logged to [Weights and Biases](https://wandb.ai/).

### Using other LLMs
This project uses LiteLLM to communicate with OpenAI and other hosted LLMs (supporting 100+ LLMs to date). To use a different model other than the OpenAI default you'll need to:
1. Export any environment variables needed by the supported LLM [following the LiteLLM instructions](https://litellm.vercel.app/docs/proxy/quick_start#supported-llms).
2. Call the name of the model using the `--model` option when calling Cover Agent.

For example (as found in the [LiteLLM Quick Start guide](https://litellm.vercel.app/docs/proxy/quick_start#supported-llms)):
```shell
export VERTEX_PROJECT="hardy-project"
export VERTEX_LOCATION="us-west"

cover-agent \
  ...
  --model "vertex_ai/gemini-pro"
```

#### OpenAI Compatible Endpoint
```shell
export OPENAI_API_KEY="<your api key>" # If <your-api-base> requires an API KEY, set this value.

cover-agent \
  ...
  --model "openai/<your model name>" \
  --api-base "<your-api-base>"
```



### Running Tests
Set up your development environment by running the `poetry install` command as you did above. 

Note: for older versions of Poetry you may need to include the `--dev` option to install Dev dependencies.

After setting up your environment run the following command:
```
poetry run pytest --junitxml=testLog.xml --cov=templated_tests --cov=cover_agent --cov-report=xml --cov-report=term --log-cli-level=INFO
```
This will also generate all logs and output reports that are generated in `.github/workflows/ci_pipeline.yml`.


