import datetime as dt

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

DUPLICATE_REVIEW = 'У вас уже есть отзыв на это произведение'


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(
            queryset=User.objects.all())])
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(
            queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('email', 'username',)


class ConfirmationSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('confirmation_code', 'username',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    def validate(self, attrs):
        if (self.context['request'].method == 'POST'
            and Review.objects.filter(
                author=self.context['request'].user,
                title=self.context['view'].kwargs.get('title_id')
        ).exists()):
            raise ValidationError(DUPLICATE_REVIEW)
        return attrs

    class Meta:

        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:

        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitleAdminSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(required=False, slug_field='slug',
                                            queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(required=False,
                                         slug_field='slug',
                                         queryset=Genre.objects.all(),
                                         many=True)

    class Meta:
        model = Title
        fields = '__all__'

    def validate_year(self, value):
        year = dt.date.today().year
        if not value <= year:
            raise serializers.ValidationError(
                'Проверьте год создания произведения!'
            )
        return value


class AdminSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(
            queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')


class UserSerializer(AdminSerializer):
    role = serializers.CharField(read_only=True)
