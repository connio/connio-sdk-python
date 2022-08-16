import datetime
import json

from connio.base import values

def iso8601_date(d):
    """
    Return a string representation of a date that the Connio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    if d == values.unset:
        return d
    elif isinstance(d, datetime.datetime):
        return str(d.date())
    elif isinstance(d, datetime.date):
        return str(d)
    elif isinstance(d, str):
        return d


def iso8601_datetime(d):
    """
    Return a string representation of a date that the Connio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    if d == values.unset:
        return d
    elif isinstance(d, datetime.datetime) or isinstance(d, datetime.date):
        return d.strftime('%Y-%m-%dT%H:%M:%SZ')
    elif isinstance(d, str):
        return d


def prefixed_collapsible_map(m, prefix):
    """
    Return a dict of params corresponding to those in m with the added prefix
    """
    if m == values.unset:
        return {}

    def flatten_dict(d, result={}, prv_keys=[]):
        for k, v in d.items():
            if isinstance(v, dict):
                flatten_dict(v, result, prv_keys + [k])
            else:
                result['.'.join(prv_keys + [k])] = v

        return result

    if isinstance(m, dict):
        flattened = flatten_dict(m)
        return {'{}.{}'.format(prefix, k): v for k, v in flattened.items()}

    return {}


def object(obj):
    """
    Return a jsonified string represenation of obj if obj is jsonifiable else
    return obj untouched
    """
    if isinstance(obj, dict) or isinstance(obj, list):
        return json.dumps(obj)
    return obj


def map(lst, serialize_func):
    """
    Applies serialize_func to every element in lst
    """
    if not isinstance(lst, list):
        return lst
    return [serialize_func(e) for e in lst]


def measurement(measurement):
    """
    Serialize a measurement object to measurement JSON
    :param measurement: PropertyInstance.Measurement
    :return: jsonified string represenation of obj 
    """    
    if measurement is values.unset or measurement is None:
        return values.unset
    return values.of({ 
        'type': measurement.type, 
        'unit': values.of({ 'label': measurement.unit.label, 'symbol': measurement.unit.symbol })
    })

def boundaries(boundaries):
    """
    Serialize a boundaries object to boundaries JSON
    :param boundaries: PropertyInstance.Boundaries
    :return: jsonified string represenation of obj 
    """    
    if boundaries is values.unset or boundaries is None:
        return values.unset
        
    return values.of({ 
        'size': boundaries.size,
        'min': boundaries.min,
        'max': boundaries.max,
        'set': boundaries.set,
        'lat': boundaries.lat,
        'lon': boundaries.lon,
        'radius': boundaries.radius,
        'inside': boundaries.inside,
    })
    
def retention(retention):
    """
    Serialize a retention object to retention JSON
    :param retention: PropertyInstance.Retention
    :return: jsonified string represenation of obj 
    """    
    from connio.rest.api.v3.account.propertyy import PropertyInstance
    if retention is values.unset or retention is None:
        return values.unset
    retentionType = values.unset
    if retention.type == PropertyInstance.Retention.RetentionType.MOSTRECENT:
        retentionType = 'mostrecent'
    elif retention.type == PropertyInstance.Retention.RetentionType.HISTORICAL:
        retentionType = 'historical'
    return_obj = {
        'type': retentionType,
        'context': values.of({'type': retention.context.type}),
        'lifetime': retention.lifetime,
        'capacity': retention.capacity,
    }
    if(retention.type == PropertyInstance.Retention.RetentionType.HISTORICAL):
        return_obj['condition'] = values.of({'when': retention.condition.when, 'value': retention.condition.value})
    return values.of(return_obj)

def location(loc):
    """
    
    """
    if loc is values.unset or loc is None or (loc.zone is None and loc.geo is None):
        return None
    else:
        geo = None
        if loc.geo is not None:
            geo = { 'lat': loc.geo.lat, 'lon': loc.geo.lon, 'alt': loc.geo.alt }
        return { 'zone': loc.zone, 'geo': geo }

def plan(plan):
    """
    Account plan serializer.
    """
    if plan is values.unset or plan is None:
        return None

    return { 'type': plan.type, 'expiresAt': plan.expires_at }

def methodImplementation(impl):
    """
    Serialize a method implementation object to JSON
    :param impl: MethodInstance.MethodImplementation
    :return: jsonified string represenation of obj 
    """    
    from connio.rest.api.v3.account.method import MethodInstance

    if impl == values.unset:
        return impl
    elif isinstance(impl, MethodInstance.MethodImplementation):
        if impl.body is None:
            return values.unset
        return { 'funcBody': impl.body, 'script': impl.lang }
    else:
        return values.unset

def conditions(conditions):
    """
    Serialize a AlertInstance.Condition object to JSON
    :param condition: AlertInstance.Condition
    :return: jsonified string represenation of obj 
    """    
    def transform(condition):
        def transform(handler):
            return { 'key': handler.key, 'notification': handler.notification }
        expression = { 'operation': condition.expression.operation, 'value': condition.expression.value }
        return { 'severity': condition.severity, 'expression': expression, 'handlers': map(condition.handlers, transform) }

    return map(conditions, transform)

def notifications(notifications):
    """
    Serialize a AlertInstance.Notification object to JSON
    :param notification: AlertInstance.Notification
    :return: jsonified string represenation of obj 
    """
    def transform(notification):
        return { 
            'action': notification.action, 
            'name': notification.name, 
            'level': notification.level,            
            'message': notification.message,
            'method': notification.method,
            'parameter': notification.parameter,
            'to': notification.to,
            'subject': notification.subject,
        }

    return map(notifications, transform)
