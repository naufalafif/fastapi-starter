from app.src.database import Session
from contextlib import contextmanager


@contextmanager
def session_manager():
    """
    example:
      with session_manager() as session:
      result = session.query(db.User).all()
      print(result)
    """

    session = Session()
    try:
        yield session
    except Exception as error:
        print("rollback transaction")
        session.rollback()
        raise error
    finally:
        print("closing connection")
        session.close()
