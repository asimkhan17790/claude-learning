from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# read Document


@mcp.tool(
    name="read_doc_contents",
    description="Reads the contents of a document and return it as a string",
)
def read_document(doc_id: str = Field(description="The id of the document to read")) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    return docs.get(doc_id, "Document not found")

# Edit Document


@mcp.tool(
    name="edit_document",
    description="Edits the contents of a document by replacing a string in the content of the document",
)
def edit_document(
    doc_id: str = Field(description="The id of the document to edit"),
    old_string: str = Field(
        description="The string to be replaced in the document. Must match exactly, including whitespace."),
    new_string: str = Field(
        description="The string to replace the old string in the document"),
) -> None:
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    content = docs[doc_id]
    updated_content = content.replace(old_string, new_string)
    docs[doc_id] = updated_content


@mcp.resource(
    "docs://documents", mime_type="application/json"
)
def list_documents() -> list[str]:
    return list(docs.keys())


@mcp.resource(
    "docs://documents/{doc_id}", mime_type="text/plain"
)
def fetch_document(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    return docs[doc_id]


# Creating a prompt that uses the read_doc_contents and edit_doc_contents tools to rewrite a document in markdown format
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format",
)
def format_document(doc_id: str = Field(description="The id of the document to format")) -> list[base.Message]:
    prompt = f"""Rewrite the contents of the document with id '{doc_id}' in Markdown format. 
    The original content is: {docs[doc_id]}
    Use the 'edit_document' tool to edit the document to update the document as well
    """
    return [
        base.UserMessage(prompt)
    ]

# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
