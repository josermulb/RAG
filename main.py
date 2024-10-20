import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--question', default='¿Qué puedes contarme sobre el libro?')
    args = parser.parse_args()

    # Create the vector database
    print("\nCreating Vector Database\n------------------------\n")
    from src.vector_store.vector_store import VectorStore
    vector_store = VectorStore()
    vector_store.run()

    # Retrieval
    print("\nRetrieving Chunks\n------------------------\n")
    from src.retrieval.retrieval_manager import RetrievalManager
    retrieval_manager = RetrievalManager('chroma')

    chunks = retrieval_manager.retrieve_chunks(args.question, top_k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in chunks])

    # Build Prompt
    print("\nBuilding Prompt\n------------------------\n")
    from src.prompts.prompt_manager import PromptManager
    prompt_manager = PromptManager()
    prompt = prompt_manager.build_prompt(context_text, args.question)

    # Inference
    print("\nRunning Inference\n------------------------\n")
    from src.inference.inference import InferenceManager
    inference_manager = InferenceManager()
    answer = inference_manager.run_inference(prompt)
    print(f"---Question---:\n{args.question}\n\n---Answer---:\n{answer.content}")
