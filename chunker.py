from langchain.text_splitter import CharacterTextSplitter
import config

def split_text(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    return splitter.split_text(text)