import logging
import os

from flask import Flask, render_template
from flask_upstatic import Upstatic

logger = logging.getLogger('flask_upstatic')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


if __name__ == '__main__':
  app = Flask(__name__)
  app.config.update(
    UPSTATIC_S3_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID'),
    UPSTATIC_S3_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    UPSTATIC_S3_BUCKET_NAME='flask_upstatic_example',
  )
  upstatic = Upstatic(app)
  upstatic.upload()

  app.add_template_global(upstatic.url_for)

  @app.route('/')
  def index():
    return render_template('index.html')

  app.run(host='0.0.0.0')
