class Endpoint:
    """
    Represents an Endpoint
    """

    def __init__(self, obj) -> None:
        self.path = obj["path"]
        queries = obj["queries"]
        self.queries = []
        if not queries:
            return
        for query in queries:
            key = query["q"]
            required = query["r"]
            self.queries.append({"key": key, "required": required})

    def __str__(self) -> str:
        return "{" + f"\n\tpath: {self.path}," + f"\n\tqueries: {self.queries}" + "\n}"
