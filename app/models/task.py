import os
from sqlalchemy import Column, Integer, String, Date, CheckConstraint, create_engine, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from dotenv import load_dotenv

load_dotenv()

def create_engine():
    if os.getenv("DATABASE_URL"):
        return create_engine(os.getenv("DATABASE_URL"))
    else:
        raise ValueError("DATABASE_URL environment variable is not set")


engine = create_engine()
Base = declarative_base()


class TaskStatus(Enum):
    """
    Enumeration representing the status of a task.

    Attributes:
        PENDING: The task is pending.
        SUCCESS: The task was completed successfully.
        FAILED: The task failed to complete.
    """
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'


class Task(Base):
    """
    Represents a task.

    Attributes:
        id (int): The unique identifier of the task.
        name (str): The name of the task.
        description (str): The description of the task.
        due_date (datetime.date): The due date of the task.
        priority (int): The priority of the task.
        status (TaskStatus): The status of the task.

    Methods:
        validate_status(attr, value): Validates the status attribute of the task.
        __repr__(): Returns a string representation of the Task instance.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(1024))
    due_date = Column(Date)
    priority = Column(Integer)
    status = Column(TaskStatus, nullable=False, default=TaskStatus.PENDING)

    @validates("status")
    def validate_status(self, attr, value):
        """
        Validates the status attribute of the task.

        Args:
            attr: The name of the attribute being validated.
            value: The value of the attribute.

        Raises:
            ValueError: If the value is not one of the valid TaskStatus values.

        Returns:
            The validated value.
        """
        if value not in [status.value for status in TaskStatus]:
            raise ValueError("Invalid status. Must be one of: {}".format(", ".join(s.value for s in TaskStatus)))
        return value

    def __repr__(self):
        return f"<Task name='{self.name}', status='{self.status.value}'>"


Base.metadata.create_all(engine)
