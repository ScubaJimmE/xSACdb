# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Kit.cost'
        db.alter_column(u'xsd_kit_kit', 'cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

        # Changing field 'Kit.value'
        db.alter_column(u'xsd_kit_kit', 'value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Kit.cost'
        raise RuntimeError("Cannot reverse this migration. 'Kit.cost' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Kit.cost'
        db.alter_column(u'xsd_kit_kit', 'cost', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # User chose to not deal with backwards NULL issues for 'Kit.value'
        raise RuntimeError("Cannot reverse this migration. 'Kit.value' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Kit.value'
        db.alter_column(u'xsd_kit_kit', 'value', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'xsd_kit.kit': {
            'Meta': {'ordering': "['type', 'size', 'name']", 'object_name': 'Kit'},
            'club_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'club_owned': ('django.db.models.fields.BooleanField', [], {}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'needs_testing': ('django.db.models.fields.BooleanField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'purchase_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'})
        },
        u'xsd_kit.loan': {
            'Meta': {'object_name': 'Loan'},
            'approved': ('django.db.models.fields.BooleanField', [], {}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kit': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['xsd_kit.Kit']", 'symmetrical': 'False'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['xsd_kit']