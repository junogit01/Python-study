def exception_hirarchy(exception_class, indent = 0):
    print("--" * indent + exception_class.__name__)
    subclasses = exception_class.__subclasses__()
    for subclass in subclasses:
        exception_hirarchy(subclass, indent + 2)

exception_hirarchy(BaseException)