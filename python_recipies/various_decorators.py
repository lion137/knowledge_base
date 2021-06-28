# decorators
import functools
import time

from decorator import decorate


# execution time decor
def meassure_time(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        en = time.time() - st
        name = func.__name__
        args_list = []
        if args:
            args_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            k_val = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            args_list.append(', '.join(k_val))
        arg_string = ', '.join(args_list)
        print('[%0.8fs] %s(%s) -> %r ' % (en, name, arg_string, res))
        return res
    return clocked


# tracing function calls internal
def _trace(f, *args, **kw):
     kwstr = ', '.join('%r: %r' % (k, kw[k]) for k in sorted(kw))
     print("calling %s with args %s, {%s}" % (f.__name__, args, kwstr))
     return f(*args, **kw)


# tracing function calls
def trace(f):
    return decorate(f, _trace)



