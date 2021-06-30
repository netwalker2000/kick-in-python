from utils.serializers import BaseSerializer


class ProductBriefSerializer(BaseSerializer):
    def convert_to_dict(self, model):
        return_dict = {
            'product_id': model.id,
            'product_name': model.name,
            'category': model.category,
            'description': model.description,
            'status': model.status
        }
        return return_dict


class CommentSerializer(BaseSerializer):
    def convert_to_dict(self, model):
        return_dict = {
            'comment_id': model.id,
            'comment_content': model.content,
            'comment_status': model.status,
            'product_id': model.topic_id
        }
        return return_dict


class PhotoSerializer(BaseSerializer):
    def convert_to_dict(self, model):
        return_dict = {
            'photo_url': "photo.shopee.com/cloud/cdn/" + model.url
        }
        return return_dict
