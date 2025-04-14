from langchain_community.docstore.document import Document
from typing import Any


def format_context(vs_results: list[tuple[Document, float]]) -> dict[str, Any]:
    context_text = ""
    sources = set()

    for doc, _score in vs_results:
      context_text += f"{doc.page_content}\n\nSource: {doc.metadata["full_source"]} \n\n{'='*40}\n\n"
      if doc.metadata["full_source"] != 'N/A':
       sources.add(doc.metadata["full_source"])
       
    context_text = context_text.rstrip("\n\n---\n\n")

    return {
       "documents": context_text,
       "sources": sources
    }
