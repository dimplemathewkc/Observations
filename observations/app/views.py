import json

from django.core import serializers
from django.db.models import Avg
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models


# Create your views here.
from .utils import get_value_unit, get_value_type, create_value_type, create_value_unit


def get_observation_by_name(request) -> JsonResponse:
    """
    Get the observation filtered by name and monitored_id from the Observations table
    """
    observation_name = request.GET.get("observation_name")
    monitored_id = request.GET.get("monitored_id")

    observation = serializers.serialize(
        "json",
        models.Observations.objects.filter(
            monitored_id=monitored_id, observation_name=observation_name
        ),
    )

    return JsonResponse(observation, safe=False)


def get_latest_observation_by_name(request) -> JsonResponse:
    """
    Get the latest observation by name from the Observations table
    """
    observation_name = request.GET.get("observation_name")
    monitored_id = request.GET.get("monitored_id")

    observation = (
        models.Observations.objects.filter(
            monitored_id=monitored_id, observation_name=observation_name
        ).latest("issued_at"),
    )
    observation = serializers.serialize("json", observation)
    return JsonResponse(observation, safe=False)


@csrf_exempt
def insert_observations(request) -> JsonResponse:
    """
    Insert observations in the Observations table
    :param request:
    :return: JSON response
    """
    if request.method == "POST":
        data = json.loads(request.body)["data"]

        for observation in data:
            _observation = models.Observations(
                monitored_id=observation.get("monitored_id"),
                observation_name=observation.get("observation_name"),
                issued_at=observation.get("issued"),
            )
            _observation.save()
            try:
                if observation.get("components"):
                    for component in observation.get("components"):
                        _component = models.Components(
                            observation_name=component.get("observation_name"),
                            value=component.get("value"),
                            value_type=get_value_type(component.get("value_type"))
                            if models.ValueTypes.objects.filter(
                                value_type=component.get("value_type")
                            ).exists()
                            else create_value_type(component.get("value_type")),
                            value_unit=get_value_unit(component.get("value_unit"))
                            if models.ValueUnits.objects.filter(
                                value_unit=component.get("value_unit")
                            ).exists()
                            else create_value_unit(component.get("value_unit")),
                        )
                        _component.save()
                        _observation.component.add(_component)
                else:
                    _component = models.Components(
                        observation_name=observation.get("observation_name"),
                        value=observation.get("value"),
                        value_type=get_value_type(observation.get("value_type"))
                        if models.ValueTypes.objects.filter(
                            value_type=observation.get("value_type")
                        ).exists()
                        else create_value_type(observation.get("value_type")),
                        value_unit=get_value_unit(observation.get("value_unit"))
                        if models.ValueUnits.objects.filter(
                            value_unit=observation.get("value_unit")
                        ).exists()
                        else create_value_unit(observation.get("value_unit")),
                    )
                    _component.save()
                    _observation.component.add(_component)
                _observation.save()
            except Exception as e:
                models.Observations.delete(_observation)
                return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "success", "message": "Observations inserted"})


def observation_mean(request):
    """
    Get the mean of the observation
    """
    observation_name = request.GET.get("observation_name")
    observation = models.Components.objects.filter(observation_name=observation_name)
    mean = observation.aggregate(Avg("value"))

    return JsonResponse({"mean": mean})
