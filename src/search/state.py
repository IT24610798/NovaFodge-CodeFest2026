class SearchState:
    def __init__(self, question, max_iterations=3):
        self.original_question = question
        self.current_query = question
        self.iteration = 0
        self.max_iterations = max_iterations
        self.retrieved_chunks = []
        self.seen_chunk_ids = set()      # tracks chunk ID
        self.search_history = []         # Query history
        self.is_sufficient = False
        self.final_answer = None

    def add_chunks(self, new_chunks):
        for chunk in new_chunks:
            chunk_id = chunk["id"]
            if chunk_id not in self.seen_chunk_ids:
                self.retrieved_chunks.append(chunk)
                self.seen_chunk_ids.add(chunk_id)

    def record_search(self, query):
        self.search_history.append(query)
        self.iteration += 1

    def has_iterations_left(self):
        return self.iteration < self.max_iterations