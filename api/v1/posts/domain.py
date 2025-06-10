from .repository import PostRepository

class PostDomain:
    def __init__(self):
        self.__repository = PostRepository()

    def create_post(self, post_data, db):
        return self.__repository.create_post(post_data, db)

    def get_post_by_id(self, post_id, db):
        return self.__repository.get_post_by_id(post_id, db)

    def get_all_posts(self, db):
        return self.__repository.get_all_posts(db)
