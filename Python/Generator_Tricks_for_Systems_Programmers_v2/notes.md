### Many functions consume an "iterable" object


- To do this, you just have to make the object, implement `__iter__()` and `next()`


### Generator Functions

- A generator function is mainly a more convenient way of writing an iterator
- You don't have to worry about the iterator protocol (`.next`, `.__iter__`, etc.)

### Generator vs Iterators

- A generator is a one-time operation. You can iterate over the generated data once, but if you want to do it again, you have to call the generator function again.
