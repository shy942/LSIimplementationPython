from semanticpy.vector_space import VectorSpace


class LSI_search:

    query_content_all = []
    vector_space_object = None


    def __init__(self, query_content, vector_space_object=None):
        self.query_content_all = query_content
        self.queue = []
        import pdb
        pdb.set_trace()
        for vsobj in vector_space_object:
            self.insert(vsobj.transformed_matrix)

    def insert(self, vsobj):
        self.queue.append(vsobj.transformed_matrix)

