from . import helpers

def get_hmm():
    """Get a thought"""
    return 'hmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())