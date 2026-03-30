# claude-learning

A hands-on learning repository for the Anthropic Claude API, covering core concepts from basic requests through streaming, structured outputs, and prompt evaluation.

## Notebooks

All notebooks are in the `anthropic-api/` directory.

| Notebook | Description |
|---|---|
| `requests.ipynb` | Basic API requests using the Anthropic SDK — creating a client, managing message history, and simple multi-turn conversations. |
| `basic_chat_bot.ipynb` | Interactive chatbot with helper functions for conversation history management and a user input loop. |
| `math_tutor.ipynb` | Math tutoring assistant demonstrating how system prompts shape model behavior — guides students step-by-step while declining off-topic questions. |
| `streaming-responses.ipynb` | Real-time streaming of Claude responses using the SDK's streaming API, displaying output as it's generated. |
| `structured_data.ipynb` | Structured data extraction using stop sequences to enforce specific output formats (JSON, bash commands, etc.) for reliable parsing. |
| `structured_data_exercise.ipynb` | Exercise generating AWS CLI commands and EventBridge rules with stop sequences to control output format. |
| `prompt_evaluation.ipynb` | Prompt evaluation pipeline — generates test cases for AWS tasks, runs prompts, and grades responses via syntax validation and model-based scoring. |
| `prompt_engineering/prompting.ipynb` | Advanced prompt engineering toolkit — `PromptEvaluator` class with concurrent dataset generation, model-graded scoring, and HTML report output. Includes an end-to-end athlete meal plan evaluation example. |

## Getting Started

1. Clone the repository.
2. Install dependencies: `pip install anthropic`
3. Set your API key: `export ANTHROPIC_API_KEY=your_key_here`
4. Open any notebook in `anthropic-api/` and run the cells.

## License

This project is currently unlicensed.
