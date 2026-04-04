# CLAUDE.md

## Project Overview

A learning repository for exploring the Anthropic Claude API. All notebooks live in `anthropic-api/` and build progressively from basic requests to more advanced patterns.

## Structure

```
claude-learning/
├── anthropic-api/
│   ├── helper_functions.py       # Shared utilities (Anthropic client, chat(), message helpers)
│   ├── dataset.json              # Test dataset for prompt evaluation
│   ├── requests.ipynb            # Basic API requests and multi-turn conversations
│   ├── basic_chat_bot.ipynb      # Interactive chatbot with history management
│   ├── math_tutor.ipynb          # System prompt design — math tutoring assistant
│   ├── streaming-responses.ipynb # Real-time streaming with the SDK
│   ├── structured_data.ipynb     # Stop sequences for structured output (JSON, bash)
│   ├── structured_data_exercise.ipynb  # AWS CLI / EventBridge structured output exercise
│   ├── prompt_evaluation.ipynb   # Prompt eval pipeline with scoring
│   ├── prompt_engineering/
│   │   └── prompting.ipynb       # PromptEvaluator class — dataset gen, concurrent eval, HTML reports
│   ├── features_of_claude/
│   │   ├── 001_thinking.ipynb    # Extended thinking / reasoning mode
│   │   └── 002_images.ipynb      # Vision / image understanding
│   ├── retrieval_augmented_generation/
│   │   ├── 001_chunking.ipynb    # Document chunking strategies
│   │   ├── 002_embeddings.ipynb  # Text embeddings
│   │   ├── 003_vectordb.ipynb    # Vector database integration
│   │   ├── 004_bm25.ipynb        # BM25 keyword search
│   │   └── 005_hybrid.ipynb      # Hybrid search (vector + BM25)
│   └── tools_use/
│       ├── tools_tutorial.ipynb  # Introduction to tool use
│       ├── 003_tool_streaming.ipynb  # Streaming with tool calls
│       ├── 005_text_editor_tool.ipynb  # Built-in text editor tool
│       └── 006_web_search.ipynb  # Web search tool integration
├── README.md
└── CLAUDE.md
```

## Key Shared Utilities (`helper_functions.py`)

- `chat(messages, ...)` — wraps `client.messages.create()`, returns text string
- `add_user_message(messages, text)` — appends a user turn to the message list
- `add_assistant_message(messages, text)` — appends an assistant turn
- `DEFAULT_MODEL` — set to `claude-sonnet-4-0`
- Client is initialized from `.env` via `load_dotenv()`

## Environment

- Python with `anthropic` and `python-dotenv` packages
- API key stored in `.env` as `ANTHROPIC_API_KEY`
- `.env` is gitignored

## Conventions

- Notebooks import from `helper_functions.py` for shared client/chat logic
- Stop sequences are used to enforce structured output formats
- Evaluation notebooks use model-based grading alongside syntax checks
