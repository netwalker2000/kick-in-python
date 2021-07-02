from utils.serializers import BaseSerializer


class CommentSerializer(BaseSerializer):
    def recursive_content(self, model, model_map):
        res = model.content
        if model.to_id is not None:
            next_comment = model_map[model.to_id]
            if next_comment is not None:
                res += " reply_to: " + self.recursive_content(next_comment, model_map)
        return res

    def convert_to_dict(self, model, model_map):
        content_chain = self.recursive_content(model, model_map)
        return_dict = {
            'comment_id': model.id,
            'comment_content': content_chain,
            'comment_status': model.status,
            'product_id': model.topic_id,
        }
        return return_dict
