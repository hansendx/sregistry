'''

Copyright (C) 2017-2018 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017-2018 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from django.conf.urls import (
    url, 
    include
)

from rest_framework import routers

from shub.apps.api.urls.containers import ContainerViewSet
from shub.apps.api.urls.collections import CollectionViewSet
from shub.apps.api.actions.push import ContainerPushViewSet

router = routers.DefaultRouter()
router.register(r'^containers', ContainerViewSet, base_name="container")
router.register(r'^collections', CollectionViewSet, base_name="collection")
router.register(r'^push', ContainerPushViewSet, base_name="push")  # push

urlpatterns = [

    url(r'^', include(router.urls))

]
