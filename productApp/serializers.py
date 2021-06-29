from utils.serializers import BaseSerializer


class ProductBriefSerializer(BaseSerializer):
	def convert_to_dict(self, model):
		return_dict = {}

		return_dict['product_id'] = model.id
		return_dict['product_name'] = model.name
		return_dict['category'] = model.category
		return_dict['description'] = model.description
		return_dict['status'] = model.status

		return return_dict

