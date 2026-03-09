from functools import wraps
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def TimerWrapper(*args, **kwargs):
        """TimerWrapper Docstring"""
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func} took end {end - start}")
    return TimerWrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    pass

def retry(func, max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    attempt = max_attempts
    @wraps(func)
    def retry_attempt(attempt, *args, **kwargs):
        if attempt == 0:
            return
        else:
            print(f"Attempt Number {attempt}:")
            func(*args, **kwargs)
            attempt -= 1
            retry_attempt(attempt, *args, **kwargs)
    return retry_attempt

@timer
@retry
def hello(s = "Hello World"):
    print(s)

hello("Hello World")

