import datetime
from decimal import Decimal, BasicContext
from email.utils import parsedate
from connio.rest.api.v3.account.__init__ import AccountInstance
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance
from connio.rest.api.v3.account.device import DeviceInstance
from connio.base import values
import pytz

ISO8601_DATE_FORMAT = '%Y-%m-%d'
ISO8601_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
ISO8601_DATETIME_FORMAT2 = '%Y-%m-%dT%H:%M:%SZ'
RFC2822_DATETIME_SPLIT_INDEX = 6

def iso8601_date(s):
    """
    Parses an ISO 8601 date string and returns a UTC date object or the string
    if the parsing failed.
    :param s: ISO 8601-formatted date string (2015-01-25)
    :return:
    """
    try:
        return datetime.datetime.strptime(s, ISO8601_DATE_FORMAT).replace(tzinfo=pytz.utc).date()
    except (TypeError, ValueError):
        return s


def iso8601_datetime(s):
    """
    Parses an ISO 8601 datetime string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: ISO 8601-formatted datetime string (2015-01-25T12:34:56.133Z)
    :return: datetime or str
    """
    try:
        return datetime.datetime.strptime(s, ISO8601_DATETIME_FORMAT).replace(tzinfo=pytz.utc)
    except (TypeError, ValueError):
        try:
            return datetime.datetime.strptime(s, ISO8601_DATETIME_FORMAT2).replace(tzinfo=pytz.utc)
        except (TypeError, ValueError):
            return s


def rfc2822_datetime(s):
    """
    Parses an RFC 2822 date string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: RFC 2822-formatted string date
    :return: datetime or str
    """
    date_tuple = parsedate(s)
    if date_tuple is None:
        return None
    return datetime.datetime(*date_tuple[:RFC2822_DATETIME_SPLIT_INDEX]).replace(tzinfo=pytz.utc)


def decimal(d):
    """
    Parses a decimal string into a Decimal
    :param d: decimal string
    :return: Decimal
    """
    if not d:
        return d
    return Decimal(d, BasicContext)


def integer(i):
    """
    Parses an integer string into an int
    :param i: integer string
    :return: int
    """
    try:
        return int(i)
    except (TypeError, ValueError):
        return i

def plan(plan):
    """
    Parses an account plan object give in JSON to AccountInstance.Plan type
    :param plan: plan in JSON
    :return: AccountInstance.Plan
    """
    if plan is None:
        return None

    return AccountInstance.Plan(plan['type'], plan.get('expiresAt'))

def measurement(measurement):
    """
    Parses a measurement object give in JSON to PropertyInstance.Measurement type
    :param measurement: measurement in JSON
    :return: PropertyInstance.Measurement
    """
    if measurement is None:
        return None

    return parseMeasurement(measurement)

def parseMeasurement(measurement):
    """
    Parses a measurement object give in JSON to measurement type
    :param measurement: measurement in JSON
    :return: PropertyInstance.Measurement
    """
    typ = measurement.get('type')
    unit = measurement.get('unit')

    if typ and unit:
        label = unit.get('label')
        symbol = unit.get('symbol')
        if label and symbol:
            return PropertyInstance.Measurement(typ, PropertyInstance.MeasurementUnit(label, symbol), measurement)
        return None
    return None

def boundaries(boundaries):
    """
    Parses a boundaries object give in JSON to Boundaries type
    :param boundaries: boundaries in JSON
    :return: PropertyInstance.Boundaries
    """
    if boundaries is None or boundaries is values.unset:
        return values.unset

    geofence = values.unset
    if boundaries.get('lat', values.unset) is not values.unset and boundaries.get('lon', values.unset) is not values.unset and boundaries.get('radius', values.unset) is not values.unset and boundaries.get('inside', values.unset) is not values.unset:
        geofence = PropertyInstance.Boundaries.Geofence(boundaries['lat'], boundaries['lon'], boundaries['radius'], boundaries['inside'])

    # v3 compatibility
    min = boundaries.get('min', values.unset)
    max = boundaries.get('max', values.unset)
    if boundaries.get('range', values.unset) is not values.unset:
        min = boundaries['range'].get('min', values.unset)
        max = boundaries['range'].get('max', values.unset)
    ##
    # v3 compatibility
    size = boundaries.get('size', values.unset)
    if size is not values.unset:
         if isinstance(boundaries['size'], dict):
            size = boundaries['size'].get('value', values.unset)
    ##

    return PropertyInstance.Boundaries(min=min,
        max=max,
        size=size,
        set=boundaries.get('set', values.unset),
        geofence=geofence,
        props=boundaries)
        
def retention(retention):
    """
    Parses a retention object give in JSON to Retention type
    :param retention: retention in JSON
    :return: PropertyInstance.Retention
    """
    DEFAULT_CONTEXT_TYPE = "default"

    if retention is None or retention is values.unset:
        return values.unset
    context = values.unset
    if retention.get('context', values.unset) is not values.unset:
        context_type = retention['context'].get('type', DEFAULT_CONTEXT_TYPE)

        if(context_type == values.unset):
            context_type = DEFAULT_CONTEXT_TYPE
        context = PropertyInstance.Context(context_type)
    condition = values.unset
    if retention.get('condition', values.unset) is not values.unset:
        condition = PropertyInstance.Condition(when=retention['condition'].get('when', values.unset), value=retention['condition'].get('value', values.unset))
    retentionType = values.unset
    if retention['type'] == 'mostrecent':
        retentionType = PropertyInstance.Retention.RetentionType.MOSTRECENT
    elif retention['type'] == 'historical':
        retentionType = PropertyInstance.Retention.RetentionType.HISTORICAL

    return PropertyInstance.Retention(type=retentionType,
        context=context,
        lifetime=retention.get('lifetime', values.unset),
        capacity=retention.get('capacity', values.unset),
        condition=condition,
        props=retention)
    
def location(loc):
    """
    
    """
    if loc is None:
        return None
    
    zone = loc.get('zone')
    geo = loc.get('geo')

    geoCoord = None
    if geo is not None:
        geoCoord = DeviceInstance.GeoCoord(geo['lat'], geo['lon'], geo.get('alt'))

    return DeviceInstance.Location(zone, geoCoord, loc)

def methodImplementation(methodImpl):
    """
    Parses a method implementation object give in JSON to method implementation type
    :param body: method body
    :param lang: script language
    :return: MethodInstance.MethodImplementation
    """

    body = methodImpl.get('funcBody')
    lang = methodImpl.get('script')

    if body is None:
        return None

    return MethodInstance.MethodImplementation(body, lang, props=methodImpl)

def conditions(conditions):
    """
    """
    from connio.rest.api.v3.account.alert import AlertInstance

    try:
        conditionList = []
        for c in conditions:
            exp = AlertInstance.Condition.Expression(c['expression']['operation'], c['expression'].get('value'))
            handlerList = []
            for h in c['handlers']:
                hand = AlertInstance.Condition.Handler(h['key'], h['notification'])
                handlerList.append(hand)
            cond = AlertInstance.Condition(c['severity'], exp, handlerList)
            conditionList.append(cond)

        return conditionList        
    except:
        return None
        
def notifications(notifications):
    """
    """
    from connio.rest.api.v3.account.alert import AlertInstance

    notificationList = []
    for n in notifications:
        notif = AlertInstance.Notification(
            action=n['action'], 
            name=n['name'], 
            level=n.get('level'),
            to=n.get('to'),
            subject=n.get('subject'),
            message=n.get('message'),
            method=n.get('method'),
            parameter=n.get('parameter'),
        )
        notificationList.append(notif)

    return notificationList
