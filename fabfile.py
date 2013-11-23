import fabengine
import os

ROOT = os.path.dirname(__file__)

fabengine.config(ROOT, gae_path=os.path.join(ROOT, 'google_appengine'))

fabengine.dev_appserver.default_arguments = ('allow_skipped_files',), {
    'blobstore_path': '/tmp/py-cobra2.blobstore',
    'datastore_path': '/tmp/py-cobra2.datastore',
    'logs_path': '/tmp/py-cobra2.logs'}

