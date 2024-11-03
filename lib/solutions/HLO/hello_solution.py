

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    assert isinstance(friend_name, str), "Friend name must be a string"
    return 'Hello, ' + friend_name + '!'