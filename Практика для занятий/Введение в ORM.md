# Введение в ORM

**Задание 1**

Необходимо реализовать следующие модели и отношения для них

**1. Пользоваели**
```python
class User(Base):
    # Таблица `users`
```

**2. Роли**
```python
class Role(Base):
    # Таблица `roles`
```

**3. Permission**
```python
class Permission(Base):
    # Таблица `permissions`
```

**Задание 2**

Необходимо реализовать ассоциативные таблицы для many-to-many

**1. Роли пользователя**
```python
user_roles = Table(
    # Таблица user_roles
)
```

**2. Права у роли**
```python
role_permissions = Table(
    # Таблица role_permissions
)
```