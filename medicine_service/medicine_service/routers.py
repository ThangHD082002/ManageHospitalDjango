# class Book:
#     route_app_labels = {'book'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'book_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'book_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the primary/replica pool.
#         """
#         db_set = {"book_db"}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'book_db'
#         return None


# class Clothes:
#     route_app_labels = {'clothes'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'clothes_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'clothes_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the primary/replica pool.
#         """
#         db_set = {"clothes_db"}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'clothes_db'
#         return None


# class Mobiles:
#     route_app_labels = {'mobile'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'mobiles_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'mobiles_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the primary/replica pool.
#         """
#         db_set = {"mobiles_db"}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'mobiles_db'
#         return None


# class Category:
#     route_app_labels = {'category'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'category_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'category_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the primary/replica pool.
#         """
#         db_set = {"category_db", "clothes_db", "book_db", "mobiles_db"}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'category_db'
#         return None



from django.conf import settings


class DatabaseRouter:
    @property
    def mapping(self):
        return getattr(settings, "DATABASE_APPS_MAPPING", {})

    def db_for_read(self, model, **hints):
        return self.mapping.get(model._meta.app_label, "default")

    def db_for_write(self, model, **hints):
        return self.mapping.get(model._meta.app_label, "default")

    def allow_relation(self, obj_1, obj_2, **hints):
        return self.mapping.get(obj_1._meta.app_label) and self.mapping.get(obj_2._meta.app_label, "default")

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return self.mapping.get(app_label, "default") == db