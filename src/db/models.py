from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "auth_users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"