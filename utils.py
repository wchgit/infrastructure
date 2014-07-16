#!/usr/bin/env python
#coding:utf-8

def safeunicode(obj, encoding='utf-8'):
    """
    Converts any given object to unicode string

        >>> type(safeunicode(u'你好')) is unicode
        True
        >>> type(safeunicode('你好')) is unicode
        True
        >>> type(safeunicode('你好'.decode('utf-8').encode('gbk'))) is unicode
        True
        >>> type(safeunicode(2.718)) is unicode
        True
    """
    t = type(obj)
    if t is unicode:
        return obj
    elif t is str:
        return obj.decode(encoding, 'ignore')
    elif t in [int, float, bool]:
        return unicode(obj)
    elif hasattr(obj, '__unicode__') or isinstance(obj, unicode):
        return unicode(obj, 'ignore')
    else:
        return str(obj).decode(encoding, 'ignore')


class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used                                                                      
    in addition to `obj['foo']`.

        >>> sto = Storage()
        >>> sto
        <Storage {}>
        >>> sto.a = 'one'
        >>> sto.a
        'one'
        >>> sto.b
        Traceback (most recent call last):                                                                                                  
        ...                                                                                                                             
        AttributeError: 'b'
    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k
    
    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
