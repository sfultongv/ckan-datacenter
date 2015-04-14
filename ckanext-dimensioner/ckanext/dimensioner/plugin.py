import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)

class DimensionerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IMapper)
    plugins.implements(plugins.ISession)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dimensioner')

    # IMapper --------------------------------------------

    def before_insert(self, mapper, connection, instance):
        pass

    def before_update(self, mapper, connection, instance):
        pass

    def before_delete(self, mapper, connection, instance):
        pass

    def after_insert(self, mapper, connection, instance):
        log.warn('Fun triggered thing here')

    def after_update(self, mapper, connection, instance):
        log.warn('Just checking')

    def after_delete(self, mapper, connection, instance):
        pass

    # ISession

    def after_begin(self, session, transaction, connection):
        pass

    def before_flush(self, session, flush_context, instances):
        pass

    def after_flush(self, session, flush_context):
        pass

    def before_commit(self, session):
        pass

    def after_commit(self, session):
        log.warn('A dream has been revived')

    def after_rollback(self, session):
        pass
