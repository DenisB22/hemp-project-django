from rest_framework import generics as rest_views
from rest_framework import serializers

from final_project.category.models import Category
from final_project.store.models import Product


# REST


class ShortProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name',)


class CategorySerializer(serializers.ModelSerializer):
    product_set = ShortProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class ShortCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


def get_or_create_category_by_name(category_name):
    try:
        return Category.objects.filter(category_name=category_name).get()

    except Category.DoesNotExist:
        return Category.objects.create(
            category_name=category_name,
        )

class ProductSerializer(serializers.ModelSerializer):
    category = ShortCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category_name = validated_data.pop('category').get('category_name')

        return Product.objects.create(
            **validated_data,
            category=get_or_create_category_by_name(category_name),
        )



