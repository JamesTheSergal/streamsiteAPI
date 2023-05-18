class Stream:

    def __init__(self, id, state, desc, streamer, viewers):
        self.id = id
        self.state = state
        self.desc = desc
        self.streamer = streamer
        self.viewers = viewers