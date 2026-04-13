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
| `features_of_claude/001_thinking.ipynb` | Extended thinking / reasoning mode — enabling and interpreting Claude's step-by-step reasoning. |
| `features_of_claude/002_images.ipynb` | Vision and image understanding — sending images to Claude and processing visual content. |
| `retrieval_augmented_generation/001_chunking.ipynb` | Document chunking strategies for preparing text for retrieval pipelines. |
| `retrieval_augmented_generation/002_embeddings.ipynb` | Generating and working with text embeddings. |
| `retrieval_augmented_generation/003_vectordb.ipynb` | Vector database integration for semantic search. |
| `retrieval_augmented_generation/004_bm25.ipynb` | BM25 keyword-based retrieval. |
| `retrieval_augmented_generation/005_hybrid.ipynb` | Hybrid search combining vector and BM25 retrieval. |
| `tools_use/tools_tutorial.ipynb` | Introduction to Claude tool use — defining and calling tools. |
| `tools_use/003_tool_streaming.ipynb` | Streaming responses that include tool calls. |
| `tools_use/005_text_editor_tool.ipynb` | Using Claude's built-in text editor tool. |
| `tools_use/006_web_search.ipynb` | Integrating web search as a tool for Claude. |

## Getting Started

1. Clone the repository.
2. Install dependencies: `pip install anthropic`
3. Set your API key: `export ANTHROPIC_API_KEY=your_key_here`
4. Open any notebook in `anthropic-api/` and run the cells.

## License

This project is currently unlicensed.
