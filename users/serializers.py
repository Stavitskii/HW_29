from rest_framework import serializers

from users.models import User, Location




class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, queryset=Location.objects.all(),
                                             many=True, slug_field='name')

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            location, _ = Location.odjects.get_or_create(name=loc)
            user.location.add(location)

        return user

    class Meta:
        model = User
        fields = "__all__"
